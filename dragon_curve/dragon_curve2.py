"""Rounded Dragon Curve"""
import colorsys

from typing import List, Tuple, Sequence
import cairo
from tqdm import tqdm


class RotationMatrix:

    def __init__(self, a00, a01, a10, a11):
        self.a00 = a00
        self.a01 = a01
        self.a10 = a10
        self.a11 = a11

    @classmethod
    def rot_90(cls):
        return RotationMatrix(0, 1, -1, 0)


class Point:

    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def rotate_90(self, c: "Point") -> "Point":
        # rotation matrix
        p = self
        r = RotationMatrix.rot_90()
        q = (p - c) * r + c
        return q

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, m: RotationMatrix) -> "Point":
        return Point(m.a00 * self.x + m.a01 * self.y,
                     m.a10 * self.x + m.a11 * self.y)


def bounded_rectangle(points: List[Point]) -> Tuple[Point, Point]:
    x_min = min(p.x for p in points)
    x_max = max(p.x for p in points)
    y_min = min(p.y for p in points)
    y_max = max(p.y for p in points)
    return Point(x_min, y_min), Point(x_max, y_max)


def sign(x: int) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def rotation_operation(points: List[Point], k: int = 0) -> List[Point]:
    c = points[-1]
    rotated_points = [p.rotate_90(c) for p in points]
    rotated_points = rotated_points[::-1]

    a, b = points[-1], points[-2]
    r, s = rotated_points[0], rotated_points[1]

    if a.x == b.x:
        p = Point(a.x, a.y - k * sign(a.y - b.y))
    else:  # a.y==b.y
        p = Point(a.x - k * sign(a.x - b.x), a.y)

    if r.x == s.x:
        q = Point(r.x, r.y + k * sign(s.y - r.y))
    else:  # r.y==s.y
        q = Point(r.x + k * sign(s.x - r.x), r.y)

    new_points = points[:-1] + [p] + [q] + rotated_points[1:]
    return new_points


def points_to_svg(output_filename: str, points: List[Point], width: int,
                  height: int, line_width: float, line_color: Sequence[float]):
    with cairo.SVGSurface(output_filename, width, height) as surf:
        # set initial parameters
        context = cairo.Context(surf)
        context.set_line_cap(cairo.LINE_CAP_ROUND)
        context.set_line_join(cairo.LINE_JOIN_ROUND)
        context.set_line_width(line_width)
        context.set_source_rgba(line_color[0], line_color[1], line_color[2],
                                1.0)

        # 2. draw points
        p = points[0]
        context.move_to(p.x, p.y)
        for pk in tqdm(points[1:],
                       total=len(points) - 1,
                       desc="Drawing dragon svg"):
            # context.set_source_rgba(1, 0, 0, 1.0)
            context.line_to(pk.x, pk.y)

        context.stroke()


def points_to_svg_gradient(output_filename: str, points: List[Point],
                           colors: List[Tuple[float, float, float]],
                           width: int, height: int, line_width: float):
    with cairo.SVGSurface(output_filename, width, height) as surf:
        # set initial parameters
        context = cairo.Context(surf)

        # 2. draw points
        p = points[0]
        print(p)
        context.move_to(p.x, p.y)
        for pk, ck in tqdm(zip(points[1:], colors),
                           total=len(points) - 1,
                           desc="Drawing dragon svg"):
            # context.set_source_rgba(1, 0, 0, 1.0)
            context.set_line_width(line_width)
            context.set_source_rgba(ck[0], ck[1], ck[2], 1.0)
            context.set_line_cap(cairo.LINE_CAP_ROUND)
            context.set_line_join(cairo.LINE_JOIN_ROUND)
            context.line_to(pk.x, pk.y)
            context.stroke()
            context.move_to(pk.x, pk.y)


def dragon_curve2(output: str, iterations: int, line_color: Tuple,
                  line_width: float):
    points = [Point(0, 0), Point(0, -4)]

    for _ in range(iterations):
        points = rotation_operation(points, k=1)

    a, b = bounded_rectangle(points)
    v = b - a
    w, h = v.x + int(2 * line_width), v.y + int(2 * line_width)
    points = [p - a for p in points]
    points_to_svg(output,
                  points,
                  w,
                  h,
                  line_width=line_width,
                  line_color=line_color)


def dragon_curve2_gradient(output: str, iterations: int, line_width: float):
    points = [Point(0, 0), Point(0, -4)]

    for _ in range(iterations):
        points = rotation_operation(points, k=1)

    n_points = len(points)
    colors = [
        colorsys.hsv_to_rgb(h / n_points, 1.0, 1.0)
        for h in range(n_points - 1)
    ]
    a, b = bounded_rectangle(points)
    v = b - a
    w, h = v.x + int(2 * line_width), v.y + int(2 * line_width)
    points = [p - a for p in points]
    points_to_svg_gradient(output, points, colors, w, h, line_width=line_width)


if __name__ == '__main__':
    gradient = True
    iterations = 6
    if gradient:
        dragon_curve2_gradient("dragon.svg",
                               iterations=iterations,
                               line_width=1.0)
    else:
        dragon_curve2("dragon.svg",
                      iterations=iterations,
                      line_width=1.0,
                      line_color=(1, 0, 0))
