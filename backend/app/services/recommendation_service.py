from itertools import combinations


class RecommendationService:

    @staticmethod
    def generate_outfits(
        clothes,
        occasion,
        temperature
    ):

        recommendations = []

        tops = [
            c for c in clothes
            if c.category == "Top"
        ]

        bottoms = [
            c for c in clothes
            if c.category == "Bottom"
        ]

        for top in tops:
            for bottom in bottoms:

                score = 50
                reasons = []

                if occasion.lower() == "interview":

                    if (
                        top.style == "Professional"
                        and bottom.style == "Professional"
                    ):
                        score += 30
                        reasons.append(
                            "Interview Appropriate"
                        )

                if temperature > 32:

                    if top.season in [
                        "Summer",
                        "All"
                    ]:
                        score += 10
                        reasons.append(
                            "Weather Suitable"
                        )

                recommendations.append(
                    {
                        "top": top.name,
                        "bottom": bottom.name,
                        "score": score,
                        "reasons": reasons
                    }
                )

        recommendations.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return recommendations[:5]