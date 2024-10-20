from db import db
from flask import session
from sqlalchemy.sql import text


def get_all_locations():
    sql = text("SELECT l.id AS id, l.location AS location, COUNT(*) AS count FROM events e, locations l WHERE e.location_id=l.id GROUP BY l.id, e.location_id;")
    return db.session.execute(sql).fetchall()

def events_from_location(location_id):
    sql = text("SELECT e.event_name AS event_name, e.id AS id, e.info AS info, e.event_date AS event_date  FROM events e, locations l WHERE e.location_id=l.id AND e.location_id=:location_id")
    return db.session.execute(sql, {"location_id": location_id}).fetchall()

def get_location_id(location):
    sql = text("SELECT id FROM locations WHERE location=:location")
    result = db.session.execute(sql, {"location":location})
    location_id = result.fetchone()
    if not location_id:
        sql = text("INSERT INTO locations (location) VALUES (:location)")
        db.session.execute(sql, {"location":location})
        db.session.commit()
        sql = text("SELECT id FROM locations WHERE location=:location")
        location_id = db.session.execute(sql, {"location": location}).fetchone()
    return location_id[0]

def get_location(location_id):
    sql = text("SELECT location FROM locations WHERE id=:location_id")
    return db.session.execute(sql, {"location_id": location_id}).fetchone()[0]
