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
        keyboard.press(_pre)
        pyautogui.sleep(0.1)
        pyautogui.write(_text)
        pyautogui.sleep(0.1)
        keyboard.press('enter')
    except Exception:
        pass


while True:
    if keyboard.is_pressed('ctrl'):
        speech_to_chat(_pre='t')
    elif keyboard.is_pressed('shift'):
        speech_to_chat(_pre='y')
