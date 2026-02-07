from fastapi import FastAPI, UploadFile, File
from PIL import Image 
import io
from inference import Predict

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # make sure it is a .png
    if not file.filename.endswith(".png"):
        return {"error": "only .png files are allowed"}
    
    # read the bytes
    contents = await file.read()

    # open the image
    img = Image.open(io.BytesIO(contents))


    # its a confirmation that backend recieved the file and img 
    # image was successfully opened # it is returned to the person who sends HTTP request 

    return Predict(img)