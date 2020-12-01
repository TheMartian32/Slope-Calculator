from rich import print
from fractions import Fraction

print('\nIMPORTANT: Slope Formula is as follows: \n [bold blue]y2-y1 / x2-x1[/]')

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
        print('\n****************************************************')
        print(f'The slope is: {slope} \nIn fraction form: {fSlope}')
        print('****************************************************')
        return slope, fSlope

if __name__ == "__main__":
    def get_params():

        # * Grabbing coordinates
        print('\nPoints on a graph or table are formatted this way: [bold]( X, Y ) ( 5, 9 )[/]')

        # ? In the future the type checker for these input functions might have to be changed to accommodate fractions
        x_coord1 = ask_for('\nFirst X coord: ','Not a number', float)
        y_coord1 = ask_for('\nFirst Y coord: ','Not a number', float)

        x_coord2 = ask_for('\nSecond X coord: ','Not a number', float)
        y_coord2 = ask_for('\nSecond Y coordinate: ','Not a number', float)

        coord_list = [x_coord1, y_coord1, x_coord2, y_coord2]

        return coord_list
    
    FS = FindSlope(get_params())

    def main():
        FS.calculate_slope()
    
    main()