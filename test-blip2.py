import io
import requests
from PIL import Image


image1 = Image.open("cat.jpg")
image2 = Image.open("dog.jpg")

def pil_image_to_bytes(image, format = "JPEG"):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format=format)
    img_byte_arr.seek(0)
    return img_byte_arr 

img1_bytes = pil_image_to_bytes(image1)
img2_bytes = pil_image_to_bytes(image2)

headers = {
    'accept': 'application/json'
}

files = [
    ("images", ("test", img1_bytes, None)), #"image/jpeg", img1_bytes)),
    ("images", ("test.asdsdasdas", img2_bytes, None)), #"image/jpeg", img2_bytes)),
    ("max_new_tokens", (None, 12)), #'64')),
    # ("prompts", (None, "What is the cat laying on?")),
    # ("prompts", (None, "What is the dog laying on?")),
]

url = "http://127.0.0.1:8004/caption/"
response = requests.post(url, headers=headers, files=files)

print(response)
print(response.json()['captions'])
