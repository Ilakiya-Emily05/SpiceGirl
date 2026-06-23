Spice Girl Backend API

An AI-powered outfit recommendation system built using FastAPI and PostgreSQL. The system generates context-aware clothing recommendations based on weather, occasion, and user preferences using a rule-based scoring engine.

Features
JWT-based authentication (register and login)
Clothing wardrobe management (CRUD operations)
Event-based context system for outfit planning
Weather-aware recommendation integration
Rule-based AI recommendation engine with scoring logic
Preference learning system based on user clothing usage
Outfit generation and saving system
Explainable recommendations using reasoning output
Modular service-based backend architecture
AI Recommendation Logic

The system uses a deterministic scoring approach to rank outfits:

Final Score =

Occasion matching
Weather suitability
Style consistency
Color compatibility
User preference weight

Each recommendation includes a reasoning breakdown to ensure explainability.

Tech Stack
FastAPI
PostgreSQL
SQLAlchemy ORM
Pydantic
Python-JOSE for JWT authentication
Passlib for password hashing
OpenWeatherMap API
Project Structure
backend/
│
├── app/
│   ├── main.py
│
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   └── utils/
│
├── requirements.txt
├── .env
└── README.md


Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/spice-girl.git
cd spice-girl/backend
2. Create virtual environment
python -m venv venv
source venv/bin/activate

On Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file:

DATABASE_URL=postgresql://user:password@localhost:5432/spicegirl

JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

WEATHER_API_KEY=your_openweather_api_key
5. Run the application
uvicorn app.main:app --reload
API Endpoints
Authentication
POST /auth/register – Register a new user
POST /auth/login – Authenticate user and return JWT
Clothes
GET /clothes/ – Retrieve all clothing items
POST /clothes/ – Add a new clothing item
GET /clothes/{id} – Get clothing item by ID
DELETE /clothes/{id} – Delete clothing item
Events
GET /events/ – Get user events
POST /events/ – Create event
POST /events/sync – Calendar sync placeholder
Outfits
GET /outfits/ – Retrieve saved outfits
POST /outfits/save – Save generated outfit
Recommendations
POST /recommendations/ – Generate outfit recommendations
Weather
GET /weather/?city=CityName – Fetch weather data
Profile
GET /profile/{user_id} – Get user profile and preferences
Example Request

POST /recommendations/

{
  "user_id": "uuid",
  "occasion": "Interview",
  "temperature": 34,
  "weather_condition": "Sunny"
}
Example Response
{
  "recommendations": [
    {
      "outfit": ["White Shirt", "Grey Trousers"],
      "score": 92,
      "reason": "Formal, weather appropriate, and matches user preference"
    }
  ]
}
System Design Overview
Modular architecture with separation of routes, services, models, and schemas
Stateless authentication using JWT
Rule-based AI recommendation engine
Explainable outputs for each recommendation
Designed for extensibility and future machine learning integration
Future Improvements
Machine learning-based recommendation engine
Image-based clothing recognition
Trend-aware fashion adaptation
Mobile frontend integration
Real-time user feedback learning system
Author

Backend system developed as part of an AI-based outfit recommendation project.
