import hashlib
import datetime

def get_sha256(input_str):
    result = hashlib.sha256(input_str.encode())
    return result.hexdigest()


def compute_token(mult, div, fix, mode, interval_minutes, custom_datetime=None):

    if custom_datetime is None:
        now = datetime.datetime.utcnow()
    else:
        now = custom_datetime

    minutes_since_midnight = now.hour * 60 + now.minute
    interval_number = minutes_since_midnight // interval_minutes

    base_token_str = f"{now.year:04d}{now.month:02d}{now.day:02d}{interval_number:04d}"
    base_int = int(base_token_str)
    modified_value = ((base_int + fix) * mult) // div
    final_input = str(modified_value)

    match mode:
        case '1':
            return get_sha256(final_input)
        case _:
            raise ValueError("Unsupported mode.")


def validate_token(received_token, mult, div, fix, mode='1', interval_minutes=5, allowed_skew=1):

    now = datetime.datetime.utcnow()

    for skew in range(-allowed_skew, allowed_skew + 1):
        check_time = now + datetime.timedelta(minutes=skew * interval_minutes)
        expected_token = compute_token(mult, div, fix, mode, interval_minutes, custom_datetime=check_time)
        if received_token == expected_token:
            return True

    return False


if __name__ == '__main__':
    station_token = compute_token(10, 20, 30, '1', interval_minutes=5)

    is_valid = validate_token(
        received_token=station_token,
        mult=10,
        div=20,
        fix=30,
        mode='1',
        interval_minutes=5,
        allowed_skew=1  # Allow previous/next interval to be accepted
    )

    print("Token is valid:", is_valid)
