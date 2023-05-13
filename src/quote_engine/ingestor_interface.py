"""
A module providing the IngestorInterface abstract base class.

The IngestorInterface abstract class defines the interface for file ingestors.
"""

from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """An abstract base class for file ingestors."""

    supported_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file extension is supported by the ingestor.

        :param path: The path to the file
        :return: True if the file extension is supported, False otherwise
        """
        ext = path.split('.')[-1]
        return ext in cls.supported_extensions

    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a file and return a list of QuoteModel objects.

        This abstract method must be implemented by subclasses.

        :param path: The path to the file
        :return: A list of QuoteModel objects containing
                 the quote body and author
        """
        pass
