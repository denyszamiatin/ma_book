"""Module for custom functions"""


def hash_tag_validation(tag):
    """hash tag validation"""
    if tag.startswith('#') and len(tag) >= 2 and tag.count("#") == 1:
        return True
    return False
