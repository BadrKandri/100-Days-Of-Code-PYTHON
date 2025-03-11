'''https://documenter.getpostman.com/view/42946578/2sAYdoFT8d'''


from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, inspect
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_cofe():
    data=db.session.execute(db.select(Cafe)).scalars().all()
    rand_num=random.randint(0,len(data))
    # Data serialization (SQLAlchemy Object -----> JSON)
    cofes=[ {c.key: getattr(cofe, c.key) for c in inspect(Cafe).mapper.column_attrs} for cofe in data ]
    return jsonify(cofes[rand_num])

@app.route("/all")
def get_all_cofes():
    data=db.session.execute(db.select(Cafe)).scalars().all()
    # Data serialization (SQLAlchemy Object -----> JSON)
    cofes=[ {c.key: getattr(cofe, c.key) for c in inspect(Cafe).mapper.column_attrs} for cofe in data ]
    return jsonify(cofes)

@app.route("/search/<loc>")
def get_by_location(loc):
    result=db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars()
    cofes=[ {c.key: getattr(cofe, c.key) for c in inspect(Cafe).mapper.column_attrs} for cofe in result ]
    return jsonify(cofes)
# HTTP GET - Read Record

# HTTP POST - Create Record
@app.route("/create_cafe", methods=["POST"])
def create_cafe():
    # Get JSON data from the POST request
    data = request.get_json()

    # Extract information from the request data
    name = data.get('name')
    location = data.get('location')
    img_url = data.get('img_url')
    map_url = data.get('map_url')
    has_sockets = data.get('has_sockets', False)
    has_toilet = data.get('has_toilet', False)
    has_wifi = data.get('has_wifi', False)
    can_take_calls = data.get('can_take_calls', False)
    coffee_price = data.get('coffee_price', "N/A")
    seats = data.get('seats', "Unknown")

    # Validate required fields
    if not name or not location or not img_url or not map_url:
        return jsonify({"message": "Name, location, img_url, and map_url are required!"}), 400
    # Create a new Cafe object
    new_cafe = Cafe(name=name,location=location,img_url=img_url,map_url=map_url,has_sockets=has_sockets,has_toilet=has_toilet,
        has_wifi=has_wifi,can_take_calls=can_take_calls,coffee_price=coffee_price,seats=seats)
    # Add to the database
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({"message": "Cafe created successfully!"}), 201


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        ## Just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        #404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
