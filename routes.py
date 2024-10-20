from app import app
from flask import render_template, request, redirect, session
import users
import events
import locations


@app.route("/")
def index():
    return render_template("index.html", locations=locations.get_all_locations())


@app.route("/location/<int:location_id>")
def show_location(location_id):
    return render_template("location.html", events=locations.events_from_location(location_id))

@app.route("/events")
def show_all_events():
    return render_template("location.html", events=events.get_all_events())


@app.route("/event/<int:event_id>")
def show_event(event_id):
    info = events.get_event_info(event_id)
    date = events.get_event_date(event_id)
    username = events.get_event_username(event_id)
    user_id = events.get_event_user_id(event_id)
    event_name = events.get_event_event_name(event_id)
    location = events.get_event_location(event_id)
    return render_template("event.html", event_name=event_name, event_id=event_id, info=info, event_date=date, user_id=user_id, username=username, location=location)


@app.route("/edit/<int:event_id>", methods=["get", "post"])
def get_edits_event(event_id):
    if request.method == "GET":
        info = events.get_event_info(event_id)
        date = events.get_event_date(event_id)
        event_name = events.get_event_event_name(event_id)
        location = events.get_event_location(event_id)
        return render_template("edit.html", event_id=event_id, event_name=event_name, info=info, event_date=date, location=location)
    if request.method == "POST":
        users.check_csrf(request.form["csrf_token"])

        if request.form["edit"] == "poista":
            events.delete_event(event_id)
        else:
            name = request.form["name"]
            info = request.form["info"]
            location = request.form["location"]
            date = request.form["date"]
            event_id = request.form["event_id"]
            events.edit_event(event_id, name, info, locations.get_location_id(location), date)
        return redirect("/user/"+str(users.user_id()))

    

@app.route("/profile")
def show_userpage():
    user_id = users.user_id()
    username = users.get_username(user_id)
    user_myevents = users.get_user_myevents(user_id)
    user_friends = users.get_user_friends(user_id)
    return render_template("user.html", user=username, myevents=user_myevents, friends=user_friends)

@app.route("/friend/<int:session_user_id>")
def show_friendpage(session_user_id):
    username = users.get_username(session_user_id)
    friend_events = users.get_user_myevents(session_user_id)
    friend_state = users.get_friend_state(users.user_id(), session_user_id)
    return render_template("friend.html", user=username, friend_events=friend_events, friend_state=friend_state, friend_id=session_user_id)




@app.route("/add", methods=["get", "post"])
def add_event():
    if request.method == "GET":
        return render_template("add.html")

    if request.method == "POST":
        users.check_csrf(request.form["csrf_token"])

        name = request.form["name"]
        info = request.form["info"]
        location = request.form["location"]
        date = request.form["date"]

        events.add_event(name, info, locations.get_location_id(location), date, users.user_id())
        return redirect("/user/"+str(users.user_id()))




@app.route("/<int:session_user_id>")
def manage_friends(session_user_id):
    state = users.get_friend_state(users.user_id(), session_user_id)

    if state == 0:
        users.follow_user(users.user_id(), session_user_id)
        return redirect("/friend/"+str(session_user_id))
        
    else:
        users.unfollow_user(users.user_id(), session_user_id)
        return redirect("/friend/"+str(session_user_id))






@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Väärä tunnus tai salasana")

        return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")







