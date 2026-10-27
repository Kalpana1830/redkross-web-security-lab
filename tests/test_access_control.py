
from flask import Flask, abort, request


def create_access_test_app():
    test_app = Flask(__name__)

    records = {
        "101": {"owner": "alice", "content": "Alice private record"},
        "102": {"owner": "bob", "content": "Bob private record"},
    }

    @test_app.route("/records/<record_id>")
    def get_record(record_id):
        # Demo only: user identity is supplied as a query parameter.
        # Real applications must use a trusted authenticated session.
        current_user = request.args.get("user")
        record = records.get(record_id)

        if record is None:
            abort(404)

        if current_user != record["owner"]:
            abort(403)

        return record["content"]

    return test_app


def test_owner_can_access_own_record():
    test_app = create_access_test_app()

    with test_app.test_client() as client:
        response = client.get("/records/101?user=alice")

    assert response.status_code == 200
    assert b"Alice private record" in response.data


def test_other_user_cannot_access_private_record():
    test_app = create_access_test_app()

    with test_app.test_client() as client:
        response = client.get("/records/101?user=bob")

    assert response.status_code == 403
