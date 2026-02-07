import joblib
from pathlib import Path
from PIL import Image
import numpy as np

def preprocess(image):
    if isinstance(image, Image.Image):
        img = image.convert("L")
    else :
        raise ValueError("Input must be PIL type")
    
    img = img.resize((8, 8))

    img_array = np.array(img)
    img_array = img_array.reshape(64)
    img_array = img_array.reshape(1, 64)

    return img_array

model_path = Path("model.joblib")

def load_model():
    return joblib.load(model_path)

model = load_model()

def Predict(image):
    x = preprocess(image)
    y = model.predict(x)
    z = int(y[0])
    return z

"""if __name__ == "__main__":
    from PIL import Image

    image_path = "photo_88.png"
    image = Image.open(image_path)

    result = predict(image)
    print(result)"""