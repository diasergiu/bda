from PIL import Image
import urllib.request
import multiprocessing as mp
import time

image_urls = [
    "https://picsum.photos/id/10/300/200",
    "https://picsum.photos/id/20/300/200",
    "https://picsum.photos/id/30/300/200",
    "https://picsum.photos/id/40/300/200",
    "https://picsum.photos/id/50/300/200",
    "https://picsum.photos/id/60/300/200",
    "https://picsum.photos/id/70/300/200",
    "https://picsum.photos/id/80/300/200",
    "https://picsum.photos/id/90/300/200",
    "https://picsum.photos/id/100/300/200",
]

def rotate_image(url):
    # Download a free sample image
    # url = "https://picsum.photos/300/200"
    nameFile = url.split("/", 1)[-1] + ".jpg"
    urllib.request.urlretrieve(url, nameFile)

    # Open the image
    image = Image.open(nameFile)

    # Rotate it 90 degrees
    rotated_image = image.rotate(90, expand=True)

    # Save the new image
    rotated_image.save("rotated_" + nameFile)

    print(f"Image rotated and saved as rotated_{nameFile}")

def rotate_image_in_parallel():
    start = time.perf_counter()
    with mp.Pool() as pool:
        pool.map(rotate_image, image_urls )
    end = time.perf_counter()
    print(f"Parallel rotation time: {end - start:.2f}s")

def rotate_image_cuncurently():
    start = time.perf_counter()
    for url in image_urls:
        rotate_image(url)
    end = time.perf_counter()
    print(f"Serial rotation time: {end - start:.2f}s")

if __name__ == "__main__":
    rotate_image_cuncurently()
    rotate_image_in_parallel()
    