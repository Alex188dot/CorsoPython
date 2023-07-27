from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import hashlib
from cryptography.fernet import Fernet
from flask import Flask, render_template, request, redirect, make_response




app = Flask(__name__)


@app.route('/')
def index():
    return render_template('cryptography.html')

@app.route('/encode', methods=['POST'])
def encode():
    text = request.form['text']
    algo = request.form['algo']

    if algo == "1":
        result = aes(text)
    elif algo == "2":
        result = rsa_encrypt(text)
    elif algo == "3":
        result = sha(text)
    elif algo == "4":
        result = rc4(text)

    return render_template('cryptography.html', result=result)




###################################################################
# Symmetric Key (AES)

def aes(text):
    # Genera una chiave casuale
    key = Fernet.generate_key()
    # Crea un oggetto Fernet con la chiave generata
    cipher = Fernet(key)
    # Dati da crittografare
    data = text.encode("utf-8")
    # Crittografa i dati
    encrypted_data = cipher.encrypt(data)
    return encrypted_data


###################################################################
#Asymmetric key (RSA)

def rsa_encrypt(text):
    # Genera una coppia di chiavi RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    # Converti la chiave privata in formato PEM
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    # Converti la chiave pubblica in formato PEM
    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    # Dati da crittografare
    data = text.encode("utf-8")
    # Crittografa i dati utilizzando la chiave pubblica
    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data

###################################################################
# Hashing (SHA-256)

def sha(text):
    hash_object = hashlib.sha256(text.encode())
    hash_value = hash_object.hexdigest()
    return hash_value

###################################################################
# Stream Cipher
def rc4(text):
    def KSA(key):
        key_length = len(key)
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def PRGA(S):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % 256]
            yield K

    def RC4(key, plaintext):
        S = KSA(key)
        keystream = PRGA(S)
        ciphertext = []
        for byte in plaintext:
            ciphertext.append(byte ^ next(keystream))
        return bytes(ciphertext)
    def print_bits(byte):
        # Stampa i bit di un byte come una sequenza di 0 e 1
        for i in range(7, -1, -1):
            bit = (byte >> i) & 1
            print(bit, end='')
        print()
    key = b'Key'  # Chiave di esempio
    plaintext = text.encode("utf-8")
    ciphertext = RC4(key, plaintext)
    bits = []
    # Loop through each byte in ciphertext and append the bits to the list
    for byte in ciphertext:
        bit_string = ""
        for i in range(7, -1, -1):
            bit = (byte >> i) & 1
            bit_string += str(bit)
        bits.append(bit_string)
    # Return a tuple of ciphertext and bits
    return (ciphertext, bits)







if __name__ == "__main__":
    app.run(debug=True)



