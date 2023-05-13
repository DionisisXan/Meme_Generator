"""
A Module containing the QuoteModel class definition.

The QuoteModel class represents a quote, including the quote's body and author.
"""


class QuoteModel:
    """A class representing a quote, including the quote's body and author."""

    def __init__(self, body, author):
        """
        Create a new QuoteModel object.

        :param body: The text of the quote
        :param author: The author of the quote
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """
        Return a string representation of the QuoteModel object.

        :return: A string containing the quote body and author
        """
        return f'"{self.body}" - {self.author}'
