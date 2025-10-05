from reactpy import component, html, hooks
import asyncio
from src.services.groq_service import groq_service
from src.services.time_service import get_current_timestamp
from src.components.message_bubble import MessageBubble, TypingIndicator
from src.components.composer import Composer

@component
def ChatApp():
    messages, set_messages = hooks.use_state([
        {
            "id": 1, 
            "sender": "other", 
            "text": "¡Hola! Soy un ChatBot experto en matematicas. ¿En qué puedo ayudarte?", 
            "ts": get_current_timestamp()
        },
    ])
    text, set_text = hooks.use_state("")
    is_loading, set_loading = hooks.use_state(False)

    async def get_groq_response():
       
        set_loading(True)
        

        await asyncio.sleep(0.5)
        
        def _process_response(prev_messages):
    
            groq_response = groq_service.call_api(prev_messages)
            
      
            new_message = {
                "id": (prev_messages[-1]["id"] + 1) if prev_messages else 1,
                "sender": "other",
                "text": groq_response,
                "ts": get_current_timestamp(),
            }
            return prev_messages + [new_message]
        
        set_messages(_process_response)
        set_loading(False)

    def send():
        t = text.strip()
        if not t:
            return
        
        def _append_user_message(prev):
            new_message = {
                "id": (prev[-1]["id"] + 1) if prev else 1,
                "sender": "me",
                "text": t,
                "ts": get_current_timestamp(),
            }
            return prev + [new_message]
        
        set_messages(_append_user_message)
        set_text("")
        

        asyncio.create_task(get_groq_response())

    return html.div({"class_name": "page"},
        html.div({"class_name": "card"},
            html.div({"class_name": "header"},
                html.div({"class_name": "avatar"}),
                html.div({"class_name": "title"},
                    html.span({"class_name": "name"}, "ChatBot Mat"),
                    html.span({"class_name": "status"}, 
                         "Escribiendo..." if is_loading else "Conectado"
                    ),
                ),
            ),
            html.div({"class_name": "chat"},
                html.div({"class_name": "scroll"},
                    [MessageBubble(m) for m in messages],
                    TypingIndicator() if is_loading else None,
                    html.div({"id": "end"}),
                    html.script("""
                        var end = document.getElementById('end');
                        if (end && end.scrollIntoView) end.scrollIntoView({behavior: 'smooth', block: 'end'});
                    """)
                ),
                Composer(text, set_text, send, is_loading)
            )
        )
    )
