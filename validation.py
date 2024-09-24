import re


def only_real_numbs(e):
    """
    Mediante expreciones regulares compruebo que solo se escriba un numero real.
    """

    value: str = e.control.value

    if len(value) > 0:
        if value[len(value) - 1] != '.':
            if not re.match( r'^\d+(\.\d+)?$', value):
                e.control.value = value[:-1]
        else:
            if re.match(r'^\d+(\.(\d+)?)\.$', value):
                e.control.value = value[:-1]

    e.control.update()