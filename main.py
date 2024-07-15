from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


app = Flask(__name__)
model = load_model("skin_disease_model.h5")


#Defining the classes

class_names  =["Cellulitis", "Impetigo", "Athelete-Foot", "Nail-Fungus", "Ringworm","Cutaneous-larva-migrans","Chickenpox", "Shingles"]


#Preparing the image before feeding it to the model
def preprocess_image(img, target_size):
    img = img.resize(target_size)
    im = img_to_array(img)
    img = np.expand_dims(img, axis =0)
    img = img / 255.0
    return img


#Defining the routes
@app.route("/", methods =["GET", "POST"])
def predict():
    if request.method == "POST":
        file = request.files["file"]

        if file:
            image = Image.open(file.stream)
            image = preprocess_image(image, target_size=(150,150))
            prediction = model.predict(image)
            predicted_class = class_names[np.argmax(prediction)]

            return render_template("index.html", prediction =  predicted_class)
        
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)