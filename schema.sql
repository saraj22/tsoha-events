CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role Integer
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    event_name TEXT,
    location_id INTEGER REFERENCES locations,
    event_date DATE,
    user_id INTEGER REFERENCES users,
    info TEXT
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    location TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events,
    user_id INTEGER REFERENCES users,
    date DATE,
    review TEXT
);


CREATE TABLE friends (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    friend_id INTEGER REFERENCES users
);

