def dec_to_binary(number):
    result = ''
    while number != 0:
        result = str(number %2) + result
        number = number // 2
    return result or '0'

