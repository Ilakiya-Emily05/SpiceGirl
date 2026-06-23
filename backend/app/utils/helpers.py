from datetime import datetime


def success_response(
    message: str,
    data=None
):

    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(
    message: str
):

    return {
        "success": False,
        "message": message
    }


def current_timestamp():

    return datetime.utcnow()