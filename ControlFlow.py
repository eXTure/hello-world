is_game_over = False
p_0_x_pos = 0
e_0_x_pos = 3
e_1_x_pos = 5

p_0_x_pos += 2
if p_0_x_pos == e_0_x_pos or p_0_x_pos == e_1_x_pos:
    is_game_over = True
else:
    e_0_x_pos += 1
    e_1_x_pos += 1


print(is_game_over)

is_game_over = False
p_x_pos = 2
e_x_pos = 3
end_x_pos = 10

while not is_game_over:
    print(p_x_pos)
    print(e_x_pos)
    if p_x_pos == e_x_pos:
        is_game_over = True
        print("You lose")
    elif p_x_pos >= end_x_pos:
        is_game_over = True
        print("You win")
    else:
        p_x_pos += 3
        e_x_pos += 1

x_pos = 5
movements = [1, -5, 4, 9, -3]

for movement in movements:
    x_pos += movement
print(x_pos)
