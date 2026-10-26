import datetime
from collections import defaultdict
from typing import List, Dict

class Commit:
    """
    Represents a single Git commit with parsed details.
    """
    def __init__(self, commit_hash: str, author: str, date_str: str, subject: str, body: str):
        self.commit_hash = commit_hash
        self.author = author
        self.date_str = date_