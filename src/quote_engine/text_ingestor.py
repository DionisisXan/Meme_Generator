"""
A module containing the TextIngestor class definition.

The TextIngestor class is responsible for ingesting plain text files and
producing a list of QuoteModel objects.
"""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    """A class to handle plain text file ingestion."""

    supported_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the plain text file and return a list of QuoteModel objects.

        :param path: The path to the plain text file
        :return: A list of QuoteModel objs containing the quote body and author
        """
        quotes = []
        with open(path, 'r') as file:
            for line in file.readlines():
                if ' - ' in line:
                  body, author = line.strip().split(' - ')
                else:
                # Skip the line without any warning message
                    continue
                quotes.append(QuoteModel(body, author))
        return quotes
