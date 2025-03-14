import requests
import cloudscraper
import base64
from app.repositories.ImageHandleRepository import ImageHandleRepository
from app.models.ImageInfo import ImageInfo

class HandleImageService:
    def __init__(self):
        self.repository = ImageHandleRepository()
    def add_multiple_images(self, images_data: list[dict]):
        try:
            images = [
                ImageInfo(
                    id=data["id"],
                    description=data["description"],
                    image_url=data["image_url"],
                )
                for data in images_data
            ]
            ids = self.repository.add_images(images)
            return {"message": "Images added", "ids": ids}
        except Exception as e:
            raise Exception(f"Service error: {e}")
    @staticmethod
    def _convert_base64(listUrl: list[str]):
        try:
            scraper = cloudscraper.create_scraper()
            image_base64_list = []
            for url in listUrl:
                response = scraper.get(url)
                if response.status_code == 200:
                    image_base64 = base64.b64encode(response.content).decode('utf-8')
                    image_base64_list.append(image_base64)
                    print(image_base64)
                else:
                    print(f"Failed to retrieve image from {url}")
            return image_base64_list
        except requests.RequestException as e:
            print(f"Lỗi khi gửi request: {e}")
            return None
async def handle_convert_base64(listUrl: list[str]) -> list[str]:
    try:
        result = HandleImageService._convert_base64(listUrl)
        return result
    except requests.RequestException as e:
        print(f"Lỗi khi gửi request: {e}")
        return None