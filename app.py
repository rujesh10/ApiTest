from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model (table)
class LotteryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Rujesh's Server!"})

# Add an entry to the database
@app.route("/submit", methods=["POST"])
def submit_data():
    data = request.json
    name = data.get("name")
    age = data.get("age")

    if not name or not age:
        return jsonify({"error": "Name and age are required!"}), 400

    # Save to database
    entry = LotteryEntry(name=name, age=age)
    db.session.add(entry)
    db.session.commit()

    return jsonify({"status": "success", "entry_id": entry.id})

# Get all entries
@app.route("/entries", methods=["GET"])
def get_entries():
    entries = LotteryEntry.query.all()
    results = [
        {"id": entry.id, "name": entry.name, "age": entry.age}
        for entry in entries
    ]
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5000)
    # app.run(debug=True)
