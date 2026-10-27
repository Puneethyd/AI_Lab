def vacuum_agent(location, status_A, status_B):
    if location == 'A' and status_A == 'Dirty':
        return 'SUCK'
    elif location == 'B' and status_B == 'Dirty':
        return 'SUCK'
    elif status_A == 'Dirty':
        return 'LEFT'
    elif status_B == 'Dirty':
        return 'RIGHT'
    else:
        return 'NO-OP'

def vacuum_simulation(location, status_A, status_B):
    while True:
        action = vacuum_agent(location, status_A, status_B)
        
        if action == 'NO-OP':
            print(f"Action: {action:<5} | Location={location}, A={status_A:<5}, B={status_B:<5}")
            break
            
        if action == 'SUCK' and location == 'A':
            status_A = 'Clean'
        elif action == 'SUCK' and location == 'B':
            status_B = 'Clean'
        elif action == 'LEFT':
            location = 'A'
        elif action == 'RIGHT':
            location = 'B'
            
        print(f"Action: {action:<5} | Location={location}, A={status_A:<5}, B={status_B:<5}")
        
    print(f"Final State : Location={location}, A={status_A}, B={status_B}")

if __name__ == "__main__":
    print("--- Test Case 1 ---")
    vacuum_simulation('A', 'Dirty', 'Dirty')

    print("\n--- Test Case 2 ---")
    vacuum_simulation('A', 'Clean', 'Dirty')

    print("\n--- Test Case 3 ---")
    vacuum_simulation('B', 'Clean', 'Clean')

    print("\n--- Test Case 4 ---")
    vacuum_simulation('B', 'Dirty', 'Dirty')

    print("\n--- Test Case 5 ---")
    vacuum_simulation('B', 'Dirty', 'Clean')

    print("\n--- Test Case 6 ---")
    vacuum_simulation('B', 'Clean', 'Dirty')

    print("\n--- Test Case 7 ---")
    vacuum_simulation('A', 'Clean', 'Clean')
