from datetime import datetime
from typing import Dict, Optional


class CalendarService:

    @staticmethod
    def classify_event(title: str) -> str:
        title = title.lower()

        keywords = {
            "interview": "Interview",
            "wedding": "Wedding",
            "party": "Party",
            "college": "College",
            "conference": "Conference",
            "date": "Date"
        }

        for key, value in keywords.items():
            if key in title:
                return value

        return "Casual"

    @staticmethod
    def upcoming_event(event) -> Dict:
        return {
            "title": event.title,
            "event_type": event.event_type,
            "event_date": event.event_date,

            # 🔥 AI CONTEXT BOOST
            "context_priority": CalendarService._priority(event.event_type)
        }

    @staticmethod
    def _priority(event_type: str) -> int:
        priority_map = {
            "Interview": 5,
            "Wedding": 5,
            "Conference": 4,
            "Party": 3,
            "Date": 3,
            "College": 2,
            "Casual": 1
        }
        return priority_map.get(event_type, 1)