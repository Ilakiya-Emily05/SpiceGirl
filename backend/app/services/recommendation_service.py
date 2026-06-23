from typing import List, Dict


class RecommendationService:

    @staticmethod
    def generate_outfits(clothes, occasion: str, temperature: float):

        recommendations: List[Dict] = []

        tops = [c for c in clothes if c.category == "Top"]
        bottoms = [c for c in clothes if c.category == "Bottom"]
        shoes = [c for c in clothes if c.category == "Footwear"]

        for top in tops:
            for bottom in bottoms:

                score = 40
                reasons = []

                # 🎯 OCCASION MATCHING
                if occasion.lower() == "interview":
                    if top.style == "Professional" and bottom.style == "Professional":
                        score += 30
                        reasons.append("Strong interview formality match")

                if occasion.lower() == "college":
                    if top.style in ["Casual", "Minimalist"]:
                        score += 15
                        reasons.append("Suitable for college environment")

                # 🌤 WEATHER LOGIC
                if temperature > 32:
                    if top.season in ["Summer", "All"]:
                        score += 10
                        reasons.append("Breathable for hot weather")
                    else:
                        score -= 10
                        reasons.append("May be too warm for current weather")

                # 🎨 COLOR COMPATIBILITY (basic but powerful)
                if top.color != bottom.color:
                    score += 5
                    reasons.append("Color contrast improves outfit balance")

                # 🔥 STYLE COHERENCE
                if top.style == bottom.style:
                    score += 10
                    reasons.append("Style consistency improves visual harmony")

                outfit = {
                    "top": top.name,
                    "bottom": bottom.name,
                    "score": score,
                    "reasons": reasons
                }

                # Optional: shoes if available
                if shoes:
                    best_shoe = shoes[0]
                    outfit["shoes"] = best_shoe.name

                recommendations.append(outfit)

        recommendations.sort(key=lambda x: x["score"], reverse=True)

        return recommendations[:5]