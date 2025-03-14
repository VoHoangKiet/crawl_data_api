# app/services/crawl_service.py
import requests
import cloudscraper
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from dotenv import load_dotenv
import os

class CrawlService:
    def __init__(self):
        load_dotenv()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com/",
        }
        self.api_key = os.getenv("GOOGLE_CUSTOM_SEARCH_API")
        self.cse_id = os.getenv("GOOGLE_CUSTOM_SEARCH_ELEMENT_ID")

    def _make_request(self, url: str) -> Optional[BeautifulSoup]:
        try:
            scraper = cloudscraper.create_scraper()
            response = scraper.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.content, "html.parser")
        except requests.RequestException as e:
            print(f"Lỗi khi gửi request: {e}")
            return None

    def _parse_images(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        images = [{"id": i + 1, "image_url": img["src"], "description": img.get("alt", "")}
                  for i, img in enumerate(soup.find_all("img", src=True))]
        return images

    def search_pins(self, url: str) -> List[Dict[str, str]]:
        soup = self._make_request(url)
        return self._parse_images(soup) if soup else []

    def google_image_search(self, query: str, num: int = 10) -> Optional[List[Dict[str, str]]]:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'q': query,
            'key': self.api_key,
            'cx': self.cse_id,
            'searchType': 'image',
            'num': num
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json()
            return [{"id": i + 1, "image_url": item['link'], "description": 'google_search'}
                    for i, item in enumerate(results.get('items', []))]
        print(f"Error: {response.status_code}")
        return None

async def crawl_image(url: str) -> List[Dict[str, str]]:
    return CrawlService().search_pins(url)

async def google_crawl_image(query: str) -> List[Dict[str, str]]:
    return CrawlService().google_image_search(query)