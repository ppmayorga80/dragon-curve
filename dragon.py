"""
Dragon curve.

Usage:
  dragon [--line-length=LENGTH] [--line-width=WIDTH] [--line-color=COLOR] [--iterations=N] [--output=OUTPUT]
  dragon --rounded [--line-width=WIDTH] [--line-color=COLOR] [--iterations=N] [--output=OUTPUT]
  dragon --rounded --gradient [--line-width=WIDTH] [--iterations=N] [--output=OUTPUT]
  dragon --version

Options:
  --rounded                         Use the rounded version algorithm (more elegant and precise)
  --gradient                        Use gradient colors instead of fixed color
  -w WIDTH,--line-width=WIDTH       Pen Line Width [default: 1.0]
  -c COLOR,--line-color=COLOR       Pen Line Color RGBA (float) [default: 1,0,1,1]
  -l LENGTH,--line-length=LENGTH    Step length [default: 4]
  -n N,--iterations=N               Set the number of iterations [default: 4]
  -o OUTPUT,--output=OUTPUT         Output file in svg format [default: dragon.svg]
  -v,--version                      shows version
"""
from docopt import docopt

from dragon_curve import dragon_curve
from dragon_curve2 import dragon_curve2, dragon_curve2_gradient


def main():
    args = docopt(__doc__, version='Dragon Curve 2.0.0 Rounded')
    rounded = args["--rounded"]
    gradient = args["--gradient"]
    line_length = float(args["--line-length"])
    line_color = tuple(float(x) for x in args["--line-color"].split(","))
    line_width = float(args["--line-width"])
    iterations = int(args["--iterations"])

    output = args["--output"]

    if rounded:
        if gradient:
            dragon_curve2_gradient(
                output=output,
                iterations=iterations,
                line_width=line_width
            )
        else:
            dragon_curve2(
                output=output,
                iterations=iterations,
                line_color=line_color,
                line_width=line_width
            )
    else:
        dragon_curve(output=output,
                     iterations=iterations,
                     line_length=line_length,
                     line_color=line_color,
                     line_width=line_width)


if __name__ == '__main__':
    main()
