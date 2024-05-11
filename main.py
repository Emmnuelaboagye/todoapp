from models import db, app
from user import *
from task import *


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

