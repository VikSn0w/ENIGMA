import hashlib
import datetime
import secrets

def get_sha256(input_str):
    result = hashlib.sha256(input_str.encode())
    return result.hexdigest()

def Enigma(mult, div, fix, salt):

    now = datetime.datetime.today()
    day_of_year = now.timetuple().tm_yday

    base_token_str = f"{now.year:04d}{now.month:02d}{now.day:02d}{day_of_year:03d}"

    try:
        base_int = int(base_token_str)
    except ValueError:
        raise ValueError("Error converting base token string to integer.")

    modified_value = ((base_int + fix) * mult) // div

    final_input = f"{modified_value}{salt}"

    return get_sha256(final_input)

if __name__ == '__main__':
    secret_salt = secrets.token_hex(16)

    token = Enigma(10, 20, 30, secret_salt)
    print("Generated Token:", token)
