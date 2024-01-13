from joystick import Joystick
from enum import Enum
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class TextPrint(object):
    """
    This is a simple class that will help us print to the screen
    It has nothing to do with the joysticks, just outputting the
    information.
    """

    def __init__(self):
        """ Constructor """
        self.reset()
        self.x_pos = 10
        self.y_pos = 10
        self.font = pygame.font.Font(None, 20)

    def print(self, my_screen, text_string):
        """ Draw text onto the screen. """
        text_bitmap = self.font.render(text_string, True, BLACK)
        my_screen.blit(text_bitmap, [self.x_pos, self.y_pos])
        self.y_pos += self.line_height

    def reset(self):
        """ Reset text to the top of the screen. """
        self.x_pos = 10
        self.y_pos = 10
        self.line_height = 15

    def indent(self):
        """ Indent the next line of text """
        self.x_pos += 10

    def unindent(self):
        """ Unindent the next line of text """
        self.x_pos -= 10


class Arrow(Enum):
    """
    Smufl Arrows
    https://w3c.github.io/smufl/latest/tables/arrows-and-arrowheads.html
    N U+EB68 arrowWhiteUp
    NW U+EB6F arrowWhiteUpLeft
    NE U+EB69 arrowWhiteUpRight
    W U+EB6E arrowWhiteLeft
    E U+EB6A arrowWhiteRight
    SW U+EB6D arrowWhiteDownLeft
    SE U+EB6B arrowWhiteDownRight
    S U+EB6C arrowWhiteDown
    """
    N = 'arrowBlackUp'
    NW = 'arrowBlackUpLeft'
    NE = 'arrowBlackUpRight'
    W = 'arrowBlackLeft'
    E = 'arrowBlackRight'
    SW = 'arrowBlackDownLeft'
    SE = 'arrowBlackDownRight'
    S = 'arrowBlackDown'

class Colour(Enum):
    """
    Arrow notes COLOURS
    https://digitlearning.co.uk/what-are-arrownotes/

    c = red N or S
    d = orange NW
    e = yellow NE
    f = light green W
    g = dark green E
    a = purple SW
    b = pink SE
    c = red N or S
    """
    N = '#FF0000'
    NW = '#ffa500'
    NE = '#FFFF00'
    W = '#00FF00'
    E = '#006400'
    SW = '#800080'
    SE = '#FF00FF'
    S = '#FF0000'

class Solfa(Enum):
    """
    Sol Fa translation of compass points
    to do, re, mi, fa, sol, la, ti, do.
    Flats and sharps COULD be represented by 'a' and 'e'
    or simply 'b' and '#'
    """
    N = 'do'
    NW = 're'
    NE = 'mi'
    W = 'fa'
    E = 'sol'
    SW = 'la'
    SE = 'ti'
    S = 'do'


# todo - transpositions!!! this is in C only. Tonic & position & arrows
#  needs to be related to parent key.
pygame.init()

# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MachAInst - basic output")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# init the joystick inst
js = Joystick()

def mainloop():
    # Get ready to print
    textPrint = TextPrint()

    while True:
        js.get_data()

        # DRAWING STEP
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        textPrint.reset()

        if js.neopitch:
            # make arrow
            compass = js.compass
            arrow_direction = Arrow[compass].value
            arrow_colour = Colour[compass].value

            # make solfa
            solfa = Solfa[compass].value

            textPrint.print(screen, "Compass {}".format(compass))
            textPrint.print(screen, "arrow_direction {}".format(arrow_direction))
            textPrint.print(screen, "arrow_colour {}".format(arrow_colour))
            textPrint.print(screen, "note {}".format(js.neopitch))
            textPrint.print(screen, "solfa {}".format(solfa))

            print(f"compass = {compass}; arrow_direction = {arrow_direction};"
                  f"arrow_colour = {arrow_colour}; "
                  f"note = {js.neopitch}; solfa = {solfa}")

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # Limit to 60 frames per second
        clock.tick(60)


if __name__ == "__main__":
    mainloop()