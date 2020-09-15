import flask
from flask import request
from yoga_api import peak_poses, lstm_model, model, embeddings, tokenizer, get_peak_pose, peak_pose_dict
from generate_class import generate_class

# initialize the app
app = flask.Flask(__name__)


@app.route("/")
def create_yoga_class():
    return flask.render_template("home_page.html",
                                 peak_poses=peak_poses,
                                 peak_pose_dict=peak_pose_dict)


@app.route("/print_class", methods=["POST", "GET"])
def print_class_sequence():
    peak_pose = get_peak_pose(request.form)
    first_half = generate_class(
        model, tokenizer, embeddings, peak_pose, "easy pose", 40)[::-1]
    second_half = generate_class(
        model, tokenizer, embeddings, peak_pose, "corpse pose", 40)
    yoga_class = first_half + second_half

    if request.method == 'POST':
        result = yoga_class
        return flask.render_template("print_class.html",
                                     result=result,
                                     peak_pose=peak_pose,
                                     )


@app.route("/take_class", methods=["POST", "GET"])
def take_class():
    return flask.render_template("yoga_class_page.html")


# for local development:
if __name__ == "__main__":
    app.run(debug=True)

# for public web serving:
app.run(host="0.0.0.0")
