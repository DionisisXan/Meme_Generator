"""A module with a DocxIngestor class for parsing quotes from DOCX files."""


import docx
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    """A class to handle DOCX file ingestion."""

    supported_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the DOCX file and return a list of QuoteModel objects.

        :param path: The path to the DOCX file
        :return: A list of QuoteModel objects containing the quote body
                 and author
        """
        quotes = []
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text:
                body, author = paragraph.text.strip().split(' - ')
                quotes.append(QuoteModel(body, author))
        return quotes
