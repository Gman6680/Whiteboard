import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("Red Square Grid")

# Define the number of rows and columns in the grid
rows, cols = 2, 3

# Create a list to store the red square divs
red_squares = []

# Create red square divs and add them to the list
for i in range(rows * cols):
    red_square = tk.Frame(root, width=100, height=100, bg="red")
    red_squares.append(red_square)

# Arrange the red square divs in a grid
for i, red_square in enumerate(red_squares):
    row, col = divmod(i, cols)
    red_square.grid(row=row, column=col, padx=10, pady=10)

# Run the tkinter event loop
root.mainloop()
