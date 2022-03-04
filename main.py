from flask import *
import json
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/view")
def view():
    con = sqlite3.connect("dataa.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from dataa")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/savedetails/", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        data = request.get_json(force=True)
        print(data)
        name = data["name"]
        email = data["email"]
        elso = data["elso"]
        masodik = data["masodik"]
        szoveg = data["szoveg"]
        with sqlite3.connect("dataa.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into dataa (name, email, elso, masodik, szoveg) values (?,?,?,?,?)", (name, email, elso, masodik, szoveg))
            con.commit()
            msg = "Employee successfully Added"
    except:
        con.rollback()
        msg = "We can not add the employee to the list"
    finally:
        return name
        con.close()

@app.route("/deleterecord/", methods=["POST"])
def deleterecord():
    data = request.get_json(force=True)
    id = str(data["id"])
    print(id)
    with sqlite3.connect("dataa.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from dataa where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"

@app.route("/updatedetails/", methods=["POST"])
def updaterecord():
    try:
        data = request.get_json(force=True)
        print(data)
        id = data["id"]
        name = data["name"]
        email = data["email"]
        elso = data["elso"]
        masodik = data["masodik"]
        szoveg = data["szoveg"]

        with sqlite3.connect("dataa.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE dataa SET name=?, email=?, address=? WHERE id=?", (name, email, elso, masodik, szoveg, id))
            con.commit()
            msg = "Employee successfully Updated"
    except:
        con.rollback()
        msg = "We can not update the employee to the list"
    finally:
        return msg
        con.close()

if __name__ == "__main__":
    app.run(debug=True)