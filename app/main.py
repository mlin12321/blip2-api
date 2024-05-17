from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from typing import List
import logging.config
from PIL import Image
from .model import load_model, generate_caption
from .utils import load_image_from_file
from .config import settings
import torch
import io 

app = FastAPI()

model_device = torch.device("cuda") 

# Load the BLIP model once when the app starts
model, processor = load_model(settings.blip_model_name)

model.to(model_device)

# Configure logging
logging.config.fileConfig('./logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

# Example root path handler
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Image Captioning API!"}

@app.post("/caption")
async def caption(images: List[UploadFile] = File(...), prompts: List[str] = None, max_new_tokens:int = Form(...)):
    captions = []

    opened_images = []

    for image in images:
        try:
            # if image.content_type not in ["image/jpeg", "image/png"]:
            #     raise HTTPException(status_code=400, detail="Invalid image format")
            loaded_image = load_image_from_file(await image.read())
            opened_images.append(loaded_image)

        except Exception as e:
            logger.exception("Error in /caption endpoint")
            raise HTTPException(status_code=500, detail="Internal server error")
        finally:
            await image.close()

    captions = generate_caption(model, processor, opened_images, prompts, max_new_tokens)

    return {"captions":captions}
