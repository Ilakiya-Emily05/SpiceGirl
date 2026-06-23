# Spice Girl API Documentation

Base URL

/api/v1

---

# Health Check

## GET /health

Response

{
"status": "running"
}

---

# Authentication

## POST /auth/register

Request

{
"name": "Emily",
"email": "[emily@example.com](mailto:emily@example.com)",
"password": "password123"
}

Response

{
"message": "User registered successfully"
}

---

## POST /auth/login

Request

{
"email": "[emily@example.com](mailto:emily@example.com)",
"password": "password123"
}

Response

{
"access_token": "jwt_token"
}

---

# Wardrobe Management

## GET /clothes

Description:
Retrieve all clothing items belonging to the user.

Response

[
{
"id": 1,
"name": "Black Blazer",
"category": "Outerwear",
"color": "Black",
"season": "All"
}
]

---

## POST /clothes

Description:
Add a new clothing item.

Request

{
"name": "White Shirt",
"category": "Top",
"color": "White",
"season": "Summer",
"style": "Professional"
}

Response

{
"message": "Clothing item added"
}

---

## GET /clothes/{id}

Description:
Retrieve a specific clothing item.

---

## PUT /clothes/{id}

Description:
Update clothing details.

---

## DELETE /clothes/{id}

Description:
Delete a clothing item.

---

# Recommendation Engine

## POST /recommendations

Description:
Generate outfit recommendations.

Request

{
"occasion": "Interview",
"temperature": 35,
"weather_condition": "Sunny"
}

Response

{
"recommendations": [
{
"top": "White Shirt",
"bottom": "Grey Trouser",
"shoes": "Black Formal Shoes",
"score": 92
}
]
}

---

# Weather Module

## GET /weather

Response

{
"temperature": 34,
"condition": "Sunny",
"humidity": 65
}

---

# Calendar Integration

## GET /events

Response

[
{
"id": 1,
"title": "Technical Interview",
"event_type": "Interview",
"date": "2026-06-28"
}
]

---

# Outfit Planner

## POST /outfits/save

Request

{
"top": "White Shirt",
"bottom": "Grey Trouser",
"shoes": "Black Formal Shoes"
}

Response

{
"message": "Outfit saved successfully"
}

---

## GET /outfits

Response

[
{
"id": 1,
"score": 92,
"created_at": "2026-06-22"
}
]

---

# User Profile

## GET /profile

Response

{
"favorite_colors": [
"Black",
"Navy"
],
"favorite_style": "Professional"
}

---

# Recommendation Scoring Logic

Final Score =

Occasion Match (40%)
+
Color Compatibility (20%)
+
Weather Suitability (15%)
+
User Preference Match (15%)
+
Outfit Diversity (10%)

Highest-scoring outfit combinations are returned to the user.
