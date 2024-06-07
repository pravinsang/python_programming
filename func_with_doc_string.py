def calculate_area_of_circle(radius):
    """
    Calculate the area of a circle given its radius.
    The area of a circle is calculated using the formula:
        area = π * radius^2
    where π (pi) is approximately 3.14159.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.

    Examples:
    >>> calculate_area_of_circle(5)
    78.53975

    >>> calculate_area_of_circle(0)
    0.0
    """
    pi = 3.14159
    area = pi * (radius ** 2)
    return area


#print(calculate_area_of_circle(5.0))   
##print(calculate_area_of_circle(3)) 
print(calculate_area_of_circle.__doc__)

