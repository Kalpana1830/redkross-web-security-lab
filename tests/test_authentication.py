
from werkzeug.security import generate_password_hash, check_password_hash


def test_password_is_stored_as_hash():
    password = "Example-Password-123!"
    stored_password = generate_password_hash(password)

    assert stored_password != password
    assert check_password_hash(stored_password, password)


def test_wrong_password_is_rejected():
    stored_password = generate_password_hash("Correct-Password-123!")

    assert not check_password_hash(
        stored_password, "Wrong-Password-123!"
    )
