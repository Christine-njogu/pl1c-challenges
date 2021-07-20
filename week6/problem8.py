import sys

"""
Notes:
- Excellent!
"""


def calculate_gravitational_force(mass1, mass2, center_dist, gravity_const=6.673 * pow(10, -11)):
    # todo: add a docstring; see class notes on how to do this
    force = float(gravity_const * mass1 * mass2 / (pow(center_dist, 2)))
    return force


def main():
    while True:
        try:
            mass_of_body1 = float(input("Enter the mass of body one: "))
            mass_of_body2 = float(input("Enter the mass of body two: "))
            dist_btn_centers = float(input("Enter the distance between centers of the two bodies: "))
            break
        except ValueError as ve:
            print(f"Wrong value {ve}")
    gravity_force = calculate_gravitational_force(mass_of_body1, mass_of_body2, dist_btn_centers)
    # todo: print units
    print(f"The gravitational force: {gravity_force}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
