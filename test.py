from langchain_google_genai import ChatGoogleGenerativeAI
from elevenlabs.client import ElevenLabs
from elevenlabs import play
from dotenv import load_dotenv
import os
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

def generate_text(prompt):
    
    cont_resp=model.invoke(prompt)
    return cont_resp

def manim_code(text):
    prompt=f"""You are a Manim code generator for the ManimCE version 0.19.0. 
Write Python code for explaining the given topic.Make more diagrams and graphs and only necessary text
- Always include `from manim import *` at the top.
- Use MathTex for formulas and wrap LaTeX strings in r" " when using Tex or MathTex.
- Always wrap math parts in `$...$` inside Tex or MathTex (e.g. `$2 \pi r$`).
- Add .wait(5) after each animation.
- Only output Python code, no explanations, no ``` fences.
- Make only one scene and name it generated_scene.
TOPIC: {text}"""

    resp_manim= model.invoke(prompt)
    return resp_manim
    

def text_to_voice(text_recv,filename="output.mp3"):
    elevenlabs=ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )
    audio = elevenlabs.text_to_speech.convert(
        text=text_recv,
        voice_id="pNInz6obpgDQGcFmaJgB",
        model_id="eleven_turbo_v2_5",
        output_format="mp3_44100_128"
    )
    with open(filename,"wb")as f:
        for chunk in audio:
            f.write(chunk)
    
def video_generator(code):
    cleaned_code = code.replace("```python","").replace("```","")
    with open("generated_video.py","w")as f:
        f.write(cleaned_code)
    os.system("manim -pql generated_video.py generated_scene")

