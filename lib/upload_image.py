import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

# LOAD .env FILE
load_dotenv()

# CONFIGURE CLOUDINARY
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

def upload_image(image_path: str) -> str | None:
    if not image_path:
        return None

    result = cloudinary.uploader.upload(
        image_path,
        folder="telegram-events",
        resource_type="image"
    )

    return result["secure_url"]
