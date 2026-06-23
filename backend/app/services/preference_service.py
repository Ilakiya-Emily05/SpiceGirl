from collections import defaultdict
from typing import Dict, List


class PreferenceService:

    @staticmethod
    def calculate_preferences(clothes: List):

        color_score = defaultdict(float)
        style_score = defaultdict(float)

        for item in clothes:

            # 🔥 usage weight matters now
            weight = getattr(item, "usage_count", 1) + 1

            color_score[item.color] += weight
            style_score[item.style] += weight

        favorite_color = max(color_score, key=color_score.get) if color_score else None
        favorite_style = max(style_score, key=style_score.get) if style_score else None

        return {
            "favorite_color": favorite_color,
            "favorite_style": favorite_style,

            # 🔥 AI SIGNALS (IMPORTANT FOR RECOMMENDER)
            "color_distribution": dict(color_score),
            "style_distribution": dict(style_score)
        }