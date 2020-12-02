from rich import print
from fractions import Fraction


# TODO: Add more UI coloring and make it better overall.

print(
    '\nIMPORTANT: Slope Formula is as follows: \n [bold blue]y2-y1 / x2-x1[/]')


def ask_for(prompt, error_msg=None, _type=None):
    """ While the desired prompt is not given, it repeats the prompt. """
    while True:
        inp = input(prompt).strip()
        if not inp:
            if error_msg:
                print(error_msg)
            continue

        if _type:
            try:
                inp = _type(inp)
            except ValueError:
                if error_msg:
                    print(error_msg)
                continue

        return inp


def get_params():

    # * Grabbing coordinates
    print(
        '\nPoints on a graph or table are formatted this way: [bold]( X, Y ) ( 5, 9 )[/]')

    # ? In the future the type checker for these input functions might have to be changed to accommodate fractions
    x_coord1 = ask_for('\nFirst X coord: ', 'Not a number', float)
    y_coord1 = ask_for('\nFirst Y coord: ', 'Not a number', float)

    x_coord2 = ask_for('\nSecond X coord: ', 'Not a number', float)
    y_coord2 = ask_for('\nSecond Y coordinate: ', 'Not a number', float)

    coord_list = [x_coord1, y_coord1, x_coord2, y_coord2]

    return coord_list


class FindSlope():
    def __init__(self, param_list=list):
        self.xc1 = param_list[0]
        self.yc1 = param_list[1]
        self.xc2 = param_list[2]
        self.yc2 = param_list[3]

    def calculate_slope(self):
        ySlope = self.yc2 - self.yc1
        xSlope = self.xc2 - self.xc1

        slope = ySlope / xSlope
        fSlope = Fraction(ySlope) / Fraction(xSlope)
        # * Can't do the above ^ in one single line because it either didn't give a correct answer or broke the code.
        print('\n****************************************************')
        print(f'The slope is: {slope} \nIn fraction form: {fSlope}')
        print('****************************************************')

        return slope, fSlope

    def perp_slope(self):
        print(
            '\nEnter in the slope of the lines you are checking in fraction form. [bold]( at least 2 lines )[/]')
        try:
            print('\n******')
            line1 = ask_for(': ', 'Not a fraction', Fraction)
            line2 = ask_for(': ', 'Not a fraction', Fraction)
            print('******')
        except:
            print('\nThe value(s) entered were not fractions.')

        if line1 * line2 == -1:
            print(line1*line2)
            print('\n[bold blue]True[/]. The lines are perpendicular.')
        else:
            print('\nThe lines [bold]are not perpendicular.[/]')


if __name__ == "__main__":
    def main():
        num_lines = ask_for(
            '\nHow many lines do you need to calculate the slope for? ( Must be an integer ): ', 'Not an integer.', int)
        for _ in range(num_lines):
            FS = FindSlope(get_params())
            FS.calculate_slope()

        find_perp_slope = ask_for(
            '\nDo you need to find out if the lines are perpendicular? (y/n): ', 'Not an answer', str)
        if find_perp_slope[0] == 'y':
            FS.perp_slope()
        else:
            print('\nContinuing...')
    main()

    print('\nWould you like to repeat the script? (y/n)')
    repeat = ask_for('\n: ', 'Error', str).lower()

    if repeat == 'y':
        main()
    if repeat == 'n':
        print('\n********************'
              ' [bold blue]End of program[/] '
              '********************')
