from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story, serious_story

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

debug = DebugToolbarExtension(app)

STORIES = {
    "silly": silly_story,
    "excited": excited_story,
    "serious": serious_story,
}

story_chosen = None


@app.get("/")
def homepage():
    """Loads the dropdown of madlib stories"""

    return render_template("dropdown.html", stories=STORIES.values())


@app.get("/questions")
def questions():
    """Loads the page with the questions for a given story"""

    story_chosen = STORIES[request.args.get("madlib-stories")]

    return render_template(
        "questions.html", prompts=story_chosen.prompts, story=story_chosen
    )


# can pass in the story as a URL parameter "/<story>/results"
@app.get("/results")
def display_results():
    """Loads the results from story inputs"""

    story = STORIES[request.args.get("chosen_story")]

    return render_template("results.html", story=story.get_result_text(request.args))
