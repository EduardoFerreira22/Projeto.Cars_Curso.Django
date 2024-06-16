import openai
import os

def get_car_ai_bio(model, brand, year):
    prompt = f"Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas especificas desse modelo."

    # Defina sua chave da API aqui
    openai.api_key = ''

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "Você é um especialista em carros."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250
    )

    return response['choices'][0]['message']['content']
