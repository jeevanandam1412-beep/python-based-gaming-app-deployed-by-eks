from flask import Flask, render_template, request
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)


@app.route("/", methods=["GET", "POST"])
def index():
    global secret_number

    message = ""T
K8s
deployment.yaml
ingress.yaml
namespace.yaml
servicw.yaml
app

    attempts = request.cookies.get("attempts", "0")

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            attempts = int(attempts) + 1

            if guess < secret_number:
                message = "Too low! Try again."
            elif guess > secret_number:
                message = "Too high! Try again."
            else:
                message = f"🎉 Correct! You won in {attempts} attempts!"
                secret_number = random.randint(1, 100)
                attempts = 0

        except ValueError:
            message = "Please enter a valid number."

    response = render_template(
        "index.html",
        message=message,
        attempts=attempts
    )

    from flask import make_response
    result = make_response(response)
    result.set_cookie("attempts", str(attempts))

    return result


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)