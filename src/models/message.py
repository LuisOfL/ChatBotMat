from dataclasses import dataclass
from typing import Literal
from datetime import datetime

@dataclass
class Message:
    id: int
    sender: Literal["me", "other"]
    text: str
    timestamp: str

    @classmethod
    def create(cls, message_id: int, sender: str, text: str):
        return cls(
            id=message_id,
            sender=sender,
            text=text,
            timestamp=cls._get_current_time()
        )

    @staticmethod
    def _get_current_time() -> str:
        return datetime.now().strftime("%I:%M %p").lstrip("0")