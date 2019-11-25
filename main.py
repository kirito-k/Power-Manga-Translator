# Import required dependencies
from google.cloud import translate_v2 as translate
from google.cloud import vision
import asyncio

def translateText(pageText, targetLang='en'):
    # Instantiates a client
    translate_client = translate.Client()

    for text in pageText:
        translation = translate_client.translate(text, target_language=targetLang)
        print(f"{text} \t=\t {translation['translatedText']}")


def detectImageText(url):
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
    print(pageText)
    translateText(pageText.split("\n"))


def main():
    path = input("Enter the path / URL to of the image to be translated.\n")
    ## Example
    # path = ("https://xy-101-j.mangapark.net/33/67/5d79ffce55f2a65b7d667633/15_337703_896_1300.jpeg")
    
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(detectImageText(path))
    except e:
        print(e)

if __name__ == "__main__":
    main()