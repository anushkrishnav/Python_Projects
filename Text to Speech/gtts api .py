from gtts import gTTS
import os
text="I use Google Text to Speech API's"
language='en'
speech=gTTS(text=text,lang=language,slow=False)
speech.save("test.mp3")
os.system("start test.mp3")