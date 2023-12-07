from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec
from src.routes import routes

app = Flask(__name__)
app.register_blueprint(routes.route)
spec = FlaskPydanticSpec('flask', title='CRUD API')
spec.register(app)


if __name__ == "__main__":
    app.run(debug = True)