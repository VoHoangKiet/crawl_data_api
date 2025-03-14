import requests
import random
import aiohttp
import asyncio
from itertools import cycle

userAgents=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
]
headers = {
    'Accept': 'text/html, image/avif, image/webp, image/apng, image/svg+xml, */*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US, en;q=0.9',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Site': 'none',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

headers['User-Agent'] = random.choice(userAgents)
url = 'https://yody.vn/post/outfit-la-gi?srsltid=AfmBOoq3WtBb8GQmze_MXhi8Xp0v1x_oEdt3y8iOS4Auvi8CY93peDFg'
data_request = requests.get(url, headers=headers)

print(data_request.status_code)

print(data_request.headers)

proxies = [
    'http://138.197.102.119:80',
    'http://23.82.137.162:80',
    'http://154.113.18.189:2020',
]

# Create a cycle iterator to rotate proxies
proxy_pool = cycle(proxies)

# Function to make an asynchronous request using a proxy
async def make_request(session, url):
    proxy = next(proxy_pool)  # Get the next proxy from the pool
    try:
        async with session.get(url, proxy=proxy, timeout=5) as response:
            print(f"Success! Proxy: {proxy}, Status Code: {response.status}")
            return await response.text()
    except Exception as e:
        print(f"Failed! Proxy: {proxy}, Error: {e}")
        return None

# Main function to run multiple requests
async def main():
    url = 'https://httpbin.org/ip'
    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, url) for _ in range(5)]  # Make 5 requests
        await asyncio.gather(*tasks)

# Run the async function
asyncio.run(main())