from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    blip_model_name: str = "Salesforce/blip2-flan-t5-xl"

settings = Settings()

# In config.py
print(dir())  # See what symbols are available at the end of the file
