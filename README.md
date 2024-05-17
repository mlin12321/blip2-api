# BLIP Image Captioning API


## Installation

1. Clone the repository:

   ```
   git clone https://github.com/askaresh/blip-image-captioning-api.git
   ```

2. Navigate to the project directory:

   ```
   cd blip-image-captioning-api
   ```

3. Run the run.sh file
   ```
   bash run.sh
   ```

   The API will be accessible at `http://localhost:8004`.

## Usage

### API Endpoint

The API provides a single endpoint for generating image captions:

- `POST /caption`: Generate a caption for an image.

### Request

To generate a caption for a list of images, send a `POST` request to the `/caption` endpoint with the following parameters:

- `image` (required): The image file to generate a caption for. The image should be sent as a multipart form data.
- `text` (optional): An optional text input to guide the caption generation process. This can be used for conditional image captioning.

Example using cURL:

```bash
curl -X POST -F "image=@path/to/image.jpg" -F "text=optional text input" http://localhost:8000/caption
```

See also ex_sample.sh.

An example for generating captions in python is in test-blip2.py.

### Response

The API will respond with a JSON object containing the generated captions:

```json
{
  "caption": ["a person riding a bike on a city street"]
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [BLIP Model](https://huggingface.co/Salesforce/blip-image-captioning-large)