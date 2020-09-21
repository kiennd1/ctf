def check_sqli(str):
    substrings = ['sle', 'hex']
    for substring in substrings:
        if substring in str:
            return True
    return False
