# Display the graph and a table of values for any "y=" equation input
def eq():
    import matplotlib.pyplot as plt
    import numpy as np
    # Prompt the user for input
    function_str = input("Enter function(s) to graph, separated by commas: ")

    # Split the input string into separate function strings
    function_list = function_str.split(',')
    # Define the axis limits
    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10

    # Define the points
    points = 10 * (xmax - xmin)

    # Define the x array
    x = np.linspace(xmin, xmax, points)

    # Create the plot
    fig, ax = plt.subplots()
    plt.axis([xmin, xmax, ymin, ymax])
    plt.plot([xmin, xmax], [0, 0], 'r')
    plt.plot([0, 0], [ymin, ymax], 'r')
    # Plot each function
    for function in function_list:
        y = eval(function)
        plt.plot(x, y, label=function)
        # Add a legend and show the plot
        plt.legend()
        plt.show()

# Solve a system of two equations without graphing
from sympy import *

def eq1():
  x, y = symbols('x y')
  first = input("Enter the Equation: ")
  second = input("Enter the Equation: ")

  # parse finite set answer as coordinate pair
  solution = linsolve([first, second], (x, y))
  x_solution = solution.args[0][0]
  y_solution = solution.args[0][1]

  print('(', x_solution, ',', y_solution, ')')

# Graph two equations and plot the point of intersection
from sympy import *
import matplotlib.pyplot as plt
import numpy as np


def eq2():
    print("First equation: y = mx + b")
    mb_1 = input("Enter m and b, separated by a comma: ")
    mb_in1 = mb_1.split(",")
    m1 = float(mb_in1[0])
    b1 = float(mb_in1[1])
    print("Second equation: y = mx + b")
    mb_2 = input("Enter m and b, separated by a comma: ")
    mb_in2 = mb_2.split(",")
    m2 = float(mb_in2[0])
    b2 = float(mb_in2[1])

    # Solve the system of equations
    x, y = symbols('x y')
    first = m1 * x + b1 - y
    second = m2 * x + b2 - y
    solution = linsolve([first, second], (x, y))
    x_solution = round(float(solution.args[0][0]), 3)
    y_solution = round(float(solution.args[0][1]), 3)

    # Make sure the window includes the solution
    xmin = int(x_solution) - 20
    xmax = int(x_solution) + 20
    ymin = int(y_solution) - 20
    ymax = int(y_solution) + 20
    points = 2 * (xmax - xmin)

    # Define the x values once for the graph
    graph_x = np.linspace(xmin, xmax, points)

    # Define the y values for the graph
    y1 = m1 * graph_x + b1
    y2 = m2 * graph_x + b2

    fig, ax = plt.subplots()
    plt.axis([xmin, xmax, ymin, ymax])  # window size
    plt.plot([xmin, xmax], [0, 0], 'b')  # blue x axis
    plt.plot([0, 0], [ymin, ymax], 'b')  # blue y axis

    # line 1
    plt.plot(graph_x, y1)

    # line 2
    plt.plot(graph_x, y2)

    # point
    plt.plot([x_solution], [y_solution], 'ro')

    plt.show()
    print(" ")
    print("Solution: (", x_solution, ",", y_solution, ")")

# Given a, b and c in a quadratic equation, plot the roots and vertex
import matplotlib.pyplot as plt
import numpy as np


def eq3():
    a = float(input("Enter the coefficient of x^2: "))
    b = float(input("Enter the coefficient of x: "))
    c = float(input("Enter the constant term: "))

    # Calculate the roots
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("No real roots")
    else:
        x1 = (-b + np.sqrt(delta)) / (2 * a)
        x2 = (-b - np.sqrt(delta)) / (2 * a)
        print("Roots: x1 = {:.2f}, x2 = {:.2f}".format(x1, x2))

        # Calculate the vertex
        vertex_x = -b / (2 * a)
        vertex_y = a * vertex_x ** 2 + b * vertex_x + c
        print("Vertex: ({:.2f}, {:.2f})".format(vertex_x, vertex_y))

        # Plot the quadratic function
        x = np.linspace(-10, 10, 100)
        y = a * x ** 2 + b * x + c
        plt.plot(x, y)

        # Plot the roots and vertex
        plt.plot([x1, x2], [0, 0], 'ro', label='Roots')
        plt.plot(vertex_x, vertex_y, 'go', label='Vertex')
        plt.legend()
        plt.show()

# loop
qst = int(input("Press number from 0 to 3: "))

if qst == 0:
  eq()
elif qst == 1:
  eq1()
elif qst == 2:
  eq2()
elif qst == 3:
  eq3()
else:
  print("select the accurate number")