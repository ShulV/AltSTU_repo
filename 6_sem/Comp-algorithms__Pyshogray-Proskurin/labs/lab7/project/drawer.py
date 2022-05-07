import matplotlib.pyplot as plt


def show_graphics_for_monte_carlo(graphic, under_points, over_points):
    """ графическое отображение испытаний методом Монте-Карло """
    fig, ax = plt.subplots()
    ax.plot(graphic['x'], graphic['y'], color='black')
    plt.scatter(over_points['x'], over_points['y'], color='red', s=10)
    plt.scatter(under_points['x'], under_points['y'], color='green', s=10)

    ax.set(xlabel='x', ylabel='f(x)',
           title='Испытания методом Монте-Карло')
    ax.grid()

    fig.savefig("test.png")
    plt.show()


def show_figure_for_finding_gravity_center(figure, gr_center_point):
    """ графическое отображение фигуры и ее центра тяжести """
    fig, ax = plt.subplots()
    ax.plot(figure['x'], figure['y'], color='black')
    plt.scatter(gr_center_point['x'], gr_center_point['y'], color='red', s=30)

    ax.set(xlabel='x', ylabel='f(x)',
           title='Нахождение центра тяжести')
    ax.grid()

    fig.savefig("test2.png")
    plt.show()
