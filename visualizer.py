from matplotlib import pyplot as plt
from math import log2

plt.style.use('ggplot')

def plot_results(results, title, filname=None):
    X = list(results['n'])

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.set_title("Time Complexity")
    ax2.set_title("Time")

    ax1.set_xlabel("List Size")
    ax2.set_xlabel("List Size")

    ax1.set_ylabel("N(Ops)")
    ax2.set_ylabel("Time(s)")

    for name in results['algorithms']:
        Y_n_ops = results['algorithms'][name]['n_ops']
        Y_time = results['algorithms'][name]['time']

        ax1.plot(X, Y_n_ops, label=name, alpha=0.7)
        ax2.plot(X, Y_time, label=name, alpha=0.7)

        ax1.legend()
        ax2.legend()

    fig.tight_layout()
    fig.canvas.set_window_title(title)
    plt.suptitle(title)

def show():
    plt.show()