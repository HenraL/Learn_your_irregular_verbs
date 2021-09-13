from pygame.math import Vector3 as V3

W,H = 900,600
FPS = 40

THEME = "human"

AA = True


MODELS = ["Aerocrush","BangDynamics","CabalysticsAndCo","Dropplet","Elbus",
            "F12","GorschType","Herschel","Illuminus"]
HERO_COLOR = (0,0,255)
HERO_MODEL = None
HERO_NAME = "Hero"

PRICE = 5000.

MOVE_DELTA_I = 5
VISIBILITY = 800
SPEED = 0#to be deleted

##HERO_POS = V3(0,-4,15)
HERO_POS = V3(0,-4,10)
ORIGINAL_HERO_POS = V3(HERO_POS)

MIN_BOX_THICKNESS = 10

RAILW = 12
RAILH = 12

TURN = 2. / 10.
FRICTION = 1. / 500.
MASS = 1. / 10.

CURRENT_QUALITY = 1.

BACKGROUNDS = {1.:"background1.jpg",
                1.5:"PaulinaRiva.png",
                2.:"ChristinArredondo.png"}

OVERTAKE_SLOWER = 0.75
LIFE_FACTOR = 10
SPEED_HUD = 80.

DEBRIS_SIZE = [0.5, 1.]
N_DEBRIS = 50
DEBRIS_ITER = 100

ANGLE_TURN = 1
ANGLE_TURN_V = 1

VISURAIL_LENGTH = 20
VISURAIL_SPACE = 2*VISURAIL_LENGTH
VISURAIL_NMAX = 10

COLOR_ROTATING = (0,255,0)
COLOR_MOVING = (255,0,0)

GARAGE_POS = V3(0,0,20)

scene = None
player = None
players = []
NPLAYERS = 12
CATEGORIES = ["Intergalatic League", "International Championship", "National cup"]

ZFINISH = 3000
ENGINE_POWER = 0.03
MIN_POWER = 0.8
MAX_POWER = 1.2
MIN_MASS = 0.6
MAX_MASS = 1.4
MIN_TURN = 0.6
MAX_TURN = 1.2
MIN_FUEL = 1800
MAX_FUEL = 2400

MERCHANT_PROBABILITY = 0.6

QUIT_GAME = False

ghost = None

def flush():
    global player, scene, players
    for p in players:
        if p.vessel:
            p.vessel.reset()
    scene = None
