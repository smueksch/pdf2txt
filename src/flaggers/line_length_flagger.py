import math


# DEPRECATED
class LineLengthFlagger:
    """ Flag up lines that appear longer than usual

    A line is considered longer than usual if it is longer than the average
    line length + one standard deviation.
    """

    def __call__(self, text: str) -> None:
        lines = text.splitlines()
        num_lines = len(lines)

        # TODO: These calculations seem a little inaccurate...
        average_len = sum([len(line) for line in lines]) / num_lines            # Also known as expected value.
        average_sq_len = sum([len(line)**2 for line in lines]) / num_lines
        standard_deviation = math.sqrt(average_sq_len - average_len**2)

        for i in range(num_lines):
            if len(lines[i]) > average_len + standard_deviation:
                print('Line potentially too long, line {i}'.format(i=i+1))
