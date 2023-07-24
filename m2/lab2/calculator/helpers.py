def is_a_number(token):
    """
    Check if a token is a number, integer or float.

    args:
        - token: the token to check

    returns:
        - True if the token is a number, False otherwise
    """

    try:
        float(token)
        return True
    except ValueError:
        return False


def is_unary_operator(token):
    """
    Check if a token is a unary operator.

    args:
        - token: the token to check

    returns:
        - True if the token is a unary operator, False otherwise
    """

    return token in ['sin', 'cos', 'tan', 'ln']


def is_binary_operator(token):
    """
    Check if a token is a binary operator.

    args:
        - token: the token to check

    returns:
        - True if the token is a binary operator, False otherwise
    """

    return token in ['+', '-', '*', '/']
