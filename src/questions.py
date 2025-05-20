import pandas as pd

class Questions:
    
    def __init__(self, *args, **kwargs):
        pass
    
    def init_quest(self):

        Questions_list=[
            {
                "factor":"Description",
                "query":"Describe in detail the situation shown in the image. Mention the people, objects, actions, or conditions present, and any other relevant elements you can identify."
            },
            {
                "factor":"Description sst",
                "query":"You are an expert in Occupational Safety and Health (OSH). Carefully examine the provided image and give a detailed description of the situation. Identify potential hazards, unsafe conditions, unsafe acts, and any violations of safety regulations."
            },
            {
                "factor":"6Mmethod",
                "query":"As an expert in Occupational Safety and Health (OSH), analyze the situation shown in the image and identify potential risks using the 6M method (Manpower, Method, Machinery, Materials, Environment, and Measurement). For each category, provide a detailed description of the associated risk factors based on the observed situation, and suggest appropriate preventive or corrective actions."
            },
            {
                "factor":"Manpower",
                "query":"""As an expert in Occupational Safety and Health (OSH), analyze the image and identify any manpower-related factors that could contribute to an accident or incident. Evaluate whether the worker is fit for the task by considering:
                        •	Knowledge and experience (training, certifications, education)
                        •	Physical condition (strength, vision, health, weight, medical issues)
                        •	Psychological condition (attitude toward safety, willingness to take unsafe actions)
                        Describe in detail any human-related risk factors present in the observed situation.
                        """
            },
            {
                "factor":"Method",
                "query":"""As an expert in Occupational Safety and Health (OSH), analyze the image and identify whether any work method factors could contribute to an accident or incident. Assess whether:
                        •	A standardized procedure exists for the task.
                        •	The method is appropriate for ensuring safety.
                        •	The worker is aware of and correctly applies the method.
                        •	There is evidence of training (photos, signatures, records).
                        Visually identify if the worker is performing unsafe acts or if there is a lack of safe working methods. Describe the potential risks associated with the absence or misuse of proper procedures.
                        """
            },
            {
                "factor":"Materials",
                "query":"""As an expert in Occupational Safety and Health (OSH), analyze the image and identify any materials-related factors that could lead to an accident or incident. Specifically evaluate:
                    •	Whether the worker is using personal protective equipment (PPE).
                    •	If the PPE used is appropriate for the task being performed.
                    •	The presence of proper and visible signage.
                    •	Whether administrative requirements are in place (e.g., work permits, supervision, signed documentation).
                    Describe any potential risks related to the absence, misuse, or inadequacy of materials or PPE observed in the scene.
                    """
            },
            {
                "factor":"Machine",
                "query":"""
                As an expert in Occupational Safety and Health (OSH), analyze the image and identify any machine, equipment, or facility factors that may have contributed—or could contribute—to an accident or incident. Visually assess the following:
                •	Is any machinery or equipment present and in use?
                •	Is it suitable for the task being performed?
                •	Is there evidence of inspections or maintenance (e.g., tags, checklists, records)?
                •	Are pre-operational conditions safe and adequate?
                •	Are there signs of poor condition, improper use, or lack of operating manuals?
                Describe any potential risks associated with malfunctioning, inadequate use, or lack of control over machinery, equipment, or facilities.
                """          
            },
            {
                "factor":"Enviroment",
                "query":"""
                    As an expert in Occupational Safety and Health (OSH), analyze the image and identify any environmental or surrounding factors that could have contributed—or could contribute—to an accident or incident. Visually assess:
                    •	Whether the environment is suitable for the task to be performed safely.
                    •	The presence of climate or weather-related risks (e.g., rain, extreme heat, humidity, fog, dust).
                    •	Any visible signs of environmental contamination (gases, smoke, airborne particles).
                    •	Whether air quality, lighting, or ventilation conditions might compromise worker safety.
                    Describe any potential risks associated with uncontrolled or inadequate environmental conditions.
                """
            },
            {
                "factor":"Messure",
                "query":"""As an expert in Occupational Safety and Health (OSH), analyze the image and identify any measurement-related factors that could pose a risk or may have contributed to an accident or incident. Consider the following:
                •	Whether any measurement instruments are visible (e.g., gas detectors, temperature or pressure gauges).
                •	If the instruments appear to be properly calibrated and suitable for the task.
                •	If critical safety measurements are being taken (e.g., TLVs, exposure levels, medical condition checks).
                •	Whether the person using the device appears trained and certified for its use.
                Describe any risks related to the absence, misuse, or error of measurement instruments or processes.
                """
            },

        ]
        return pd.DataFrame(Questions_list)
    
    def get_question_analisys(self):
        Question_analisys="""
        You are an expert in Occupational Health and Safety (OHS). You will receive a detailed textual description of a workplace situation.
        1.Summarize the most relevant aspects of the situation.
        2.Identify any risks present.
        3.Identify any unsafe acts (actions performed in a hazardous way by individuals).
        4.Identify any unsafe conditions (hazardous environmental, equipment, material, or procedural elements).
        5.Based on your analysis, determine the most critical risks.
        6.Issue a risk alert using the following system:
        🔴 Red Alert: If there is a real and immediate risk of death, amputation, serious injury, or major harm to people or the facility.
        🟡 Yellow Alert: If there are potential risks that could escalate but do not require immediate work stoppage.
        🔵 Blue Alert: If no significant risk is present and the task can continue safely.
        """
        return Question_analisys
    
    def generate_full_question_for_llm(self, df_questions):
        description_sst=self.get_question_analisys()
        for i, query in df_questions.iterrows():
            description_sst=description_sst+query["factor"]+": "
            description_sst=description_sst+query["answer"]
        
        return description_sst

    

#list_query=Questions().init_quest()
#print(list_query)

