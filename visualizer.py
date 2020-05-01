from matplotlib import pyplot as plt
from math import log2

plt.style.use('ggplot')

def plot_results(results, title, filname=None):
    X = list(results['n'])

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.set_title("Randomly Ordered Keys")
    ax2.set_title("Sorted Keys")

    ax1.set_xlabel("Input Size (n)")
    ax2.set_xlabel("Input Size (n)")

    ax1.set_ylabel("Time (s)")
    ax2.set_ylabel("Time (s)")

    for operation in results['datatype']['Sorted Data']:
        Y = results['datatype']['Sorted Data'][operation]
        ax1.plot(X, Y, label=operation, alpha=0.7)

    for operation in results['datatype']['Random Data']:
        Y = results['datatype']['Random Data'][operation]
        ax2.plot(X, Y, label=operation, alpha=0.7)

    #ax1.plot(X, [x for x in range(len(X))], label="Linear")

    ax1.legend()
    ax2.legend()

    fig.tight_layout()
    fig.canvas.set_window_title(title)
    plt.suptitle(title)

def show():
    plt.show()