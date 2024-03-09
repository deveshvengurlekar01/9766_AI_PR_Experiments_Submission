def pour_water(state, action):
    x, y = state
    if action == 'fill_4':
        return (4, y)
    elif action == 'fill_3':
        return (x, 3)
    elif action == 'empty_4':
        return (0, y)
    elif action == 'empty_3':
        return (x, 0)
    elif action == 'pour_4_to_3':
        amount = min(x, 3 - y)
        return (x - amount, y + amount)
    elif action == 'pour_3_to_4':
        amount = min(y, 4 - x)
        return (x + amount, y - amount)
    else:
        return state

def dfs(state, visited):
    if state[0] == 2:
        return [state]
    visited.add(state)
    for action in ['fill_4', 'fill_3', 'empty_4', 'empty_3', 'pour_4_to_3', 'pour_3_to_4']:
        new_state = pour_water(state, action)
        if new_state not in visited:
            path = dfs(new_state, visited)
            if path:
                return [state] + path
    return None

def print_steps(path):
    for i, state in enumerate(path):
        jug_4, jug_3 = state
        print(f"Step {i+1}: Jug 4: {jug_4} gallons, Jug 3: {jug_3} gallons")

initial_state = (0, 0)
visited = set()
path = dfs(initial_state, visited)
if path:
    print("Steps to measure 2 gallons:")
    print_steps(path)
else:
    print("No solution found.")
