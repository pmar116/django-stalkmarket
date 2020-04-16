import datetime

def ismorning():
    if datetime.datetime.now().hour <12:
        return True
    else:
        return False