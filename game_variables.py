screen_width, screen_height = (480, 600)
player_width, player_height = (30, 40)


player_acc = 0.5
player_gravity = 0.6
player_jump = 20
font = "freesansbold.ttf"

# friction is there to emulate air + floor resistance/ so friction = -k* velocity
friction = -0.1
air_resistance = -0.03
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

platform_list = [(0, screen_height-40, screen_width, 40),
                 ((screen_width / 2) + 50, (screen_height * (4 / 14)), 100, 25),
                 ((screen_width / 2) - 170, (screen_height * (4 / 7)), 100, 30),
                 (300, 450, 100, 10),
                 (120, 80, 50, 20)]

title = "Platformer"
FPS = 60

