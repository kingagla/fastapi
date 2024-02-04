from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import DBUser

from schemas import UserBase

def create_user(db: Session, request: UserBase):
    # hasło musi być zahashowane!
    new_user = DBUser(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(DBUser).all()


def get_user(db: Session, id: int):
    return db.query(DBUser).filter(DBUser.id == id).first()
    # można podwójnie filtrować, np. db.query(DBUser).filter(DBUser.id == id).filter(DBUser.email == email).first()
    
    
def update_user(db: Session, id: int, request:UserBase):
    user = db.query(DBUser).filter(DBUser.id == id)
    # TODO: Handle exceptions
    user.update({
        DBUser.username: request.username,
        DBUser.email: request.email,
        DBUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return "ok"


def delete_user(db: Session, id: int):
    user = db.query(DBUser).filter(DBUser.id == id).first()
    # TODO: Handle exceptions
    db.delete(user)
    db.commit()
    return f"User {id} removed correctly."