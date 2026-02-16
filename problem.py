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

    