import random

class Problem:
    def __init__(self, initial_state_tuple):
        self.initial_state = initial_state_tuple
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    @staticmethod
    def create_random_puzzle():
        tiles = list(range(9))
        random.shuffle(tiles)
        return tuple(tiles)

    @staticmethod
    def get_user_puzzle():
        print("\nEnter your 9 puzzle numbers (0-8), separated by spaces,")
        print("entering them row by row, e.g., '1 2 3 4 5 6 7 8 0'.")

        while True:
            try:
                line = input("Enter 9 numbers: ")
                full_list = [int(n) for n in line.split()]

                if len(full_list) != 9:
                    print("Error: You must enter exactly 9 numbers.")
                    continue

                if set(full_list) != set(range(9)):
                    print("Error: Puzzle must contain all numbers 0 through 8 exactly once.")
                    continue

                return tuple(full_list)

            except ValueError:
                print("Invalid input. Please ensure all entries are valid integers.")

    def is_goal(self, state):
        return state == self.goal_state

    def get_successors(self, state):
        successors = []
        index = state.index(0)
        row, col = divmod(index, 3)

        moves = {
            'up': (row - 1, col),
            'down': (row + 1, col),
            'left': (row, col - 1),
            'right': (row, col + 1)
        }

        for action, (r, c) in moves.items():
            if 0 <= r < 3 and 0 <= c < 3:
                new_index = r * 3 + c
                new_state = list(state)

                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                successors.append((action, tuple(new_state)))

        return successors

    @staticmethod
    def get_trace_puzzle():
        return (1, 0, 3, 4, 2, 6, 7, 5, 8)
