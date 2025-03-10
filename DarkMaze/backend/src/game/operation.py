from ..database.operation import save_game_state
from .judge import hit_obstacle, game_over, arrive_at_destination

def move_location(game_state, direction):
    if game_over(game_state["health"]):
        return game_state
    
    x, y = game_state["current_position"]
    map_width = game_state["map_size"][0]
    map_height = game_state["map_size"][1]
    
    # Update position based on direction
    moves = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }
    
    if direction in moves:
        dx, dy = moves[direction]
        new_x = x + dx
        new_y = y + dy
        
        if 0 <= new_x < map_width and 0 <= new_y < map_height:
            new_position = [new_x, new_y]
            
            if hit_obstacle(new_position, game_state["current_level_name"]):
                game_state["health"] -= 1
            else:
                if new_position not in game_state["path"]:
                    game_state["path"].append(new_position)
                game_state["current_position"] = new_position

            if arrive_at_destination(game_state["current_level_name"], game_state["current_position"]):
                game_state["health"] = 666

            save_game_state(
                game_state['username'],
                game_state["current_level_name"],
                game_state["map_size"],
                game_state["health"],
                game_state["path"],
                game_state["current_position"]
            )
    
    return game_state
