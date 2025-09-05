# ubuntu_requests

# 🌍 Ubuntu_Requests

**Ubuntu Image Fetcher** – A mindful tool for collecting images from the web, built with Python’s `requests` library.  
Inspired by Ubuntu principles of **community, respect, sharing, and practicality**.  

> *"A person is a person through other persons." – Ubuntu philosophy*  

---

## ✨ Features
- 📥 Fetch **multiple images** from URLs at once  
- 🛡️ Precautions against unsafe sources (checks content type & file size)  
- 🔄 Prevents **duplicate downloads** using file hashes  
- 📂 Automatically organizes images in a `Fetched_Images` directory  
- 🙏 Handles errors gracefully without crashing  

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Ubuntu_Requests.git
cd Ubuntu_Requests

pip install requests

##   RUN THE CODE 
python ubuntu_requests.py

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter image URLs (separated by commas): https://example.com/img1.jpg, https://example.com/img2.png
✓ Successfully fetched: img1.jpg
✓ Image saved to Fetched_Images/img1.jpg
✓ Successfully fetched: img2.png
✓ Image saved to Fetched_Images/img2.png

Connection strengthened. Community enriched.
Respecting safety, sharing resources mindfully, and serving a real need.





Requirements

Use the requests library to fetch the image

Check for HTTP errors and handle them appropriately

Create the directory if it doesn't exist using os.makedirs() with exist_ok=True

Extract the filename from the URL or generate one if not available

Save the image in binary mode

Ubuntu Principles to Implement

Community: Your program should connect to the wider web community

Respect: Handle errors gracefully without crashing

Sharing: Organize the fetched images for later sharing

Practicality: Create a tool that serves a real need

Save Your Work in a GitHub Repo Called "Ubuntu_Requests" and Submit the URL for this Repository to Complete the Assignment. 

Example Output
Terminal Output Text
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.

Starter Code Structure
python
import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:
            filename = "downloaded_image.jpg"
            
        # Save the image
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()

    Modify the program to handle multiple URLs at once.

Implement precautions that you should  take when downloading files from unknown sources.

Implement a feature that prevents downloading duplicate images.

Implement what HTTP headers might be important to check before saving the response content.

Evaluation Criteria

Proper use of the requests library for fetching content

Effective error handling for network issues

Appropriate file management and directory creation

Clean, readable code with clear comments

Faithfulness to Ubuntu principles of community and respect

Remember:

"A person is a person through other persons." - Ubuntu philosophy. Your program connects you to the work of others across the web.