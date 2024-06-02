"""
This module contains Exception handling.
"""
 
 
class ImageReferenceNotFoundError(Exception):
    """Class for ImageReferenceNotFoundError."""
 
    def __init__(
        self,
        description: str = "Image Name not found in the Database",
    ) -> None:
        """Init constructor for ImageReferenceNotFoundError"""
        self.description = description
 
 
class IDReferenceNotFoundError(Exception):
    """Class for IDReferenceNotFoundError."""
 
    def __init__(
        self,
        description: str = "Circular Object ID is not found",
    ) -> None:
        """Init constructor for IDReferenceNotFoundError"""
        self.description = description