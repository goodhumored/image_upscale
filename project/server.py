from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import io
from keras._tf_keras.keras.models import load_model

sr_model = load_model("model256_50_epochs.h5")

app = Flask(__name__)

@app.route('/upscale', methods=['POST'])
def upscale_image():
    file = request.files['image'].stream
    img = Image.open(file).resize((512, 512))
    img.save("tmp.jpg")
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    # Предсказание через модель
    upscaled_img_array = sr_model.predict(img_array)[0]
    upscaled_img_array = (upscaled_img_array * 255).astype(np.uint8)
    upscaled_img = Image.fromarray(upscaled_img_array)

    # Возвращаем результат
    img_io = io.BytesIO()
    upscaled_img.save(img_io, 'JPEG')
    img_io.seek(0)

    return img_io

if __name__ == "__main__":
    
    app.run(debug=True)
