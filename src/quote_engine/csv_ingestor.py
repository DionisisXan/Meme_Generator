"""
A module for ingesting CSV files and creating QuoteModel instances.

This module contains the CSVIngestor class.

This class is responsible for parsing quotes from CSV files.
"""

import pandas as pd
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """A class to handle CSV file ingestion."""

    supported_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the CSV file and return a list of QuoteModel objects.

        :param path: The path to the CSV file
        :return: A list of QuoteModel objects with the quote body and author
        """
        quotes = []
        data = pd.read_csv(path)

        for _, row in data.iterrows():
            quotes.append(QuoteModel(row['body'], row['author']))

        return quotes
