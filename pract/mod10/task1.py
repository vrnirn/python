import re
import doctest


def check_password(password):
    """
    Эта функция проверяет, является ли входная строка допустимым паролем в соответствии с данными ограничениями.

    Args:
    password (str): Строка, представляющая собой пароль.

    Returns:
    bool: True если входная строка является допустимым паролем, False в противном случае.
    
    >>> check_password('rtG&3FG#Tr^e')
    True
    >>> check_password('a^A1@*@1Aa')
    True
    >>> check_password('oF^a1D@y5%e6')
    True
    >>> check_password('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    >>> check_password('пароль')
    False
    >>> check_password('password')
    False
    >>> check_password('qwerty')
    False
    >>> check_password('lOngPa$$W0Rd')
    False
    """
    # Проверка наличия только латинских символов, цифр и специальных символов
    if not re.match(r'^[a-zA-Z0-9^$%@#&*]+$', password):
        return False
    
    # Проверка длины пароля (пароль должен состоять из не менее чем восьми символов)
    if len(password) < 8:
        return False
    
    # Проверка наличия по крайней мере двух латинских символов в нижнем регистре
    if len(re.findall(r'[a-z]', password)) < 2:
        return False
    
    # Проверка наличия по крайней мере одной цифры
    if not re.search(r'\d', password):
        return False
    
    # Проверка наличия по крайней мере трех различных специальных символов ^$%@#&*
    if len(set(re.findall(r'[\^$%@#&*]', password))) < 3:
        return False
    
    # Проверка отсутствия символов ,.!?
    if re.search(r'[,\.\!\?]', password):
        return False
    
    return True

doctest.testmod(verbose=True)