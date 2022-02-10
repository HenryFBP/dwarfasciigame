import logging
from typing import List, Tuple, Dict

import numpy

from dwarfasciigame.settings import DEFAULT_SIZE


class Renderable:
    def __init__(self, sprite_sheet):
        self.sprite_sheet = sprite_sheet
        if not sprite_sheet:
            self.sprite_sheet = ['?', '??\n'
                                      '??', '???\n'
                                            '???\n'
                                            '???']

    def render(self, scale: int = 1) -> str:
        normscale = scale - 1
        return self.sprite_sheet[normscale]


class Entity:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.stamina = 100

    def move(self, vecoffset: Tuple[int, int]):
        xoffset, yoffset = vecoffset

        self.x += xoffset
        self.y += yoffset

    def calcOffset(self, vec: Tuple[int, int]) -> Tuple[int, int]:
        """Where would I move, if I did move?"""
        xoffset, yoffset = vec

        return (
            self.x + xoffset,
            self.y + yoffset
        )

    def moveUp(self):
        self.move((0, 1))

    def moveDown(self):
        self.move((0, -1))

    def moveLeft(self):
        self.move((-1, 0))

    def moveRight(self):
        self.move((1, 0))


class Player(Entity, Renderable):

    def __init__(self):
        # super(Entity, self).__init__()

        # super(Renderable, self).__init__(sprite_sheet=['$', '[]\n'
        #                                                     '%%'])

        super(Entity).__init__()
        super(Renderable).__init__(['$', '[]\n'
                                         '%%'])


class Items:
    """
    A bunch of default items.
    """

    @staticmethod
    def Rock():
        return Item("Rock",
                    charsheet=['*'])

    @staticmethod
    def Gold_Nugget():
        return Item("Gold Nugget",
                    charsheet=['c'])

    @staticmethod
    def Stick():
        return Item("Stick",
                    charsheet=['\\'])


class Item:
    def __init__(self, name, charsheet: List[str] = None):
        self.name = name
        self.charsheet = charsheet

    def render(self, scale=1):
        return self.charsheet[scale - 1]


class Tile:
    def __init__(self, name: str, charsheet: List[str] = None, drops: Dict[float, Item] = None):
        self.name = name
        self.charsheet = charsheet
        self.drops = drops

    def render(self, scale=1) -> str:
        return self.charsheet[scale - 1]


def gen_tile(choices: List[Tile] = None, weights: List[int] = None) -> Tile:
    if choices is None:
        choices = [Tiles.Tree(),
                   Tiles.Dirt()]

    if weights is None:
        weights = [5, 100]

    if len(weights) != len(choices):
        ve = ValueError(f"Weights and choices for {gen_tile.__name__}() must be the same length!")
        logging.error(ve)
        raise ve

    weights = numpy.asarray(weights)

    normalizedWeights = weights

    if weights.sum() != 1:
        normalizedWeights = weights / weights.sum()

    return numpy.random.choice(choices, p=normalizedWeights)


class Tiles:
    """
    A bunch of default tiles.
    """

    @staticmethod
    def Dirt():
        return Tile('Dirt',
                    [',', ',.\n'
                          '.,', ',.,\n'
                                '.,.\n'
                                ',.,'],
                    {0.99: Items.Rock(),
                     0.01: Items.Gold_Nugget()})

    @staticmethod
    def Tree():
        return Tile('Tree',
                    ['t', '/\\\n'
                          '||', '/|\\\n'
                                ';|;\n'
                                '/|\\\n'],
                    {1.00: Items.Stick()})


class World:

    def get_height(self):
        return self.size[1]

    def get_width(self):
        return self.size[0]

    @staticmethod
    def gen_random_world(size: Tuple[int, int]) -> List[List[Tile]]:
        width, height = size
        resultworld = []
        for y in range(0, height):
            row = []
            for x in range(0, width):
                row.append(gen_tile())
            resultworld.append(row)
        return resultworld

    def __init__(self, name="Gaia", size=DEFAULT_SIZE):
        self.size = size
        self.name = name
        self.worlddata = World.gen_random_world(size)
        self.gametick = 0

    def get_tile_at(self, x: int, y: int):
        return self.worlddata[y][x]


class Game:
    def __init__(self, player: Player = None, world: World = None):

        if player is None:
            player = Player()

        if world is None:
            world = World()

        self.player = player
        self.world = world

    def get_tile_at_player_feet(self) -> Tile:
        return self.world.get_tile_at(self.player.x, self.player.y)

    def render_world(self, scale: int = 1) -> List[List[str]]:
        r"""
        :param scale: Scaling for sprites.      <br><br><pre><code>
        |   1 = x, 2 = \/, 3 = \ /, etc.        <br>
        |              /\       x               <br>
        |                      / \              <br></pre></code>
        :return: A list of tiles.
        """

        ret = []

        for row in self.world.worlddata:
            retrow = []
            for tile in row:
                sprite = tile.render(scale=scale)
                logging.debug('render: {}'.format(sprite))
                retrow.append(sprite)  # TODO: will break with scale>2... we need to print to a buffer
            ret.append(retrow)

        # TODO: Assert ret is well-formed

        logging.info("player x,y={:2d},{:2d}".format(self.player.x, self.player.y))
        ret[self.player.y][self.player.x] = self.player.render(scale=scale)

        return ret

    def move_player(self, vec):
        possiblePosition = self.player.calcOffset(vec)

        # check bounds
        if (
                (possiblePosition[0] < 0) or
                (possiblePosition[1] < 0) or
                (possiblePosition[0] >= self.world.get_width()) or
                (possiblePosition[1] >= self.world.get_height())
        ):
            logging.debug("Tried to move OOB! {} would have resulted in {}".format(vec, possiblePosition))
            return

        self.player.move(vec)
