import os
import requests
from typing import List, Dict, Any

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")  #La llave, si no deja subirla github, pon cualquier cosa y sube
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

class GroqService:
    def __init__(self):
        self.api_key = GROQ_API_KEY
        self.api_url = GROQ_API_URL

    def call_api(self, messages_history: List[Dict[str, Any]]) -> str:
        """Llama a la API de Groq para obtener una respuesta"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        formatted_messages = []
        for msg in messages_history:
            role = "user" if msg["sender"] == "me" else "assistant"
            formatted_messages.append({
                "role": role,
                "content": msg["text"]
            })
        
        payload = {
            "messages": formatted_messages,
            "model": "llama-3.1-8b-instant",
            "temperature": 0.7,
            "max_tokens": 1024,
            "top_p": 1,
            "stream": False
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
        
        except requests.exceptions.RequestException as e:
            return f"Error al conectar con Groq: {str(e)}"
        except (KeyError, IndexError) as e:
            return "Error procesando la respuesta de Groq"
        except Exception as e:
            return f"Error inesperado: {str(e)}"


groq_service = GroqService()
