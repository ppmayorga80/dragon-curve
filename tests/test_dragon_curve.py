import os.path

from src.dragon_curve import min_rectangle, rotate_points, points_to_svg, dragon_sequence, dragon_points, \
    dragon_curve


def test_min_rectangle():
    points = [(1, 1), (3, 3), (2, 4)]
    expected_points = [(0, 0), (2, 2), (1, 3)]
    expected_width = 2
    expected_height = 3
    pts, w, h = min_rectangle(points)
    assert pts == expected_points
    assert w == expected_width
    assert h == expected_height


def test_rotate_points():
    points = [(1, 1), (3, 3), (2, 4)]
    expected_points = [(-1, 1), (-3, 3), (-4, 2)]
    pts = rotate_points(points, origin=(0, 0))
    assert pts == expected_points


def test_points_to_svg(tmp_path):
    points = [(1, 1), (3, 3), (2, 4)]
    svg_file = str(tmp_path) + ".svg"

    assert not os.path.exists(svg_file)
    points_to_svg(output=svg_file,
                  points=points,
                  width=5,
                  height=5,
                  line_width=1,
                  line_color=(1, 0, 0))
    assert os.path.exists(svg_file)


def test_dragon_sequence():
    assert dragon_sequence(0) == ""
    assert dragon_sequence(1) == "R"
    assert dragon_sequence(2) == "RRL"
    assert dragon_sequence(3) == "RRLRRLL"


def test_dragon_points():
    assert dragon_points(n=0, line_length=1) == [(0, 0), (0, 1)]
    assert dragon_points(n=1, line_length=1) == [(0, 0), (0, 1), (-1, 1)]
    assert dragon_points(n=2, line_length=1) == [(0, 0), (0, 1), (-1, 1),
                                                 (-1, 0), (-2, 0)]
    assert dragon_points(n=3, line_length=1) == [(0, 0), (0, 1), (-1, 1),
                                                 (-1, 0), (-2, 0), (-2, -1),
                                                 (-1, -1), (-1, -2), (-2, -2)]


def test_dragon_curve(tmp_path):
    svg_file = str(tmp_path) + ".svg"
    dragon_curve(svg_file,
                 iterations=4,
                 line_length=10.0,
                 line_color=(1, 0, 1, 1),
                 line_width=1.0)
    assert os.path.exists(svg_file)
