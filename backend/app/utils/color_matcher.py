COLOR_COMPATIBILITY = {
    ("Black", "White"): 10,
    ("White", "Black"): 10,

    ("Blue", "White"): 9,
    ("White", "Blue"): 9,

    ("Grey", "Black"): 8,
    ("Black", "Grey"): 8,

    ("Beige", "Brown"): 8,
    ("Brown", "Beige"): 8,

    ("Red", "Green"): 2,
    ("Green", "Red"): 2,
}


def color_score(color1: str, color2: str):

    if color1 == color2:
        return 8

    return COLOR_COMPATIBILITY.get(
        (color1, color2),
        5
    )