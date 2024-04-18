import requests
from properties import *

def create_session(api_key, face_id, intro, prompt, time_limit, user_name, voice_id):
    # URL de la API de Simli para crear una sesión
    simli_url = "http://35.214.172.224:8080/startSession"

    # Datos del cuerpo de la solicitud
    payload = {
        'apiKey': api_key,
        'faceId': face_id,
        'intro': intro,
        'prompt': prompt,
        'timeLimit': {
            'limit': time_limit  # Definir timeLimit como un diccionario
        },
        'userName': user_name,
        'voiceId': voice_id
    }

    # Cabeceras de la solicitud
    headers = {'Content-Type': 'application/json'}

    try:
        # Realizar la solicitud POST a la API de Simli
        response = requests.post(simli_url, json=payload, headers=headers)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            data = response.json()
            # Construir la URL de la sala
            room_url = "https://simli-test.daily.co/" + data['meetingUrl'][-15:]
            return room_url
        else:
            print("Error al crear la sesión:", response.text)
            return None
    except Exception as e:
        print("Error de conexión:", e)
        return None

api_key = api_key
face_id = face_id
intro = intro
prompt = prompt
time_limit = time_limit
user_name = user_name
voice_id = voice_id

room_url = create_session(api_key, face_id, intro, prompt, time_limit, user_name, voice_id)
if room_url:
    print("URL de la sala:", room_url)
else:
    print("No se pudo crear la sesión.")
