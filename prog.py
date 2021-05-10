import Crypto.Cipher.AES as AES
import hashlib
import base64

fileToDecrypt = open(
    r"C:\Users\avish\Downloads\tmpy7o220", 'r')
fileToHash    = open(
    r"C:\Users\avish\Downloads\tmpyOSkLQ.txt", 'r')

message = base64.b64decode(fileToDecrypt.read())
key =     fileToHash.read()


keyAndIv = hashlib.md5(key).digest()[:16]
cipher = AES.new(keyAndIv, AES.MODE_CBC,keyAndIv)
print("---------------------------------------")
print("Message:")
print("---------------------------------------")
print(cipher.decrypt(message))
print("=======================================")

print("=======================================")
print("MD5")

keyAndIv = hashlib.sha1(key).digest()[:16]
cipher = AES.new(keyAndIv, AES.MODE_CBC,keyAndIv)
print("=======================================")
print("Sha1")
print("---------------------------------------")
print("Message:")
print("---------------------------------------")
print(cipher.decrypt(message))
print("=======================================")


keyAndIv = hashlib.sha256(key).digest()[:16]
cipher = AES.new(keyAndIv, AES.MODE_CBC,keyAndIv)
print("=======================================")
print("Sha256")
print("---------------------------------------")
print("Message:")
print("---------------------------------------")
print(cipher.decrypt(message))
print("=======================================")

keyAndIv = hashlib.sha512(key).digest()[:16]
cipher = AES.new(keyAndIv, AES.MODE_CBC,keyAndIv)
print("=======================================")
print("Sha512")
print("---------------------------------------")
print("Message:")
print("---------------------------------------")
print(cipher.decrypt(message))
print("=======================================")
