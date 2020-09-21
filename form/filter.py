def check_sqli(str):
    substrings = ['sle', 'hex', ' ']
    str = str.lower()
    for substring in substrings:
        if substring in str:
            return True
    return False

def check_path(str):
    if str.count('/') == len(str):
        return True
    substrings = ['README.md', 'ctf', 'db.sqlite3', '.gitignore', 'form', 'manage.py']
    for substring in substrings:
        if substring in str:
            return True
    return False
