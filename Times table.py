character_name = "Tomas"
x_pos = 5
speed = 2.5
is_game_over = False

print(type(x_pos))

for i in range(10):
    if i!=0:
        for j in range(10):
            if j!=0:
                print(i, "x", j, "=", i*j)
