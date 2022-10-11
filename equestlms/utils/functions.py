def booleanize(value):
    """
    This function turns statements into booleans

    Returns:
        Boolean: True or False
    """
    returned_value = None
    if value == "on":
        returned_value = True
    elif value == "off":
        returned_value = False
    return returned_value
