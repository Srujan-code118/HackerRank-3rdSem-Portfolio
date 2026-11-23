from datetime import datetime

def timeConversion(s):
    return datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")
