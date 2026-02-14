class SearchNode:
    def __init__(self, current_state, previous_node=None, move=None, cost_so_far=0, heuristic_value=0):
        self.current_state = current_state
        self.previous_node = previous_node
        self.move = move
        self.cost_so_far = cost_so_far
        self.heuristic_value = heuristic_value
        self.total_cost = cost_so_far + heuristic_value
