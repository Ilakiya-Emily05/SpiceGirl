from datetime import datetime


class CalendarService:

    @staticmethod
    def classify_event(title: str):

        title = title.lower()

        if "interview" in title:
            return "Interview"

        if "wedding" in title:
            return "Wedding"

        if "party" in title:
            return "Party"

        if "college" in title:
            return "College"

        return "Casual"

    @staticmethod
    def upcoming_event(event):

        return {
            "title": event.title,
            "event_type": event.event_type,
            "event_date": event.event_date
        }