import math
import sys

"""
Notes:
- Very good attempt! 
- Using git gives us the freedom to keep the code clean and remove dangling comments.
- The real challenge in programming is providing an easy to use interface (UI). How can you improve yours?
"""


def calculate_velocity_eqn1(initial_vel, accel, time):
    # todo: add a docstring; see class notes on how to do this
    velocity = float(initial_vel + accel * time)
    return velocity


def calculate_velocity_eqn2(initial_vel, accel, initial_position, final_position):
    # todo: add a docstring; see class notes on how to do this
    velocity = float(math.sqrt(pow(initial_vel, 2) + (2 * accel * (final_position - initial_position))))
    return velocity


def calculate_position_eqn3(initial_position, initial_vel, time, accel):
    # todo: add a docstring; see class notes on how to do this
    position = initial_position + initial_vel * time + (accel * time ** 2) / 2
    return position


def calculate_position_eqn4(initial_position, fin_vel, initial_vel, time):
    # todo: add a docstring; see class notes on how to do this
    position = initial_position + ((fin_vel + initial_vel) * time) / 2
    return position


def calculate_position_eqn5(initial_position, fin_vel, time, accel):
    # todo: add a docstring; see class notes on how to do this
    position = initial_position + fin_vel * time - (accel * time ** 2) / 2
    return position


def main():
    vel_particle1 = calculate_velocity_eqn1(23, 9, 10)
    print(f"Final velocity of particle1: {vel_particle1}")
    vel_particle2 = calculate_velocity_eqn2(50, 2, 15, 100)
    print(f"Final velocity of particle2: {vel_particle2}\n")
    num_of_variables = 0
    while True:
        try:
            num_of_variables = int(input("Enter the number of variables you have: "))
        except ValueError as ve:
            print(f"wrong value {ve}")
        if num_of_variables <= 6:
            break
    x = 0
    user_selection = []
    print("Key:")
    print("Final velocity - 1")
    print("Initial velocity - 2")
    print("Acceleration - 3")
    print("Time interval - 4")
    print("Initial position - 5")
    print("Final position - 6")
    while x < num_of_variables:
        user_variables = int(input("Enter the number for the variables you have: "))
        user_selection.append(user_variables)
        x += 1
    # fixme: consider using keys that convey meaning e.g. 'r0' for initial position
    #   instead of '5'
    variables = {1: 'final velocity', 2: 'Initial velocity', 3: 'Acceleration', 4: 'Time interval',
                 5: 'Initial position', 6: 'Final position'}
    values_list = []
    for key, value in variables.items():
        for items in user_selection:
            if items == key:
                print(f"{value}", end=":")
                value_of_variable = float(input('enter value:'))
                values_list.append(value_of_variable)
    my_dict = dict(zip(user_selection, values_list))
    if 2 in my_dict and 3 in my_dict and 4 in my_dict:
        final_velocity = calculate_velocity_eqn1(my_dict.get(2), my_dict.get(3), my_dict.get(4))
        print(f"Final velocity, v: {final_velocity}")
    elif 2 in my_dict and 3 in my_dict and 5 in my_dict and 6 in my_dict:
        final_velocity = calculate_velocity_eqn2(my_dict.get(2), my_dict.get(3), my_dict.get(5), my_dict.get(6))
        print(f"Final velocity, v: {final_velocity}")
    elif 2 in my_dict and 3 in my_dict and 4 in my_dict and 5 in my_dict:
        final_position = calculate_position_eqn3(my_dict.get(5), my_dict.get(2), my_dict.get(4), my_dict.get(3))
        print(f"Final position, r: {final_position}")
    elif 1 in my_dict and 2 in my_dict and 4 in my_dict and 5 in my_dict:
        final_position = calculate_position_eqn4(my_dict.get(5), my_dict.get(1), my_dict.get(2), my_dict.get(4))
        print(f"Final position, r: {final_position}")
    elif 1 in my_dict and 3 in my_dict and 4 in my_dict and 5 in my_dict:
        final_position = calculate_position_eqn5(my_dict.get(5), my_dict.get(1), my_dict.get(4), my_dict.get(3))
        print(f"Final position, r: {final_position}")
    else:
        print('error')


if __name__ == "__main__":
    sys.exit(main())
