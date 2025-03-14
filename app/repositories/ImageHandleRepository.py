from app.config.database import db
from app.models.ImageInfo import ImageInfo
class ImageHandleRepository:
    def __init__(self):
        self.collection = db.get_collection('images')
    def add_images(self, images: list[ImageInfo]):
        try:
            data = [image.to_dict() for image in images]
            result = self.collection.insert_many(data)
            return [str(id) for id in result.inserted_ids]
        except Exception as e:
            raise Exception(f"Error creating multiple students: {e}")