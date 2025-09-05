import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for the image URL
    url = input("Enter the image URL: ").strip()
    
    # Create the Fetched_Images directory if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)
    
    try:
        # Send GET request to fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad status codes
        
        # Try to extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If no valid filename, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"
        
        # Full path to save image
        save_path = os.path.join(save_dir, filename)
        
        # Save image in binary mode
        with open(save_path, "wb") as file:
            file.write(response.content)
        
        print(f"✅ Image successfully downloaded and saved as: {save_path}")
    
    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL. Please include http:// or https://")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
