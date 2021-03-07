from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [128, 128, 128]

# print_matrix test
m2 = [[1.00, 4.00], [2.00, 5.00], [3.00, 6.00], [1.00, 1.00]]
print("Testing print_matrix. m2 = ")
print_matrix(m2)
print()

# ident test
m1 = new_matrix()
ident(m1)
print("Testing ident. m1 = ")
print_matrix(m1)
print()

# matrix mult test
print("Testing matrix mult. m1 * m2 = ")
matrix_mult(m1, m2)
print_matrix(m2)
print()
print("Testing matrix mult. m1 = ")
m1 = [[1.0, 4.0, 7.0, 10.0], [2.0, 5.0, 8.0, 11.0], [3.0, 6.0, 9.0, 12.0], [1.0, 1.0, 1.0, 1.0]]
print_matrix(m1)
print()
print("Testing matrix mult. m1 * m2 = ")
matrix_mult(m1, m2)
print_matrix(m2)
print()

# add point test
m3 = [[1.0, 2.0], [3.0, 4.0], [0.0, 0.0], [1.0, 1.0]]
print("Testing add point. m3 = ")
print_matrix(m3)
print()
print("After add point. Added (7.0, 8.0). m3 = ")
add_point(m3, 7.0, 8.0)
print_matrix(m3)
print()
print("Testing add edge. Added (9.0, 10.0), (11.0, 12.0). m3 = ")
add_edge(m3, 9.0, 10.0, 0.0, 11.0, 12.0, 0.0)
print_matrix(m3)

# gridlock image
# buildings
buildings = new_matrix(0)
for x in range(125):
    add_edge(buildings, x, 0, 0, x, 125, 0)
    add_edge(buildings, x, 187, 0, x, 312, 0)
    add_edge(buildings, x, 374, 0, x, 499, 0)
    add_edge(buildings, x + 187, 0, 0, x + 187, 125, 0)
    add_edge(buildings, x + 187, 187, 0, x + 187, 312, 0)
    add_edge(buildings, x + 187, 374, 0, x + 187, 499, 0)
    add_edge(buildings, x + 374, 0, 0, x + 374, 125, 0)
    add_edge(buildings, x + 374, 187, 0, x + 374, 312, 0)
    add_edge(buildings, x + 374, 374, 0, x + 374, 499, 0)
draw_lines(buildings, screen, color )

# yellow lines for road
color = [225, 225, 0]
road = new_matrix(0)
for i in range(6):
    x = i * 22
    add_edge(road, x, 156, 0, x + 10, 156, 0)
    add_edge(road, x + 187, 156, 0, x + 197, 156, 0)
    add_edge(road, x + 374, 156, 0, x + 384, 156, 0)
    add_edge(road, x, 343, 0, x + 10, 343, 0)
    add_edge(road, x + 187, 343, 0, x + 197, 343, 0)
    add_edge(road, x + 374, 343, 0, x + 384, 343, 0)
    add_edge(road, 156, x, 0, 156, x + 10, 0)
    add_edge(road, 156, x + 187, 0, 156, x + 197, 0)
    add_edge(road, 156, x + 374, 0, 156, x + 384, 0)
    add_edge(road, 343, x, 0, 343, x + 10, 0)
    add_edge(road, 343, x + 187, 0, 343, x + 197, 0)
    add_edge(road, 343, x + 374, 0, 343, x + 384, 0)
draw_lines(road, screen, color)

# red cars
color = [204, 0, 0]
redCars = new_matrix(0)
for i in range(7):
    x = i * 50
    for j in range(40):
        add_edge(redCars, j + x, 130, 0, j + x, 150, 0)
        add_edge(redCars, XRES - (j + x), 348, 0, XRES - (j + x), 368, 0)
draw_lines(redCars, screen, color)

# blue cars
color = [0, 0, 204]
blueCars = new_matrix(0)
for i in range(7):
    x = i * 50
    for j in range(40):
        add_edge(blueCars, 130, YRES - (j + x), 0, 150, YRES - (j + x), 0)
        add_edge(blueCars, 348, (j + x), 0, 368, (j + x), 0)
draw_lines(blueCars, screen, color)

display(screen)
save_ppm(screen, 'binary.ppm')
save_ppm_ascii(screen, 'ascii.ppm')
save_extension(screen, 'img.png')