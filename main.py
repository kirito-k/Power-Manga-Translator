# Import required dependencies
from google.cloud import translate_v2 as translate
from google.cloud import vision
import asyncio


def translateText(pageText: str, targetLang='en'):
    # Instantiates a client for translation
    translate_client = translate.Client()

    for text in pageText:
        translation = translate_client.translate(text, target_language=targetLang)
        print(f"{text} \t=\t {translation['translatedText']}")


"""
This fuction detects all the texts inside the Image and intrinsically calls translator function when it is done
"""
def detectImageText(url: str):
    # Instantiates a client for detection
    client = vision.ImageAnnotatorClient()
    
    if url.startswith('http'):
        image = vision.types.Image()
        image.source.image_uri = url
    else:
        with opne('path', 'rb') as imageFile:
            content = imageFile.read()
        image = vision.types.Image(content=content)
        
    response = client.text_detection(image=image)
    pageText = response.text_annotations[0].description
    
    # Prints the detected text
    print(f"Detected Text in image:\n{pageText}")

    # Call to translate function
    translateText(pageText.split("\n"))


def main():
    # Get user input
    path = input("Enter the path / URL to of the image to be translated.\n")
    
    ## Example tests
    # path = ("https://xy-101-j.mangapark.net/33/67/5d79ffce55f2a65b7d667633/15_337703_896_1300.jpeg")
    
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(detectImageText(path))
    except e:
        print(e)


if __name__ == "__main__":
    main()