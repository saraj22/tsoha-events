import os
from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["csrf_token"] = os.urandom(16).hex()
            return True
        else:
            return False

def user_id():
    return session.get("user_id", 0)

def logout():
    del session["user_id"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def check_csrf(csrf_token):
    if session["csrf_token"] != csrf_token:
        abort(403)





def get_username(user_id):
    sql = text("SELECT username FROM users WHERE id=:user_id")
    return db.session.execute(sql, {"user_id": user_id}).fetchone()[0]

def get_user_myevents(user_id):
    sql = text("SELECT * FROM events WHERE user_id=:user_id")
    return db.session.execute(sql, {"user_id": user_id}).fetchall()

def get_user_friends(user_id):
    sql = text("SELECT u.id, u.username FROM friends f JOIN users u ON f.friend_id=u.id WHERE f.user_id=:user_id")
    return db.session.execute(sql, {"user_id": user_id}).fetchall()
    

def get_friend_state(user_id, friend_id):
    sql = text("SELECT * FROM friends WHERE user_id=:user_id AND friend_id=:friend_id")
    result = db.session.execute(sql, {"user_id": user_id, "friend_id": friend_id})
    state = result.fetchall()

    if not state: return 0
    else: return 1




def follow_user(user_id, friend_id):
    sql = text("INSERT INTO friends (user_id, friend_id) VALUES (:user_id, :friend_id)")
    db.session.execute(sql, {"user_id":user_id, "friend_id":friend_id})
    db.session.commit()
    return

def unfollow_user(user_id, friend_id):
    sql = text("DELETE FROM friends WHERE user_id=:user_id AND friend_id=:friend_id")
    db.session.execute(sql, {"user_id":user_id, "friend_id":friend_id})
    db.session.commit()
    return