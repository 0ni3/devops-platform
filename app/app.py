from flask import Flask, jsonify
import os
import psycopg2


app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "1.0.0")


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DATABASE_HOST", "database"),
        database=os.getenv("DATABASE_NAME", "platform"),
        user=os.getenv("DATABASE_USER", "devops"),
        password=os.getenv("DATABASE_PASSWORD", "devops")
    )


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to DevOps Platform",
        "version": VERSION
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/database")
def database():

    try:
        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute(
            "SELECT version();"
        )

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return jsonify({
            "database": "connected",
            "version": result[0]
        })

    except Exception as error:
        return jsonify({
            "database": "error",
            "message": str(error)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )