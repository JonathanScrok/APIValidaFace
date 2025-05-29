from flask import Flask, request, jsonify
import face_recognition
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

@app.route('/validar', methods=['POST'])
def validar():
    if 'imagem1' not in request.files or 'imagem2' not in request.files:
        return jsonify({'erro': 'Envie as duas imagens'}), 400

    imagem1 = face_recognition.load_image_file(request.files['imagem1'])
    imagem2 = face_recognition.load_image_file(request.files['imagem2'])

    try:
        encoding1 = face_recognition.face_encodings(imagem1)[0]
        encoding2 = face_recognition.face_encodings(imagem2)[0]
    except IndexError:
        return jsonify({'erro': 'Rosto não detectado em uma das imagens'}), 400

    resultado = face_recognition.compare_faces([encoding1], encoding2)[0]

    return jsonify({'rosto_igual': bool(resultado)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
