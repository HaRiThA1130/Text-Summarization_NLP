from flask import Flask, render_template, request
from transformers import BartForConditionalGeneration, BartTokenizer

app = Flask(__name__)

# Load model and tokenizer
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    summary_length = 0

    if request.method == "POST":
        text = request.form.get("input_text")
        if text:
            # Tokenize and generate summary
            inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
            summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
            summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            summary_length = len(summary)

    return render_template("index.html", summary=summary, summary_length=summary_length)

# About route
@app.route("/about")
def about():
    return render_template("about.html")

# Contact route
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)