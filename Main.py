import subprocess
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api = IAMAuthenticator("sxsynl8DH7Vc9s4mfPM1UHDekyNwUmNYAfuI27cqeTqi")
stt = SpeechToTextV1(authenticator=api)
stt.set_service_url("https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/3878cdcc-3cb7-4b00-86e4-dbed75307d3f")
with open(r"C:\Users\MANISH\Desktop\1.wav","rb" ) as audio_file:
    result = stt.recognize(
        audio=audio_file,content_type="audio/wav"
    ).get_result()
print(result)
