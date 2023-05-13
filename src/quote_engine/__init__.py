"""
A package for ingesting quote data from various file formats.

Also creating QuoteModel instances.

The package includes classes for ingesting text.

For example CSV, PDF, DOCX file formats as well as a unified Ingestor class.
"""

from .ingestor import Ingestor, QuoteModel
