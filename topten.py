import db_helper
from flask import Flask, render_template, jsonify, request
from db_helper import add_new_tourn_data, total_points

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add")
def add_result():
    return render_template("add_entry.html")

@app.route("/admin")
def admin_page():
    return render_template("admin.html")

@app.route("/top_ten")
def view_results():
    return render_template("view_data.html")

@app.route("/add_result")
def add_data():
    return render_template("add_entry.html")

@app.route("/about")
def about_help():
    return render_template("about.html")

@app.route("/api/add_data", methods=["POST"])
def add_tournament_information():
    data = request.get_json()
    add_new_tourn_data(data)
    return jsonify({"message": "Data received"}), 200

@app.route("/api/schools")
def populate_schools():
    schools = db_helper.get_schools()
    if len(schools) > 0:
        data = db_helper.school_data_helper(schools)
        return jsonify(data), 200

@app.route("/api/divisions")
def populate_division():
    divisions = db_helper.get_divisions()
    if len(divisions) >0:
        data = db_helper.two_column_helper(divisions)
        return jsonify(data), 200

@app.route("/api/belt_ranks")
def populate_belts():
    belt_ranks = db_helper.get_belt_ranks()
    if len(belt_ranks) >0:
        data = db_helper.two_column_helper(belt_ranks)
        return jsonify(data), 200

@app.route("/api/events")
def populate_events():
    events = db_helper.get_events()
    if len(events) >0:
        data = db_helper.two_column_helper(events)
        return jsonify(data), 200

@app.route("/api/tournaments")
def populate_tournaments():
    tourn = db_helper.get_tournaments()
    if len(tourn) >0:
        data = db_helper.tournament_helper(tourn)
        return jsonify(data), 200

@app.route("/api/all_tourn")
def populate_all_tourn_data():
    tourn = db_helper.get_all_tournaments()
    if len(tourn) > 0:
        data = db_helper.all_tournament_helper(tourn)
        return jsonify(data), 200

@app.route("/api/topten")
def populate_top_ten():
    top_ten_raw = db_helper.populate_top_ten(request=request)
    if len(top_ten_raw) > 0:
        data = db_helper.top_ten_data_helper(top_ten_raw)
        return jsonify(data), 200
    else:
        return [{}], 204

@app.route("/api/<table>/<row_id>", methods=["POST"])
def update_data(table, row_id):
    value = request.get_json()
    if table != "topten":
        db_helper.admin_update(table, row_id, value)
    return jsonify({table: row_id}), 200

@app.route("/api/update_rankings")
def update_rankings():
    total_points()
    db_helper.rank()
    return jsonify({"message": "Rankings recalculated."})

app.run(debug=True)
