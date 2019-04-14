width = 800
height = 400
color = (255, 255, 0)
# data_something is [pos_x, pos_y, size_x, size_y, vel_x, vel_y, max_vel_x, max_vel_y, name, color]
data_player_one = [width * 0.1, height * 0.4375, width * 0.0125, height * 0.125, 0, 0, 5, 5, "player", color]
data_player_two = [width * 0.9, height * 0.4375, width * 0.0125, height * 0.125, 0, 0, 5, 5, "player", color]
data_ball = [width * 0.4875, height * 0.475, width * 0.025, height * 0.05, 0, 3.0, 5, 2.576, "ball", color]
data_bounds_left = [-100, -100, 100, height + 200, 0, 0, 0, 0, "bound_left", (100, 100, 100)]
data_bounds_right = [width, -100, 100, height + 200, 0, 0, 0, 0,"bound_right", (100, 100, 100)]
data_bounds_top = [0, -100, width, 100, 0, 0, 0, 0,"bound_top_bottom", (100, 100, 100)]
data_bounds_bottom = [0, height, width, 100, 0, 0, 0, 0, "bound_top_bottom", (100, 100, 100)]
change_size = 0.1
text_color = (200, 200, 200)
pos_index_one = (width * 0.01, height * 0.02)
pos_index_two = (width * 0.98, height * 0.02)