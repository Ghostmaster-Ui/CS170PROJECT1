import heapq
from node import SearchNode


"""
SearchAlgos class contains all search strategies
for solving the 8-puzzle problem.
"""

class SearchAlgos:

    def __init__(self, puzzle_instance):
        self.problem = puzzle_instance
        self.start_state = puzzle_instance.initial_state
        self.goal_state = puzzle_instance.goal_state

        self.visited = set()
        self.expanded_count = 0
        self.largest_frontier = 1


    
    def uniform_cost_search(self):

        self.visited.clear()
        self.expanded_count = 0
        self.largest_frontier = 1

        start_node = SearchNode(self.start_state)
        frontier = [start_node]
        heapq.heapify(frontier)

        self.visited.add(start_node.current_state)

        while frontier:

            self.largest_frontier = max(self.largest_frontier, len(frontier))
            node = heapq.heappop(frontier)
            self.expanded_count += 1

            board = node.current_state
            print(f"Expanding node with g(n)={node.cost_so_far}")

            for i in range(0, len(board), 3):
                print(board[i:i+3])

            if self.problem.is_goal(board):
                stats = {
                    "nodes_expanded": self.expanded_count,
                    "max_queue_size": self.largest_frontier,
                    "depth": node.cost_so_far
                }
                return node, stats

            for move, new_state in self.problem.get_successors(board):
                if new_state not in self.visited:
                    child = SearchNode(
                        current_state=new_state,
                        previous_node=node,
                        move=move,
                        cost_so_far=node.cost_so_far + 1
                    )
                    heapq.heappush(frontier, child)
                    self.visited.add(new_state)


    
    def astar_manhattan(self):

        self.visited.clear()
        self.expanded_count = 0
        self.largest_frontier = 1

        def manhattan_distance(state):
            total = 0
            for tile in range(1, 9): 
                r1, c1 = divmod(state.index(tile), 3)
                r2, c2 = divmod(self.goal_state.index(tile), 3)
                total += abs(r1 - r2) + abs(c1 - c2)
            return total

        start_node = SearchNode(
            current_state=self.start_state,
            cost_so_far=0,
            heuristic_value=manhattan_distance(self.start_state)
        )

        frontier = [start_node]
        heapq.heapify(frontier)

        while frontier:

            self.largest_frontier = max(self.largest_frontier, len(frontier))
            node = heapq.heappop(frontier)
            self.expanded_count += 1

            board = node.current_state
            g = node.cost_so_far
            h = node.heuristic_value

            print(f"Expanding node with g(n)={g} and h(n)={h}")

            for i in range(0, len(board), 3):
                print(board[i:i+3])

            if self.problem.is_goal(board):
                stats = {
                    "nodes_expanded": self.expanded_count,
                    "max_queue_size": self.largest_frontier,
                    "depth": g
                }
                return node, stats

            self.visited.add(board)

            for move, new_state in self.problem.get_successors(board):
                if new_state not in self.visited:
                    child = SearchNode(
                        current_state=new_state,
                        previous_node=node,
                        move=move,
                        cost_so_far=g + 1,
                        heuristic_value=manhattan_distance(new_state)
                    )
                    heapq.heappush(frontier, child)


   
    