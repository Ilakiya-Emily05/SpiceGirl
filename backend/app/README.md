backend/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── constants.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   └── base.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── clothing.py
│   │   ├── outfit.py
│   │   ├── event.py
│   │   └── preference.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── clothing.py
│   │   ├── outfit.py
│   │   ├── event.py
│   │   └── recommendation.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── clothes.py
│   │   ├── recommendations.py
│   │   ├── weather.py
│   │   ├── events.py
│   │   ├── outfits.py
│   │   └── profile.py
│   │
│   ├── services/
│   │   ├── recommendation_service.py
│   │   ├── weather_service.py
│   │   ├── calendar_service.py
│   │   └── preference_service.py
│   │
│   ├── utils/
│   │   ├── color_matcher.py
│   │   ├── scoring.py
│   │   └── helpers.py
│   │
│   └── tests/
│       ├── test_auth.py
│       ├── test_clothes.py
│       └── test_recommendations.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md