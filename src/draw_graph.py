import matplotlib.pyplot as plt


def graph(time_capture: list, memory_capture: list):
    """draw a graph of the memory usage over time"""

    plt.plot(time_capture, memory_capture)
    plt.xlabel("Time (secs)")
    plt.ylabel("Memory usage (MB)")
    plt.title("Memory Usage Overview")
    plt.show()
