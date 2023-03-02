# PDF-to-Audiobook App
This is a Python application that converts PDF files to audiobook using the Google Cloud Text-to-Speech API. The app reads a PDF file, extracts the text from all pages, and converts the text to an MP3 audio file using the Text-to-Speech API. The generated audio file can be played back using any media player that supports MP3 format.

## Installation
Before running the app, you need to install the required Python libraries and set up your Google Cloud credentials. Here are the steps:

1. Install the `google-cloud-texttospeech` library using pip:

    ```
    pip install google-cloud-texttospeech
    ```

2. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your Google Cloud service account key file:

    ```
    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/keyfile.json
    ```
    
    Replace `/path/to/your/keyfile.json` with the actual path to your key file.

## Usage
To use the app, follow these steps:

1. Place the PDF file that you want to convert in the same directory as the pdf_to_speech.py file.

2. In the terminal, navigate to the directory containing the `pdf_to_speech.py` file.

3. Run the following command:

    ```
    python pdf_to_speech.py <pdf_filename>
    ```

    Replace `<pdf_filename>` with the actual filename of your PDF file.

4. Wait for the app to finish processing the PDF file. The generated audio file will be saved in the same directory as the `pdf_to_speech.py` file, with the name `<pdf_filename>.mp3`.

5. Play the generated audio file using any media player that supports MP3 format.

![img](./img.png)
