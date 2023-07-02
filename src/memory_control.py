import sys

from psutil import virtual_memory

from .view import memory_saturation


def memory_control():
    """check if there is more than 20% of memory available
    if not the script will be stopped"""

    if virtual_memory().percent > 80:
        memory_saturation()
        sys.exit()
