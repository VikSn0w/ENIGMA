import hashlib
import datetime

def getMd5(input):
    result = hashlib.md5(input.encode())
    return result.hexdigest()

def Enigma(mult, div, fix):
    date = datetime.datetime.today()
    day_of_year = datetime.datetime.today().timetuple().tm_yday
    base_token = float(date.year + date.month + date.day + day_of_year)
    base_token = (((base_token + fix) * mult) / div)
    return getMd5(str(base_token))

if __name__ == '__main__':
    print(Enigma(10, 20, 30))