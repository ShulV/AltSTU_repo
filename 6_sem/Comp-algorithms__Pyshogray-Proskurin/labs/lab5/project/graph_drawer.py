import matplotlib.pyplot as plt


def draw_graphs(x_lists, y_lists):
    for x_list, y_list in zip(x_lists, y_lists):
        plt.plot(x_list, y_list)
    plt.show()
