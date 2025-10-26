from typing import TYPE_CHECKING, Tuple, Dict

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from world._bizhawk.context import BizHawkClientContext, BizHawkClientCommandProcessor

SADV2_ZONE_SELECT_TABLE = 0xd7508 #rom
SADV2_UPDATE_ZONE_SELECT = 0x30EB2 #rom
SADV2_UPDATE_EMERALDS = 0x6c5d4 #rom
SADV2_CHARACTERS_UNLOCKED = 0x266b #ewram
SADV2_SONIC_EMERALDS = 0x2664 #ewram
SADV2_SONIC_LEVELS_UNLOCKED = 0x265f #ewram
SADV2_AREA_53_UNLOCKED = 0x2672
SADV2_LEVEL_COMPLETE = 0x54a8 #iwram
SADV2_STAGE_FLAGS = 0x5424 #iwram, seventh bit is demo mode (i think)
SADV2_CURRENT_LEVEL = 0x55b4 #iwram
SADV2_CURRENT_CHARACTER = 0x54f0 #iwram


zone_data: Dict[int, Tuple[int, int, int, int]] = {
    # ID: (Act 1 ID, Act 1 Offset, Act 2 ID, Act 2 Offset)
    200: [0x00, 0x00, 0x01, 0x01], # Leaf Forest
    201: [0x04, 0x02, 0x05, 0x03], # Hot Crater
    202: [0x08, 0x04, 0x09, 0x05], # Music Plant
    203: [0x0c, 0x06, 0x0d, 0x07], # Ice Paradise
    204: [0x10, 0x08, 0x11, 0x09], # Sky Canyon
    205: [0x14, 0x0a, 0x15, 0x0b], # Techno Base
    206: [0x18, 0x0c, 0x19, 0x0d], # Egg Utopia
    207: [0x1c, 0x0e] # XX
}

class SonicAdvance2Client(BizHawkClient):
    game = "Sonic Advance 2"
    system = "GBA"

    starting_zone: int
    did_setup: bool = False

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            game_code: bytes = ((await bizhawk.read(ctx.bizhawk_ctx, [(0xac, 4, "ROM")])))
            
            if game_code[0] != b"A2NE":
                print(game_code)
                return False
        except bizhawk.RequestFailedError:
            return False
        
        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True

        return True
    
    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        if ((ctx.server is None) or (ctx.server.socket.closed) or (ctx.slot_data is None)):
            return
        
        if not self.did_setup:
            print(ctx.slot_data)
            starting_zone = ctx.slot_data["starting_zone"]
            starting_zone += 200

            sz_act1 = zone_data[starting_zone][0]
            sz_act2 = zone_data[starting_zone][2]
            sz_list = [sz_act1, sz_act2, sz_act1, sz_act2, sz_act1, sz_act2, sz_act1, sz_act2,
                        sz_act1, sz_act2, sz_act1, sz_act2, sz_act1, sz_act2]
            print(sz_list)

            # Update the zone table to only point to our starting zone
            await bizhawk.write(ctx.bizhawk_ctx, [(SADV2_ZONE_SELECT_TABLE, sz_list, "ROM")])
            # Update unlocked characters to only our starting character
            await bizhawk.write(ctx.bizhawk_ctx, [(SADV2_CHARACTERS_UNLOCKED, [0x05], "EWRAM")])
            # This NOPs the instruction that awards chaos emeralds
            await bizhawk.write(ctx.bizhawk_ctx, [(SADV2_UPDATE_EMERALDS, [0x00, 0x00], "ROM")])
            # This NOPs the instruction that unlocks XX when the Egg Frog is defeated
            await bizhawk.write(ctx.bizhawk_ctx, [(SADV2_UPDATE_ZONE_SELECT, [0x00, 0x00], "ROM")])
            # Full level select access up to Egg Utopia
            await bizhawk.write(ctx.bizhawk_ctx, [(SADV2_SONIC_LEVELS_UNLOCKED, [0x18, 0x18, 0x18, 0x18, 0x18], "EWRAM")])

            self.did_setup = True
        try:
            level_complete, demo_mode, zone_id, character_id = await bizhawk.read(ctx.bizhawk_ctx, [
                (SADV2_LEVEL_COMPLETE, 1, "IWRAM"), (SADV2_STAGE_FLAGS, 1, "IWRAM"),
                (SADV2_CURRENT_LEVEL, 1, "IWRAM"), (SADV2_CURRENT_CHARACTER, 1, "IWRAM")])
            
            if not (int.from_bytes(demo_mode, "little") & 0x40):
                if (int.from_bytes(level_complete, "little") == 0xFF):
                    print(int.from_bytes(level_complete, "little"))
                    location_id = 0x10000 + (int.from_bytes(character_id) * 0x1000) + (int.from_bytes(zone_id) * 0x10)
                    if location_id not in ctx.checked_locations:
                        await ctx.send_msgs([{
                            "cmd": "LocationChecks",
                            "locations": [location_id]
                        }])
        except bizhawk.RequestFailedError:
            pass

        