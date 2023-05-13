"""
A module providing the Ingestor class.

The Ingestor class encapsulates all supported file ingestors and provides a
unified interface for parsing quotes.
"""

from typing import List
from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface
from .text_ingestor import TextIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .csv_ingestor import CSVIngestor


class Ingestor(IngestorInterface):
    """A class encapsulating all supported file ingestors."""

    ingestors = [TextIngestor, DocxIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a file and return a list of QuoteModel objects.

        This method delegates parsing to the appropriate file ingestor based
        on the file extension.

        :param path: The path to the file
        :return: A list of QuoteModel objects,
                 containing the quote body and author
        :raises ValueError: If the file type is not supported
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f'Unsupported file type: {path}')
