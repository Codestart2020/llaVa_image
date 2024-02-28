import requests
import json
import re
import base64
from urllib.parse import urlparse

url = "http://localhost:11434/api/generate"

header = {
    "Content-Type": "application/json"
}


def encode_image_to_base64(image_content):
    """Encode image content to base64."""
    base64_image = base64.b64encode(image_content).decode('utf-8')
    return base64_image


def send_request(image_path_or_url):
    """Send request to image captioning API."""
    # Check if the provided image path is a URL
    parsed_url = urlparse(image_path_or_url)

    # If it's a URL, directly encode the image from the URL
    if parsed_url.scheme and parsed_url.netloc:
        try:
            response = requests.get(image_path_or_url)
            response.raise_for_status()
            image_content = response.content
        except requests.exceptions.RequestException as e:
            return f"Error accessing URL: {e}"
    else:
        # If it's a local file path, read the image content from the file
        try:
            with open(image_path_or_url, "rb") as image_file:
                image_content = image_file.read()
        except FileNotFoundError:
            return f"File not found: {image_path_or_url}"

    base64_image = encode_image_to_base64(image_content)

    data = {
        "model": "LLaVA",
        "stream": False,
        "prompt": "what is this image?",
        "images": [base64_image]
    }

    # Send POST request to the API
    try:
        response = requests.post(url, headers=header, data=json.dumps(data))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error sending request: {e}"

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data['response']
        actual_response = re.sub(r'\d', '', actual_response)
        return actual_response
    else:
        return response.status_code, response.text


def send_request_with_condition(images_path, images_url):
    if images_path:
        text_captioning = send_request(images_path)
    else:
        text_captioning = send_request(images_url)
    return text_captioning


# Example usage with a local file path
images_path = ""
images_url =  ("")
text_captioning = send_request_with_condition(images_path, images_url)
print(text_captioning)
