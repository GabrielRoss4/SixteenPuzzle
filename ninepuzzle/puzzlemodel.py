'''
* This class maintains the puzzle state according to manual moves from the GUI
  and also houses the code for all solving algorithms
'''

import puzzleGUI
from random import randint
from copy import copy
from math import sqrt
from puzzlehelpers import queue, stack


class puzzleModel(object):
    def __init__(self):
        self.ordered_state = (1,2,3,4,5,6,7,8,9)
        self.max_moves = 35
        # Randomizes puzzle using self.max_moves number of valid moves
        self.puzzle_start = self.randomize_puzzle([1,2,3,4,5,6,7,8,9])
        # Create a copy of the beginning state so that we can retrace
        # the winning line from ordered to beginning state when solving
        self.current_puzzle_state = tuple(copy(self.puzzle_start))
        #self.puzzleGUI(self)

        
    def __find_blank_index(self, puzzle_state):
        return puzzle_state.index(9)

    def __swap_index(self, puzzle_state, index_to_swap):
        index_value = puzzle_state[index_to_swap]
        blank_index = self.__find_blank_index(puzzle_state)
        new_board_state = list(puzzle_state)
        new_board_state[blank_index] = index_value
        new_board_state[index_to_swap] = 9

        return tuple(new_board_state)

    def update_puzzle_state_from_GUI(self, button_pressed: int):
        # This method will take in the button pressed on the GUI
        # and will validate the move and then update the global
        # current puzzle state
        valid_states = self.adjacent_states(self.current_puzzle_state)
        attempted_move = self.__swap_index(self.current_puzzle_state, self.current_puzzle_state.index(button_pressed))
        if attempted_move in valid_states:
            self.current_puzzle_state = attempted_move

    def move_up(self, local_state):
        local_state = copy(local_state)
        blank_index = self.__find_blank_index(local_state)
        if (blank_index < 3):
            return False
        return self.__swap_index(local_state, blank_index-3)

    def move_down(self, local_state):
        local_state = copy(local_state)
        blank_index = self.__find_blank_index(local_state)
        if (blank_index > 5):
            return False
        return self.__swap_index(local_state, blank_index+3)
    
    def move_left(self, local_state):
        local_state = copy(local_state)
        blank_index = self.__find_blank_index(local_state)
        if (blank_index in [0,3,6]):
            return False
        return self.__swap_index(local_state, blank_index-1)

    def move_right(self, local_state):
        local_state = copy(local_state)
        blank_index = self.__find_blank_index(local_state)
        if (blank_index in [2,5,8]):
            return False
        return self.__swap_index(local_state, blank_index+1)

    def adjacent_states(self, puzzle_state):
        states = [self.move_up, self.move_down, self.move_left, self.move_right]
        valid_states = []
        for func in states:
            state = func(puzzle_state)
            if state:
                valid_states.append(state)

        return valid_states

    def random_move(self, puzzle_state, previous_state):
        adjacent_states = self.adjacent_states(puzzle_state)
        valid_states = []
        for state in adjacent_states:
            if state != previous_state:
                valid_states.append(state)

        random_state = valid_states[randint(0,len(valid_states)-1)]
        return random_state

    def randomize_puzzle(self, ordered_puzzle):
        current_state = ordered_puzzle
        previous_state = None
        for i in range(self.max_moves):
            new_state = self.random_move(current_state, previous_state)
            previous_state = current_state
            current_state = new_state
        return current_state

    def solve_BFS(self):

        to_visit = queue()
        visited_set = set()
        dequeued_set = set()
        predecessor_node = {}
        dist = {}

        start = self.current_puzzle_state
        to_visit.enqueue(start)
        visited_set.add(start)
        predecessor_node[start] = start
        dist[start] = 0

        too_far = False
        found_winning_state = (start == self.ordered_state)

        while (not to_visit.empty() and not found_winning_state and not too_far):

            cur_state = to_visit.dequeue()

            if (cur_state in dequeued_set):
                print("Dequeued a node twice")
                break
            else:
                dequeued_set.add(cur_state)

            # Want to update the puzzle GUI here

            adjacent_states = self.adjacent_states(cur_state)

            for state in adjacent_states:
                if state not in visited_set:
                    predecessor_node[state] = cur_state
                    dist[state] = dist[cur_state] + 1
                    if state == self.ordered_state:
                        found_winning_state = True
                        break
                    if dist[state] > self.max_moves:
                        print("The maximum distance a state can be from the start has been exceeded. There is no solution.")
                        too_far = True
                        break
                    visited_set.add(state)
                    to_visit.enqueue(state)

        # Prints the winning line of board states using the predecessor dict
        if found_winning_state:
            print(f"Found the winning state. It was {dist[self.ordered_state]} moves away!")
            winning_line = []
            cur_state = self.ordered_state
            while state != predecessor_node[state]:
                winning_line.insert(0, state)
                state = predecessor_node[state]

            print(f"Winning line: {winning_line}")
            return winning_line
        return []
