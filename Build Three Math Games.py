# Scatter Plot Game
def spgame():
    import matplotlib.pyplot as plt

    score = 0

    xmin = -100
    xmax = 100
    ymin = -100
    ymax = 100

    fig, ax = plt.subplots()

    for i in range(0, 3):
        xpoint = int(input("Enter the coordinates of X: "))
        ypoint = int(input("Enter the coordinates of Y: "))
        x = [xpoint]
        y = [ypoint]
        plt.axis([xmin, xmax, ymin, ymax])  # window size
        plt.plot([xmin, xmax], [0, 0], 'b')  # blue x axis
        plt.plot([0, 0], [ymin, ymax], 'b')  # blue y axis
        plt.plot(x, y, 'ro')
        print(" ")
        plt.grid()  # displays grid lines on graph
        plt.show()
        guess = input("Enter the coordinates of the red point point: \n")
        guess_array = guess.split(",")
        xguess = int(guess_array[0])
        yguess = int(guess_array[1])
        if xguess == xpoint and yguess == ypoint:
            score = score + 1

    print("Your score: ", score)  # notice this is not in the loop

# Algebric Practice Game
# converts string input (even fractions) to float
def string_frac(in_string):
    if "/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n/d
        return ans
    else:
        ans = float(in_string)
        return ans
# Simplest one-step addition
def one_step_add():
    import random
    # Display problem
    a = random.randint(-4,10)
    b = random.randint(2,24)
    print("x + ", a, " = ", b)
    ans = float(input("x = "))
    answer = b-a
    # Test input
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")
# One-step additon with negaive numbers
def one_step_subtract():
    import random
    a = random.randint(-19,-1)
    b = random.randint(2,24)
    print(a, " + x = ", b)
    ans = float(input("x = "))
    # test
    answer = b-a
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")
# One-step multiply
def one_step_mult():
    # Uses string_frac(<input string>)
    import random
    a = random.randint(1,11)
    b = random.randint(2,24)
    print(a, "x = ", b)
    ans_in = (input("x = "))
    answer = b/a
    # test
    if string_frac(ans_in)==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")
# One-step divide
def one_step_div():
    import random
    a = random.randint(1,11)
    b = random.randint(2,24)
    print("x/", a, " = ", b)
    ans = float(input("x = "))
    answer = b*a
    # test
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")
# Two-step problems
def two_step():
    import random
    # Uses string_frac()
    a = random.randint(1,11)
    b = random.randint(-7,12)
    c = random.randint(2,36)
    print(a, "x + ", b, " = ", c)
    print("Round answer to two decimal places")
    ans_in = input("x = ")
    answer = (c-b)/a
    # test
    if round(string_frac(ans_in),2)==round(answer,2):
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")
def algebric():
  # test loop
  for a in range(2):
      one_step_add()
      one_step_subtract()
      one_step_mult()
      one_step_div()
      two_step()
      print(" ")

# Projectile Game
from ipywidgets import interactive


def projectile():
    import matplotlib.pyplot as plt
    import numpy as np

    # Set up the game parameters
    wall_height = np.random.randint(5, 15)  # Random wall height between 5 and 15 meters
    wall_distance = np.random.randint(20, 30)  # Random wall distance between 20 and 30 meters
    threshold_height = np.random.randint(wall_height + 1, 20)  # Random threshold height above the wall
    print("Wall height:", wall_height)
    print("Wall distance:", wall_distance)
    print("Threshold height:", threshold_height)

    # Set up the physics parameters
    g = 9.81  # Acceleration due to gravity (m/s^2)
    t = np.linspace(0, 10, 1000)  # Time array (s)

    # Try different initial velocities to clear the wall
    for v0 in range(20, 101, 5):  # Initial velocity range between 20 and 100 m/s
        v0x = v0  # Assume no air resistance, so v0x = v0
        v0y = v0 * np.sin(np.deg2rad(45))  # Launch angle of 45 degrees
        x = v0x * t
        y = v0y * t - 0.5 * g * t ** 2
        # Check if the rocket clears the wall
        if np.any(y > wall_height) and np.max(x[y > wall_height]) > wall_distance:
            print("Initial velocity:", v0)
            # Plot the rocket path
            plt.plot(x, y, label=f"v0={v0} m/s")
            break

    # Plot the wall
    plt.plot([0, wall_distance], [0, 0], 'k-', linewidth=2)
    plt.plot([wall_distance, wall_distance], [0, wall_height], 'k-', linewidth=2)
    plt.plot([wall_distance, wall_distance + 5], [wall_height, wall_height], 'k-', linewidth=2)
    # Plot the threshold height
    plt.plot([0, wall_distance + 5], [threshold_height, threshold_height], 'r--', linewidth=2)
    plt.text(wall_distance + 5, threshold_height, f"{threshold_height} m", fontsize=12)
    plt.legend()
    plt.xlabel("Horizontal distance (m)")
    plt.ylabel("Vertical distance (m)")
    plt.title("Projectile game")
    plt.show()
    interactive_plot = interactive(projectile, wall_distance=(-9, 9), wall_height=(-9, 9), threshold_height=(-9, 9),
                                   zoom=(1, 100))
    interactive_plot

# loop
print("Welcome to the three math games. \n Select the opiton which game do you wanna play")
print('A for Scatter Plot Game \nB for Algebric Pratice Game \nC for Projectile Game')
qst = str(input("Which One! : "))

if qst == 'A':
  spgame()
elif qst == 'B':
  algebric()
elif qst == "C":
  projectile()
else:
  print("Use BIG Alphabets Like 'A' 'B' 'C' ")