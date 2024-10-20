from db import db
from flask import session
from sqlalchemy.sql import text

def get_all_events():
    sql = text("SELECT id, event_name, info, event_date FROM events ORDER BY event_date")
    return db.session.execute(sql).fetchall()


def show_event(event_id):
    sql = text("SELECT e.event_name AS event_name, e.id AS id, e.topic AS topic, e.info AS info, e.event_date AS event_date, u.username AS username FROM events e, locations l, users u WHERE e.id=:event_id AND e.location_id=l.id AND e.user_id=u.id")
    return db.session.execute(sql, {"event_id": event_id}).fetchall()



def get_event_info(event_id):
    sql = text("SELECT info FROM events WHERE id=:event_id")
    return db.session.execute(sql, {"event_id": event_id}).fetchone()[0]

def get_event_date(event_id):
    sql = text("SELECT event_date FROM events WHERE id=:event_id")
    return db.session.execute(sql, {"event_id": event_id}).fetchone()[0]

def get_event_user_id(event_id):
    sql = text("SELECT u.id FROM events e, users u WHERE e.id=:event_id AND e.user_id=u.id")
    return db.session.execute(sql, {"event_id": event_id}).fetchone()[0]

def get_event_username(event_id):
    sql = text("SELECT username FROM events e, users u WHERE e.id=:event_id AND e.user_id=u.id")
    return db.session.execute(sql, {"event_id": event_id}).fetchone()[0]

def get_event_event_name(event_id):
    sql = text("SELECT event_name FROM events WHERE id=:event_id")
    return db.session.execute(sql, {"event_id": event_id}).fetchone()[0]

def get_event_location(event_id):
    sql = text("SELECT l.location FROM events e, locations l WHERE e.id=:event_id AND e.location_id=l.id")
    return db.session.execute(sql, {"event_id": event_id}).fetchone()[0]


    
def add_event(name, info, location, date, user_id):
    sql = text("INSERT INTO events (event_name, location_id, event_date, user_id, info) VALUES (:name, :location, :date, :user_id, :info)")
    db.session.execute(sql, {"name":name, "location":location, "date":date, "user_id":user_id, "info":info})
    db.session.commit()
    return

def edit_event(event_id, name, info, location, date):
    sql = text("UPDATE events SET event_name=:name, location_id=:location, event_date=:date, info=:info WHERE id=:event_id")
    db.session.execute(sql, {"name":name, "location":location, "date":date, "info":info, "event_id":event_id})
    db.session.commit()
    return

def delete_event(event_id):
    sql = text("DELETE FROM events WHERE id=:event_id")
    db.session.execute(sql, {"event_id":event_id})
    db.session.commit()
    return
