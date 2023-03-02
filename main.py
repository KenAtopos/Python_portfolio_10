import requests
import io
import PyPDF2
from google.cloud import texttospeech
import os

# Replace with your own Google Cloud API key
api_key = os.environ.get("API_KEY")

# Open the PDF file in read binary mode
with open('file.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Create a text buffer to store the extracted text
    text_buffer = io.StringIO()

    # Loop through all the pages and extract the text
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text_buffer.write(page.extractText())

    # Get the extracted text as a string
    text = text_buffer.getvalue()

    # Initialize the Text-to-Speech client with the API key
    client = texttospeech.TextToSpeechClient.from_service_account_file(api_key)

    # Set the voice configuration
    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)

    # Set the audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3)

    # Call the Text-to-Speech API to generate speech
    synthesis_input = texttospeech.SynthesisInput(text=text)
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config)

    # Save the generated audio to a file
    with open('output.mp3', 'wb') as audio_file:
        audio_file.write(response.audio_content)

    # Send a request to play the generated audio
    requests.get('https://translate.google.com/translate_tts?ie=UTF-8&q=' + text + '&tl=en&client=tw-ob')

