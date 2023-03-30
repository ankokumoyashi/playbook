import openai
import os

def call_turbo(s_txt, u_txt):
    openai.api_key = os.environ.get('API_KEY')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': s_txt},
            {'role': 'user', 'content': u_txt}
        ],
        temperature=0.0,
    )
    return response

if __name__ == "__main__":
    main()

