from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def homepage():
    """Loads the homepage"""

    return render_template("questions.html", prompts=silly_story.prompts)

@app.get("/results")
def display_results():
    """Loads the results from story inputs"""
    #TODO: use request.args directly

    story_ans = {}

    for word in silly_story.prompts:
        story_ans[word] = request.args.get(word)

    return render_template("results.html",story = silly_story.get_result_text(story_ans))