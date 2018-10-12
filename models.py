from sql import *
    patients = [
    {
        "id":1,
        "diabetes": "true",
        "priorOrgan": "true",
        "name": "Gaurav Jain",
        "bloodType": "b",
        "dob": "1998-08-09"
    },
    {
        "id":2,
        "diabetes": "true",
        "priorOrgan": "false",
        "name": "Nidhi Jha",
        "bloodType": "o",
        "dob": "1998-08-07"
    },
    {
        "id":3,
        "diabetes": "false",
        "priorOrgan": "true",
        "name": "Arpit Bharti",
        "bloodType": "b",
        "dob": "1998-07-09"
    },
    {
        "id":4,
        "diabetes": "true",
        "priorOrgan": "false",
        "name": "Rishab Lamba",
        "bloodType": "b",
        "dob": "1997-08-09"
    },
    {
        "id":5,
        "diabetes": "false",
        "priorOrgan": "true",
        "name": "Rajat Sharma",
        "bloodType": "a",
        "dob": "1998-08-10"
    },
    {
        "id":6,
        "diabetes": "true",
        "priorOrgan": "false",
        "name": "Manish Aneja",
        "bloodType": "b",
        "dob": "1998-08-19"
    },
    {
        "id":7,
        "diabetes": "false",
        "priorOrgan": "true",
        "name": "Gaurav Jain",
        "bloodType": "b",
        "dob": "1998-09-09"
    }
]
    organs = [
    {
        "hName": "jndjnj",
        "organId": "jnjdns",
        "hState": "Andaman and Nicobar Islands",
        "hAddress": "jbjbs",
        "gridRadios": "1",
        "date": "2018-04-06",
        "time": "00:59",
        "storingSolution": "idin",
        "temperature": "3",
        "donorName": "jnjnd",
        "donorId": "hhbhs",
        "dob": "2017-06-06",
        "gender": "female",
        "bloodType": "A",
        "donorState": "Andaman and Nicobar Islands",
        "donorAddress": "njns",
        "donorAadhar": "123456789123",
        "kinName": " jmsjs`kjs`",
        "kinPhoneNo": "9810020853",
        "kinAadhar": "981002085312"
    },
    {
        "hName": "jndjnj",
        "organId": "jnjdns",
        "hState": "Andaman and Nicobar Islands",
        "hAddress": "jbjbs",
        "gridRadios": "1",
        "date": "2018-04-06",
        "time": "00:59",
        "storingSolution": "idin",
        "temperature": "3",
        "donorName": "jnjnd",
        "donorId": "hhbhs",
        "dob": "2017-06-06",
        "gender": "female",
        "bloodType": "O",
        "donorState": "Andaman and Nicobar Islands",
        "donorAddress": "njns",
        "donorAadhar": "123456789123",
        "kinName": " jmsjs`kjs`",
        "kinPhoneNo": "9810020853",
        "kinAadhar": "981002085312"
    },
    {
        "hName": "jndjnj",
        "organId": "jnjdns",
        "hState": "Andaman and Nicobar Islands",
        "hAddress": "jbjbs",
        "gridRadios": "1",
        "date": "2018-04-06",
        "time": "00:59",
        "storingSolution": "idin",
        "temperature": "3",
        "donorName": "jnjnd",
        "donorId": "hhbhs",
        "dob": "2017-06-06",
        "gender": "female",
        "bloodType": "A",
        "donorState": "Andaman and Nicobar Islands",
        "donorAddress": "njns",
        "donorAadhar": "123456789123",
        "kinName": " jmsjs`kjs`",
        "kinPhoneNo": "9810020853",
        "kinAadhar": "981002085312"
    }
]


@app.route('/')
def index():
    return render_template('mainApp/index.html') 

@app.route('/organInput')
def organInput():
    return render_template('mainApp/about.html')

@app.route('/organOutput')
def organOutput(id=None):
    if id is None:
        organs = Kidney.objects.all()
    else:
        organs = Kidney.objects.get(id)
        if organs is None:
            return redirect('/')
    return render_template('mainApp/organs.html',organs = organs)

p=0

@app.route('/patientInput')
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
        patient(id=p,name=request.FORM['name'],bloodType=request.FORM['blood'],diabetes=request.d,priorOrgan=p,dob=request.FORM['dob'])
        p+=1
        patientMaster(id=p,pid=p-1,epts=epts,nepts=nepts,blood = request.FORM['blood'],dob=request.FORM['dob'])
    return render_template('mainApp/patientInput.html')


def patientUpdate(request):
    return render_template('mainApp/patientUpdate.html')

@app.route('/patientOutput')
def patientOutput(id=None):
    if id is None:
        patient = getP(m=False)
    else:
        patient = Patient.objects.get(id)
        if patient is None:
            return redirect('/')
    return render_template('mainApp/patientOutput.html')

@app.route('/patient/listing')
def priorityListing():
    patient = PatientMaster.objects.all().order_by('epts')
    return render_template('mainApp/patientOutput.html')

@app.route('/matching')
def matchingList():
    match = []
    organl = 0
    for patient in patients:
        for organ in organs:
            if patient["bloodType"].upper() == 'AB' or (patient["bloodType"] == organ["bloodType"]):
                match.append((patient["id"],organ["organId"]))
                organs[organl]["bloodType"]=""
            elif patient["bloodType"].upper() == 'O' and organ["bloodType"].upper() == 'A' :
                match.append((patient["id"],organ["organId"]))
                organs[organl]["bloodType"]=""
            elif patient["bloodType"].upper() == 'A' and organ["bloodType"].upper() == 'O' :
                match.append((patient["id"],organ["organId"]))
                organs[organl]["bloodType"]=""
            elif patient["bloodType"].upper() == 'B' and organ["bloodType"].upper() == 'O' :
                match.append((patient["id"],organ["organId"]))
                organs[organl]["bloodType"]=""
            else:
                organl-=1
            organl+=1
    return str(match)


if __name__ == '__main__':
    app.run(debug = True,port=8000)