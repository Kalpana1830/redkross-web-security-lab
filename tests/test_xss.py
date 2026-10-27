
from flask import Flask, render_template_string


def create_xss_test_app():
    test_app = Flask(__name__)

    @test_app.route("/search")
    def search():
        from flask import request

        query = request.args.get("q", "")
        return render_template_string(
            "<h1>Search results</h1><p>{{ query }}</p>",
            query=query,
        )

    return test_app


def test_search_escapes_html_input():
    test_app = create_xss_test_app()

    with test_app.test_client() as client:
        response = client.get(
            "/search?q=%3Cscript%3Ealert%281%29%3C%2Fscript%3E"
        )

    assert response.status_code == 200
    assert b"&lt;script&gt;" in response.data
    assert b"<script>alert(1)</script>" not in response.data
