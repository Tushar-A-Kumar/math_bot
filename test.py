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
    prompt=f"""you are a manim code generator, write manim code for this text as the audio.
            - Use MathTex for formulas
            - add .wait(2) after each animation
            - only python code , no explanations 
            TEXT:{text}"""
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
    return 0

