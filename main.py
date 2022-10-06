import numpy as np
import uvicorn
from fastapi import FastAPI, File, UploadFile
from PIL import Image

import get_items

app = FastAPI()


@app.get('/')
def index() -> dict[str, str]:
    return {'message': 'Send an image to /generate-receipt'}


@app.post('/get-items')
def create_item_list(file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    items = get_items.get_receipt(image)
    return {
        'list of items': items,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
