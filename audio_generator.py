import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    sample_text = "Hello! This is a sample text-to-speech conversion."  
    text_to_speech(sample_text)