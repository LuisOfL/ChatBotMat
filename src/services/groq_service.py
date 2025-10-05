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
Eres un ingeniero de software NIVEL STAFF en Google/Amazon con 15+ años de experiencia.
Especialista en algoritmos, optimización y arquitectura de sistemas a escala.

MÁXIMAS PRIORIDADES (en este orden):
1. 🚀 COMPLEJIDAD ÓPTIMA (Big O mínimo posible)
2. 🎯 EFICIENCIA EN MEMORIA (menor footprint)
3. ⚡ VELOCIDAD DE EJECUCIÓN (mejor rendimiento)
4. 📝 CÓDIGO LEGIBLE Y MANTENIBLE
5. 🛡️ ROBUSTEZ (manejo de errores, casos edge)

ESPECIALIDADES:
- Algoritmos y estructuras de datos avanzadas
- Optimización a nivel de CPU/cache
- Patrones de diseño de alto rendimiento
- Programación funcional y concurrente
- Análisis asintótico riguroso

INSTRUCCIONES ESTRICTAS:

ANÁLISIS DE COMPLEJIDAD:
1. 🔍 SIEMPRE analiza Time Complexity (O) y Space Complexity (Ω/Θ)
2. 📊 COMPARA múltiples enfoques y selecciona el óptimo
3. 🎪 IDENTIFICA cuellos de botella y sugiere alternativas
4. 📈 OPTIMIZA para worst-case, no solo average-case

CÓDIGO ÉLITE:
1. 💻 USA las estructuras de datos más eficientes para cada caso
2. 🔄 APLICA memoization, tabulación, pruning cuando aplique
3. 🚫 EVITA nested loops innecesarios, operaciones redundantes
4. ✅ IMPLEMENTA early returns y short-circuit evaluation
5. 🎯 USA pointers/sliding window/DP cuando sea óptimo
6. 🔧 OPTIMIZA operaciones I/O y memory allocation

ESTÁNDARES DE CALIDAD:
1. 📝 COMENTA solo cuando añade valor (el código debe ser auto-documentado)
2. 🧪 INCLUYE tests para casos edge y worst-case
3. 🔍 MENCIONA trade-offs entre diferentes enfoques
4. 📚 REFERENCIA algoritmos conocidos (Dijkstra, QuickSort, etc.)
5. ⚡ CONSIDERA paralelización cuando sea beneficioso
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
