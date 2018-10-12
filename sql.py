import sqlite3
from flask import g,Flask, redirect, url_for, request,render_template

app = Flask(__name__)

MDATABASE = './sql/master.db'
SDATABASE = './sql/slave.db'

def get_mdb():
    db = getattr(g, '_mdatabase', None)
    if db is None:
        db = g._mdatabase = sqlite3.connect(MDATABASE)
    return db

def get_sdb():
    db = getattr(g, '_sdatabase', None)
    if db is None:
        db = g._sdatabase = sqlite3.connect(SDATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    mdb = getattr(g, '_mdatabase', None)
    sdb = getattr(g, '_sdatabase', None)
    if sdb is not None:
        sdb.close()
    if mdb is not None:
        mdb.close()

def init_db():
    with app.app_context():
        mdb = get_mdb()
        sdb = get_sdb()
        with app.open_resource('sql/master.sql', mode='r') as f:
            mdb.cursor().executescript(f.read())
        mdb.commit()
        with app.open_resource('sql/slave.sql', mode='r') as f:
            sdb.cursor().executescript(f.read())
        sdb.commit()

def query_db(query, args=(), one=False,m=False):
    if m:
        cur = get_mdb().execute(query, args)
    else:
        cur = get_sdb().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def patientMaster(id,pid,epts,nepts):
    command = "INSERT INTO patient(id,pid,epts,nepts) VALUES({},{},{},{});".format(id,pid,epts,nepts) 
    query_db(command,m=True)
    
def user(id,username,password,address):
    command = "INSERT INTO patient(id,username,password,address) VALUES({},{},{});".format(id,username,password,address)
    query_db(command)

def patient(id,name,blood_type,diabetes,priorOrgan,dob):
    command = "INSERT INTO patient(id,name,blood-type,diabetes,priorOrgan,dob) VALUES({},{},{});".format(id,name,blood_type,diabetes,priorOrgan,dob)
    query_db(command)

def get(table,m=False,id=None):
    if id is None:
        command = "SELECT * FROM {}".format(table)
    else:
        command = "SELECT * FROM {} WHERE id={}".format(table,id)
    return query_db(command,m=m)

def getP(id = None,m=False):
    if id is None:
        data = []
        for d in get('patient',m=m):
            if m:
                (id,pid,epts) = d
                data.append({'id':id,'pid':pid,'epts':epts})
            else:
                (id,name,blood_type,diabetes,priorOrgan,dob) = d
                data.append({'id':id,'name':name,'blood_type':blood_type,'diabetes':diabetes,'priorOrgan':priorOrgan,'dob':dob})
        return data
    else:
        try:
            if m:
                (id,pid,epts) = get('patient',id=id,m=m)[0]
                return {'id':id,'pid':pid,'epts':epts}
            else:
                (id,name,blood_type,diabetes,priorOrgan,dob) = get('patient',id=id,m=m)[0]
                return {'id':id,'name':name,'blood_type':blood_type,'diabetes':diabetes,'priorOrgan':priorOrgan,'dob':dob}
        except:
            return {'error':"NON"}

def getU(id = None):
    if id is None:
        data = []
        for d in get('user',m=False):
            (id,username,password,address) = d
            data.append({'id':id,'username':username,'password':password,'address':address})
        return data
    else:
        if m:
            (id,pid,epts) = d
            return {'id':id,'pid':pid,'epts':epts}
        else:
            (id,name,blood_type,diabetes,priorOrgan,dob) = get('user',id=id,m=False)
            data.append({'id':id,'username':username,'password':password,'address':address})


if __name__ == '__main__':
    with app.app_context():
        patientMaster(2,2,5)
        print(getP(id=2,m=True))
        print(getP(id=2,m=False))



