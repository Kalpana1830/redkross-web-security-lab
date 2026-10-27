
from database import create_database, find_user


def test_existing_user_is_found():
    connection = create_database()
    try:
        results = find_user(connection, "alice")
        assert len(results) == 1
        assert results[0][1] == "alice"
    finally:
        connection.close()


def test_unknown_user_is_not_found():
    connection = create_database()
    try:
        results = find_user(connection, "charlie")
        assert results == []
    finally:
        connection.close()


def test_sql_injection_input_does_not_return_all_users():
    connection = create_database()
    try:
        payload = "' OR '1'='1"
        results = find_user(connection, payload)
        assert results == []
    finally:
        connection.close()
