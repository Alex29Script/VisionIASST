import re
from datetime import datetime as dt
from openai import OpenAI

class ModelLLM():
    
    def __init__(self, model_name,api_key, *args, **kwargs):
        self.model_name=model_name
        self.api_key=api_key


    def generate_inference_with_llm(self,consulta:str):
        try:
            client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
            print(f"Entrando a consulta...{dt.now().strftime('%d/%m/%Y %H:%M')}")
            completion = client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "As an expert in Occupational Safety and Health (OSH)"},
                {"role": "user", "content": consulta}
            ],
            temperature=0.7,
            )
            
            tex=completion.choices[0].message.content
            match = re.search(r"<think>(.*?)</think>", tex, re.DOTALL)
            if match:
                thinking = match.group(1).strip()
                
            else:
                thinking="No se encontró la etiqueta <think>"
            respuesta = re.sub(r"<think>.*?</think>", "", tex, flags=re.DOTALL)
            return thinking, respuesta
        except Exception as e:
            error=f"Sin respuesta por el modelo dado al siguiente error: {e}"
            return error , error
        finally:
    
            client.close()
            print(f"consulta completada...{dt.now().strftime('%d/%m/%Y %H:%M')}")

        
    def get_llm_response(self,consulta:str):
    
        hora_consulta=dt.now().strftime("%d/%m/%Y %H:%M")+"\n\n"
        text_input_hr=hora_consulta+consulta
        thinking,respuesta=self.generate_inference_with_llm(consulta)
        hora_respuesta=dt.now().strftime("%d/%m/%Y %H:%M")+"\n\n"
        thinking_hr=hora_respuesta+thinking
        respuesta_hr=hora_respuesta+respuesta
        #thinking="Hola mundo thinking"
        #respuesta="Hola Mundo Respuesta"
        return text_input_hr,thinking_hr, respuesta_hr
    