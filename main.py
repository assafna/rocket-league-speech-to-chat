import keyboard
import pyautogui
import speech_recognition as sr


def speech_to_chat(_pre):
    try:
        _r = sr.Recognizer()
        with sr.Microphone() as _source:
            _audio_data = _r.listen(_source)
            _text = _r.recognize_google(_audio_data)
        print(_text)
        pyautogui.write(_pre + _text)
        keyboard.press('enter')
    except Exception:
        pass


while True:
    if keyboard.is_pressed('ctrl'):
        speech_to_chat(_pre='t')
    elif keyboard.is_pressed('shift'):
        speech_to_chat(_pre='y')
