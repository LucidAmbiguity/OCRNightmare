""" HELPERS """
import re

def valid_uuid(uuid:str)->bool:
    """Check that uuid is a valid uuid4 value

    Args:
        uuid (string): uuid as a string

    Returns:
        boolean: True if valid uuid4
    """
    regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}', re.I) # pylint: disable=line-too-long
    match = regex.match(uuid)
    return bool(match)
