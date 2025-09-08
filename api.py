from fastapi import FastAPI
from test import generate_text , manim_code , text_to_voice , video_generator
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (frontend URLs)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Prompt(BaseModel):
    text:str
    
@app.get('/users/search')
def text_gen(query:str):
    prompt = f" you are a math expert , explain {query} in simple terms . Output only one example at the end and dont give long explanations"
    response=generate_text(prompt)
    text = response.content
    code=manim_code(text)
    video =video_generator(code)
    audio= text_to_voice(text)
    return {'content':response,
             'video':video,
             'audio':audio}