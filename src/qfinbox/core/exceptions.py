"""Custom exceptions for qfinbox."""


class QFinBoxError(Exception):
    """Base exception for qfinbox."""

    pass


class ValidationError(QFinBoxError):
    """Raised when input validation fails."""

    pass


class DataError(QFinBoxError):
    """Raised when there are issues with data processing."""

    pass


class CalculationError(QFinBoxError):
    """Raised when mathematical calculations fail."""

    pass
