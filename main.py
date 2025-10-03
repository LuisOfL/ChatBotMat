import os
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

@app.get("/")
async def root():
    return {"message": "Chat App con Groq"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Esto es importante para Gunicorn
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
