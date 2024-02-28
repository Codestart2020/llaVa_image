# llaVa_image

This project is a Python application that uses the LLaVa API to generate captions for images. The application can handle both local image files and image URLs.

Dependencies

The project uses the following Python libraries:

requests
json
re
base64
urllib.parse

How it Works 

encode_image_to_base64(image_content): This function takes in image content and encodes it to base64.  

send_request(image_path_or_url): This function sends a request to the LLaVa API. It takes in either a local image file path or an image URL, encodes the image to base64, and sends a POST request to the API. If the API call is successful, it returns the generated caption. If not, it returns the status code and response text.

send_request_with_condition(images_path, images_url): This function checks if a local image path is provided. If so, it calls send_request() with the local image path. If not, it calls send_request() with the image URL


