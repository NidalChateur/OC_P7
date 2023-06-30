import sys

from psutil import virtual_memory


def memory_control():
    """check if there is more than 20% of memory available
    if not the script will be stopped"""

    if virtual_memory().percent > 80:
        print("\nSorry... there is not enough memory in your PC to continue.\n")
        sys.exit()
