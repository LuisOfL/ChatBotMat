from datetime import datetime

def get_current_timestamp() -> str:
    return datetime.now().strftime("%I:%M %p").lstrip("0")