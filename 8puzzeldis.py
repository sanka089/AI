def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def find_blank(state):
    return state.index(-1)

def is_goal(state, target):
    return state == target

def actions(state):
    blank_index = find_blank(state)
    possible_actions = []

    if blank_index not in [0, 1, 2]:
        possible_actions.append(-3)     
    if blank_index not in [6, 7, 8]:
        possible_actions.append(3)  
    if blank_index not in [0, 3, 6]:
        possible_actions.append(-1)  
    if blank_index not in [2, 5, 8]:
        possible_actions.append(1)   

    return possible_actions

def apply_action(state, action):
    blank_index = find_blank(state)
    new_state = state.copy()
    new_state[blank_index], new_state[blank_index + action] = new_state[blank_index + action], new_state[blank_index]
    return new_state

def depth_limited_dfs(src, target, depth_limit, path=[]):
    if depth_limit < 0:
        return None
    if src == target:
        return path + [src]

    for action in actions(src):
        new_state = apply_action(src, action)
        result = depth_limited_dfs(new_state, target, depth_limit - 1, path + [src])
        if result:
            return result

    return False

def iddfs(src, target, max_depth):
    for depth_limit in range(max_depth + 1):
        result = depth_limited_dfs(src, target, depth_limit)
        if result:
            return result
    return False

src1 = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target1 = [1, 2, 3, 4, 5, -1, 6, 7, 8]
depth1 = 1
print(iddfs(src1, target1, depth1))  

src2 = [3, 5, 2, 8, 7, 6, 4, 1, -1]
target2 = [-1, 3, 7, 8, 1, 5, 4, 6, 2]
depth2 = 1
print(iddfs(src2, target2, depth2)) 

src3 = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target3 = [1, 2, 3, 6, 4, 5, -1, 7, 8]
depth3 = 1
print(iddfs(src3, target3, depth3))  
