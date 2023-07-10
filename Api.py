from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def main():
    return "getting started with job konnect API"
