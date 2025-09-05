# Ubuntu_Requests

## A Python script that:

1. Prompts the user for a URL containing an image

2. Creates a directory called "Fetched_Images" if it doesn't exist

3. Downloads the image from the provided URL

4. Saves it to the Fetched_Images directory with an appropriate filename

5. Handles errors gracefully, respecting that not all connections succeed

## Requirements

1. Use the requests library to fetch the image

2. Check for HTTP errors and handle them appropriately

3. Create the directory if it doesn't exist using os.makedirs() with exist_ok=True

4. Extract the filename from the URL or generate one if not available

5. Save the image in binary mode

## Ubuntu Principles to Implement

**1. Community:** Your program should connect to the wider web community
**2. Respect:** Handle errors gracefully without crashing
**3. Community:** Your program should connect to the wider web community
**4. Sharing:** Organize the fetched images for later sharing
**5. Practicality:** Create a tool that serves a real need

Sharing: Organize the fetched images for later sharing

Practicality: Create a tool that serves a real need
