from neoscore.common import *
from enum import Enum

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
    Inspired by Figure Notes
    https://figurenotes.org/what-is-figurenotes/

    And Arrow notes concept
    https://digitlearning.co.uk/what-are-arrownotes/

    c = red N or S
    b = green NE
    a = yellow NW
    g = black E
    f = Blue W
    e = grey SE
    d = brown SW
    c = red N or S

    """
    N = '#ff0000'
    NE = '#33cc33'
    NW = '#FFA500'
    W = '#0099ff'
    E = '#000000'
    SE = '#d9d9d9'
    SW = '#996633'
    S = '#ff0000'

class Solfa(Enum):
    """
    Sol Fa translation of compass points
    to do, re, mi, fa, sol, la, ti, do.
    Flats and sharps COULD be represented by 'a' and 'e'
    or simply 'b' and '#'
    """
    # todo - flats and sharps
    N = 'do'
    NW = 're'
    NE = 'mi'
    W = 'fa'
    E = 'sol'
    SW = 'la'
    SE = 'ti'
    S = 'do'


class Notation:
    """Builds all the notation images for the game"""

    def __init__(self):
        # init neoscore
        neoscore.setup()

        # note to print
        self.note_to_show = None

        # save path
        self.save_path = "../media/generated_notes/"

        # compile a list of generated png's to optimise any duplications
        # self.notelist = os.listdir(self.save_path)

    def make_notation(self, notes: list,
                      compass: str,
                      arrow_help: bool = True,
                      name_help: bool = True
                      ) -> str:
        """
        Makes a new neoscore note on stave with option help indications of arrow and name

        :param notes: list of notes to put on stave
        :param compass: compass direction for mapping to arrow glyph and colour

        :return: path to created neoscore glyph
        """

        # setup an empty list for removal later
        list_of_objects = []

        # iterate through note list
        for i, note in enumerate(notes):
            # move position along for each note
            pos_offset_x = i * 10

            # make a new note name to build extra help factors
            note_filename = note+compass
            if arrow_help:
                note_filename += "_arrow"
            if name_help:
                note_filename += "_name"
            note_filename += ".png"

            empty_staff = Staff(ORIGIN, None, Mm(200), line_spacing=Mm(5))
            Clef(Mm(60), empty_staff, 'treble')

            n = Chordrest(Mm(100 + (pos_offset_x + 10)),
                           empty_staff,
                           [note],
                           Duration(1, 2))
            # add to existing note list
            list_of_objects.append(n)

            if arrow_help:
                arrow_direction = Arrow[compass].value
                arrow_colour = Colour[compass].value
                colour_brush = Brush(color=arrow_colour)
                help_arrow = MusicText((Mm(20), Mm(-20)), n, arrow_direction,
                                     alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER,
                                     brush=colour_brush,
                                       scale=2
                                     )
                list_of_objects.append(help_arrow)

            if name_help:
                upper_note = note[0].upper() + note[1:]
                help_text = Text((Mm(-20), Mm(-15)), n, upper_note,
                     alignment_x=AlignmentX.CENTER,
                     alignment_y=AlignmentY.CENTER,
                                 scale=4
                     )
                list_of_objects.append(help_text)

            # render new image
            save_dest = self.save_path + note_filename
            neoscore.render_image(rect=None,
                                  dest=save_dest,
                                  autocrop=True,
                                  preserve_alpha=False,
                                  wait=True
                                  )
            print(f"Saving new image to {save_dest}")

            # delete them all
            for o in list_of_objects:
                # print(o)
                o.remove()

    def make_neonote(self,
                     octave,
                     add_accidental,
                     compass,
                     arrow_help,
                     name_help
                     ):

        # match compass to notes
        match compass:
            case 'S':
                note = 'C'
            case 'SE':
                note = 'E'
            case 'E':
                note = 'G'
            case 'NE':
                note = 'B'
            case 'N':
                note = 'C'
            case 'NW':
                note = 'A'
            case 'W':
                note = 'F'
            case 'SW':
                note = 'D'

        # print(note)
        # adjust note for enharmonic shift
        match add_accidental:
            case 1:
                note = f"{note}#"
            case -1:
                note = f"{note}b"

        # make fs style note str
        fs_note = f"{note}-{octave + 1}"

        # make into neoscore note value
        if note[-1] == "#":
            self.neopitch = f"{note[0].lower()}#"
        elif note[-1] == "b":
            self.neopitch = f"{note[0].lower()}b"
        else:
            self.neopitch = note[0].lower()

        # add higher octave indicators "'"
        if octave > 4:
            ticks = octave - 4
            for tick in range(ticks):
                self.neopitch += "'"

        # add lower octave indicators ","
        elif octave < 4:
            if octave == 3:
                self.neopitch += ","
            elif octave == 2:
                self.neopitch += ",,"
            elif octave == 1:
                self.neopitch += ",,,"
            elif octave == 0:
                self.neopitch += ",,,,"

        # make into neoscore png for display
        print(self.neopitch, compass, arrow_help, name_help)
        self.make_notation([self.neopitch],
                           compass,
                           arrow_help=arrow_help,
                           name_help=name_help
                           )

if __name__ == "__main__":
    test = Notation()
    compass_list = ["S", "SW", "SE", "W", "E", "NW", "NE", "N"]
    octave_range = [2, 3, 4, 5, 6]
    accidental_list = [0, 1, -1]
    helplist = [[True, True], [False, True], [False, False]]
    for octa in octave_range:
        for acc in accidental_list:
            for comp in compass_list:
                for help in helplist:
                    test.make_neonote(octa,
                                 acc,
                                 comp,
                                 help[0],
                                 help[1]
                                 )
