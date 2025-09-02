import csv
import requests
from bs4 import BeautifulSoup
try:
    url = 'https://www.weebly.com/in'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.get_text(strip=True)
        if href:
            data.append([text, href])
    with open('links.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Text', 'Href'])
        writer.writerows(data)
    images = soup.find_all('img', {'src': True})
    image_data = []
    for img in images:
        src = img.get('src')
        if src:
            image_data.append([src])
    with open('images.csv', 'w', newline='', encoding='utf-8') as img_file:
        writer = csv.writer(img_file)
        writer.writerow(['Image URL'])
        writer.writerows(image_data)
    print("✅ Links and image URLs successfully extracted and saved.")
except requests.exceptions.RequestException as e:
    print(f"❌ Network error occurred: {e}")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")