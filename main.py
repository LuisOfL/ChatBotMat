from fastapi import FastAPI
from reactpy.backend.fastapi import configure, Options
from reactpy import html  

from src.styles.css import CSS
from src.components.chat_app import ChatApp

app = FastAPI(title="Chat con Groq")

configure(
    app,
    ChatApp,
    options=Options(
        head=html.head( 
            html.meta({"charset": "utf-8"}),
            html.meta({"name": "viewport", "content": "width=device-width, initial-scale=1"}),
            html.style(CSS),
        )
    ),
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)