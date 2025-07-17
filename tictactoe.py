board=[" "]*9
def show():
    print("\n"+"\n".join(["|".join(board[i:i+3]) for i in range(0,9,3)])) 

def win(p):return any(all(board[i]==p for i in line) for line in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])

p="X"

for _ in range(9):
    show()
    move=int(input(f"{p} move(0-8):"))
    if board[move]!= " ": print("taken");continue
    board[move]=p
    if win(p): show(); print(f"{p} wins!"); break
    p="O" if p=="X" else "X"
else:
    show();print("Draw!")
    