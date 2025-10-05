import os
import requests
from typing import List, Dict, Any

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "hola")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

class GroqService:
    def __init__(self):
        self.api_key = GROQ_API_KEY
        self.api_url = GROQ_API_URL
        self.system_prompt = """Eres un experto en matemáticas con amplio conocimiento en:
- Álgebra y cálculo
- Geometría y trigonometría
- Estadística y probabilidad
- Matemáticas avanzadas
- Resolución de problemas matemáticos

Instrucciones:
1. Explica conceptos matemáticos de manera clara y paso a paso
2. Proporciona ejemplos prácticos cuando sea posible
3. Verifica cálculos y soluciones
4. Usa notación matemática adecuada
5. Sé preciso y riguroso en tus explicaciones
6. Adapta tu explicación al nivel del usuario
7. Si el usuario tiene dudas, acláralas con paciencia

Siempre responde en el mismo idioma que el usuario."""

    def call_api(self, messages_history: List[Dict[str, Any]]) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # INCLUIR EL SYSTEM PROMPT + historial de mensajes
        formatted_messages = [
            {"role": "system", "content": self.system_prompt}  # ← ESTA LÍNEA ES CLAVE
        ]
        
        for msg in messages_history:
            role = "user" if msg["sender"] == "me" else "assistant"
            formatted_messages.append({
                "role": role,
                "content": msg["text"]
            })
        
        payload = {
            "messages": formatted_messages,  # Ahora incluye el system prompt
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
