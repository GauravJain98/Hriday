from flask_sqlalchemy import SQLAlchemy
import datetime
from flask import Flask, redirect, url_for, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/slave.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/master.db'
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db2 = SQLAlchemy(app2)

SQLALCHEMY_DATABASE_URI = 'postgres://localhost/main'
SQLALCHEMY_BINDS = {
    'users':        'mysqldb://localhost/users',
    'appmeta':      'sqlite:////path/to/appmeta.db'
}

""" 
category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
    nullable=False)
category = db.relationship('Category',
    backref=db.backref('posts', lazy=True))
"""

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    archived = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    archived =  db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    user = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    archived =  db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    updated_by = db.Column(db.String(50), unique=False, nullable=False)
    name = db.Column(db.String(50), unique=False, nullable=False)
    dob = db.Column(db.DateTime, default=db.func.now())
    diabetes =  db.Column(db.Boolean)
    priorOrgan =  db.Column(db.Boolean)
    blood_type = db.Column(db.String(3), unique=False, nullable=False)
    

class PatientMaster(db2.Model):
    id = db2.Column(db2.Integer, primary_key=True)
    archived = db2.Column(db2.Boolean)
    created_at = db2.Column(db2.DateTime, default=db2.func.now())
    updated_at = db2.Column(db2.DateTime, default=db2.func.now())
    patient = db2.Column(db2.Integer,nullable=False)
    epts = db2.Column(db2.Integer, nullable=False)
    blood_type = db2.Column(db2.String(3), unique=False, nullable=False)

class Kidney(db2.Model):
    id = db2.Column(db2.Integer, primary_key=True)
    archived = db2.Column(db2.Boolean)
    created_at = db2.Column(db2.DateTime, default=db2.func.now())
    updated_at = db2.Column(db2.DateTime, default=db2.func.now())
    blood_type = db2.Column(db2.String(3), unique=False, nullable=False)
    temo 
    age
    
    
@app.route('/')
def index(request):
    return render('mainApp/index.html')

@app.route('/organ/add')
def organInput():
    if request.method == 'POST':
        organ = Kidney(blood_type = request.POST['blood'])
        organ.save()
    return render('mainApp/organInput.html')

@app.route('/organ/<id>')
def organOutput(id=None):
    if id is None:
        organs = Kidney.objects.all()
    else:
        organs = Kidney.objects.get(id)
        if organs is None:
            return redirect('/')
    return render('mainApp/organOutput.html',organs = organs)

@app.route('/patient/add')
def patientInput(id=None):
    if request.method == 'POST':
        if id is None:
            age = 18
            if age > 25:
                val = age-25
            else:
                val = 0
            diabetes = request.POST['diabetes']
            priorOrgan = request.POST['priorOrgan']
            d = int(diabetes)
            p= int(priorOrgan)
            epts = 0.047*val + (-0.015) * d * val + 0.398*p + (-0.237* d*p) + 0.315*log(dialysis+1) + 0.13*dialysis +(-0.348)*d*dialysis + 1.262*d
            patient = Patient(name = request.POST['name'],dob=request.POST['dob'],blood_type=request.POST['blood'],dialysis = dialysis,diabetes = diabetes,priorOrgan=priorOrgan)
            patient.save()
            master = PatientMaster(patient = patient,epts = epts,blood_type = request.POST['blood'])
        else:
            patient = Patient.objects.get(id = id)
            if patient is None:
                return render('mainApp/patientInput.html')
    return render('mainApp/patientInput.html')


def patientUpdate(request):
    return render('mainApp/patientUpdate.html')

@app.route('/patient/<id>')
def patientOutput(id=None):
    if id is None:
        patient = Patient.objects.all()
    else:
        patient = Patient.objects.get(id)
        if patient is None:
            return redirect('/')
    return render('mainApp/patientOutput.html')

@app.route('/patient/listing')
def priorityListing(request):
    patient = PatientMaster.objects.all().order_by('epts')
    return render('mainApp/patientOutput.html')

@app.route('/matching')
def matchingList(request):
    patients = PatientMaster.objects.all().order_by('epts')
    organs = Kidney.objects.all().order_by('~created_at')
    match = []
    organ = 0
    for patient in patients:
        if patient.blood_type == 'AB' or (patient.blood_type == organ.blood_type):
            match.append((patient.id,organ.id))
        elif patient.blood_type == 'O' and organ.blood_type == 'A' :
            match.append((patient.id,organ.id))
        elif patient.blood_type == 'A' and organ.blood_type == 'O' :
            match.append((patient.id,organ.id))
        elif patient.blood_type == 'B' and organ.blood_type == 'O' :
            match.append((patient.id,organ.id))
        else:
            organ-=1
        organ+=1
    return render('mainApp/matchingList.html')


if __name__ == '__main__':

    db.create_all()
    app.run(debug = True)