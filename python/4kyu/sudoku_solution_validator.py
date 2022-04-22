def valid_solution(board):
  """
  board: matrix of 9x9 elements representing a sudoku grid
  return: if board is a valid sudoku or not
  """
  for row in board:
    if sorted(row) != [i for i in range(1, 10)]: # tests if rows contain every number
      return False
    for cell in range(len(row)): # tests if columns contain every number
      if sorted([i[cell] for i in board]) != [i for i in range(1, 10)]:
        return False

  # this is where it gets messy and complicated but i'll try to explain      
  for i in range(3): # this is for verifying that each square contains every number
    for j in range(3):
      sub_list = [board[3*i:3*i+3][k][3*j:3*j+3] for k in range(3)]
      # board[3*i:3*i+3] means that it selects the rows from 0 to 3, then from 3 to 6, etc.
      # [k] is the current row from those selected you're taking the elements of
      # [3*j:3*j+3] means you take the elt from 0 to 3, then from 3 to 6, etc. from the k row of those selected
      # it ends up analzing square from left to right, from top to bottom
      sub_square = []
      for elt in sub_list:
        sub_square += [*elt] # just makes a list out of the element of the sub_list
      if sorted(sub_square) != [i for i in range(1,10)]: # tests if there are every number in the sub_square
        return False
  return True

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]))