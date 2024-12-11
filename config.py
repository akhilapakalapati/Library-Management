import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///library.db"  # Replace with your DB connection string
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")  # For JWT tokens or sensitive data


