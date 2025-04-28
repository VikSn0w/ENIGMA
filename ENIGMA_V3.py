import hashlib
import datetime

def get_sha256(input_str):
    result = hashlib.sha256(input_str.encode())
    return result.hexdigest()


def Enigma(mult, div, fix, interval_minutes=5):
    now = datetime.datetime.utcnow()

    minutes_since_midnight = now.hour * 60 + now.minute
    interval_number = minutes_since_midnight // interval_minutes

    base_token_str = f"{now.year:04d}{now.month:02d}{now.day:02d}{interval_number:04d}"

    base_int = int(base_token_str)
    modified_value = ((base_int + fix) * mult) // div

    final_input = str(modified_value)

    return get_sha256(final_input)


if __name__ == '__main__':
    token = Enigma(10, 20, 30, interval_minutes=5)
    print("Generated Token:", token)
