class NoCopiesError(Exception):
    """Raised when a book has no available copies to borrow."""

class MaxLoansExceededError(Exception):
    """Raised when a member reached their active-loans limit."""

class AlreadyReturnedError(Exception):
    """Raised when trying to return a loan that is already returned."""
