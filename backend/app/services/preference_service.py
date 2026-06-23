class PreferenceService:

    @staticmethod
    def calculate_preferences(clothes):

        color_count = {}
        style_count = {}

        for item in clothes:

            color_count[item.color] = (
                color_count.get(item.color, 0) + 1
            )

            style_count[item.style] = (
                style_count.get(item.style, 0) + 1
            )

        favorite_color = None
        favorite_style = None

        if color_count:
            favorite_color = max(
                color_count,
                key=color_count.get
            )

        if style_count:
            favorite_style = max(
                style_count,
                key=style_count.get
            )

        return {
            "favorite_color": favorite_color,
            "favorite_style": favorite_style
        }