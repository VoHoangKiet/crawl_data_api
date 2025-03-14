from pydantic import BaseModel

class ImageInfo(BaseModel):
    id: int
    description: str
    image_url: str

    def to_dict(self):
        data = {
            "id": self.id,
            "description": self.description,
            "image_url": self.image_url,
        }
        return data