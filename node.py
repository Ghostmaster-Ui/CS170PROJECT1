class SearchNode:
    def __init__(self, current_state, previous_node=None, move=None, cost_so_far=0, heuristic_value=0):
        self.current_state = current_state
        self.previous_node = previous_node
        self.move = move
        
