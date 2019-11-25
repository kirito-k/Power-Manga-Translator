### Power Translator is a powerful script which allows users to input URL or image file to the program which then detects the texts along with its language and translate it to any provided language

## Technologies Used
The program uses Google Cloud Vision(GCV) API's to detect the text from images.
It uses Google Translate API for auto detecting and converting the text in any other language(English default)

## Practical Uses
- Reading Scholarly Articles
- Reading Chinese Mangas      ..This is why I created this project :)
- Reading posters

## Pre-requisites
- Clone this repository
- Login/Register to Google Could Platform (GCP)
- Create a project on GCP
- Enable Google Vision and Google Translate APIs from API Manager
- Create and download a API key for the project and place it in root directory of this project
- Install the requirements.txt by running 
    "pip install -r requirements.txt"
- Set the environment variables for your Keys by running the following command in terminal
    export GOOGLE_APPLICATION_CREDENTIALS="[PATH TO JSON FILE CONTAINING KEYS]"
- Run the "main.py" file and provide URL / complete_path_to_image 
- Enjoy