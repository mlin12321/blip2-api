import logging
import torch
from typing import List
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration

logger = logging.getLogger(__name__)

def load_model(model_name):
    model_dtype = torch.float16 

    try:
        # Load the pre-trained BLIP model for image-to-text captioning
        processor = Blip2Processor.from_pretrained(model_name)
        model = Blip2ForConditionalGeneration.from_pretrained(model_name, torch_dtype=model_dtype)
        logger.info(f"Loaded model: {model_name}")
        return model, processor
    except Exception as e:
        logger.exception(f"Error loading model: {model_name}")
        raise e

def generate_caption(model, processor, opened_images: List[Image.Image], prompts: List[str] = None, max_new_tokens: int = 32):
    device = torch.device("cuda") if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    try:
        # Prepare the inputs for captioning
        if prompts is None:
            # Conditional image captioning
            inputs = processor(images=opened_images, return_tensors="pt").to(device, dtype)
            generated_ids = model.generate(**inputs, max_new_tokens=max_new_tokens)
            captions = processor.batch_decode(generated_ids, skip_special_tokens=True)
        else:
            # Unconditional image captioning
            assert len(opened_images) == len(prompts), "Number of images and prompts must match"

            # Note that this throws errors if the prompts aren't the same length, which probably requires some sort of padding
            # In the use case this is designed for though I don't believe this is required since prompts are the same, so I 
            # omit this for now. 
            inputs = processor(images=opened_images, text=prompts, return_tensors="pt").to(device, dtype)
            generated_ids = model.generate(**inputs, max_new_tokens=max_new_tokens)
            captions = processor.batch_decode(generated_ids, skip_special_tokens=True)


        # Generate the caption
        #caption = processor.decode(out[0], skip_special_tokens=True)
        logger.info(f"Generated caption: {captions}")

        return captions
    except Exception as e:
        logger.exception("Error during caption generation")
        raise e