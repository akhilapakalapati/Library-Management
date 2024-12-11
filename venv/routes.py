from flask import Blueprint, request, jsonify
from models import db, User
import bcrypt

routes = Blueprint("routes", __name__)

@routes.route("/api/users", methods=["POST"])
def create_user():
    """
    Create a new library user.
    Request body:
        {
            "email": "user@example.com",
            "password": "securepassword",
            "role": "user"
        }
    """
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        role = data.get("role", "user")  # Default to 'user'

        # Validate inputs
        if not email or not password:
            return jsonify({"error": "Email and password are required."}), 400

        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "User with this email already exists."}), 400

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Create the new user
        new_user = User(email=email, password=hashed_password.decode("utf-8"), role=role)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully!", "user_id": new_user.id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
