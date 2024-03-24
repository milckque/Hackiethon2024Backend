# bot code goes here
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import defense_actions, attack_actions, projectile_actions
from Game.gameSettings import HP, LEFTBORDER, RIGHTBORDER, LEFTSTART, RIGHTSTART, PARRYSTUN


# PRIMARY CAN BE: Teleport, Super Saiyan, Meditate, Dash Attack, Uppercut, One Punch
# SECONDARY CAN BE : Hadoken, Grenade, Boomerang, Bear Trap

# TODO FOR PARTICIPANT: Set primary and secondary skill here
PRIMARY_SKILL = DashAttackSkill
SECONDARY_SKILL = BearTrap

#constants, for easier move return
#movements
JUMP = ("move", (0,1))
FORWARD = ("move", (1,0))
BACK = ("move", (-1,0))
JUMP_FORWARD = ("move", (1,1))
JUMP_BACKWARD = ("move", (-1, 1))

# attacks and block
LIGHT = ("light",)
HEAVY = ("heavy",)
BLOCK = ("block",)

PRIMARY = get_skill(PRIMARY_SKILL)
SECONDARY = get_skill(SECONDARY_SKILL)
CANCEL = ("skill_cancel", )

# no move, aka no input
NOMOVE = "NoMove"
# for testing
moves = SECONDARY,
moves_iter = iter(moves)

# TODO FOR PARTICIPANT: WRITE YOUR WINNING BOT
class Script:
    def __init__(self):
        self.primary = PRIMARY_SKILL
        self.secondary = SECONDARY_SKILL
        
    # DO NOT TOUCH
    def init_player_skills(self):
        return self.primary, self.secondary
    # MAIN FUNCTION that returns a single move to the game manager
    def get_move(self, player, enemy, player_projectiles, enemy_projectiles):
        distance = abs(get_pos(player)[0] - get_pos(enemy)[0])
        # dodge projectiles 
        if get_stun_duration(enemy) > 0:
            player_x, player_y = get_pos(player)
            enemy_x, enemy_y = get_pos(enemy)
            if player_y == enemy_y and abs(player_x - enemy_x) == 1:
                if get_past_move(player, 1) == LIGHT:
                    if get_past_move(player, 2) == LIGHT:
                        return HEAVY
                    else:
                        return LIGHT
                else:
                    return LIGHT
            return FORWARD
        if enemy_projectiles:
            if get_proj_pos(enemy_projectiles[0])[0] - 1 <= get_pos(player)[0] <= \
                get_proj_pos(enemy_projectiles[0])[0] + 1:
                return JUMP
        if get_last_move(enemy) == ('dash_attack', 'startup') and distance <= 4: 
            return JUMP_FORWARD
        
        if get_last_move(enemy) == ('dash_attack', 'startup') and distance > 4: 
            return JUMP_BACKWARD
        
        if (get_pos(player)[0] <= 1 or get_pos(player)[0] >= 14) and distance <= 3:
            return PRIMARY
        
        if not secondary_on_cooldown(player) and get_pos(player)[1] == 0:
            return SECONDARY
        
        if secondary_on_cooldown or distance <= 3:
            return BACK
        
        
        
        
        
        
        
