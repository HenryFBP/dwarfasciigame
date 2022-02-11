import logging
from typing import Union

from asciimatics.event import KeyboardEvent

from lithicrivers.model import Vector2, Viewport

GAME_NAME = 'LithicRivers'
# DEFAULT_SIZE = (50, 15)
DEFAULT_SIZE = Vector2(20, 20)
DEFAULT_VIEWPORT = Viewport(Vector2(0, 0), Vector2(5, 5))
DEFAULT_PLAYER_POSITION = Vector2(0, 0)
LOGFILENAME = GAME_NAME + '.log'

VEC_UP = Vector2(0, 1)
VEC_DOWN = Vector2(0, -1)
VEC_LEFT = Vector2(-1, 0)
VEC_RIGHT = Vector2(1, 0)


class Keymap:
    def __init__(self):
        self.MOVE_UP = 'w'
        self.MOVE_LEFT = 'a'
        self.MOVE_DOWN = 's'
        self.MOVE_RIGHT = 'd'

        self.MOVEMENT_VECTOR_MAP = {
            self.MOVE_UP: Vector2(0, -1),
            self.MOVE_LEFT: Vector2(-1, 0),
            self.MOVE_DOWN: Vector2(0, 1),
            self.MOVE_RIGHT: Vector2(1, 0)
        }

        self.VIEWPORT_SLIDE_LEFT = '['
        self.VIEWPORT_SLIDE_RIGHT = ']'

        self.MINE = 'u'

    @staticmethod
    def char_from_keyboard_event(ke: KeyboardEvent) -> Union[None, str]:
        try:
            ke_char = chr(ke.key_code).lower()
            return ke_char
        except ValueError as ve:
            logging.debug(
                "Could not handle this KeyboardEvent -- {} -- probably a special key: {}".format(ke.key_code, ke, ))
            return None

    def matches_keyboard_event(self, key_name: str, ke: KeyboardEvent):

        try:
            key = self.__getattribute__(key_name)
        except AttributeError as ae:
            raise AttributeError("No key named {} found.\nValid keys: {}".format(key_name, dir(self)))

        ke_char = Keymap.char_from_keyboard_event(ke)

        return ke_char == key.lower()


KEYMAP = Keymap()
