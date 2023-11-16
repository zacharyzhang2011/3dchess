import ursina
from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(fullscreen=True)
starting_board = [
                ["R", "N", "B", "Q", "K", "B", "N", "R"],
                ["P", "P", "P", "P", "P", "P", "P", "P"],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", "P", " ", " ", " ", " ", " ", " "],
                ["p", "p", "p", "p", "p", "p", "p", "p"],  # Note: uppercase for black pieces
                ["r", "n", "b", "q", "k", "b", "n", "r"]]
map_of_board = [
                ["R", "N", "B", "Q", "K", "B", "N", "R"],
                ["P", "P", "P", "P", "P", "P", "P", "P"],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", "P", " ", " ", " ", " ", " ", " "],
                ["p", "p", "p", "p", "p", "p", "p", "p"],  # Note: uppercase for black pieces
                ["r", "n", "b", "q", "k", "b", "n", "r"]]
piece_inputs = []
row_column_of_input = []
moveable_spaces = []
def highlight(tile):
    tile.visible = True
    tile.color = color.black33
    moveable_spaces.append(tile)

white_move = True

def unhighlight(highlighted):
    for tile in highlighted:
        tile.visible = False


def process_input(position, row, column, white_move):
    if len(piece_inputs) == 1:
        if len(moveable_spaces) != 1:
            if white_move:
                if map_of_position_to_tile[row][column] in moveable_spaces:
                    if position != piece_inputs[0]:
                        if position == " ":
                            moved_piece = map_of_position_to_piece[piece_inputs[0]]
                            moved_piece.set_x(map_of_position_to_tile[row][column].position[0])
                            moved_piece.set_y(map_of_position_to_tile[row][column].position[1])
                            map_of_board[row][column] = map_of_board[row_column_of_input[0]][row_column_of_input[1]]
                            map_of_board[row_column_of_input[0]][row_column_of_input[1]] = " "
                            map_of_position_to_piece.update({position: moved_piece})
                            map_of_position_to_piece.update({piece_inputs[0]: None})
                            print(map_of_board)
                            print(map_of_position_to_piece)
                            unhighlight(moveable_spaces)
                            moveable_spaces.clear()
                            piece_inputs.clear()
                            white_move = False




                        else:
                            pass
                else:
                    unhighlight(moveable_spaces)
                    moveable_spaces.clear()
                    piece_inputs.clear()
            else:
                if map_of_position_to_tile[row][column] in moveable_spaces:
                    if position != piece_inputs[0]:
                        if position == " ":
                            moved_piece = map_of_position_to_piece[piece_inputs[0]]
                            moved_piece.set_x(map_of_position_to_tile[row][column].position[0])
                            moved_piece.set_y(map_of_position_to_tile[row][column].position[1])
                            map_of_board[row][column] = map_of_board[row_column_of_input[0]][row_column_of_input[1]]
                            map_of_board[row_column_of_input[0]][row_column_of_input[1]] = " "
                            map_of_position_to_piece.update({position: moved_piece})
                            map_of_position_to_piece.update({piece_inputs[0]: None})
                            print(map_of_board)
                            print(map_of_position_to_piece)
                            unhighlight(moveable_spaces)
                            moveable_spaces.clear()
                            piece_inputs.clear()
                            white_move = False




    if len(piece_inputs) == 0:
        unhighlight(moveable_spaces)
        moveable_spaces.clear()
        if white_move:
            if position != " ":
                piece = position
                if not piece.isupper():
                    highlighted_tile = map_of_position_to_tile[row][column]
                    piece_inputs.append(highlighted_tile)
                    row_column_of_input.append(row)
                    row_column_of_input.append(column)
                    highlight(highlighted_tile)
                    if piece == "p":
                        process_white_pawn_selected(row, column)
                    if piece == "n":
                        process_knight_selected(row, column)
                    if len(moveable_spaces) == 1:
                        piece_inputs.clear()
        else:
            if position != " ":
                piece = position
                if piece.isupper():
                    highlighted_tile = map_of_position_to_tile[row][column]
                    piece_inputs.append(highlighted_tile)
                    row_column_of_input.append(row)
                    row_column_of_input.append(column)
                    highlight(highlighted_tile)
                    if piece == "P":
                        process_black_pawn_selected(row, column)
                    if piece == "N":
                        process_knight_selected(row, column)
                    if len(moveable_spaces) == 1:
                        piece_inputs.clear()






def process_white_pawn_selected(row, column):
    if map_of_board[row-1][column] == " ":
        highlighted_tile = map_of_position_to_tile[row - 1][column]
        highlight(highlighted_tile)
        if map_of_board[row][column] == starting_board[row][column]:
            if map_of_board[row - 2][column] == " ":
                highlighted_tile = map_of_position_to_tile[row - 2][column]
            highlight(highlighted_tile)
    if column != 7 and map_of_board[row-1][column+1] != " ":
        if map_of_board[row-1][column+1].isupper():
            highlighted_tile = map_of_position_to_tile[row-1][column+1]
            highlight(highlighted_tile)
    if column != 0 and map_of_board[row-1][column-1] != " ":
        if map_of_board[row-1][column-1].isupper():
            highlighted_tile = map_of_position_to_tile[row - 1][column - 1]
            highlight(highlighted_tile)

def process_black_pawn_selected(row, column):
    if map_of_board[row+1][column] == " ":
        highlighted_tile = map_of_position_to_tile[row + 1][column]
        highlight(highlighted_tile)
        if map_of_board[row][column] == starting_board[row][column]:
            if map_of_board[row + 2][column] == " ":
                highlighted_tile = map_of_position_to_tile[row + 2][column]
            highlight(highlighted_tile)
    if column != 7 and map_of_board[row+1][column-1] != " ":
        if map_of_board[row-1][column+1].isupper():
            highlighted_tile = map_of_position_to_tile[row+1][column-1]
            highlight(highlighted_tile)
    if column != 0 and map_of_board[row+1][column+1] != " ":
        if map_of_board[row-1][column-1].isupper():
            highlighted_tile = map_of_position_to_tile[row + 1][column + 1]
            highlight(highlighted_tile)

def process_knight_selected(row, column):
    X = [2, 1, -1, -2, -2, -1, 1, 2];
    Y = [1, 2, 2, 1, -1, -2, -2, -1];
    if 6 > row > 1:
        if 6 > column > 1:
            for i in range(8):
                # Position of knight after move
                x = row + X[i];
                y = column + Y[i];
                highlighted_tile = map_of_position_to_tile[x][y]
                highlight(highlighted_tile)


def a1_selected():
    position = map_of_board[7][0]
    process_input(position, 7, 0, white_move)

def b1_selected():
    position = map_of_board[7][1]
    process_input(position, 7, 1, white_move)
def c1_selected():
    position = map_of_board[7][2]
    process_input(position, 7, 2, white_move)
def d1_selected():
    position = map_of_board[7][3]
    process_input(position, 7, 3, white_move)
def e1_selected():
    position = map_of_board[7][4]
    process_input(position, 7, 4, white_move)
def f1_selected():
    position = map_of_board[7][5]
    process_input(position, 7, 5, white_move)
def g1_selected():
    position = map_of_board[7][6]
    process_input(position, 7, 6, white_move)
def h1_selected():
    position = map_of_board[7][7]
    process_input(position, 7, 7, white_move)
def a2_selected():
    position = map_of_board[6][0]
    process_input(position, 6, 0, white_move)

def b2_selected():
    position = map_of_board[6][1]
    process_input(position, 6, 1, white_move)

def c2_selected():
    position = map_of_board[6][2]
    process_input(position, 6, 2, white_move)
def d2_selected():
    position = map_of_board[6][3]
    process_input(position, 6, 3, white_move)
def e2_selected():
    position = map_of_board[6][4]
    process_input(position, 6, 4, white_move)
def f2_selected():
    position = map_of_board[6][5]
    process_input(position, 6, 5, white_move)
def g2_selected():
    position = map_of_board[6][6]
    process_input(position, 6, 6, white_move)
def h2_selected():
    position = map_of_board[6][7]
    process_input(position, 6, 7, white_move)
def a3_selected():
    position = map_of_board[5][0]
    process_input(position, 5, 0, white_move)
def b3_selected():
    position = map_of_board[5][1]
    process_input(position, 5, 1, white_move)
def c3_selected():
    position = map_of_board[5][2]
    process_input(position, 5, 2, white_move)
def d3_selected():
    position = map_of_board[5][3]
    process_input(position, 5, 3, white_move)
def e3_selected():
    position = map_of_board[5][4]
    process_input(position, 5, 4, white_move)
def f3_selected():
    position = map_of_board[5][5]
    process_input(position, 5, 5, white_move)
def g3_selected():
    position = map_of_board[5][6]
    process_input(position, 5, 6, white_move)
def h3_selected():
    position = map_of_board[5][7]
    process_input(position, 5, 7, white_move)
def a4_selected():
    position = map_of_board[4][0]
    process_input(position, 4, 0, white_move)
def b4_selected():
    position = map_of_board[4][1]
    process_input(position, 4, 1, white_move)
def c4_selected():
    position = map_of_board[4][2]
    process_input(position, 4, 2, white_move)
def d4_selected():
    position = map_of_board[4][3]
    process_input(position, 4, 3, white_move)
def e4_selected():
    position = map_of_board[4][4]
    process_input(position, 4, 4, white_move)
def f4_selected():
    position = map_of_board[4][5]
    process_input(position, 4, 5, white_move)
def g4_selected():
    position = map_of_board[4][6]
    process_input(position, 4, 6, white_move)

def h4_selected():
    position = map_of_board[4][7]
    process_input(position, 4, 7, white_move)
def a5_selected():
    position = map_of_board[3][0]
    process_input(position, 3, 0, white_move)
def b5_selected():
    position = map_of_board[3][1]
    process_input(position, 3, 1, white_move)
def c5_selected():
    position = map_of_board[3][2]
    process_input(position, 3, 2, white_move)
def d5_selected():
    position = map_of_board[3][3]
    process_input(position, 3, 3, white_move)
def e5_selected():
    position = map_of_board[3][4]
    process_input(position, 3, 4, white_move)
def f5_selected():
    position = map_of_board[3][4]
    process_input(position, 3, 5, white_move)
def g5_selected():
    position = map_of_board[3][6]
    process_input(position, 3, 6, white_move)
def h5_selected():
    position = map_of_board[3][7]
    process_input(position, 3, 7, white_move)

def a6_selected():
    position = map_of_board[2][0]
    process_input(position, 2, 0, white_move)

def b6_selected():
    position = map_of_board[2][1]
    process_input(position, 2, 1, white_move)

def c6_selected():
    position = map_of_board[2][2]
    process_input(position, 2, 2, white_move)

def d6_selected():
    position = map_of_board[2][3]
    process_input(position, 2, 3, white_move)

def e6_selected():
    position = map_of_board[2][4]
    process_input(position, 2, 4, white_move)



def f6_selected():
    position = map_of_board[2][5]
    process_input(position, 2, 5, white_move)

def g6_selected():
    position = map_of_board[2][6]
    process_input(position, 2, 6, white_move)
def h6_selected():
    position = map_of_board[2][7]
    process_input(position, 2, 7, white_move)
def a7_selected():
    position = map_of_board[1][0]
    process_input(position, 1, 0, white_move)
def b7_selected():
    position = map_of_board[1][1]
    process_input(position, 1, 1, white_move)
def c7_selected():
    position = map_of_board[1][2]
    process_input(position, 1, 2, white_move)
def d7_selected():
    position = map_of_board[1][3]
    process_input(position, 1, 3, white_move)
def e7_selected():
    position = map_of_board[1][4]
    process_input(position, 1, 4, white_move)
def f7_selected():
    position = map_of_board[1][5]
    process_input(position, 1, 5, white_move)
def g7_selected():
    position = map_of_board[1][6]
    process_input(position, 1, 6, white_move)
def h7_selected():
    position = map_of_board[1][7]
    process_input(position, 1, 7, white_move)

def a8_selected():
    position = map_of_board[0][0]
    process_input(position, 0, 0, white_move)
def b8_selected():
    position = map_of_board[0][1]
    process_input(position, 0, 1, white_move)
def c8_selected():
    position = map_of_board[0][2]
    process_input(position, 0, 2, white_move)
def d8_selected():
    position = map_of_board[0][3]
    process_input(position, 0, 3, white_move)
def e8_selected():
    position = map_of_board[0][4]
    process_input(position, 0, 4, white_move)
def f8_selected():
    position = map_of_board[0][5]
    process_input(position, 0, 5, white_move)
def g8_selected():
    position = map_of_board[0][6]
    process_input(position, 0, 6, white_move)
def h8_selected():
    position = map_of_board[0][7]
    process_input(position, 0, 7, white_move)

def selected(obj):

    obj.visible=True
    obj.color = color.random_color()
def change_color_on_click(entity):
    # Define the new
    #
    # .visible=Truecolor you want when the entity is clicked
    new_color = color.random_color()

    # Assign the new color to the entity's color attribute
    entity.color = new_color


board=Entity(model='scene.fbx', texture='Black-board-4.jpg', scale_x=0.01, scale_z=0.01, scale_y=0.005, shader=lit_with_shadows_shader)
a1=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=a1_selected)
b1=Entity(model='cube', color=color.black33, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=b1_selected)
c1=Entity(model='cube', color=color.black33, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=c1_selected)
d1=Entity(model='cube', color=color.black33, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=d1_selected)
e1=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=e1_selected)
f1=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=f1_selected)
g1=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=g1_selected)
h1=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=h1_selected)
a2=Entity(model='cube', color=color.black33, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=a2_selected)
b2=Entity(model='cube', color=color.black33, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=b2_selected)
c2=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=c2_selected)
d2=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=d2_selected)
e2=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=e2_selected)
f2=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=f2_selected)
g2=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=g2_selected)
h2=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=h2_selected)
a3=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=a3_selected)
b3=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=b3_selected)
c3=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=c3_selected)
d3=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=d3_selected)
e3=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=e3_selected)
f3=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=f3_selected)
g3=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=g3_selected)
h3=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=h3_selected)
a4=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=a4_selected)
b4=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=b4_selected)
c4=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=c4_selected)
d4=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=d4_selected)
e4=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=e4_selected)
f4=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=f4_selected)
g4=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=g4_selected)
h4=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=h4_selected)
a5=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=a5_selected)
b5=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=b5_selected)
c5=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=c5_selected)
d5=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=d5_selected)
e5=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=e5_selected)
f5=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=f5_selected)
g5=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=g5_selected)
h5=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=h5_selected)
a6=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=a6_selected)
b6=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=b6_selected)
c6=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=c6_selected)
d6=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=d6_selected)
e6=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=e6_selected)
f6=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=f6_selected)
g6=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=g6_selected)
h6=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=h6_selected)
a7=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=a7_selected)
b7=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=b7_selected)
c7=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=c7_selected)
d7=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=d7_selected)
e7=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=e7_selected)
f7=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=f7_selected)
g7=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=g7_selected)
h7=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=h7_selected)
a8=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=a8_selected)
b8=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=b8_selected)
c8=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=c8_selected)
d8=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=d8_selected)
e8=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=e8_selected)
f8=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=f8_selected)
g8=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=g8_selected)
h8=Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01, scale_y=0.477, on_click=h8_selected)
board1=Entity(model='cube', texture='img_1.png', scale_x=5.2, scale_z=0.1, scale_y=5.2, position=(0, 0, 2.8), shader=lit_with_shadows_shader)
pos_reference=Entity(model='cube', visible=False)
plate=Entity(model="cube", color=color.black, scale=10, collider="mesh", position=(0,-10,0))
king1=Entity(model='king.fbx', scale=0.012, texture='white.png')
king2=Entity(model='king.fbx', scale=0.012, texture='black.png')
queen1 = Entity(model='queen.fbx', scale=0.0075, texture='white.png')
queen2 = Entity(model='queen.fbx', scale=0.0075, texture='black.png')
rook1 = Entity(model='rook.fbx', scale=0.0075, texture='white.png')
rook2 = Entity(model='rook.fbx', scale=0.0075, texture='white.png')
rook3 = Entity(model='rook.fbx', scale=0.0075, texture='black.png')
rook4 = Entity(model='rook.fbx', scale=0.0075, texture='black.png')
bishop1 = Entity(model='bishop.fbx', scale=0.012, texture='white.png')
bishop2 = Entity(model='bishop.fbx', scale=0.012, texture='white.png')
bishop3 = Entity(model='bishop.fbx', scale=0.012, texture='black.png')
bishop4 = Entity(model='bishop.fbx', scale=0.012, texture='black.png')
knight1 = Entity(model='knight.fbx', scale=0.012, texture='white.png')
knight2 = Entity(model='knight.fbx', scale=0.012, texture='white.png')
knight1.rotation_x = 90
knight2.rotation_x = 90
knight3 = Entity(model='knight.fbx', scale=0.012, texture='black.png')
knight4 = Entity(model='knight.fbx', scale=0.012, texture='black.png')
pawn1=Entity(model='pawn.fbx', scale=0.012, texture='white.png')
pawn2=Entity(model='pawn.fbx', scale=0.012, texture='white.png')
pawn3=Entity(model='pawn.fbx', scale=0.012, texture='white.png')
pawn4=Entity(model='pawn.fbx', scale=0.012, texture='white.png')
pawn5=Entity(model='pawn.fbx', scale=0.012, texture='white.png')
pawn6=Entity(model='pawn.fbx', scale=0.012, texture='white.png')
pawn7=Entity(model='pawn.fbx', scale=0.012, texture='white.png')
pawn8=Entity(model='pawn.fbx', scale=0.012, texture='white.png')
pawn9=Entity(model='pawn.fbx', scale=0.012, texture='black.png')
pawn10=Entity(model='pawn.fbx', scale=0.012, texture='black.png')
pawn11=Entity(model='pawn.fbx', scale=0.012, texture='black.png')
pawn12=Entity(model='pawn.fbx', scale=0.012, texture='black.png')
pawn13=Entity(model='pawn.fbx', scale=0.012, texture='black.png')
pawn14=Entity(model='pawn.fbx', scale=0.012, texture='black.png')
pawn15=Entity(model='pawn.fbx', scale=0.012, texture='black.png')
pawn16=Entity(model='pawn.fbx', scale=0.012, texture='black.png')
map_of_position_to_tile = [
    [a8, b8, c8, d8, e8, f8, g8, h8],
    [a7, b7, c7, d7, e7, f7, g7, h7],
    [a6, b6, c6, d6, e6, f6, g6, h6],
    [a5, b5, c5, d5, e5, f5, g5, h5],
    [a4, b4, c4, d4, e4, f4, g4, h4],
    [a3, b3, c3, d3, e3, f3, g3, h3],
    [a2, b2, c2, d2, e2, f2, g2, h2],
    [a1, b1, c1, d1, e1, f1, g1, h1]
]
map_of_position_to_piece = {
    a8: rook4, b8: knight4, c8: bishop4, d8: king2, e8: queen2, f8: bishop3, g8: knight3, h8: rook3,
    a7: pawn8, b7: pawn7, c7: pawn6, d7: pawn5, e7: pawn4, f7: pawn3, g7: pawn2, h7: pawn1,
    a6: None, b6: None, c6: None, d6: None, e6: None, f6: None, g6: None, h6: None,
    a5: None, b5: None, c5: None, d5: None, e5: None, f5: None, g5: None, h5: None,
    a4: None, b4: None, c4: None, d4: None, e4: None, f4: None, g4: None, h4: None,
    a3: None, b3: None, c3: None, d3: None, e3: None, f3: None, g3: None, h3: None,
    a2: pawn1, b2: pawn2, c2: pawn3, d2: pawn4, e2: pawn5, f2: pawn6, g2: pawn7, h2: pawn8,
    a1: rook1, b1: knight1, c1: bishop1, d1: king1, e1: queen1, f1: bishop2, g1: knight2, h1: rook2
}
"""FirstPersonController()"""


"""position=(-1.6467,-1.6467,-0.1)"""

"""pivot = Entity()
SpotLight(parent=pivot, z=-100, shadows=True, rotation=(0, 0, 0))"""
camera.z-=5
Sky()
"""king1.set_position((0.24, -1.647, -0.53), relative_to=pos_reference)
king2.set_position((0.24, 1.647, -0.53), relative_to=pos_reference)
queen1.set_position((-0.22, -1.647, -0.53), relative_to=pos_reference)
queen2.set_position((-0.22, 1.647, -0.53), relative_to=pos_reference)
pawn1.set_position((-1.633, -1.17, -0.53), relative_to=pos_reference)
pawn2.set_position((-1.159, -1.17, -0.53), relative_to=pos_reference)
pawn3.set_position((-0.69, -1.17, -0.53), relative_to=pos_reference)
pawn4.set_position((-0.22, -1.17, -0.53), relative_to=pos_reference)
pawn5.set_position((0.24, -1.17, -0.53), relative_to=pos_reference)
pawn6.set_position((0.71, -1.17, -0.53), relative_to=pos_reference)
pawn7.set_position((1.18, -1.17, -0.53), relative_to=pos_reference)
pawn8.set_position((1.65, -1.17, -0.53), relative_to=pos_reference)
pawn9.set_position((-1.633, 1.172, -0.53), relative_to=pos_reference)
pawn10.set_position((-1.159, 1.172, -0.53), relative_to=pos_reference)
pawn11.set_position((-0.69, 1.172, -0.53), relative_to=pos_reference)
pawn12.set_position((-0.22, 1.172, -0.53), relative_to=pos_reference)
pawn13.set_position((0.24, 1.172, -0.53), relative_to=pos_reference)
pawn14.set_position((0.71, 1.172, -0.53), relative_to=pos_reference)
pawn15.set_position((1.18, 1.172, -0.53), relative_to=pos_reference)
pawn16.set_position((1.65, 1.172, -0.53), relative_to=pos_reference)
a1.set_position((-1.633, -1.647, -0.03), relative_to=pos_reference)
b1.set_position((-1.159, -1.647, -0.03), relative_to=pos_reference)
c1.set_position((-0.69, -1.647, -0.03), relative_to=pos_reference)
d1.set_position((-0.22, -1.647, -0.03), relative_to=pos_reference)
e1.set_position((0.24, -1.647, -0.03), relative_to=pos_reference)
f1.set_position((0.71, -1.647, -0.03), relative_to=pos_reference)
g1.set_position((1.18, -1.647, -0.03), relative_to=pos_reference)
h1.set_position((1.65, -1.647, -0.03), relative_to=pos_reference)
a2.set_position((-1.633, -1.17, -0.03), relative_to=pos_reference)
b2.set_position((-1.159, -1.17, -0.03), relative_to=pos_reference)
c2.set_position((-0.69, -1.17, -0.03), relative_to=pos_reference)
d2.set_position((-0.22, -1.17, -0.03), relative_to=pos_reference)
e2.set_position((0.24, -1.17, -0.03), relative_to=pos_reference)
f2.set_position((0.71, -1.17, -0.03), relative_to=pos_reference)
g2.set_position((1.18, -1.17, -0.03), relative_to=pos_reference)
h2.set_position((1.65, -1.17, -0.03), relative_to=pos_reference)
a3.set_position((-1.633, -0.694, -0.03), relative_to=pos_reference)
b3.set_position((-1.159, -0.694, -0.03), relative_to=pos_reference)
c3.set_position((-0.69, -0.694, -0.03), relative_to=pos_reference)
d3.set_position((-0.22, -0.694, -0.03), relative_to=pos_reference)
e3.set_position((0.24, -0.694, -0.03), relative_to=pos_reference)
f3.set_position((0.71, -0.694, -0.03), relative_to=pos_reference)
g3.set_position((1.18, -0.694, -0.03), relative_to=pos_reference)
h3.set_position((1.65, -0.694, -0.03), relative_to=pos_reference)
a4.set_position((-1.633, -0.231, -0.03), relative_to=pos_reference)
b4.set_position((-1.159, -0.231, -0.03), relative_to=pos_reference)
c4.set_position((-0.69, -0.231, -0.03), relative_to=pos_reference)
d4.set_position((-0.22, -0.231, -0.03), relative_to=pos_reference)
e4.set_position((0.24, -0.231, -0.03), relative_to=pos_reference)
f4.set_position((0.71, -0.231, -0.03), relative_to=pos_reference)
g4.set_position((1.18, -0.231, -0.03), relative_to=pos_reference)
h4.set_position((1.65, -0.231, -0.03), relative_to=pos_reference)
a5.set_position((-1.633, 0.243, -0.03), relative_to=pos_reference)
b5.set_position((-1.159, 0.243, -0.03), relative_to=pos_reference)
c5.set_position((-0.69, 0.243, -0.03), relative_to=pos_reference)
d5.set_position((-0.22, 0.243, -0.03), relative_to=pos_reference)
e5.set_position((0.24, 0.243, -0.03), relative_to=pos_reference)
f5.set_position((0.71, 0.243, -0.03), relative_to=pos_reference)
g5.set_position((1.18, 0.243, -0.03), relative_to=pos_reference)
h5.set_position((1.65, 0.243, -0.03), relative_to=pos_reference)
a6.set_position((-1.633, 0.718, -0.03), relative_to=pos_reference)
b6.set_position((-1.159, 0.718, -0.03), relative_to=pos_reference)
c6.set_position((-0.69, 0.718, -0.03), relative_to=pos_reference)
d6.set_position((-0.22, 0.718, -0.03), relative_to=pos_reference)
e6.set_position((0.24, 0.718, -0.03), relative_to=pos_reference)
f6.set_position((0.71, 0.718, -0.03), relative_to=pos_reference)
g6.set_position((1.18, 0.718, -0.03), relative_to=pos_reference)
h6.set_position((1.65, 0.718, -0.03), relative_to=pos_reference)
a7.set_position((-1.633, 1.172, -0.03), relative_to=pos_reference)
b7.set_position((-1.159, 1.172, -0.03), relative_to=pos_reference)
c7.set_position((-0.69, 1.172, -0.03), relative_to=pos_reference)
d7.set_position((-0.22, 1.172, -0.03), relative_to=pos_reference)
e7.set_position((0.24, 1.172, -0.03), relative_to=pos_reference)
f7.set_position((0.71, 1.172, -0.03), relative_to=pos_reference)
g7.set_position((1.18, 1.172, -0.03), relative_to=pos_reference)
h7.set_position((1.65, 1.172, -0.03), relative_to=pos_reference)
a8.set_position((-1.633, 1.647, -0.03), relative_to=pos_reference)
b8.set_position((-1.159, 1.647, -0.03), relative_to=pos_reference)
c8.set_position((-0.69, 1.647, -0.03), relative_to=pos_reference)
d8.set_position((-0.22, 1.647, -0.03), relative_to=pos_reference)
e8.set_position((0.24, 1.647, -0.03), relative_to=pos_reference)
f8.set_position((0.71, 1.647, -0.03), relative_to=pos_reference)
g8.set_position((1.18, 1.647, -0.03), relative_to=pos_reference)
h8.set_position((1.65, 1.647, -0.03), relative_to=pos_reference)
board.rotation_x = pos_reference.rotation_x + 90
board1.rotation_x = pos_reference.rotation_x
king1.rotation_x = pos_reference.rotation_x + 270
king1.rotation_y = pos_reference.rotation_y
king2.rotation_x = pos_reference.rotation_x + 270
king2.rotation_y = pos_reference.rotation_y
queen1.rotation_x = pos_reference.rotation_x + 270
queen1.rotation_y = pos_reference.rotation_y
queen2.rotation_x = pos_reference.rotation_x + 270
queen2.rotation_y = pos_reference.rotation_y
pawn1.rotation_x = pos_reference.rotation_x+270
pawn1.rotation_y = pos_reference.rotation_y
pawn2.rotation_x = pos_reference.rotation_x + 270
pawn2.rotation_y = pos_reference.rotation_y
pawn3.rotation_x = pos_reference.rotation_x + 270
pawn3.rotation_y = pos_reference.rotation_y
pawn4.rotation_x = pos_reference.rotation_x + 270
pawn4.rotation_y = pos_reference.rotation_y
pawn5.rotation_x = pos_reference.rotation_x + 270
pawn5.rotation_y = pos_reference.rotation_y
pawn6.rotation_x = pos_reference.rotation_x + 270
pawn6.rotation_y = pos_reference.rotation_y
pawn7.rotation_x = pos_reference.rotation_x + 270
pawn7.rotation_y = pos_reference.rotation_y
pawn8.rotation_x = pos_reference.rotation_x + 270
pawn8.rotation_y = pos_reference.rotation_y
pawn9.rotation_x = pos_reference.rotation_x+270
pawn9.rotation_y = pos_reference.rotation_y
pawn10.rotation_x = pos_reference.rotation_x + 270
pawn10.rotation_y = pos_reference.rotation_y
pawn11.rotation_x = pos_reference.rotation_x + 270
pawn11.rotation_y = pos_reference.rotation_y
pawn12.rotation_x = pos_reference.rotation_x + 270
pawn12.rotation_y = pos_reference.rotation_y
pawn13.rotation_x = pos_reference.rotation_x + 270
pawn13.rotation_y = pos_reference.rotation_y
pawn14.rotation_x = pos_reference.rotation_x + 270
pawn14.rotation_y = pos_reference.rotation_y
pawn15.rotation_x = pos_reference.rotation_x + 270
pawn15.rotation_y = pos_reference.rotation_y
pawn16.rotation_x = pos_reference.rotation_x + 270
pawn16.rotation_y = pos_reference.rotation_y"""
king1.set_position((0.24, -1.647, -0.55), relative_to=pos_reference)
king2.set_position((0.24, 1.647, -0.55), relative_to=pos_reference)
queen1.set_position((-0.22, -1.647, -0.35), relative_to=pos_reference)
queen2.set_position((-0.22, 1.647, -0.35), relative_to=pos_reference)
rook1.set_position((-1.633, -1.647, -0.35), relative_to=pos_reference)
rook2.set_position((1.65, -1.647, -0.35), relative_to=pos_reference)
rook3.set_position((-1.633, 1.647, -0.35), relative_to=pos_reference)
rook4.set_position((1.65, 1.647, -0.35), relative_to=pos_reference)
bishop1.set_position((-0.69, -1.647, -0.59), relative_to=pos_reference)
bishop2.set_position((0.71, -1.647, -0.59), relative_to=pos_reference)
bishop3.set_position((-0.69, 1.647, -0.59), relative_to=pos_reference)
bishop4.set_position((0.71, 1.647, -0.59), relative_to=pos_reference)
knight1.set_position((-1.159, -1.647, -0.53), relative_to=pos_reference)
knight2.set_position((1.18, -1.647, -0.53), relative_to=pos_reference)
knight3.set_position((-1.159, 1.647, -0.53), relative_to=pos_reference)
knight4.set_position((1.18, 1.647, -0.53), relative_to=pos_reference)
pawn1.set_position((-1.633, -1.17, -0.53), relative_to=pos_reference)
pawn2.set_position((-1.159, -1.17, -0.53), relative_to=pos_reference)
pawn3.set_position((-0.69, -1.17, -0.53), relative_to=pos_reference)
pawn4.set_position((-0.22, -1.17, -0.53), relative_to=pos_reference)
pawn5.set_position((0.24, -1.17, -0.53), relative_to=pos_reference)
pawn6.set_position((0.71, -1.17, -0.53), relative_to=pos_reference)
pawn7.set_position((1.18, -1.17, -0.53), relative_to=pos_reference)
pawn8.set_position((1.65, -1.17, -0.53), relative_to=pos_reference)
pawn9.set_position((-1.633, 1.172, -0.53), relative_to=pos_reference)
pawn10.set_position((-1.159, 1.172, -0.53), relative_to=pos_reference)
pawn11.set_position((-0.69, 1.172, -0.53), relative_to=pos_reference)
pawn12.set_position((-0.22, 1.172, -0.53), relative_to=pos_reference)
pawn13.set_position((0.24, 1.172, -0.53), relative_to=pos_reference)
pawn14.set_position((0.71, 1.172, -0.53), relative_to=pos_reference)
pawn15.set_position((1.18, 1.172, -0.53), relative_to=pos_reference)
pawn16.set_position((1.65, 1.172, -0.53), relative_to=pos_reference)#put pieces outside of update to move
def update():
    pos_reference.rotation_x += held_keys["w"]
    pos_reference.rotation_x -= held_keys["s"]
    pos_reference.rotation_y -= held_keys["d"]
    pos_reference.rotation_y += held_keys["a"]
    pos_reference.rotation_y -= held_keys["e"]
    pos_reference.rotation_y += held_keys["q"]
    board.rotation_x += held_keys["w"]
    board.rotation_x -= held_keys["s"]
    board.rotation_y -= held_keys["d"]
    board.rotation_y += held_keys["a"]
    board.rotation_y -= held_keys["e"]
    board.rotation_y += held_keys["q"]
    board1.rotation_x += held_keys["w"]
    board1.rotation_x -= held_keys["s"]
    board1.rotation_y -= held_keys["d"]
    board1.rotation_y += held_keys["a"]
    board1.rotation_y -= held_keys["e"]
    board1.rotation_y += held_keys["q"]
    a1.set_position((-1.633, -1.647, -0.03), relative_to=pos_reference)
    b1.set_position((-1.159, -1.647, -0.03), relative_to=pos_reference)
    c1.set_position((-0.69, -1.647, -0.03), relative_to=pos_reference)
    d1.set_position((-0.22, -1.647, -0.03), relative_to=pos_reference)
    e1.set_position((0.24, -1.647, -0.03), relative_to=pos_reference)
    f1.set_position((0.71, -1.647, -0.03), relative_to=pos_reference)
    g1.set_position((1.18, -1.647, -0.03), relative_to=pos_reference)
    h1.set_position((1.65, -1.647, -0.03), relative_to=pos_reference)
    a2.set_position((-1.633, -1.17, -0.03), relative_to=pos_reference)
    b2.set_position((-1.159, -1.17, -0.03), relative_to=pos_reference)
    c2.set_position((-0.69, -1.17, -0.03), relative_to=pos_reference)
    d2.set_position((-0.22, -1.17, -0.03), relative_to=pos_reference)
    e2.set_position((0.24, -1.17, -0.03), relative_to=pos_reference)
    f2.set_position((0.71, -1.17, -0.03), relative_to=pos_reference)
    g2.set_position((1.18, -1.17, -0.03), relative_to=pos_reference)
    h2.set_position((1.65, -1.17, -0.03), relative_to=pos_reference)
    a3.set_position((-1.633, -0.694, -0.03), relative_to=pos_reference)
    b3.set_position((-1.159, -0.694, -0.03), relative_to=pos_reference)
    c3.set_position((-0.69, -0.694, -0.03), relative_to=pos_reference)
    d3.set_position((-0.22, -0.694, -0.03), relative_to=pos_reference)
    e3.set_position((0.24, -0.694, -0.03), relative_to=pos_reference)
    f3.set_position((0.71, -0.694, -0.03), relative_to=pos_reference)
    g3.set_position((1.18, -0.694, -0.03), relative_to=pos_reference)
    h3.set_position((1.65, -0.694, -0.03), relative_to=pos_reference)
    a4.set_position((-1.633, -0.231, -0.03), relative_to=pos_reference)
    b4.set_position((-1.159, -0.231, -0.03), relative_to=pos_reference)
    c4.set_position((-0.69, -0.231, -0.03), relative_to=pos_reference)
    d4.set_position((-0.22, -0.231, -0.03), relative_to=pos_reference)
    e4.set_position((0.24, -0.231, -0.03), relative_to=pos_reference)
    f4.set_position((0.71, -0.231, -0.03), relative_to=pos_reference)
    g4.set_position((1.18, -0.231, -0.03), relative_to=pos_reference)
    h4.set_position((1.65, -0.231, -0.03), relative_to=pos_reference)
    a5.set_position((-1.633, 0.243, -0.03), relative_to=pos_reference)
    b5.set_position((-1.159, 0.243, -0.03), relative_to=pos_reference)
    c5.set_position((-0.69, 0.243, -0.03), relative_to=pos_reference)
    d5.set_position((-0.22, 0.243, -0.03), relative_to=pos_reference)
    e5.set_position((0.24, 0.243, -0.03), relative_to=pos_reference)
    f5.set_position((0.71, 0.243, -0.03), relative_to=pos_reference)
    g5.set_position((1.18, 0.243, -0.03), relative_to=pos_reference)
    h5.set_position((1.65, 0.243, -0.03), relative_to=pos_reference)
    a6.set_position((-1.633, 0.718, -0.03), relative_to=pos_reference)
    b6.set_position((-1.159, 0.718, -0.03), relative_to=pos_reference)
    c6.set_position((-0.69, 0.718, -0.03), relative_to=pos_reference)
    d6.set_position((-0.22, 0.718, -0.03), relative_to=pos_reference)
    e6.set_position((0.24, 0.718, -0.03), relative_to=pos_reference)
    f6.set_position((0.71, 0.718, -0.03), relative_to=pos_reference)
    g6.set_position((1.18, 0.718, -0.03), relative_to=pos_reference)
    h6.set_position((1.65, 0.718, -0.03), relative_to=pos_reference)
    a7.set_position((-1.633, 1.172, -0.03), relative_to=pos_reference)
    b7.set_position((-1.159, 1.172, -0.03), relative_to=pos_reference)
    c7.set_position((-0.69, 1.172, -0.03), relative_to=pos_reference)
    d7.set_position((-0.22, 1.172, -0.03), relative_to=pos_reference)
    e7.set_position((0.24, 1.172, -0.03), relative_to=pos_reference)
    f7.set_position((0.71, 1.172, -0.03), relative_to=pos_reference)
    g7.set_position((1.18, 1.172, -0.03), relative_to=pos_reference)
    h7.set_position((1.65, 1.172, -0.03), relative_to=pos_reference)
    a8.set_position((-1.633, 1.647, -0.03), relative_to=pos_reference)
    b8.set_position((-1.159, 1.647, -0.03), relative_to=pos_reference)
    c8.set_position((-0.69, 1.647, -0.03), relative_to=pos_reference)
    d8.set_position((-0.22, 1.647, -0.03), relative_to=pos_reference)
    e8.set_position((0.24, 1.647, -0.03), relative_to=pos_reference)
    f8.set_position((0.71, 1.647, -0.03), relative_to=pos_reference)
    g8.set_position((1.18, 1.647, -0.03), relative_to=pos_reference)
    h8.set_position((1.65, 1.647, -0.03), relative_to=pos_reference)
    board.rotation_x = pos_reference.rotation_x + 90
    board1.rotation_x = pos_reference.rotation_x
    king1.rotation_x = pos_reference.rotation_x + 270
    king1.rotation_y = pos_reference.rotation_y
    king2.rotation_x = pos_reference.rotation_x + 270
    king2.rotation_y = pos_reference.rotation_y
    queen1.rotation_x = pos_reference.rotation_x + 270
    queen1.rotation_y = pos_reference.rotation_y
    queen2.rotation_x = pos_reference.rotation_x + 270
    queen2.rotation_y = pos_reference.rotation_y
    rook1.rotation_x = pos_reference.rotation_x + 270
    rook1.rotation_y = pos_reference.rotation_y
    rook2.rotation_x = pos_reference.rotation_x + 270
    rook2.rotation_y = pos_reference.rotation_y
    rook3.rotation_x = pos_reference.rotation_x + 270
    rook3.rotation_y = pos_reference.rotation_y
    rook4.rotation_x = pos_reference.rotation_x + 270
    rook4.rotation_y = pos_reference.rotation_y
    bishop1.rotation_x = pos_reference.rotation_x + 270
    bishop1.rotation_y = pos_reference.rotation_y
    bishop2.rotation_x = pos_reference.rotation_x + 270
    bishop2.rotation_y = pos_reference.rotation_y
    bishop3.rotation_x = pos_reference.rotation_x + 270
    bishop3.rotation_y = pos_reference.rotation_y
    bishop4.rotation_x = pos_reference.rotation_x + 270
    bishop4.rotation_y = pos_reference.rotation_y
    knight1.rotation_x -= held_keys["w"]
    knight1.rotation_x += held_keys["s"]
    knight1.rotation_y = pos_reference.rotation_y + 180
    """knight2.rotation_x = pos_reference.rotation_x + 270"""
    knight2.rotation_x -= held_keys["w"]
    knight2.rotation_x += held_keys["s"]
    knight2.rotation_y = pos_reference.rotation_y + 180
    knight3.rotation_x = pos_reference.rotation_x + 270
    knight3.rotation_y = pos_reference.rotation_y
    knight4.rotation_x = pos_reference.rotation_x + 270
    knight4.rotation_y = pos_reference.rotation_y
    pawn1.rotation_x = pos_reference.rotation_x + 270
    pawn1.rotation_y = pos_reference.rotation_y
    pawn2.rotation_x = pos_reference.rotation_x + 270
    pawn2.rotation_y = pos_reference.rotation_y
    pawn3.rotation_x = pos_reference.rotation_x + 270
    pawn3.rotation_y = pos_reference.rotation_y
    pawn4.rotation_x = pos_reference.rotation_x + 270
    pawn4.rotation_y = pos_reference.rotation_y
    pawn5.rotation_x = pos_reference.rotation_x + 270
    pawn5.rotation_y = pos_reference.rotation_y
    pawn6.rotation_x = pos_reference.rotation_x + 270
    pawn6.rotation_y = pos_reference.rotation_y
    pawn7.rotation_x = pos_reference.rotation_x + 270
    pawn7.rotation_y = pos_reference.rotation_y
    pawn8.rotation_x = pos_reference.rotation_x + 270
    pawn8.rotation_y = pos_reference.rotation_y
    pawn9.rotation_x = pos_reference.rotation_x + 270
    pawn9.rotation_y = pos_reference.rotation_y
    pawn10.rotation_x = pos_reference.rotation_x + 270
    pawn10.rotation_y = pos_reference.rotation_y
    pawn11.rotation_x = pos_reference.rotation_x + 270
    pawn11.rotation_y = pos_reference.rotation_y
    pawn12.rotation_x = pos_reference.rotation_x + 270
    pawn12.rotation_y = pos_reference.rotation_y
    pawn13.rotation_x = pos_reference.rotation_x + 270
    pawn13.rotation_y = pos_reference.rotation_y
    pawn14.rotation_x = pos_reference.rotation_x + 270
    pawn14.rotation_y = pos_reference.rotation_y
    pawn15.rotation_x = pos_reference.rotation_x + 270
    pawn15.rotation_y = pos_reference.rotation_y
    pawn16.rotation_x = pos_reference.rotation_x + 270
    pawn16.rotation_y = pos_reference.rotation_y
    a1.rotation_x = pos_reference.rotation_x
    a1.rotation_y = pos_reference.rotation_y
    b1.rotation_x = pos_reference.rotation_x
    b1.rotation_y = pos_reference.rotation_y
    c1.rotation_x = pos_reference.rotation_x
    c1.rotation_y = pos_reference.rotation_y
    d1.rotation_x = pos_reference.rotation_x
    d1.rotation_y = pos_reference.rotation_y
    e1.rotation_x = pos_reference.rotation_x
    e1.rotation_y = pos_reference.rotation_y
    f1.rotation_x = pos_reference.rotation_x
    f1.rotation_y = pos_reference.rotation_y
    g1.rotation_x = pos_reference.rotation_x
    g1.rotation_y = pos_reference.rotation_y
    h1.rotation_x = pos_reference.rotation_x
    h1.rotation_y = pos_reference.rotation_y
    a2.rotation_x = pos_reference.rotation_x
    a2.rotation_y = pos_reference.rotation_y
    b2.rotation_x = pos_reference.rotation_x
    b2.rotation_y = pos_reference.rotation_y
    c2.rotation_x = pos_reference.rotation_x
    c2.rotation_y = pos_reference.rotation_y
    d2.rotation_x = pos_reference.rotation_x
    d2.rotation_y = pos_reference.rotation_y
    e2.rotation_x = pos_reference.rotation_x
    e2.rotation_y = pos_reference.rotation_y
    f2.rotation_x = pos_reference.rotation_x
    f2.rotation_y = pos_reference.rotation_y
    g2.rotation_x = pos_reference.rotation_x
    g2.rotation_y = pos_reference.rotation_y
    h2.rotation_x = pos_reference.rotation_x
    h2.rotation_y = pos_reference.rotation_y
    a3.rotation_x = pos_reference.rotation_x
    a3.rotation_y = pos_reference.rotation_y
    b3.rotation_x = pos_reference.rotation_x
    b3.rotation_y = pos_reference.rotation_y
    c3.rotation_x = pos_reference.rotation_x
    c3.rotation_y = pos_reference.rotation_y
    d3.rotation_x = pos_reference.rotation_x
    d3.rotation_y = pos_reference.rotation_y
    e3.rotation_x = pos_reference.rotation_x
    e3.rotation_y = pos_reference.rotation_y
    f3.rotation_x = pos_reference.rotation_x
    f3.rotation_y = pos_reference.rotation_y
    g3.rotation_x = pos_reference.rotation_x
    g3.rotation_y = pos_reference.rotation_y
    h3.rotation_x = pos_reference.rotation_x
    h3.rotation_y = pos_reference.rotation_y
    a4.rotation_x = pos_reference.rotation_x
    a4.rotation_y = pos_reference.rotation_y
    b4.rotation_x = pos_reference.rotation_x
    b4.rotation_y = pos_reference.rotation_y
    c4.rotation_x = pos_reference.rotation_x
    c4.rotation_y = pos_reference.rotation_y
    d4.rotation_x = pos_reference.rotation_x
    d4.rotation_y = pos_reference.rotation_y
    e4.rotation_x = pos_reference.rotation_x
    e4.rotation_y = pos_reference.rotation_y
    f4.rotation_x = pos_reference.rotation_x
    f4.rotation_y = pos_reference.rotation_y
    g4.rotation_x = pos_reference.rotation_x
    g4.rotation_y = pos_reference.rotation_y
    h4.rotation_x = pos_reference.rotation_x
    h4.rotation_y = pos_reference.rotation_y
    a5.rotation_x = pos_reference.rotation_x
    a5.rotation_y = pos_reference.rotation_y
    b5.rotation_x = pos_reference.rotation_x
    b5.rotation_y = pos_reference.rotation_y
    c5.rotation_x = pos_reference.rotation_x
    c5.rotation_y = pos_reference.rotation_y
    d5.rotation_x = pos_reference.rotation_x
    d5.rotation_y = pos_reference.rotation_y
    e5.rotation_x = pos_reference.rotation_x
    e5.rotation_y = pos_reference.rotation_y
    f5.rotation_x = pos_reference.rotation_x
    f5.rotation_y = pos_reference.rotation_y
    g5.rotation_x = pos_reference.rotation_x
    g5.rotation_y = pos_reference.rotation_y
    h5.rotation_x = pos_reference.rotation_x
    h5.rotation_y = pos_reference.rotation_y
    a6.rotation_x = pos_reference.rotation_x
    a6.rotation_y = pos_reference.rotation_y
    b6.rotation_x = pos_reference.rotation_x
    b6.rotation_y = pos_reference.rotation_y
    c6.rotation_x = pos_reference.rotation_x
    c6.rotation_y = pos_reference.rotation_y
    d6.rotation_x = pos_reference.rotation_x
    d6.rotation_y = pos_reference.rotation_y
    e6.rotation_x = pos_reference.rotation_x
    e6.rotation_y = pos_reference.rotation_y
    f6.rotation_x = pos_reference.rotation_x
    f6.rotation_y = pos_reference.rotation_y
    g6.rotation_x = pos_reference.rotation_x
    g6.rotation_y = pos_reference.rotation_y
    h6.rotation_x = pos_reference.rotation_x
    h6.rotation_y = pos_reference.rotation_y
    a7.rotation_x = pos_reference.rotation_x
    a7.rotation_y = pos_reference.rotation_y
    b7.rotation_x = pos_reference.rotation_x
    b7.rotation_y = pos_reference.rotation_y
    c7.rotation_x = pos_reference.rotation_x
    c7.rotation_y = pos_reference.rotation_y
    d7.rotation_x = pos_reference.rotation_x
    d7.rotation_y = pos_reference.rotation_y
    e7.rotation_x = pos_reference.rotation_x
    e7.rotation_y = pos_reference.rotation_y
    f7.rotation_x = pos_reference.rotation_x
    f7.rotation_y = pos_reference.rotation_y
    g7.rotation_x = pos_reference.rotation_x
    g7.rotation_y = pos_reference.rotation_y
    h7.rotation_x = pos_reference.rotation_x
    h7.rotation_y = pos_reference.rotation_y
    a8.rotation_x = pos_reference.rotation_x
    a8.rotation_y = pos_reference.rotation_y
    b8.rotation_x = pos_reference.rotation_x
    b8.rotation_y = pos_reference.rotation_y
    c8.rotation_x = pos_reference.rotation_x
    c8.rotation_y = pos_reference.rotation_y
    d8.rotation_x = pos_reference.rotation_x
    d8.rotation_y = pos_reference.rotation_y
    e8.rotation_x = pos_reference.rotation_x
    e8.rotation_y = pos_reference.rotation_y
    f8.rotation_x = pos_reference.rotation_x
    f8.rotation_y = pos_reference.rotation_y
    g8.rotation_x = pos_reference.rotation_x
    g8.rotation_y = pos_reference.rotation_y
    h8.rotation_x = pos_reference.rotation_x
    h8.rotation_y = pos_reference.rotation_y


app.run()

#table
"""table=Entity(model='table1.fbx', texture="mask_dirt.jpg", scale_x=0.01, scale_z=0.01, scale_y=0.01, position=(0,-3.3, 3))
table1=Entity(model='table1.fbx', texture="ambient_occlusion.jpg", scale_x=0.01, scale_z=0.01, scale_y=0.01, position=(0,-3.3, 3))
table.rotation_y+=90
table.rotation_z+=25
table1.rotation_y+=90
table1.rotation_z+=25"""
"""table.rotation_x+=held_keys["w"]
    table.rotation_x -= held_keys["s"]
    table.rotation_y -= held_keys["d"]
    table.rotation_y += held_keys["a"]
    table.rotation_z += held_keys["e"]
    table.rotation_z -= held_keys["q"]
    table1.rotation_x += held_keys["w"]
    table1.rotation_x -= held_keys["s"]
    table1.rotation_y -= held_keys["d"]
    table1.rotation_y += held_keys["a"]
    table1.rotation_z += held_keys["e"]
    table1.rotation_z -= held_keys["q"]"""