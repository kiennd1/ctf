import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

def encrypt(plaintext):
    key = '5468617473206D79'
    iv = 'UEwe6QAmK5mby09T'
    plaintext = _pad(plaintext)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(cipher.encrypt(plaintext))

def _pad(s):
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
