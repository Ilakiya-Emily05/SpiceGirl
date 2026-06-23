from app.utils.color_matcher import color_score


def calculate_score(
    top,
    bottom,
    occasion,
    temperature
):

    score = 0
    reasons = []

    # Occasion

    if occasion.lower() == "interview":

        if (
            top.style == "Professional"
            and bottom.style == "Professional"
        ):
            score += 40
            reasons.append(
                "Interview Appropriate"
            )

    # Color

    score += color_score(
        top.color,
        bottom.color
    ) * 2

    reasons.append(
        "Color Compatibility"
    )

    # Weather

    if temperature > 30:

        if top.season in [
            "Summer",
            "All"
        ]:
            score += 15
            reasons.append(
                "Weather Suitable"
            )

    return score, reasons