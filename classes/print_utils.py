
# from print_utils import PrintUtils
# print_utils = PrintUtils()

class PrintUtils():

    def __init__(self):
        self.BOX_HORIZONTAL = u'\u2500'  # single line top/bottom bar
        self.BOX_VERTICAL = u'\u2502'  # single line vertical bar
        self.BOX_TOP_LEFT = u'\u250c'  # single line top left corner
        self.BOX_TOP_RIGHT = u'\u2510'  # single line top right corner
        self.BOX_BOTTOM_LEFT = u'\u2514'  # single line bottom left corner
        self.BOX_BOTTOM_RIGHT = u'\u2518'  # single line bottom right corner
        self.BOX_VERTICAL_LEFT = u'\u251c'  # single line vertical left
        self.BOX_VERTICAL_RIGHT = u'\u2524'  # single line vertical right
        self.BOX_TOP_COLUMN = u'\u252c'  # single line top column
        self.BOX_BOTTOM_COLUMN = u'\u2534'  # single line bottom column
        self.BOX_COLUMN_CROSS = u'\u253c'  # single line column cross
        return

    def print_message(self, row_data, column_widths):
        self.seperator_line(column_widths)
        print("{0} {1} {2} {3} {4} {5} {6} {7} {8} " \
              "{9} {10} {11} {12} {13} {14} {15} {16}".format(self.BOX_VERTICAL,
                                                              row_data[1].ljust(column_widths[1], " "),
                                                              self.BOX_VERTICAL,
                                                              row_data[2].rjust(column_widths[2], " "),
                                                              self.BOX_VERTICAL,
                                                              row_data[3].rjust(column_widths[3], " "),
                                                              self.BOX_VERTICAL,
                                                              row_data[4].rjust(column_widths[4], " "),
                                                              self.BOX_VERTICAL,
                                                              row_data[5].rjust(column_widths[5], " "),
                                                              self.BOX_VERTICAL,
                                                              row_data[6].rjust(column_widths[6], " "),
                                                              self.BOX_VERTICAL,
                                                              row_data[7].ljust(column_widths[7], " "),
                                                              self.BOX_VERTICAL,
                                                              row_data[8].ljust(column_widths[8], " "),
                                                              self.BOX_VERTICAL))
        self.bottom_line(column_widths)

    def print_headings(self, headings, column_widths):
        self.top_line(column_widths)
        print("{0} {1} {2} {3} {4} {5} {6} {7} {8} " \
              "{9} {10} {11} {12} {13} {14} {15} {16}".format(self.BOX_VERTICAL,
                                                              headings[1].ljust(column_widths[1], " "),
                                                              self.BOX_VERTICAL,
                                                              headings[2].ljust(column_widths[2], " "),
                                                              self.BOX_VERTICAL,
                                                              headings[3].ljust(column_widths[3], " "),
                                                              self.BOX_VERTICAL,
                                                              headings[4].ljust(column_widths[4], " "),
                                                              self.BOX_VERTICAL,
                                                              headings[5].ljust(column_widths[5], " "),
                                                              self.BOX_VERTICAL,
                                                              headings[6].ljust(column_widths[6], " "),
                                                              self.BOX_VERTICAL,
                                                              headings[7].ljust(column_widths[7], " "),
                                                              self.BOX_VERTICAL,
                                                              headings[8].ljust(column_widths[8], " "),
                                                              self.BOX_VERTICAL))
        self.bottom_line(column_widths)
        self.seperator_line(column_widths)

    def top_line(self, column_widths):
        print("{0}{1}{2}{3}{4}{5}{6}{7}{8}" \
              "{9}{10}{11}{12}{13}{14}{15}{16}".format(self.BOX_TOP_LEFT,
                                                       self.BOX_HORIZONTAL * (column_widths[1] + 2),
                                                       self.BOX_TOP_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[2] + 2),
                                                       self.BOX_TOP_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[3] + 2),
                                                       self.BOX_TOP_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[4] + 2),
                                                       self.BOX_TOP_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[5] + 2),
                                                       self.BOX_TOP_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[6] + 2),
                                                       self.BOX_TOP_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[7] + 2),
                                                       self.BOX_TOP_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[8] + 2),
                                                       self.BOX_TOP_RIGHT))

    def bottom_line(self, column_widths):
        print("{0}{1}{2}{3}{4}{5}{6}{7}{8}" \
              "{9}{10}{11}{12}{13}{14}{15}{16}".format(self.BOX_BOTTOM_LEFT,
                                                       self.BOX_HORIZONTAL * (column_widths[1] + 2),
                                                       self.BOX_BOTTOM_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[2] + 2),
                                                       self.BOX_BOTTOM_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[3] + 2),
                                                       self.BOX_BOTTOM_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[4] + 2),
                                                       self.BOX_BOTTOM_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[5] + 2),
                                                       self.BOX_BOTTOM_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[6] + 2),
                                                       self.BOX_BOTTOM_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[7] + 2),
                                                       self.BOX_BOTTOM_COLUMN,
                                                       self.BOX_HORIZONTAL * (column_widths[8] + 2),
                                                       self.BOX_BOTTOM_RIGHT))

    def seperator_line(self, column_widths):
        print("\033[F{0}{1}{2}{3}{4}{5}{6}{7}{8}" \
              "{9}{10}{11}{12}{13}{14}{15}{16}".format(self.BOX_VERTICAL_LEFT,
                                                       self.BOX_HORIZONTAL * (column_widths[1] + 2),
                                                       self.BOX_COLUMN_CROSS,
                                                       self.BOX_HORIZONTAL * (column_widths[2] + 2),
                                                       self.BOX_COLUMN_CROSS,
                                                       self.BOX_HORIZONTAL * (column_widths[3] + 2),
                                                       self.BOX_COLUMN_CROSS,
                                                       self.BOX_HORIZONTAL * (column_widths[4] + 2),
                                                       self.BOX_COLUMN_CROSS,
                                                       self.BOX_HORIZONTAL * (column_widths[5] + 2),
                                                       self.BOX_COLUMN_CROSS,
                                                       self.BOX_HORIZONTAL * (column_widths[6] + 2),
                                                       self.BOX_COLUMN_CROSS,
                                                       self.BOX_HORIZONTAL * (column_widths[7] + 2),
                                                       self.BOX_COLUMN_CROSS,
                                                       self.BOX_HORIZONTAL * (column_widths[8] + 2),
                                                       self.BOX_VERTICAL_RIGHT))
