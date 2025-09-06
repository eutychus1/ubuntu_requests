import os
import requests
import hashlib
from urllib.parse import urlparse
import pkg_resources  # To fetch installed version


def get_file_hash(filepath):
    """Generate a SHA256 hash of the file to detect duplicates."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def download_image(url, save_dir, existing_hashes):
    """Download a single image with error handling and duplicate prevention."""
    try:
        # Fetch the image with timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Check content type and size
        content_type = response.headers.get("Content-Type", "")
        content_length = response.headers.get("Content-Length", "")

        if "image" not in content_type.lower():
            print(f"✗ Skipping {url} (not an image, Content-Type={content_type})")
            return None

        if content_length and int(content_length) > 10_000_000:  # 10 MB limit
            print(f"✗ Skipping {url} (file too large: {int(content_length)/1_000_000:.2f} MB)")
            return None

        # Extract filename or generate default
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
        filepath = os.path.join(save_dir, filename)

        # Handle duplicate filenames by renaming
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(filepath):
            # Compare hash to detect actual duplicates
            if get_file_hash(filepath) == hashlib.sha256(response.content).hexdigest():
                print(f"⚠ Duplicate skipped: {filename}")
                return None
            filename = f"{base}_{counter}{ext}"
            filepath = os.path.join(save_dir, filename)
            counter += 1

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        # Store hash to prevent future duplicates
        file_hash = get_file_hash(filepath)
        existing_hashes.add(file_hash)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return filepath

    except requests.exceptions.MissingSchema:
        print(f"✗ Invalid URL provided: {url}. Please include http:// or https://")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP Error for {url}: {e}")
    except requests.exceptions.ConnectionError:
        print(f"✗ Connection error for {url}. Please check your internet.")
    except requests.exceptions.Timeout:
        print(f"✗ Timeout for {url}. Try again later.")
    except Exception as e:
        print(f"✗ An unexpected error occurred for {url}: {e}")
    return None


def create_requirements_file():
    """Create requirements.txt with the exact requests version installed."""
    try:
        version = pkg_resources.get_distribution("requests").version
        with open("requirements.txt", "w") as f:
            f.write(f"requests=={version}\n")
        print(f"\n📄 requirements.txt created with requests=={version}")
    except Exception as e:
        print(f"✗ Could not create requirements.txt: {e}")


def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("🤝 A tool for mindfully collecting images from the web\n")

    # Get multiple URLs from user
    urls = input("Please enter image URLs (separated by commas): ").split(",")
    urls = [u.strip() for u in urls if u.strip()]

    if not urls:
        print("✗ No URLs provided. Exiting.")
        return

    # Create directory for images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    existing_hashes = set()

    for url in urls:
        download_image(url, save_dir, existing_hashes)

    # Create requirements.txt
    create_requirements_file()

    print("\n✅ Connection strengthened. Community enriched.")
    print("✨ Respecting safety, sharing resources mindfully, and serving a real need.")


if __name__ == "__main__":
    main()
