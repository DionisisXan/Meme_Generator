# Meme Generator

## Overview

The Meme Generator is a Python-based application designed to create customized meme images with captions using a collection of quotes and images. This generator can import quotes from various file formats, such as `.txt`, `.csv`, `.pdf`, and `.docx`. It combines a randomly selected quote with a user-provided or randomly chosen image to create a meme with an overlaid caption. The application shows the power of Python libraries and CLI utilities to process and manipulate text and images.

The project is organized into modular components for easy understanding and maintainability. It demonstrates the use of object-oriented programming principles, such as inheritance and abstract base classes, as well as effective error handling and Python best practices.


## Setup and Installation

To set up and run the Meme Generator, follow these steps:

1. Download the project files.

2. Make sure you have Python 3.6 or higher installed. You can check your Python version with the following command:
    ```
    python --version
    ```
    Please make sure that you have downloaded the Xpdf command line tools:xpdf-tools-win-4.04.zip and then unzip it and copy to the project folder (you need to add the path to the environment variables, for pdftotext executable file).


3. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate  # For Windows
    ```

4. Install the required dependencies using the `requirements.txt` file:
    ```
    pip install -r requirements.txt
    ```

## Running the Program

You can run the Meme Generator using the following command: python3 app.py


Then, open your web browser and visit `http://127.0.0.1:5000/` to use the web-based Meme Generator interface.

Also, you can run the program from the command line using the following command:

    ```
    python3 meme.py

    ```
 Note that the full command (including the optional arguments): 

python3 meme.py --body "Your quote body" --author "Quote Author" --path "/path/to/image.jpg"

The script returns a path to a generated image. 

If any argument is not defined, a random selection is used.

The `--body`, `--author`, and `--path` arguments are optional. If not provided, the program will randomly select a quote and image to generate the meme.

Please note that you can add sample images to \src\images folder. You can use them for testing the program. 

## Modules Overview

- `quote_engine`: This module contains the classes responsible for ingesting and parsing different file formats (txt, docx, pdf, csv) containing quotes. It uses the strategy object design pattern and defines an abstract base class `IngestorInterface` that other specific ingestor classes inherit.

- `meme_generator`: This module contains the `MemeGenerator` class that uses the Pillow library to generate memes by adding captions to images. It includes functions for resizing images, adding captions, and saving the resulting meme images to a specified output directory.

For more details on each module and their dependencies, please refer to the comments and documentation within each module's source code.

1. `MemeGenerator` - Responsible for generating meme images with captions. It uses the Pillow library to perform basic image operations like resizing and adding text. This module is located in the `meme_generator.py` file.

2. `QuoteModel` - Defines a simple data structure to hold quotes consisting of a body and author. This class can be found in the `quote_model.py` file.

3. `IngestorInterface` - An abstract base class that provides a blueprint for various file ingestors. The interface is defined in the `ingestor_interface.py` file.

4. `TextIngestor`, `CSVIngestor`, `PDFIngestor`, and `DocxIngestor` - These classes inherit from `IngestorInterface` and implement methods for ingesting quotes from different file formats. They can be found in the corresponding `.py` files (e.g., `text_ingestor.py`).

5. `Ingestor` - The main ingestor class that encapsulates all the file ingestors and provides a single interface for loading quotes from any supported file type. It is implemented in the `ingestor.py` file.

### Dependencies

- Pillow - for image manipulation
- pandas - for reading CSV files
- python-docx - for reading DOCX files
- pdftotext (CLI utility) - for extracting text from PDF files
- requests - for downloading images from a URL
- Flask - for running the web app
- typing - for type hints
- argparse - for parsing command line arguments

Please check requirements.txt for more details.





