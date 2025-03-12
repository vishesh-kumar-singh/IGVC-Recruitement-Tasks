# BFS Algorithm had been used to complete the required task.


from collections import deque      # Importing deque for BFS
import numpy as np                 # We are dealing with a Map as Matrix ofc :)


# Getting the input matrix from the string I copied and pasted from the problem statement
List='''1 1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 0 1
1 0 0 0 2 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 2 1
1 2 0 0 1 1 1 0 0 0 1
1 0 0 0 1 1 1 0 0 0 1
1 3 0 0 1 1 1 0 0 0 1
1 0 0 0 1 1 1 2 2 0 1
1 0 0 0 1 1 1 0 0 0 1
1 0 0 0 1 1 1 0 0 0 1
1 0 2 0 0 0 0 0 0 0 1
1 0 0 0 0 0 2 0 0 0 1
1 0 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 1'''.split()

array=np.array(List)

grid=array.reshape(14,11).astype(int)



# Locating the Starting Position
start = None
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 3:
            start = (r, c)
            break
    if start is not None:
        break
if start is None:
    raise ValueError("No starting position (value 3) found in the grid.")    # Although I know there's a starting point but still these things seem to be cool towritting exception handling.

# Helper Function: get_drivable_neighbors
# Purpose: Look around a cell (up, down, left, right) and return those cells that are drivable (cels with values 0 or 3 ofc)
def get_drivable_neighbors(r, c):
    """Return 4-directional neighbors that are drivable (cells 0 or 3)."""
    neighbors = []
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        # Checking if the neighbor is within bounds and if it's a road (or the start)
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] in [0, 3]:
            neighbors.append((nr, nc))
    return neighbors

# Helper Function: compute_drivable_area
# Purpose: Starting from the start cell, explore every reachable drivable cell.
def compute_drivable_area(start):
    """Return the set of all cells (r,c) that are drivable and connected to the start."""
    seen = set()               # We keep track of visited cells (because repeating is so last season)
    stack = [start]            # Our adventure stack
    while stack:
        cell = stack.pop()
        if cell in seen:
            continue
        seen.add(cell)
        for nb in get_drivable_neighbors(*cell):
            if nb not in seen:
                stack.append(nb)
    return seen

# Computing the drivable area
drivable_area = compute_drivable_area(start)
if not drivable_area:
    raise ValueError("No drivable area found from the starting position.")   # Just pr

# Determining the extreme boundaries (min/max rows and columns) of the drivable area.
min_r = min(r for (r, c) in drivable_area)
max_r = max(r for (r, c) in drivable_area)
min_c = min(c for (r, c) in drivable_area)
max_c = max(c for (r, c) in drivable_area)

# With these extremas I aim to make check points, that is I let the car to reach the top lane, the right lane, the left lane which will will make sure of completing the whole around the track instead of making a small loop 
def update_mask(r, c, mask):
    if r == min_r+2:
        mask |= 1 << 0
    if r == max_r-2:
        mask |= 1 << 1
    if c == min_c+2:
        mask |= 1 << 2
    if c == max_c-2:
        mask |= 1 << 3
    return mask

# The target mask when all four checkpoints have been visited.
TARGET_MASK = (1 << 4) - 1  

# Motion Definitions: Cardinal Directions
# Purpose: Maping our numeric directions to row/column movements.
directions = {
    0: (0, 1),   # East: row unchanged, col increases
    1: (1, 0),   # South: row increases, col unchanged
    2: (0, -1),  # West:  row unchanged, col decreases
    3: (-1, 0)   # North: row decreases, col unchanged
}

def get_lateral_vector(d, lateral):
    """
    For a given forward direction d, return the lateral shift.
    lateral = -1: shift left (90° counterclockwise from forward)
    lateral =  1: shift right (90° clockwise from forward)
    lateral =  0: no lateral shift.
    """
    if lateral == 0:
        return (0, 0)
    dr, dc = directions[d]
    if lateral == -1:
        return (-dc, dr)
    elif lateral == 1:
        return (dc, -dr)

def is_drivable(r, c):
    # Returns True if cell (r, c) is drivable (0 or 3).
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return False
    return grid[r][c] in [0, 3]

# BFS Setup
# Limiting the maximum speed to avoid runaway states
max_speed = 5

# The state is represented as (row, col, speed, direction, lap_started, checkpoints_mask)
# - lap_started becomes True once we leave the starting cell.
# - checkpoints_mask records which extreme positions have been visited.
initial_mask = update_mask(start[0], start[1], 0)
initial_states = [(start[0], start[1], 0, d, False, initial_mask) for d in range(4)]

queue = deque()
visited = set()  # to store states we've seen
pred = {}        # to reconstruct the path

for state in initial_states:
    queue.append((state, 0))  # (state, move_count)
    visited.add(state)
    pred[state] = None

solution = None
solution_moves = None


# Main BFS Loop
while queue:
    state, moves = queue.popleft()
    r, c, speed, d, lap_started, mask = state

    # Checking lap completion:
    # The lap is complete if the car has left the start, returned to it with speed 0, and covered all the checkpoints
    if lap_started and (r, c) == start and speed == 0 and mask == TARGET_MASK and moves > 0:
        solution = state
        solution_moves = moves
        break

    # Trying all acceleration options: a in {-1, 0, 1}.
    for a in [-1, 0, 1]:
        new_speed = speed + a
        if new_speed < 0 or new_speed > max_speed:
            continue

        # As per the clarification mentioned we need to decrease the forward speed to 0 and take a other directional speed of 1, I made sure to check if the new speed is 0 then I can make a turn, i.e. change direction.
        if new_speed > 0:
            new_d_options = [d]
        else:
            new_d_options = [d, (d + 1) % 4]
        
        # Looping for every new direction possible, with the loop over lateral shifts
        for new_d in new_d_options:
            for lateral in [-1, 0, 1]:
                dr, dc = directions[new_d]
                lat_dr, lat_dc = get_lateral_vector(new_d, lateral)
                new_r = r + new_speed * dr + lat_dr
                new_c = c + new_speed * dc + lat_dc

                # Checking every cell along the forward path (to avoid "jumping" over obstacles)
                valid = True
                for step in range(1, new_speed + 1):
                    inter_r = r + step * dr
                    inter_c = c + step * dc
                    if not is_drivable(inter_r, inter_c):
                        valid = False
                        break
                if not valid:
                    continue

                # Checking the final cell (after lateral move)
                if not is_drivable(new_r, new_c):
                    continue

                # Updating the lap_started flag
                # It becomes True as soon as we leave the starting cell.
                new_lap_started = lap_started or ((r, c) == start and (new_r, new_c) != start) or ((r, c) != start)

                # Updating the checkpoint mask based on the new position.
                new_mask = update_mask(new_r, new_c, mask)

                # Defining the new state after the movement
                new_state = (new_r, new_c, new_speed, new_d, new_lap_started, new_mask)
                if new_state not in visited:
                    visited.add(new_state)
                    pred[new_state] = state
                    queue.append((new_state, moves + 1))


# Reconstructing the Resulting Path and Visualize on the Matrix

if solution is not None:
    # Reconstructing the list of grid positions (row, col) from the predecessor chain.
    path_positions = []
    s = solution
    while s is not None:
        r, c, sp, di, ls, cp = s
        path_positions.append((r, c))
        s = pred[s]
    path_positions.reverse()
    
    print("Number of moves:", solution_moves)
    
    # Creating a visual copy of the grid to should the resulting path
    # I just converted the numeric representations to symbols(Looks cooler!!)
    #   1 -> '#' (boundary)
    #   2 -> 'X' (obstacle)
    #   0 -> '.' (drivable)
    #   3 -> 'S' (start)
    visual_grid = []
    for row in grid:
        visual_row = []
        for cell in row:
            if cell == 1:
                visual_row.append('#')
            elif cell == 2:
                visual_row.append('X')
            elif cell == 3:
                visual_row.append('S')
            else:
                visual_row.append('.')
        visual_grid.append(visual_row)
    
    # Marking the path positions with '*' (except keep the starting cell as 'S').
    for (r, c) in path_positions:
        if visual_grid[r][c] == 'S':  # do not overwrite the start
            continue
        visual_grid[r][c] = '*'
    
    # Printing the visual grid.
    print("\nMatrix with path marked:")
    for row in visual_grid:
        print(" ".join(row))
else:
    print("No solution found.")


# Result

# The vehicle reaches start point with velocity one but making speed 0 doesn't make any physical step since making speed 0 means not moving at all in the next step.
# Since this step of making velocity 0 from 1 doesn't make any movement I didn't consider adding this.
# Adding this may increase the resultant value by 1.

#
'''
Number of moves: 17

Matrix with path marked:
# # # # # # # # # # #
# . . . . . . . . . #
# . . . X . . . . . #
# . . * * . * . . X #
# X * . # # # * * . #
# * . . # # # . . * #
# S . . # # # . . . #
# * . . # # # X X * #
# . * . # # # . * . #
# . . * # # # . * . #
# . X . . * . * . . #
# . . . . . X . . . #
# . . . . . . . . . #
# # # # # # # # # # #
'''


# Explaination of the movement

'''
1. start with upward velocity of 1
2. change direction to right and shift up
3. move right with velocity 1 and shift up
4. move right with velocity 1
5. move right with velocity 2
6. move right with velocity 1 and shift down
7. move right with velocity 1
8. change direction to down shift in right direction
9. move down with speed 2
10. move down with speed 1 and shift left
11. move down with speed 1
12. change direction to left and shift 1
13. move left with velocity 2
14. move left with velocity 2 and shift up
15. move left with velocity 1 and shift up
16. change direction to up and shift right
17. move up with velocity one
'''



