import matplotlib.pyplot as plt

def draw_graphs(x_list, y_list, lagrange_y_list, label):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(title='График функции ' + label,
           xlabel='X',
           ylabel='Y')
    ax.plot(x_list, y_list, color='black')
    ax.plot(x_list, lagrange_y_list, color='red')
    plt.show()
