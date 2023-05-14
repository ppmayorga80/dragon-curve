"""Dragon curve"""
from typing import Tuple

import cairo
from tqdm import tqdm


def min_rectangle(points: list[tuple[float, float]]) -> tuple[list[tuple[float, float]], float, float]:
    """computes the minimum rectangle that enclose all points
    then, translate all points to this rectangle

    :param points: input points
    :return: the new points, width and height
    """
    min_x = min([x for x, _ in tqdm(points, total=len(points), desc="min(x)")])
    max_x = max([x for x, _ in tqdm(points, total=len(points), desc="max(x)")])
    min_y = min([y for _, y in tqdm(points, total=len(points), desc="min(y)")])
    max_y = max([y for _, y in tqdm(points, total=len(points), desc="max(y)")])
    width = max_x - min_x
    height = max_y - min_y
    points = [(x - min_x, y - min_y) for x, y in tqdm(points, total=len(points), desc="Updating points")]
    return points, width, height


def rotate_points(points: list[tuple[int, int]], origin: tuple[int, int]) -> list[tuple[int, int]]:
    """rotate all points 90°

    :param points: the list of points to be rotated
    :type points: list[tuple[int, int]]
    :param origin: offset vector
    :return: the rotated points
    :rtype: list[tuple[int, int]]
    """
    cos_pi_2 = 0
    sin_pi_2 = 1
    r = [
        [cos_pi_2, -sin_pi_2],
        [sin_pi_2, cos_pi_2]
    ]
    h, k = origin
    rotated_points = [
        (
            r[0][0] * (x - h) + r[0][1] * (y - k) + h,
            r[1][0] * (x - h) + r[1][1] * (y - k) + k
        )
        for x, y in points
    ]
    return rotated_points


def points_to_svg(output: str,
                  points: list[tuple[float, float]],
                  width: float,
                  height: float,
                  line_width: float,
                  line_color: Tuple):
    """save points to a svg file

    :param output: the output file
    :param points: the list of points
    :param width: image width
    :param height: image height
    :param line_width: line width
    :param line_color: rgba color
    """

    with cairo.SVGSurface(output, width, height) as surface:
        # set initial parameters
        context = cairo.Context(surface)
        context.set_line_width(line_width)
        context.set_source_rgba(line_color[0], line_color[1], line_color[2],
                                line_color[3] if len(line_color) == 4 else 1.0)

        # 2. draw points
        xo, yo = points[0]
        context.move_to(xo, yo)
        for xk, yk in tqdm(points[1:], total=len(points) - 1, desc="Drawing dragon svg"):
            context.line_to(xk, yk)

        # stroke out the color and width property
        context.stroke()


def dragon_sequence(n: int) -> str:
    """Computes the dragon sequence
    Each iteration can be found by copying the previous iteration,
    then an R, then a second copy of the previous iteration
    in reverse order with the L and R letters swapped.


    :param n: number of iterations
    :return: the sequence
    """
    s = ""
    for _ in tqdm(range(n), total=n, desc="Compute dragon sequence"):
        # 1. copy previous sequence in reverse order
        r = s[::-1]
        # 2. taking the reverse sequence and replace L <-> R
        r = r.replace("L", "X")
        r = r.replace("R", "L")
        r = r.replace("X", "R")
        # 3. new sequence is:
        #   previous string + R + previous sequence in reverse order with L,R swapped
        s = f"{s}R{r}"

    return s


def dragon_points(n: int, line_length: float) -> list:
    # compute the sequence in string version -> angle version -> rotation matrix version
    cos_pi_2 = 0
    sin_pi_2 = 1
    rotation_fn = {
        "R": [
            [cos_pi_2, -sin_pi_2],
            [sin_pi_2, cos_pi_2],
        ],
        "L": [
            [cos_pi_2, sin_pi_2],
            [-sin_pi_2, cos_pi_2],
        ]
    }
    sequence_str = dragon_sequence(n=n)
    rotations = [
        rotation_fn[s]
        for s in tqdm(sequence_str, total=len(sequence_str), desc="Compute dragon rotations")
    ]
    # set initial values
    x, y = 0, 0
    a, b = 0, line_length

    points = [(x, y), (x + a, y + b)]
    x, y = x + a, y + b  # update position
    for m in tqdm(rotations, total=len(rotations), desc="Computing dragon points"):
        # 2.1 rotate
        a, b = m[0][0] * a + m[0][1] * b, m[1][0] * a + m[1][1] * b
        # 2.2 compute new points and append to the output
        nx, ny = x + a, y + b
        points.append((nx, ny))
        # 2.3 update points
        x, y = nx, ny

    return points


def dragon_curve(output: str, iterations: int, line_length: float, line_color: Tuple, line_width: float):
    """Main function"""

    points = dragon_points(n=iterations, line_length=line_length)
    points, width, height = min_rectangle(points)
    points_to_svg(output, points, width + 2 * line_width, height + 2 * line_width, line_width, line_color)
