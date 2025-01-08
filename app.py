from flask import Flask, render_template, request, redirect, url_for

# Create the Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        sport = request.form["sport"]
        return redirect(url_for('thank_you', name=name, sport=sport))
    return render_template("index.html")  # Load the index.html file for GET request

@app.route("/thank_you")
def thank_you():
    # Get the parameters from the URL
    name = request.args.get('name')
    sport = request.args.get('sport')
    # Render the thank_you.html template and pass name and email as context
    return render_template("thank_you.html", name=name, sport=sport)

if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask server