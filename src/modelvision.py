import torch
from transformers import AutoModelForCausalLM, AutoProcessor
import pandas as pd
from PIL import Image
from src.questions import Questions

class ModelVision():
    
    def __init__(self,model_name:str,ruth_imagen:str, df_questions:pd.DataFrame,*args, **kwargs):
        self.model_name=model_name
        self.ruth_imagen=ruth_imagen
        self.df_questions=df_questions
        
    
    def get_model(self):
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            trust_remote_code=True,
            device_map="auto",
            torch_dtype=torch.bfloat16,
            attn_implementation="flash_attention_2",
        )
        
    
    def get_processor(self):
        self.processor = AutoProcessor.from_pretrained(self.model_name, trust_remote_code=True)

    def get_image(self):
        image = Image.open(self.ruth_imagen)
        return image


    def vision_model_image_description(self):
        image=self.get_image()
        self.get_model()
        self.get_processor()
        for i,query in self.df_questions.iterrows():
            
            Questions=query["query"]
            
            conversation = [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "image": image},
                        {"type": "text", "text": Questions},
                    ]
                }
            ]
            inputs = self.processor(conversation=conversation, return_tensors="pt")
            inputs = {k: v.cuda() if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}
            if "pixel_values" in inputs:
                inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
            output_ids = self.model.generate(**inputs, max_new_tokens=270)
            response = self.processor.batch_decode(output_ids, skip_special_tokens=True)[0].strip()
            print(query["factor"])
            print(response)
            self.df_questions.loc[i,"answer"]=response
        return self.df_questions


    
        

    


        





#df_questions=pd.DataFrame(Questions().init_quest())
#df_questions["answer"]=""

#Modelvision=ModelVision("DAMO-NLP-SG/VideoLLaMA3-2B-Image","F:\Proyectos Programacion\Proyectos Python\VisionSST\VisionIASST\situation/escalera.png",df_questions)
#print(Modelvision.model_name)
#print(Modelvision.vision_model_image_description())
    