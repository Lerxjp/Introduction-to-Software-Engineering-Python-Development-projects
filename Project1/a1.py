"""
Project 1
"""

from a1_support import *

# Actions
ATTACK = 'a'
HELP = '?'
QUIT = 'q'
REVERT_TO_CHECKPOINT = 'n'

def get_position_in_direction(position, direction):
    '''return the position that would result from moving from given postion
    in the given direction
    Parameters:
        position (tuple<int, int>): The row, column position of a tile.
        direction (tuple<int, int>): The row, column in diretion.
        
    Returns:
        Position_in_direction (tuple<int, int>): The row, column in position in direction'''
    
    x, y = position
    dx, dy = DIRECTIONS[direction]
    return x + dx, y + dy

def get_tile_at_position(level,position):
    '''Return the character representing the tile at the given position
    in a level string.
    Parameters:
        level (str): The level string.
        position (tuple<int, int>): The row, column position of a tile.
        
    Returns:
        tile (str): The level string.'''
    
    size = level_size(level)
    index = position_to_index(position, size)
    tile = level[index]
    return tile 

def get_tile_in_direction(level, position, direction):
    '''Determine the new position which results from moving the given position
    in the given direction, and return the character representing the tile
    found at this new position
        Parameters:
            level (str): The level string.
            position (tuple<int, int>): The row, column position of a tile.
            direction (tuple<int, int>): The row, column in diretion.
            
        Returns:
            tile_at_position (str): The tile string.'''
    
    return get_tile_at_position(level, (get_position_in_direction(position, direction)))

def remove_from_level(level, position):
    '''return a level string exactly the same as the one given,
    but with the given position replaced by air
        Parameters:
            level (str): The level string.
            position (tuple<int, int>): The row, column position of a tile.
            
        Returns:
            Load_level (str): The level string.'''
    
    size = level_size(level)
    index = position_to_index(position, size)
    return level[:index] + AIR + level[index+1:]

def move(level, position, direction):
    '''Return the updated position that results from moving the character from the given position in the given direction.
    If the tile at the updated position is a wall tile, adjust the position up until an air tile is found and return that as the position
    instead
    Parameters:
        level (str): The level string.
        position (tuple<int, int>): The row, column position of a tile.
        direction (tuple<int, int>): The row, column in diretion.
            
    Returns:
        position (tuple<int, int>): The row, column position that the player is moved towards'''
    
    position = get_position_in_direction(position, direction)

    while get_tile_at_position(level, position) == WALL:
        
        position = get_position_in_direction(position, UP)
        
    while get_tile_in_direction(level,position,DOWN) == AIR:
        position = get_position_in_direction(position, DOWN)
    
    return position
        
def print_level(level, position):
    '''print the level (i.e. string) with the tile of the given position
    replaced by the player
    Parameters:
        level(str): The level string.
        position (tuple<int, int>): The row, column position of a tile.
    prints:
     Load_level : the level as a string.:
    '''
    size = level_size(level)
    index = position_to_index(position, size)
    Load_level = level[:index] + PLAYER + level[index+1:]
    print(Load_level)
       
def attack(level, position):
    '''Check for MONSTER tile to the left and right of the Player position
    then remove MONSTER tile from the string 
    Parameters:
        level(str): The level string.
        position (tuple<int, int>): The row, column position of a tile.
    prints:
     new_level : The new level string.:
    '''

    right = get_tile_in_direction( level, position, RIGHT )
    left = get_tile_in_direction( level, position, LEFT )

    if left == MONSTER:
        monster_position = get_position_in_direction(position, LEFT)  
        print("Attacking the monster on your left!")
        new_level = remove_from_level(level, monster_position)
        return new_level

    if right == MONSTER:
        monster_position = get_position_in_direction(position, RIGHT)
        print("Attacking the monster on your right!")  
        new_level = remove_from_level(level, monster_position)
        return new_level
    else:
        print("No monsters to attack!")
        return level
    
def tile_status(level,position):
    ''' Checks the tile at the characters position.
    Parameters:
        level(str): The level string.
        position (tuple<int, int>): The row, column position of a tile.
    returns:
        tuple containing the tile character and the level
    '''
    
    tile = get_tile_at_position(level, position)
    if tile == GOAL:
        print('Congratulations! You finished the level')
    elif tile == MONSTER:
        print('Hit a monster!')
    elif tile in (COIN, CHECKPOINT):
        new_level = remove_from_level(level, position)
        level = remove_from_level(level, position)
    
    return tile, level

def main():
    '''Handles the main interaction with the user.
    Parameters:
        none
    Returns:
        none'''
    
    level = load_level(input("Please enter the name of the level file (e.g. level1.txt): "))
    score = 0
    position = (0, 1)

    checkpoint = None

    while True:
        print(f"Score: {score}")
        print_level(level, position)

        command = input("Please enter an action (enter '?' for help): ")

        if command in (LEFT, RIGHT):
            position = move(level, position, command)
            tile, level = tile_status(level, position)

            if tile == GOAL:
                break
            elif tile == MONSTER:
                if not checkpoint:
                    break
                level, score, position = checkpoint
            elif tile == COIN:
                score += 1
            elif tile == CHECKPOINT:
                checkpoint = level, score, position

        elif command == ATTACK:
            level = attack(level, position)

        elif command == HELP:
            print(HELP_TEXT)

        elif command == REVERT_TO_CHECKPOINT and checkpoint:
            level, score, position = checkpoint

        elif command == QUIT:
            break

if __name__ == "__main__":
    main()
