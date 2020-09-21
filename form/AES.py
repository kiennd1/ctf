import base64
from Crypto.Cipher import AES
from django.shortcuts import render

def encrypt(request, plaintext):
    key = '5468617473206D79'
    iv = 'UEwe6QAmK5mby09T'
    try:
        plaintext = _pad(plaintext)
    except:
        return render(request, 'form/index.html', {})
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(cipher.encrypt(plaintext)).decode("utf-8")

def _pad(s):
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
