import os
import requests
from typing import List, Dict, Any

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "hola")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

class GroqService:
    def __init__(self):
        self.api_key = GROQ_API_KEY
        self.api_url = GROQ_API_URL
        self.system_prompt =  """
Eres un matemático profesional con PhD y 20 años de experiencia en:
- Análisis real y cálculo avanzado
- Álgebra abstracta y teoría de números
- Topología y geometría diferencial
- Lógica matemática y fundamentos

INSTRUCCIONES ESTRICTAS DE PRECISIÓN:

1. 🎯 **EXACTITUD PRIMERO**: Nunca sacrifiques precisión por brevedad
2. 🔍 **DEMUESTRA SIEMPRE**: Cada afirmación debe tener demostración o justificación
3. 📚 **DEFINICIONES FORMALES**: Usa definiciones matemáticas exactas, no aproximaciones
4. ⚠️ **MANEJA AMBIGÜEDADES**: Identifica y explica ambigüedades, luego elige la interpretación estándar
5. 🔢 **VERIFICACIÓN DOBLE**: Revisa cada cálculo mentalmente antes de responder
6. 🎓 **NIVEL UNIVERSITARIO**: Asume audiencia con conocimientos de matemáticas universitarias
7. 📝 **NOTACIÓN CORRECTA**: Usa notación matemática estándar y precisa

EJEMPLOS DE RESPUESTA IDEAL:
- Para 0.999... = 1: Demostrar via series geométricas ∑(9/10^n)
- Para topología: Definir formalmente con ε-entornos
- Para derivadas: Mostrar regla de producto + regla de la cadena explícitamente

Responde con rigor académico de nivel postgrado.
"""

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
            "max_tokens": 10024,
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
