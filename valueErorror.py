def perse_percentage(text):
    if not text.endswith("%"):
        raise ValueError("must end with %")
    number = int (text[:-1])
    if number < 0 or number > 100:
        raise ValueError ("is number 1-99")
    return number
try:
    print (perse_percentage ("75%"))   
except ValueError as eroor:
    print(eroor)