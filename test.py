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

# if __name__ == "__main__":
#     query = "Curve filling"
#     query_content = generate_text(query)
#     text = query_content.content
#     example_part = text.split("Example:")[-1].strip()
#     print(text)
#     print("EXAMPLE:\n", example_part, "\n")
#     manim_code(example_part)


# query= input("enter topic")
# prompt=f"you are an math expert . Explain {query} in professionally and add a example section at last"
# cont=generate_text(prompt)
# example_part = cont.content.split("Example:")[-1].strip()
# print(cont.content)
# print(manim_code(example_part))
# text_to_voice(example_part)