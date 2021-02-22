from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
        <h1>Hejsa styrmand</h1>
        <h4>Her er en liste over flaskeposter</h4>
        <ul>
            <li>Jeg er sulten og fanget på havet</li>
            <li>Jeg har spist min fugl</li>
        </ul>
    """