'''
* This class provides the interactive GUI for the game
'''

import tkinter as tk
from puzzlemodel import puzzleModel
from time import sleep

class puzzleGUI(object):
    def __init__(self):
        self.root = tk.Tk()
        self.puzzle_frame = tk.Frame(self.root)
        self.puzzle_frame.pack()
        self.puzzle_model = puzzleModel()

        # puzzleGUI is going to initialize a puzzlemodel object and then
        # create buttons according to the initial puzzle state
        self.initialize_GUI()


        self.root.mainloop()

    def initialize_GUI(self):
        # Method should create the necessary buttons for the game and order
        # them according to the generated puzzle state

        self.solveBFSbutton = tk.Button(self.puzzle_frame, text = "Solve using BFS", padx=10, pady=10, command=self.solve_BFS)
        self.solveBFSbutton.grid(row=0, column=3)

        self.button_one = tk.Button(self.puzzle_frame, text="1", padx=20, pady=20, command=lambda: self.update_puzzle_state(1))
        self.button_two = tk.Button(self.puzzle_frame, text="2", padx=20, pady=20, command=lambda: self.update_puzzle_state(2))
        self.button_three = tk.Button(self.puzzle_frame, text="3", padx=20, pady=20, command=lambda: self.update_puzzle_state(3))
        self.button_four = tk.Button(self.puzzle_frame, text="4", padx=20, pady=20, command=lambda: self.update_puzzle_state(4))
        self.button_five = tk.Button(self.puzzle_frame, text="5", padx=20, pady=20, command=lambda: self.update_puzzle_state(5))
        self.button_six = tk.Button(self.puzzle_frame, text="6", padx=20, pady=20, command=lambda: self.update_puzzle_state(6))
        self.button_seven = tk.Button(self.puzzle_frame, text="7", padx=20, pady=20, command=lambda: self.update_puzzle_state(7))
        self.button_eight = tk.Button(self.puzzle_frame, text="8", padx=20, pady=20, command=lambda: self.update_puzzle_state(8))
        self.button_blank = tk.Button(self.puzzle_frame, padx=20, pady=20, bg="black")
        self.button_dict = {1:self.button_one,
                            2:self.button_two,
                            3:self.button_three,
                            4:self.button_four,
                            5:self.button_five,
                            6:self.button_six,
                            7:self.button_seven,
                            8:self.button_eight,
                            9:self.button_blank}

        self.update_display(self.puzzle_model.current_puzzle_state)

    def update_puzzle_state(self, button_pressed: int):
        # This method will update the backend puzzle state according
        # to the button pressed. This will require implementing
        # a function in the puzzle model class that takes in the button
        # pressed, validates the move, and then updates the puzzle state
        # maintained back there. This method will then call the update
        # diplay method (?)
        self.puzzle_model.update_puzzle_state_from_GUI(button_pressed)
        self.update_display(self.puzzle_model.current_puzzle_state)


    def update_display(self, puzzle_state: tuple):
        # This method will update the display based off of the 
        # current puzzle state (?)
            # I want this to also be able to display the winning
            # line that will be returned from the solve functions
        self.puzzle_frame.grid_forget()
        puzzle_state = list(puzzle_state)
        for row in range(3):
            for column in range(3):
                self.button_dict[puzzle_state.pop(0)].grid(row=row,column=column)
        self.puzzle_frame.update_idletasks()
        

    def solve_BFS(self):
        # This method will call the solve method of the puzzleModel
        # which will return the winning line. The winning line will
        # then be iterated through and each puzzle state will be 
        # displayed using the update_display method(?)
            # One issue I forsee is do I want update_display to take
            # in a puzzle state? Or just update based off of the puzzle
            # state of the model (which is global and would not need
            # be passed)
        winning_line = self.puzzle_model.solve_BFS()
        for state in winning_line:
            self.update_display(state)
            sleep(.2)

    def solve_DFS(self):
        pass

    def solve_astar(self):
        pass

    


