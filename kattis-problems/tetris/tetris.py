from sys import stdin,stdout

orientations_of_pieces = {
  1 : [[0], [0, 0, 0, 0]], 
  2 : [[0, 0]],
  3 : [[0, 0, 1], [0, -1]],
  4 : [[0,-1, 0], [0, 1]],
  5 : [[0, 0, 0], [0, 1], [0,-1], [0, -1, 1]],
  6 : [[0, 0, 0], [0, 0], [0, 1, 0], [0, -2]],
  7 : [[0, 0, 0], [0, 0], [0, 2], [0, 0, -1]]
}

def tetris(columns,board,orientations):
  count = 0

  for i in range(columns):
    for orientation in orientations:
      if(i + len(orientation) <= columns):
        current_column = board[i]
        can_fit = True
        for j in range(len(orientation)):
          if((board[i+j]-current_column) != orientation[j]):
            can_fit = False
          current_column = board[i+j]
        if(can_fit):
          count+=1
  return count

data = [int(n) for n in stdin.readline().split(" ")]
board = [int(s) for s in stdin.readline().split(" ")]
stdout.write(str(tetris(data[0],board,orientations_of_pieces[data[1]])))
