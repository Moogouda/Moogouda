"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the remaining bake time.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Calculate preparation time based on number of layers.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - preparation time (in minutes).
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed cooking time.

    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - time already spent baking.
    :return: int - total time elapsed (in minutes).
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time
