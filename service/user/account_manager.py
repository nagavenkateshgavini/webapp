from app.extensions import db
from app.models.user import User


def get_user_info() -> None:
    pass


def insert_user(user_obj) -> None:
    import pdb; pdb.set_trace()
    db.session.add(user_obj)
    db.session.commit()
