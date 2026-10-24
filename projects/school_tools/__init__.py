"""Example package for the packages lesson.

Re-export make_greeting so callers can import it directly from school_tools.
"""

from .greetings import make_greeting

__all__ = ["make_greeting"]
