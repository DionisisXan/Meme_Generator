"""
A module for ingesting PDF files and creating QuoteModel instances.

This module contains the PDFIngestor class.

The class is responsible for parsing quotes from PDF files.
"""

import subprocess
import os
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    """A class to handle PDF file ingestion."""

    supported_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the PDF file and return a list of QuoteModel objects.

        :param path: The path to the PDF file
        :return: A list of QuoteModel obj containing the quote body and author
        """
        temp_txt_file = f'{path}.txt'
        subprocess.run(['pdftotext', path, temp_txt_file])

        quotes = []
        with open(temp_txt_file, 'r') as file:
            for line in file.readlines():
                if line.strip():
                    parts = line.strip().split(' - ')
                    body = ' - '.join(parts[:-1])
                    author = parts[-1]

                    quotes.append(QuoteModel(body, author))
        os.remove(temp_txt_file)
        return quotes
