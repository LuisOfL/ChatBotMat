from reactpy import component, html
from src.services.time_service import get_current_timestamp

@component
def MessageBubble(message):
    side = "right" if message["sender"] == "me" else "left"
    klass = "msg sent" if message["sender"] == "me" else "msg received"
    
    return html.div({"class_name": f"row {side}"},
        html.div({"class_name": klass},
            html.div(message["text"]),
            html.div({"class_name": "meta"}, 
                html.span(message["ts"])
            )
        )
    )

@component
def TypingIndicator():
    return html.div({"class_name": "row left"},
        html.div({"class_name": "msg received"},
            html.div({"class_name": "typing-indicator"},
                html.div({"class_name": "typing-dot"}),
                html.div({"class_name": "typing-dot"}),
                html.div({"class_name": "typing-dot"})
            )
        )
    )