def validMove(moveset, player, enemy):
    valid_moves = [-1,0,1]
    #TODO prevent double jumps
    if moveset[0] not in valid_moves or moveset[1] not in valid_moves:
        return False
    # check if out of bound 
    # *assuming the screen is 0-30
    elif (player.xCoord - moveset[0] <0 or player.xCoord + moveset[0] >30):
        return False
    #check if position is taken
    elif (player.xCoord + moveset[0]==enemy.xCoord and player.yCoord + moveset[1]== enemy.yCoord):
        return False
    return True
def flip_orientation(player1, player2):
    if player1.xCoord > player2.xCoord:
        # should flip orientations if they switch sides
        return True
    return False