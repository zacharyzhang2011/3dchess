
from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina(fullscreen=True)

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

class Pieces():
    def __init__(self):
        self.map_of_starting_board=[["R", "N", "B", "Q", "K", "B", "N", "R"],
                                    ["P", "P", "P", "P", "P", "P", "P", "P"],
                                    [" ", " ", " ", " ", " ", " ", " ", " "],
                                    [" ", " ", " ", " ", " ", " ", " ", " "],
                                    [" ", " ", " ", " ", " ", " ", " ", " "],
                                    [" ", " ", " ", " ", " ", " ", " ", " "],
                                    [" ", " ", " ", " ", " ", " ", " ", " "],
                                    [" ", " ", " ", " ", " ", " ", " ", " "],
                                    ["P", "P", "P", "P", "P", "P", "P", "P"],
                                    ["R", "N", "B", "Q", "K", "B", "N", "R"]]
        self.a1 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.a1_selected)
        self.b1 = Entity(model='cube', color=color.black33, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.b1_selected)
        self.c1 = Entity(model='cube', color=color.black33, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.c1_selected)
        self.d1 = Entity(model='cube', color=color.black33, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.d1_selected)
        self.e1 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.e1_selected)
        self.f1 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.f1_selected)
        self.g1 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.g1_selected)
        self.h1 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.h1_selected)
        self.a2 = Entity(model='cube', color=color.black33, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.a2_selected)
        self.b2 = Entity(model='cube', color=color.black33, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.b2_selected)
        self.c2 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.c2_selected)
        self.d2 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.d2_selected)
        self.e2 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.e2_selected)
        self.f2 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.f2_selected)
        self.g2 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.g2_selected)
        self.h2 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.h2_selected)
        self.a3 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.a3_selected)
        self.b3 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.b3_selected)
        self.c3 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.c3_selected)
        self.d3 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.d3_selected)
        self.e3 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.e3_selected)
        self.f3 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.f3_selected)
        self.g3 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.g3_selected)
        self.h3 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.h3_selected)
        self.a4 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.a4_selected)
        self.b4 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.b4_selected)
        self.c4 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.c4_selected)
        self.d4 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.d4_selected)
        self.e4 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.e4_selected)
        self.f4 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.f4_selected)
        self.g4 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.g4_selected)
        self.h4 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.h4_selected)
        self.a5 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.a5_selected)
        self.b5 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.b5_selected)
        self.c5 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.c5_selected)
        self.d5 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.d5_selected)
        self.e5 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.e5_selected)
        self.f5 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.f5_selected)
        self.g5 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.g5_selected)
        self.h5 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.h5_selected)
        self.a6 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.a6_selected)
        self.b6 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.b6_selected)
        self.c6 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.c6_selected)
        self.d6 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.d6_selected)
        self.e6 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.e6_selected)
        self.f6 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.f6_selected)
        self.g6 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.g6_selected)
        self.h6 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.h6_selected)
        self.a7 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.a7_selected)
        self.b7 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.b7_selected)
        self.c7 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.c7_selected)
        self.d7 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.d7_selected)
        self.e7 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.e7_selected)
        self.f7 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.f7_selected)
        self.g7 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.g7_selected)
        self.h7 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.h7_selected)
        self.a8 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.a8_selected)
        self.b8 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.b8_selected)
        self.c8 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.c8_selected)
        self.d8 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.d8_selected)
        self.e8 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.e8_selected)
        self.f8 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.f8_selected)
        self.g8 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.g8_selected)
        self.h8 = Entity(model='cube', color=color.black, visible=False, collider="mesh", scale_x=0.477, scale_z=0.01,
                    scale_y=0.477, on_click=Pieces.h8_selected)
        self.board = Entity(model='scene.fbx', texture='Black-board-4.jpg', scale_x=0.01, scale_z=0.01, scale_y=0.005,
                       shader=lit_with_shadows_shader)
        self.board1 = Entity(model='cube', texture='img_1.png', scale_x=5.1, scale_z=0.1, scale_y=5.1, position=(0, 0, 2.75),
                        shader=lit_with_shadows_shader)
        self.pos_reference = Entity(model='cube', visible=False)
        self.plate = Entity(model="cube", color=color.black, scale=10, collider="mesh", position=(0, -10, 0))
        self.king1 = Entity(model='king.fbx', scale=0.012, texture='white.png')
        self.king2 = Entity(model='king.fbx', scale=0.012, texture='black.png')
        self.pawn1 = Entity(model='pawn.fbx', scale=0.012, texture='white.png')
        self.pawn2 = Entity(model='pawn.fbx', scale=0.012, texture='white.png')
        self.pawn3 = Entity(model='pawn.fbx', scale=0.012, texture='white.png')
        self.pawn4 = Entity(model='pawn.fbx', scale=0.012, texture='white.png')
        self.pawn5 = Entity(model='pawn.fbx', scale=0.012, texture='white.png')
        self.pawn6 = Entity(model='pawn.fbx', scale=0.012, texture='white.png')
        self.pawn7 = Entity(model='pawn.fbx', scale=0.012, texture='white.png')
        self.pawn8 = Entity(model='pawn.fbx', scale=0.012, texture='white.png')
        self.pawn9 = Entity(model='pawn.fbx', scale=0.012, texture='black.png')
        self.pawn10 = Entity(model='pawn.fbx', scale=0.012, texture='black.png')
        self.pawn11 = Entity(model='pawn.fbx', scale=0.012, texture='black.png')
        self.pawn12 = Entity(model='pawn.fbx', scale=0.012, texture='black.png')
        self.pawn13 = Entity(model='pawn.fbx', scale=0.012, texture='black.png')
        self.pawn14 = Entity(model='pawn.fbx', scale=0.012, texture='black.png')
        self.pawn15 = Entity(model='pawn.fbx', scale=0.012, texture='black.png')
        self.pawn16 = Entity(model='pawn.fbx', scale=0.012, texture='black.png')
        self.board1.rotation_x += 180
        camera.z -= 3
        self.board.rotation_x += 90
        Sky()
    def a1_selected(self):
        self.a1.visible = True
        self.a1.color = color.random_color()
        if self.map_of_starting_board[1][1] == "P":
            self.a2.color=color.black33

    def b1_selected(self):
        self.b1.visible = True
        self.b1.color = color.random_color()

    def c1_selected(self):
        self.c1.visible = True
        self.c1.color = color.random_color()

    def d1_selected(self):
        self.d1.visible = True
        self.d1.color = color.random_color()

    def e1_selected(self):
        self.e1.visible = True
        self.e1.color = color.random_color()

    def f1_selected(self):
        self.f1.visible = True
        self.f1.color = color.random_color()

    def g1_selected(self):
        self.g1.visible = True
        self.g1.color = color.random_color()

    def h1_selected(self):
        self.h1.visible = True
        self.h1.color = color.random_color()

    def a2_selected(self):
        self.a2.visible = True
        self.a2.color = color.random_color()

    def b2_selected(self):
        self.b3.visible = True
        self.b2.color = color.random_color()

    def c2_selected(self):
        self.c2.visible = True
        self.c2.color = color.random_color()

    def d2_selected(self):
        self.d2.visible = True
        self.d2.color = color.random_color()

    def e2_selected(self):
        self.e2.visible = True
        self.e2.color = color.random_color()

    def f2_selected(self):
        self.f2.visible = True
        self.f2.color = color.random_color()

    def g2_selected(self):
        self.g2.visible = True
        self.g2.color = color.random_color()

    def h2_selected(self):
        self.h2.visible = True
        self.h2.color = color.random_color()

    def a3_selected(self):
        self.a3.visible = True
        self.a3.color = color.random_color()

    def b3_selected(self):
        self.b3.visible = True
        self.b3.color = color.random_color()

    def c3_selected(self):
        self.c3.visible = True
        self.c3.color = color.random_color()

    def d3_selected(self):
        self.d3.visible = True
        self.d3.color = color.random_color()

    def e3_selected(self):
        self.e3.visible = True
        self.e3.color = color.random_color()

    def f3_selected(self):
        self.f3.visible = True
        self.f3.color = color.random_color()

    def g3_selected(self):
        self.g3.visible = True
        self.g3.color = color.random_color()

    def h3_selected(self):
        self.h3.visible = True
        self.h3.color = color.random_color()

    def a4_selected(self):
        self.a4.visible = True
        self.a4.color = color.random_color()

    def b4_selected(self):
        self.b4.visible = True
        self.b4.color = color.random_color()

    def c4_selected(self):
        self.c4.visible = True
        self.c4.color = color.random_color()

    def d4_selected(self):
        self.d4.visible = True
        self.d4.color = color.random_color()

    def e4_selected(self):
        self.e4.visible = True
        self.e4.color = color.random_color()

    def f4_selected(self):
        self.f4.visible = True
        self.f4.color = color.random_color()

    def g4_selected(self):
        self.g4.visible = True
        self.g4.color = color.random_color()

    def h4_selected(self):
        self.h4.visible = True
        self.h4.color = color.random_color()

    def a5_selected(self):
        self.a5.visible = True
        self.a5.color = color.random_color()

    def b5_selected(self):
        self.b5.visible = True
        self.b5.color = color.random_color()

    def c5_selected(self):
        self.c5.visible = True
        self.c5.color = color.random_color()

    def d5_selected(self):
        self.d5.visible = True
        self.d5.color = color.random_color()

    def e5_selected(self):
        self.e5.visible = True
        self.e5.color = color.random_color()

    def f5_selected(self):
        self.f5.visible = True
        self.f5.color = color.random_color()

    def g5_selected(self):
        self.g5.visible = True
        self.g5.color = color.random_color()

    def h5_selected(self):
        self.h5.visible = True
        self.h5.color = color.random_color()

    def a6_selected(self):
        self.a6.visible = True
        self.a6.color = color.random_color()

    def b6_selected(self):
        self.b6.visible = True
        self.b6.color = color.random_color()

    def c6_selected(self):
        self.c6.visible = True
        self.c6.color = color.random_color()

    def d6_selected(self):
        self.d6.visible = True
        self.d6.color = color.random_color()

    def e6_selected(self):
        self.e6.visible = True
        self.e6.color = color.random_color()

    def f6_selected(self):
        self.f6.visible = True
        self.f6.color = color.random_color()

    def g6_selected(self):
        self.g6.visible = True
        self.g6.color = color.random_color()

    def h6_selected(self):
        self.h6.visible = True
        self.h6.color = color.random_color()

    def a7_selected(self):
        self.a7.visible = True
        self.a7.color = color.random_color()

    def b7_selected(self):
        self.b7.visible = True
        self.b7.color = color.random_color()

    def c7_selected(self):
        self.c7.visible = True
        self.c7.color = color.random_color()

    def d7_selected(self):
        self.d7.visible = True
        self.d7.color = color.random_color()

    def e7_selected(self):
        self.e7.visible = True
        self.e7.color = color.random_color()

    def f7_selected(self):
        self.f7.visible = True
        self.f7.color = color.random_color()

    def g7_selected(self):
        self.g7.visible = True
        self.g7.color = color.random_color()

    def h7_selected(self):
        self.h7.visible = True
        self.h7.color = color.random_color()

    def a8_selected(self):
        self.a8.visible = True
        self.a8.color = color.random_color()

    def b8_selected(self):
        self.b8.visible = True
        self.b8.color = color.random_color()

    def c8_selected(self):
        self.c8.visible = True
        self.c8.color = color.random_color()

    def d8_selected(self):
        self.d8.visible = True
        self.d8.color = color.random_color()

    def e8_selected(self):
        self.e8.visible = True
        self.e8.color = color.random_color()

    def f8_selected(self):
        self.f8.visible = True
        self.f8.color = color.random_color()

    def g8_selected(self):
        self.g8.visible = True
        self.g8.color = color.random_color()

    def h8_selected(self):
        self.h8.visible = True
        self.h8.color = color.random_color()

    def update(self):
        # self.a1.on_click = selected(self.a1)
        self.king1.set_position((0.24, -1.647, -0.55), relative_to=self.pos_reference)
        self.king2.set_position((0.24, 1.647, -0.55), relative_to=self.pos_reference)
        self.pawn1.set_position((-1.633, -1.17, -0.53), relative_to=self.pos_reference)
        self.pawn2.set_position((-1.159, -1.17, -0.53), relative_to=self.pos_reference)
        self.pawn3.set_position((-0.69, -1.17, -0.53), relative_to=self.pos_reference)
        self.pawn4.set_position((-0.22, -1.17, -0.53), relative_to=self.pos_reference)
        self.pawn5.set_position((0.24, -1.17, -0.53), relative_to=self.pos_reference)
        self.pawn6.set_position((0.71, -1.17, -0.53), relative_to=self.pos_reference)
        self.pawn7.set_position((1.18, -1.17, -0.53), relative_to=self.pos_reference)
        self.pawn8.set_position((1.65, -1.17, -0.53), relative_to=self.pos_reference)
        self.pawn9.set_position((-1.633, 1.172, -0.53), relative_to=self.pos_reference)
        self.pawn10.set_position((-1.159, 1.172, -0.53), relative_to=self.pos_reference)
        self.pawn11.set_position((-0.69, 1.172, -0.53), relative_to=self.pos_reference)
        self.pawn12.set_position((-0.22, 1.172, -0.53), relative_to=self.pos_reference)
        self.pawn13.set_position((0.24, 1.172, -0.53), relative_to=self.pos_reference)
        self.pawn14.set_position((0.71, 1.172, -0.53), relative_to=self.pos_reference)
        self.pawn15.set_position((1.18, 1.172, -0.53), relative_to=self.pos_reference)
        self.pawn16.set_position((1.65, 1.172, -0.53), relative_to=self.pos_reference)
        self.a1.set_position((-1.633, -1.647, -0.03), relative_to=self.pos_reference)
        self.b1.set_position((-1.159, -1.647, -0.03), relative_to=self.pos_reference)
        self.c1.set_position((-0.69, -1.647, -0.03), relative_to=self.pos_reference)
        self.d1.set_position((-0.22, -1.647, -0.03), relative_to=self.pos_reference)
        self.e1.set_position((0.24, -1.647, -0.03), relative_to=self.pos_reference)
        self.f1.set_position((0.71, -1.647, -0.03), relative_to=self.pos_reference)
        self.g1.set_position((1.18, -1.647, -0.03), relative_to=self.pos_reference)
        self.h1.set_position((1.65, -1.647, -0.03), relative_to=self.pos_reference)
        self.a2.set_position((-1.633, -1.17, -0.03), relative_to=self.pos_reference)
        self.b2.set_position((-1.159, -1.17, -0.03), relative_to=self.pos_reference)
        self.c2.set_position((-0.69, -1.17, -0.03), relative_to=self.pos_reference)
        self.d2.set_position((-0.22, -1.17, -0.03), relative_to=self.pos_reference)
        self.e2.set_position((0.24, -1.17, -0.03), relative_to=self.pos_reference)
        self.f2.set_position((0.71, -1.17, -0.03), relative_to=self.pos_reference)
        self.g2.set_position((1.18, -1.17, -0.03), relative_to=self.pos_reference)
        self.h2.set_position((1.65, -1.17, -0.03), relative_to=self.pos_reference)
        self.a3.set_position((-1.633, -0.694, -0.03), relative_to=self.pos_reference)
        self.b3.set_position((-1.159, -0.694, -0.03), relative_to=self.pos_reference)
        self.c3.set_position((-0.69, -0.694, -0.03), relative_to=self.pos_reference)
        self.d3.set_position((-0.22, -0.694, -0.03), relative_to=self.pos_reference)
        self.e3.set_position((0.24, -0.694, -0.03), relative_to=self.pos_reference)
        self.f3.set_position((0.71, -0.694, -0.03), relative_to=self.pos_reference)
        self.g3.set_position((1.18, -0.694, -0.03), relative_to=self.pos_reference)
        self.h3.set_position((1.65, -0.694, -0.03), relative_to=self.pos_reference)
        self.a4.set_position((-1.633, -0.231, -0.03), relative_to=self.pos_reference)
        self.b4.set_position((-1.159, -0.231, -0.03), relative_to=self.pos_reference)
        self.c4.set_position((-0.69, -0.231, -0.03), relative_to=self.pos_reference)
        self.d4.set_position((-0.22, -0.231, -0.03), relative_to=self.pos_reference)
        self.e4.set_position((0.24, -0.231, -0.03), relative_to=self.pos_reference)
        self.f4.set_position((0.71, -0.231, -0.03), relative_to=self.pos_reference)
        self.g4.set_position((1.18, -0.231, -0.03), relative_to=self.pos_reference)
        self.h4.set_position((1.65, -0.231, -0.03), relative_to=self.pos_reference)
        self.a5.set_position((-1.633, 0.243, -0.03), relative_to=self.pos_reference)
        self.b5.set_position((-1.159, 0.243, -0.03), relative_to=self.pos_reference)
        self.c5.set_position((-0.69, 0.243, -0.03), relative_to=self.pos_reference)
        self.d5.set_position((-0.22, 0.243, -0.03), relative_to=self.pos_reference)
        self.e5.set_position((0.24, 0.243, -0.03), relative_to=self.pos_reference)
        self.f5.set_position((0.71, 0.243, -0.03), relative_to=self.pos_reference)
        self.g5.set_position((1.18, 0.243, -0.03), relative_to=self.pos_reference)
        self.h5.set_position((1.65, 0.243, -0.03), relative_to=self.pos_reference)
        self.a6.set_position((-1.633, 0.718, -0.03), relative_to=self.pos_reference)
        self.b6.set_position((-1.159, 0.718, -0.03), relative_to=self.pos_reference)
        self.c6.set_position((-0.69, 0.718, -0.03), relative_to=self.pos_reference)
        self.d6.set_position((-0.22, 0.718, -0.03), relative_to=self.pos_reference)
        self.e6.set_position((0.24, 0.718, -0.03), relative_to=self.pos_reference)
        self.f6.set_position((0.71, 0.718, -0.03), relative_to=self.pos_reference)
        self.g6.set_position((1.18, 0.718, -0.03), relative_to=self.pos_reference)
        self.h6.set_position((1.65, 0.718, -0.03), relative_to=self.pos_reference)
        self.a7.set_position((-1.633, 1.172, -0.03), relative_to=self.pos_reference)
        self.b7.set_position((-1.159, 1.172, -0.03), relative_to=self.pos_reference)
        self.c7.set_position((-0.69, 1.172, -0.03), relative_to=self.pos_reference)
        self.d7.set_position((-0.22, 1.172, -0.03), relative_to=self.pos_reference)
        self.e7.set_position((0.24, 1.172, -0.03), relative_to=self.pos_reference)
        self.f7.set_position((0.71, 1.172, -0.03), relative_to=self.pos_reference)
        self.g7.set_position((1.18, 1.172, -0.03), relative_to=self.pos_reference)
        self.h7.set_position((1.65, 1.172, -0.03), relative_to=self.pos_reference)
        self.a8.set_position((-1.633, 1.647, -0.03), relative_to=self.pos_reference)
        self.b8.set_position((-1.159, 1.647, -0.03), relative_to=self.pos_reference)
        self.c8.set_position((-0.69, 1.647, -0.03), relative_to=self.pos_reference)
        self.d8.set_position((-0.22, 1.647, -0.03), relative_to=self.pos_reference)
        self.e8.set_position((0.24, 1.647, -0.03), relative_to=self.pos_reference)
        self.f8.set_position((0.71, 1.647, -0.03), relative_to=self.pos_reference)
        self.g8.set_position((1.18, 1.647, -0.03), relative_to=self.pos_reference)
        self.h8.set_position((1.65, 1.647, -0.03), relative_to=self.pos_reference)
        self.pos_reference.rotation_x += held_keys["w"]
        self.pos_reference.rotation_x -= held_keys["s"]
        self.pos_reference.rotation_y -= held_keys["d"]
        self.pos_reference.rotation_y += held_keys["a"]
        self.pos_reference.rotation_y -= held_keys["e"]
        self.pos_reference.rotation_y += held_keys["q"]
        self.board.rotation_x += held_keys["w"]
        self.board.rotation_x -= held_keys["s"]
        self.board.rotation_y -= held_keys["d"]
        self.board.rotation_y += held_keys["a"]
        self.board.rotation_y -= held_keys["e"]
        self.board.rotation_y += held_keys["q"]
        self.board1.rotation_x += held_keys["w"]
        self.board1.rotation_x -= held_keys["s"]
        self.board1.rotation_y -= held_keys["d"]
        self.board1.rotation_y += held_keys["a"]
        self.board1.rotation_y -= held_keys["e"]
        self.board1.rotation_y += held_keys["q"]
        self.king1.rotation_x = self.pos_reference.rotation_x + 270
        self.king1.rotation_y = self.pos_reference.rotation_y
        self.king2.rotation_x = self.pos_reference.rotation_x + 270
        self.king2.rotation_y = self.pos_reference.rotation_y
        self.pawn1.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn1.rotation_y = self.pos_reference.rotation_y
        self.pawn2.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn2.rotation_y = self.pos_reference.rotation_y
        self.pawn3.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn3.rotation_y = self.pos_reference.rotation_y
        self.pawn4.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn4.rotation_y = self.pos_reference.rotation_y
        self.pawn5.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn5.rotation_y = self.pos_reference.rotation_y
        self.pawn6.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn6.rotation_y = self.pos_reference.rotation_y
        self.pawn7.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn7.rotation_y = self.pos_reference.rotation_y
        self.pawn8.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn8.rotation_y = self.pos_reference.rotation_y
        self.pawn9.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn9.rotation_y = self.pos_reference.rotation_y
        self.pawn10.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn10.rotation_y = self.pos_reference.rotation_y
        self.pawn11.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn11.rotation_y = self.pos_reference.rotation_y
        self.pawn12.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn12.rotation_y = self.pos_reference.rotation_y
        self.pawn13.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn13.rotation_y = self.pos_reference.rotation_y
        self.pawn14.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn14.rotation_y = self.pos_reference.rotation_y
        self.pawn15.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn15.rotation_y = self.pos_reference.rotation_y
        self.pawn16.rotation_x = self.pos_reference.rotation_x + 270
        self.pawn16.rotation_y = self.pos_reference.rotation_y
        self.a1.rotation_x = self.pos_reference.rotation_x
        self.a1.rotation_y = self.pos_reference.rotation_y
        self.b1.rotation_x = self.pos_reference.rotation_x
        self.b1.rotation_y = self.pos_reference.rotation_y
        self.c1.rotation_x = self.pos_reference.rotation_x
        self.c1.rotation_y = self.pos_reference.rotation_y
        self.d1.rotation_x = self.pos_reference.rotation_x
        self.d1.rotation_y = self.pos_reference.rotation_y
        self.e1.rotation_x = self.pos_reference.rotation_x
        self.e1.rotation_y = self.pos_reference.rotation_y
        self.f1.rotation_x = self.pos_reference.rotation_x
        self.f1.rotation_y = self.pos_reference.rotation_y
        self.g1.rotation_x = self.pos_reference.rotation_x
        self.g1.rotation_y = self.pos_reference.rotation_y
        self.h1.rotation_x = self.pos_reference.rotation_x
        self.h1.rotation_y = self.pos_reference.rotation_y
        self.a2.rotation_x = self.pos_reference.rotation_x
        self.a2.rotation_y = self.pos_reference.rotation_y
        self.b2.rotation_x = self.pos_reference.rotation_x
        self.b2.rotation_y = self.pos_reference.rotation_y
        self.c2.rotation_x = self.pos_reference.rotation_x
        self.c2.rotation_y = self.pos_reference.rotation_y
        self.d2.rotation_x = self.pos_reference.rotation_x
        self.d2.rotation_y = self.pos_reference.rotation_y
        self.e2.rotation_x = self.pos_reference.rotation_x
        self.e2.rotation_y = self.pos_reference.rotation_y
        self.f2.rotation_x = self.pos_reference.rotation_x
        self.f2.rotation_y = self.pos_reference.rotation_y
        self.g2.rotation_x = self.pos_reference.rotation_x
        self.g2.rotation_y = self.pos_reference.rotation_y
        self.h2.rotation_x = self.pos_reference.rotation_x
        self.h2.rotation_y = self.pos_reference.rotation_y
        self.a3.rotation_x = self.pos_reference.rotation_x
        self.a3.rotation_y = self.pos_reference.rotation_y
        self.b3.rotation_x = self.pos_reference.rotation_x
        self.b3.rotation_y = self.pos_reference.rotation_y
        self.c3.rotation_x = self.pos_reference.rotation_x
        self.c3.rotation_y = self.pos_reference.rotation_y
        self.d3.rotation_x = self.pos_reference.rotation_x
        self.d3.rotation_y = self.pos_reference.rotation_y
        self.e3.rotation_x = self.pos_reference.rotation_x
        self.e3.rotation_y = self.pos_reference.rotation_y
        self.f3.rotation_x = self.pos_reference.rotation_x
        self.f3.rotation_y = self.pos_reference.rotation_y
        self.g3.rotation_x = self.pos_reference.rotation_x
        self.g3.rotation_y = self.pos_reference.rotation_y
        self.h3.rotation_x = self.pos_reference.rotation_x
        self.h3.rotation_y = self.pos_reference.rotation_y
        self.a4.rotation_x = self.pos_reference.rotation_x
        self.a4.rotation_y = self.pos_reference.rotation_y
        self.b4.rotation_x = self.pos_reference.rotation_x
        self.b4.rotation_y = self.pos_reference.rotation_y
        self.c4.rotation_x = self.pos_reference.rotation_x
        self.c4.rotation_y = self.pos_reference.rotation_y
        self.d4.rotation_x = self.pos_reference.rotation_x
        self.d4.rotation_y = self.pos_reference.rotation_y
        self.e4.rotation_x = self.pos_reference.rotation_x
        self.e4.rotation_y = self.pos_reference.rotation_y
        self.f4.rotation_x = self.pos_reference.rotation_x
        self.f4.rotation_y = self.pos_reference.rotation_y
        self.g4.rotation_x = self.pos_reference.rotation_x
        self.g4.rotation_y = self.pos_reference.rotation_y
        self.h4.rotation_x = self.pos_reference.rotation_x
        self.h4.rotation_y = self.pos_reference.rotation_y
        self.a5.rotation_x = self.pos_reference.rotation_x
        self.a5.rotation_y = self.pos_reference.rotation_y
        self.b5.rotation_x = self.pos_reference.rotation_x
        self.b5.rotation_y = self.pos_reference.rotation_y
        self.c5.rotation_x = self.pos_reference.rotation_x
        self.c5.rotation_y = self.pos_reference.rotation_y
        self.d5.rotation_x = self.pos_reference.rotation_x
        self.d5.rotation_y = self.pos_reference.rotation_y
        self.e5.rotation_x = self.pos_reference.rotation_x
        self.e5.rotation_y = self.pos_reference.rotation_y
        self.f5.rotation_x = self.pos_reference.rotation_x
        self.f5.rotation_y = self.pos_reference.rotation_y
        self.g5.rotation_x = self.pos_reference.rotation_x
        self.g5.rotation_y = self.pos_reference.rotation_y
        self.h5.rotation_x = self.pos_reference.rotation_x
        self.h5.rotation_y = self.pos_reference.rotation_y
        self.a6.rotation_x = self.pos_reference.rotation_x
        self.a6.rotation_y = self.pos_reference.rotation_y
        self.b6.rotation_x = self.pos_reference.rotation_x
        self.b6.rotation_y = self.pos_reference.rotation_y
        self.c6.rotation_x = self.pos_reference.rotation_x
        self.c6.rotation_y = self.pos_reference.rotation_y
        self.d6.rotation_x = self.pos_reference.rotation_x
        self.d6.rotation_y = self.pos_reference.rotation_y
        self.e6.rotation_x = self.pos_reference.rotation_x
        self.e6.rotation_y = self.pos_reference.rotation_y
        self.f6.rotation_x = self.pos_reference.rotation_x
        self.f6.rotation_y = self.pos_reference.rotation_y
        self.g6.rotation_x = self.pos_reference.rotation_x
        self.g6.rotation_y = self.pos_reference.rotation_y
        self.h6.rotation_x = self.pos_reference.rotation_x
        self.h6.rotation_y = self.pos_reference.rotation_y
        self.a7.rotation_x = self.pos_reference.rotation_x
        self.a7.rotation_y = self.pos_reference.rotation_y
        self.b7.rotation_x = self.pos_reference.rotation_x
        self.b7.rotation_y = self.pos_reference.rotation_y
        self.c7.rotation_x = self.pos_reference.rotation_x
        self.c7.rotation_y = self.pos_reference.rotation_y
        self.d7.rotation_x = self.pos_reference.rotation_x
        self.d7.rotation_y = self.pos_reference.rotation_y
        self.e7.rotation_x = self.pos_reference.rotation_x
        self.e7.rotation_y = self.pos_reference.rotation_y
        self.f7.rotation_x = self.pos_reference.rotation_x
        self.f7.rotation_y = self.pos_reference.rotation_y
        self.g7.rotation_x = self.pos_reference.rotation_x
        self.g7.rotation_y = self.pos_reference.rotation_y
        self.h7.rotation_x = self.pos_reference.rotation_x
        self.h7.rotation_y = self.pos_reference.rotation_y
        self.a8.rotation_x = self.pos_reference.rotation_x
        self.a8.rotation_y = self.pos_reference.rotation_y
        self.b8.rotation_x = self.pos_reference.rotation_x
        self.b8.rotation_y = self.pos_reference.rotation_y
        self.c8.rotation_x = self.pos_reference.rotation_x
        self.c8.rotation_y = self.pos_reference.rotation_y
        self.d8.rotation_x = self.pos_reference.rotation_x
        self.d8.rotation_y = self.pos_reference.rotation_y
        self.e8.rotation_x = self.pos_reference.rotation_x
        self.e8.rotation_y = self.pos_reference.rotation_y
        self.f8.rotation_x = self.pos_reference.rotation_x
        self.f8.rotation_y = self.pos_reference.rotation_y
        self.g8.rotation_x = self.pos_reference.rotation_x
        self.g8.rotation_y = self.pos_reference.rotation_y
        self.h8.rotation_x = self.pos_reference.rotation_x
        self.h8.rotation_y = self.pos_reference.rotation_y



"""FirstPersonController()"""

"""self.position=(-1.6467,-1.6467,-0.1)"""
"""pivot = Entity()
SpotLight(parent=pivot, z=-100, shadows=True, rotation=(0, 0, 0))"""

Pieces()
app.run()

#table
"""table=Entity(model='table1.fbx', texture="mask_dirt.jpg", scale_x=0.01, scale_z=0.01, scale_y=0.01, self.position=(0,-3.3, 3))
table1=Entity(model='table1.fbx', texture="ambient_occlusion.jpg", scale_x=0.01, scale_z=0.01, scale_y=0.01, self.position=(0,-3.3, 3))
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