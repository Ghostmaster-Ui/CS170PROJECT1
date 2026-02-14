from search_algos import SearchAlgos
from problem import Problem

"""
Driver program for the 8-puzzle solver
"""

def run_solver():
    print("Welcome to the 8-Puzzle Solver")
    print("Press 1 to use default puzzle")
    print("Press 2 to input your own puzzle")

    user_option = input("Selection: ")

    if user_option == '1':
        start_state = Problem.get_trace_puzzle()
    elif user_option == '2':
        start_state = Problem.get_user_puzzle()
    else:
        print("Invalid selection. Generating random puzzle...")
        start_state = Problem.create_random_puzzle()

    problem_instance = Problem(start_state)
    search_engine = SearchAlgos(problem_instance)

    print("\nInitial Configuration:")

    state_display = problem_instance.initial_state
    index = 0
    while index < len(state_display):
        print(state_display[index:index + 3])
        index += 3

    print("\nChoose Algorithm:")
    print("1 - Uniform Cost Search")
    print("2 - A* (Misplaced Tile)")
    print("3 - A* (Euclidean Distance)")

    algorithm_option = input("Selection: ")

    if algorithm_option == '1':
        result_node, metrics = search_engine.uniform_cost_search()
    elif algorithm_option == '2':
        result_node, metrics = search_engine.astar_misplaced()
    elif algorithm_option == '3':
        result_node, metrics = search_engine.astar_euclidean()
    else:
        print("Invalid algorithm choice.")
        return

    if result_node is not None:
        print("\nSolution Found!")
        print(f"Solution Depth: {metrics['depth']}")
        print(f"Total Nodes Expanded: {metrics['nodes_expanded']}")
        print(f"Maximum Queue Size: {metrics['max_queue_size']}")
    else:
        print("No solution could be found.")


if __name__ == "__main__":
    run_solver()
