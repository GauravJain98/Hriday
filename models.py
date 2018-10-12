import datetime
from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('mainApp/about.html') 

@app.route('/organ/add')
def organInput():
    return render_template('mainApp/organInput.html')

@app.route('/organ/<id>')
def organOutput(id=None):
    if id is None:
        organs = Kidney.objects.all()
    else:
        organs = Kidney.objects.get(id)
        if organs is None:
            return redirect('/')
    return render_template('mainApp/organOutput.html',organs = organs)

p=0

@app.route('/patient/add')
def patientInput():
    if request.method == 'POST':
        age = 18
        if age > 25:
            val = age-25
        else:
            val = 0
        diabetes = request.FORM['diabetes']
        priorOrgan = request.FORM['priorOrgan']
        d = int(diabetes)
        p= int(priorOrgan)
        epts = 0.047*val + (-0.015) * d * val + 0.398*p + (-0.237* d*p) + 0.315*log(dialysis+1) + 0.13*dialysis +(-0.348)*d*dialysis + 1.262*d
        nepts = 0.047*val + (-0.015) * d * val + 0.398*p + (-0.237* d*p) + 1.262*d
        patient(id=p,name=request.FORM['name'],blood_type=request.FORM['blood'],diabetes=request.d,priorOrgan=p,dob=request.FORM['dob'])
        p+=1
        patientMaster(id=p,pid=p-1,epts=epts,nepts=nepts,blood = request.FORM['blood'],dob=request.FORM['dob'])
    return render_template('mainApp/patientInput.html')


def patientUpdate(request):
    return render_template('mainApp/patientUpdate.html')

@app.route('/patient/<id>')
def patientOutput(id=None):
    if id is None:
        patient = getP(m=False)
    else:
        patient = Patient.objects.get(id)
        if patient is None:
            return redirect('/')
    return render_template('mainApp/patientOutput.html')

@app.route('/patient/listing')
def priorityListing(request):
    patient = PatientMaster.objects.all().order_by('epts')
    return render_template('mainApp/patientOutput.html')

@app.route('/matching')
def matchingList(request):
    patients = "SELECT * FROM patient order by epts".format(table)
    organs = {}
    match = []
    organl = 0
    for patient in patients:
        for organ in organs:
            if patient.blood_type == 'AB' or (patient.blood_type == organ.blood_type):
                match.append((patient.id,organ.id))
                organs.organl.blood_type=""
            elif patient.blood_type == 'O' and organ.blood_type == 'A' :
                match.append((patient.id,organ.id))
                organs.organl.blood_type=""
            elif patient.blood_type == 'A' and organ.blood_type == 'O' :
                match.append((patient.id,organ.id))
                organs.organl.blood_type=""
            elif patient.blood_type == 'B' and organ.blood_type == 'O' :
                match.append((patient.id,organ.id))
                organs.organl.blood_type=""
            else:
                organl-=1
            organl+=1
    return render_template('mainApp/matchingList.html')


if __name__ == '__main__':
    app.run(debug = True,port=8000)