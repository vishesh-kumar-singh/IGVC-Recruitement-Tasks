

# This is not my Submission File!! Check the other file in this folder for evaluation

'''
This had been a **failed** approach of mine.

Either due to computational expense or maybe due to some error in code this program ran for about 30 minutes still didn't gave any output!!
But still wanted to share this.

Here i just tried to build a tree kind of algorithm.
The plan was to make a tree with root node as the starting point and splitting in all possible movements by checking if the movement is possible.
I manually measured distance on a randomly chosen path by me and it turned out that the distance was 30. For any movement with minimum steps it will be either less than or equal to that, by that I limited the depth of tree, that is did pruning of tree after that
by this I planned to get the leaf values for all the paths and velocity combination
further I tried to recursively get the one with Minimum no. of steps.
'''



# This is not my Submission File!! Check the other file in this folder for evaluation






import numpy as np
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

Map=array.reshape(14,11).astype(int)
print("The Map\n",Map)

for i in range(14):
    for j in range(11):
        if Map[i][j] == 3:
            start_r, start_c = i, j
            break



def is_turn_downright(i, j, v, dir):
    try:
        value = True
        for k in range(1, v):
            if dir == "u" and Map[i-k, j] != 0:
                value = False
            elif dir == "d" and Map[i+k, j] != 0:
                value = False
            elif dir == "l" and Map[i, j-k] != 0:
                value = False
            elif dir == "r" and Map[i, j+k] != 0:
                value = False
        if dir == "u" and Map[i-v+1, j+1] != 0:
            value = False
        elif dir == "d" and Map[i+v-1, j-1] != 0:
            value = False
        elif dir == "l" and Map[i-1, j-v+1] != 0:
            value = False
        elif dir == "r" and Map[i+1, j+v-1] != 0:
            value = False
        return value
    except IndexError:
        return False

def is_turn_constright(i, j, v, dir):
    try:
        value = True
        for k in range(1, v+1):
            if dir == "u" and Map[i-k, j] != 0:
                value = False
            elif dir == "d" and Map[i+k, j] != 0:
                value = False
            elif dir == "l" and Map[i, j-k] != 0:
                value = False
            elif dir == "r" and Map[i, j+k] != 0:
                value = False
        if dir == "u" and Map[i-v, j+1] != 0:
            value = False
        elif dir == "d" and Map[i+v, j-1] != 0:
            value = False
        elif dir == "l" and Map[i-1, j-v] != 0:
            value = False
        elif dir == "r" and Map[i+1, j+v] != 0:
            value = False
        return value
    except IndexError:
        return False

def is_turn_upright(i, j, v, dir):
    try:
        value = True
        for k in range(1, v+2):
            if dir == "u" and Map[i-k, j] != 0:
                value = False
            elif dir == "d" and Map[i+k, j] != 0:
                value = False
            elif dir == "l" and Map[i, j-k] != 0:
                value = False
            elif dir == "r" and Map[i, j+k] != 0:
                value = False
        if dir == "u" and Map[i-v-1, j+1] != 0:
            value = False
        elif dir == "d" and Map[i+v+1, j-1] != 0:
            value = False
        elif dir == "l" and Map[i-1, j-v-1] != 0:
            value = False
        elif dir == "r" and Map[i+1, j+v+1] != 0:
            value = False
        return value
    except IndexError:
        return False

def is_turn_downleft(i, j, v, dir):
    try:
        value = True
        for k in range(1, v):
            if dir == "u" and Map[i-k, j] != 0:
                value = False
            elif dir == "d" and Map[i+k, j] != 0:
                value = False
            elif dir == "l" and Map[i, j-k] != 0:
                value = False
            elif dir == "r" and Map[i, j+k] != 0:
                value = False
        if dir == "u" and Map[i-v+1, j-1] != 0:
            value = False
        elif dir == "d" and Map[i+v-1, j+1] != 0:
            value = False
        elif dir == "l" and Map[i+1, j-v+1] != 0:
            value = False
        elif dir == "r" and Map[i-1, j+v-1] != 0:
            value = False
        return value
    except IndexError:
        return False

def is_turn_constleft(i, j, v, dir):
    try:
        value = True
        for k in range(1, v+1):
            if dir == "u" and Map[i-k, j] != 0:
                value = False
            elif dir == "d" and Map[i+k, j] != 0:
                value = False
            elif dir == "l" and Map[i, j-k] != 0:
                value = False
            elif dir == "r" and Map[i, j+k] != 0:
                value = False
        if dir == "u" and Map[i-v, j-1] != 0:
            value = False
        elif dir == "d" and Map[i+v, j+1] != 0:
            value = False
        elif dir == "l" and Map[i+1, j-v] != 0:
            value = False
        elif dir == "r" and Map[i-1, j+v] != 0:
            value = False
        return value
    except IndexError:
        return False

def is_turn_upleft(i, j, v, dir):
    try:
        value = True
        for k in range(1, v+2):
            if dir == "u" and Map[i-k, j] != 0:
                value = False
            elif dir == "d" and Map[i+k, j] != 0:
                value = False
            elif dir == "l" and Map[i, j-k] != 0:
                value = False
            elif dir == "r" and Map[i, j+k] != 0:
                value = False
        if dir == "u" and Map[i-v-1, j-1] != 0:
            value = False
        elif dir == "d" and Map[i+v+1, j+1] != 0:
            value = False
        elif dir == "l" and Map[i+1, j-v-1] != 0:
            value = False
        elif dir == "r" and Map[i-1, j+v+1] != 0:
            value = False
        return value
    except IndexError:
        return False

def is_turn_left(v, i, j):
    try:
        if v == 1 or v == 0:
            if dir == "l" and Map[i+1, j] == 0:
                return True
            elif dir == "r" and Map[i-1, j] == 0:
                return True
            elif dir == "u" and Map[i, j-1] == 0:
                return True
            elif dir == "d" and Map[i, j+1] == 0:
                return True
        return False
    except IndexError:
        return False

def is_turn_right(v, i, j):
    try:
        if v == 1 or v == 0:
            if dir == "l" and Map[i-1, j] == 0:
                return True
            elif dir == "r" and Map[i+1, j] == 0:
                return True
            elif dir == "u" and Map[i, j+1] == 0:
                return True
            elif dir == "d" and Map[i, j-1] == 0:
                return True
        return False
    except IndexError:
        return False

def is_moveup(i, j, v, dir):
    try:
        value = True
        for k in range(1, v+2):
            if dir == "u" and Map[i-k, j] != 0:
                value = False
            elif dir == "d" and Map[i+k, j] != 0:
                value = False
            elif dir == "l" and Map[i, j-k] != 0:
                value = False
            elif dir == "r" and Map[i, j+k] != 0:
                value = False
        return value
    except IndexError:
        return False

def is_const(i, j, v, dir):
    try:
        if dir == "u" and Map[i-1, j] != 0:
            return False
        elif dir == "d" and Map[i+1, j] != 0:
            return False
        elif dir == "l" and Map[i, j-1] != 0:
            return False
        elif dir == "r" and Map[i, j+1] != 0:
            return False
        return True
    except IndexError:
        return False

def is_movedown(v):
    if v==0:
        return False
    else:
        return True
    
def is_wrong(i,j,v,dir,steps):
        if steps >= 30:
            return True
        elif [i, j] == [start_r, start_c] and v == 0 and steps!=0:
            return True
        elif 3 < j < 7 and 0 < i < 4 and dir=="l":    # region to go right
            return True
        elif 0 < j < 4 and 3 < i < 10 and dir=="d":   # region to go up
            return True
        elif 3 < j < 7 and 9 < i < 13 and dir=="r":   # region to go left
            return True
        elif 6 < j < 10 and 3 < i < 10 and dir=="u":   # region to go down
            return True
        elif v==2:
            if dir == "u" and Map[i-1, j] != 0:
                return True
            elif dir == "d" and Map[i+1, j] != 0:
                return True
            elif dir == "l" and Map[i, j-1] != 0:
                return True
            elif dir == "r" and Map[i, j+1] != 0:
                return True
        elif v == 3:
            if dir == "u" and (Map[i-1, j] != 0 or Map[i-2, j] != 0):
                return True
            elif dir == "d" and (Map[i+1, j] != 0 or Map[i+2, j] != 0):
                return True
            elif dir == "l" and (Map[i, j-1] != 0 or Map[i, j-2] != 0):
                return True
            elif dir == "r" and (Map[i, j+1] != 0 or Map[i, j+2] != 0):
                return True
        else:
            return False
    
def loop_complete(i,j,v,steps):
    if [i, j] == [start_r, start_c] and v == 1 and steps!=0:
        return True

class Node:
    def __init__(self, i, j, v, dir, const=None, mul=None, mur=None, mdl=None, mdr=None, mcl=None, mcr=None, mu=None, md=None, l=None, r=None, steps=0, past=[]):
        self.i = i
        self.j = j
        self.v = v
        self.dir = dir
        self.const = const
        self.mul = mul
        self.mur = mur
        self.mdl = mdl
        self.mdr = mdr
        self.mcl = mcl
        self.mcr = mcr
        self.mu = mu
        self.md = md
        self.l = l
        self.r = r
        self.steps = steps
        self.past = past + [[self.i, self.j]]

    def is_leaf(self):
        return self.steps is not None
    

    

class Tree:
    def __init__(self,Map):
        self.Map=Map
        self.start=None

    def Begin(self,i,j,v,dir,steps,past):
        if is_wrong(i,j,v,dir,steps):   # Cases where it gets crashed or have moved more than 30 steps
            return Node(i,j,v,dir,steps=30)
        elif loop_complete(i,j,v,steps):
            return Node(i,j,v,dir,steps=steps)
        else:
            if is_turn_constleft(i, j, v, dir):
                new_past=past[:]
                if dir == "u":
                    new_past.append([i-v, j-1])
                    mcl = self.Begin(i-v, j-1, v, "u", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i+v, j+1])
                    mcl = self.Begin(i+v, j+1, v, "d", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i+1, j-v])
                    mcl = self.Begin(i+1, j-v, v, "l", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i-1, j+v])
                    mcl = self.Begin(i-1, j+v, v, "r", steps+1, new_past)
            else:
                mcl=None
            if is_turn_constright(i, j, v, dir):
                new_past=past[:]
                if dir == "u":
                    new_past.append([i-v, j+1])
                    mcr = self.Begin(i-v, j+1, v, "u", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i+v, j-1])
                    mcr = self.Begin(i+v, j-1, v, "d", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i-1, j-v])
                    mcr = self.Begin(i-1, j-v, v, "l", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i+1, j+v])
                    mcr = self.Begin(i+1, j+v, v, "r", steps+1, new_past)
            else:
                mcr=None
            if is_const(i, j, v, dir):
                new_past = past[:]
                if dir == "u":
                    new_past.append([i-v, j])
                    const = self.Begin(i-v, j, v, "u", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i+v, j])
                    const = self.Begin(i+v, j, v, "d", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i, j-v])
                    const = self.Begin(i, j-v, v, "l", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i, j+v])
                    const = self.Begin(i, j+v, v, "r", steps+1, new_past)
            else:
                const=None
            if is_moveup(i, j, v, dir):
                new_past=past[:]
                if dir == "u":
                    new_past.append([i-v-1, j])
                    mu = self.Begin(i-v-1, j, v+1, "u", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i+v+1, j])
                    mu = self.Begin(i+v+1, j, v+1, "d", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i, j-v-1])
                    mu = self.Begin(i, j-v-1, v+1, "l", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i, j+v+1])
                    mu = self.Begin(i, j+v+1, v+1, "r", steps+1, new_past)
            else:
                mu=None

            if is_movedown(v):
                new_past=past[:]
                if dir == "u":
                    new_past.append([i-v+1, j])
                    md = self.Begin(i-v+1, j, v-1, "u", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i+v-1, j])
                    md = self.Begin(i+v-1, j, v-1, "d", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i, j-v+1])
                    md = self.Begin(i, j-v+1, v-1, "l", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i, j+v-1])
                    md = self.Begin(i, j+v-1, v-1, "r", steps+1, new_past)
            else:
                md=None
            if is_turn_upleft(i, j, v, dir):
                new_past = past[:]
                if dir == "u":
                    new_past.append([i-v-1, j-1])
                    mul = self.Begin(i-v-1, j-1, v+1, "u", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i+v+1, j+1])
                    mul = self.Begin(i+v+1, j+1, v+1, "d", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i+1, j-v-1])
                    mul = self.Begin(i+1, j-v-1, v+1, "l", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i-1, j+v+1])
                    mul = self.Begin(i-1, j+v+1, v+1, "r", steps+1, new_past)
            else:
                mul = None

            if is_turn_downleft(i, j, v, dir):
                new_past = past[:]
                if dir == "u":
                    new_past.append([i-v+1, j-1])
                    mdl = self.Begin(i-v+1, j-1, v-1, "u", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i+v-1, j+1])
                    mdl = self.Begin(i+v-1, j+1, v-1, "d", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i+1, j-v+1])
                    mdl = self.Begin(i+1, j-v+1, v-1, "l", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i-1, j+v-1])
                    mdl = self.Begin(i-1, j+v-1, v-1, "r", steps+1, new_past)
            else:
                mdl = None
            if is_turn_downright(i, j, v, dir):
                new_past = past[:]
                if dir == "u":
                    new_past.append([i-v+1, j+1])
                    mdr = self.Begin(i-v+1, j+1, v-1, "u", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i+v-1, j-1])
                    mdr = self.Begin(i+v-1, j-1, v-1, "d", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i-1, j-v+1])
                    mdr = self.Begin(i-1, j-v+1, v-1, "l", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i+1, j+v-1])
                    mdr = self.Begin(i+1, j+v-1, v-1, "r", steps+1, new_past)
            else:
                mdr = None

            if is_turn_upright(i, j, v, dir):
                new_past = past[:]
                if dir == "u":
                    new_past.append([i-v-1, j+1])
                    mur = self.Begin(i-v-1, j+1, v+1, "u", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i+v+1, j-1])
                    mur = self.Begin(i+v+1, j-1, v+1, "d", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i-1, j-v-1])
                    mur = self.Begin(i-1, j-v-1, v+1, "l", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i+1, j+v+1])
                    mur = self.Begin(i+1, j+v+1, v+1, "r", steps+1, new_past)
            else:
                mur = None

            if is_turn_left(v, i, j):
                new_past = past[:]
                if dir == "u":
                    new_past.append([i, j-1])
                    l = self.Begin(i, j-1, v, "l", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i, j+1])
                    l = self.Begin(i, j+1, v, "r", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i+1, j])
                    l = self.Begin(i+1, j, v, "d", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i-1, j])
                    l = self.Begin(i-1, j, v, "u", steps+1, new_past)
            else:
                l = None

            if is_turn_right(v, i, j):
                new_past = past[:]
                if dir == "u":
                    new_past.append([i, j+1])
                    r = self.Begin(i, j+1, v, "r", steps+1, new_past)
                elif dir == "d":
                    new_past.append([i, j-1])
                    r = self.Begin(i, j-1, v, "l", steps+1, new_past)
                elif dir == "l":
                    new_past.append([i-1, j])
                    r = self.Begin(i-1, j, v, "u", steps+1, new_past)
                elif dir == "r":
                    new_past.append([i+1, j])
                    r = self.Begin(i+1, j, v, "d", steps+1, new_past)
            else:
                r = None

            return Node(i, j, v, dir, const, mul, mur, mdl, mdr, mcl, mcr, mu, md, l, r,past=past)
        
    def drive(self):
        self.start=self.Begin(start_r,start_c,v=0,dir="u",steps=0,past=[])
    
    def find_min_steps_leaf(self, node, min_steps_leaf=None):
    # Base case: if the node is a leaf (no children), return it if it has the minimum steps
        if node.is_leaf():
            if min_steps_leaf is None or node.steps < min_steps_leaf.steps:
                return node
            else:
                return min_steps_leaf
    
    # Recursively check all children
        children = [node.const, node.mul, node.mur, node.mdl, node.mdr, node.mcl, node.mcr, node.mu, node.md, node.l, node.r]
        for child in children:
            if child is not None:
                min_steps_leaf = self.find_min_steps_leaf(child, min_steps_leaf)

        return min_steps_leaf

# After building the tree, find the leaf node with the minimum steps
tree = Tree(Map)
tree.drive()
min_leaf = tree.find_min_steps_leaf(tree.start)

# Retrieve the path and steps
if min_leaf:
    print(f"Minimum steps: {min_leaf.steps}")
    print(f"Path: {min_leaf.past}")
else:
    print("No valid path found.")
