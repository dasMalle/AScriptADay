
game= [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]


def Winner(g, p):
    if g[1][1] == p:
        return (g[0][0] == p and g[2][2] == p) \
               or (g[1][0] == p and g[1][2] == p) \
               or (g[0][1] == p and g[2][1] == p)\
               or (g[0][2] == p and g[2][0] == p)
    else:
        return (g[0][0] == p and g[0][1] == p and g[0][2])\
               or (g[0][0] == p and g[2][1] == p and g[2][2])\
               or (g[0][0] == p and g[1][0] == p and g[2][0])\
               or (g[0][2] == p and g[1][2] == p and g[2][2])\


print("Welcome, please input your move as row, column")
for i in range(9):
    if i%2 == 0:  # player X
        print("player X: ")
        row, column = input().split(",")
        game[int(row)][int(column)] = "X"
        if Winner(game, "X"):
            print("X, won")
            break
    else:
        print("Player Q")
        row, column = input().split(",")
        game[int(row)][int(column)] = "Q"
        if Winner(game, "Q"):
            print("Q won")
            break
    print(str(game[0])+"\n" + str(game[1])+"\n"+str(game[2]))

print(str(game[0])+"\n" + str(game[1])+"\n"+str(game[2]))

