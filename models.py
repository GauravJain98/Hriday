from sql import *
 

@app.route('/')
def index():
    return render_template('mainApp/index.html') 

@app.route('/organInput')
def organInput():
    return render_template('mainApp/about.html')

@app.route('/organOutput')
def organOutput(id=None):
    if id is None:
        organ = organs
    else:
        organ = Kidney.objects.get(id)
        if organ is None:
            return redirect('/')
    return render_template('mainApp/organs.html',organs = organ)

p=1000

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
        patients.append({"id":p,"name":request.FORM['name'],"bloodType":request.FORM['blood'],"diabetes":request.d,"priorOrgan":p,"dob":request.FORM['dob']})
        p+=1
        patientMaster(id=p,pid=p-1,epts=epts,nepts=nepts,blood = request.FORM['blood'],dob=request.FORM['dob'])
    return render_template('mainApp/patientInput.html')


def patientUpdate(request):
    return render_template('mainApp/patientUpdate.html')

@app.route('/patientOutput')
def patientOutput(id=None):
    if id is None:
        patient = patients
    else:
        patient = Patient.objects.get(id)
        if patient is None:
            return redirect('/')
    return render_template('mainApp/store.html',patients=patient)

@app.route('/patient/listing')
def priorityListing():
    patient = getP(m=True)
    return render_template('mainApp/patientOutput.html',patient=patient)

@app.route('/matchingList')
def matchingList():
    match = []
    organl = 0
    organsT = organs
    for patient in patients:
        for organ in organsT:
            if patient["bloodType"].upper() == 'AB' or (patient["bloodType"] == organ["bloodType"]):
                match.append({"patient":patient["id"],"organ":organ["organId"],"dob":organ["dob"]})
                organs[organl]["bloodType"]=""
            elif patient["bloodType"].upper() == 'O' and organ["bloodType"].upper() == 'A' :
                match.append({"patient":patient["id"],"organ":organ["organId"],"dob":organ["dob"]})
                organs[organl]["bloodType"]=""
            elif patient["bloodType"].upper() == 'A' and organ["bloodType"].upper() == 'O' :
                match.append({"patient":patient["id"],"organ":organ["organId"],"dob":organ["dob"]})
                organs[organl]["bloodType"]=""
            elif patient["bloodType"].upper() == 'B' and organ["bloodType"].upper() == 'O' :
                match.append({"patient":patient["id"],"organ":organ["organId"],"dob":organ["dob"]})
                organs[organl]["bloodType"]=""
            else:
                organl-=1
            organl+=1
    return str(len(match))
    return render_template('mainApp/matchingList.html',organs=match)


if __name__ == '__main__':
    app.run(debug = True,port=8000)