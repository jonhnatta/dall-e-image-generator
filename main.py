import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os
import requests

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI()

st.title("Gerador de Imagens com DALL-E")

prompt = st.text_input("Descreva a imagem que deseja gerar:")

if st.button("Gerar Imagem"):
    st.write("Aguarde...")
    
    response_image = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response_image.data[0].url
    print(image_url)
    
    st.image(image_url, caption="Imagem gerada")

    get_image = requests.get(image_url)
    
    st.empty()

    # if get_image.status_code == 200:
    #     with open("imagem.jpg", "wb") as arquivo:
    #         arquivo.write(get_image.content)
    #     st.success("Imagem salva!!!")
    # else:
    #     st.error("Falha ao criar imagem")
