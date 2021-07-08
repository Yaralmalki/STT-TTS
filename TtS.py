from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'FUsEaqvbD0bPcLbYtN9jMn56Jb5ruLZ1KilB1p3HUjVV'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/6d0c018c-fa12-4540-84c6-448fb517d392'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('tex.txt', 'r') as f:
    text = f.readlines()
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)
with open('./audio.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content) 