import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91/ref=sr_1_2?crid=2381Y6PWVRNRY&keywords=playstation%2B5&qid=1702833730&sprefix=pla%2Caps%2C462&sr=8-2&th=1'

# Make a request to the Amazon product page
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the image tag using its ID
    image_tag = soup.find('img', {'id': 'landingImage'})

    # Extract the image source URL
    if image_tag:
        image_url = image_tag.get('src')
        print("Image URL:", image_url)

        # Download the image
        image_response = requests.get(image_url)
        with open('product_image.jpg', 'wb') as image_file:
            image_file.write(image_response.content)
        print("Image downloaded successfully.")

    else:
        print("Image not found on the page.")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
