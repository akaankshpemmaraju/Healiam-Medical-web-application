from http.client import HTTPResponse

from django.shortcuts import render

from drugprediction.beans import DrugResult
from drugprediction.forms import PatientForm, DrugReview, LoginForm
from drugprediction.fusioncharts import FusionCharts
from drugprediction.models import PatientModel, DrugReviewModel
from drugprediction.sentimentanalyzer import getCommentSentiment
from drugprediction.service import loadData


def adddrug(request):
    status = False

    if request.method == "POST":
        # Get the posted form
        patientForm = PatientForm(request.POST)

        if patientForm.is_valid():

            patientModel = PatientModel()
            patientModel.name = patientForm.cleaned_data["name"]
            patientModel.mobile = patientForm.cleaned_data["mobile"]
            patientModel.drug = patientForm.cleaned_data["drug"]

            try:
                patientModel.save()
                status = True
            except:
                status = False
    if status:
        return render(request, 'adddrug.html', {"message": "success"})
    else:
        response = render(request, 'adddrug.html', {"message": "Failed"})

    return response

def login(request):
    uname = ""
    upass = ""
    if request.method == "GET":
        # Get the posted form
        loginForm = LoginForm(request.GET)

        if loginForm.is_valid():

            uname = loginForm.cleaned_data["username"]
            upass = loginForm.cleaned_data["password"]

            if uname == "admin" and upass == "admin":
                return render(request, "adddrug.html", {})
            elif uname == "medplus" and upass == "medplus":
                return render(request, "adddrug.html", {})
            else:
                return render(request, "index.html", {"status" : "invalid username and password"})

    return render(request, "index.html", {"status" : "invalid request"})

def patientlogin(request):

    uname = request.GET['name']
    mobile = request.GET['mobile']

    user = PatientModel.objects.filter(name=uname, mobile=mobile).first()

    if user is not None:
        request.session['username']=uname

        return render(request, "postreview.html",{"medicines": PatientModel.objects.filter(name=request.session['username']),"drugs": DrugReviewModel.objects.all()})

    else:
        return render(request, 'patientlogin.html', {"message": "Invalid Credentials"})

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'index.html', {})

def postreview(request):

    return render(request,"postreview.html",{"medicines":PatientModel.objects.filter(name=request.session['username']),"drugs":DrugReviewModel.objects.all()})

def postreviewaction(request):

    status = False

    reviewForm = DrugReview(request.POST)

    if reviewForm.is_valid():

        drugname = reviewForm.cleaned_data['drugname']
        condition = reviewForm.cleaned_data['condition']
        review =reviewForm.cleaned_data['review']
        sentiment=getCommentSentiment(review)

        print(drugname)
        print(condition)
        print(review)
        print(sentiment)

        new_review = DrugReviewModel(drugname=drugname,condition=condition,review=review,sentiment=sentiment)

        try:
            new_review.save()
            status = True
        except Exception as e:
            print(e)
            status = False

    if status:
        return render(request, "postreview.html", {"message": "Success","drugs":DrugReviewModel.objects.all()})
    else:
        response = render(request, 'postreview.html', {"message": "Failed","drugs":DrugReviewModel.objects.all()})

    return response

def viewdrug(request):

    drugs=DrugReviewModel.objects.all()
    results=set()
    for drug in drugs:
        results.add(drug.condition)

    return render(request, "viewdrugs.html", {"conditions":results})

def getdrugs(request):

    condition = request.GET["condition"]

    models = DrugReviewModel.objects.filter(condition=condition)

    drugs={}

    for model in models:
        if model.drugname in drugs.keys() and model.sentiment in 'positive':
            drugs[model.drugname]=drugs[model.drugname]+1
        else:
            drugs[model.drugname]=1

    sorted_keys = sorted(drugs, key=drugs.get, reverse=True)

    results = []

    i = 0
    for key in sorted_keys:
        if i == 5:
            break
        results.append(DrugResult(key,drugs[key]))
        i = i + 1

    return render(request, 'viewdrugs.html', {'output':results,"conditions":DrugReviewModel.objects.all()})

def viewreviews(request):
    return render(request, "viewreviews.html", {"drugs":DrugReviewModel.objects.all()})

def getconditions(request):

    drugs=DrugReviewModel.objects.filter(drugname=request.GET['drug'])
    result=set()
    for drug in drugs:
        result.add(drug.condition)

    return render(request, "viewreviews.html", {"drug":request.GET['drug'],"conditions":result})

def getreviews(request):

    drug = request.GET["drug"]
    condition=request.GET["condition"]
    models=DrugReviewModel.objects.filter(drugname=drug,condition=condition)
    return render(request, "viewreviews.html", {"reviews":models})

def viewsentiment(request):
    return render(request, "viewsentiment.html", {"drugs":DrugReviewModel.objects.all()})

def getconditions1(request):

    drugs=DrugReviewModel.objects.filter(condition=request.GET['condition'])

    result=set()

    for drug in drugs:
        result.add(drug.drugname)

    return render(request, "viewsentiment.html", {"condition":request.GET['condition'],"drugs":result})

def getsentiment(request):

    drug = request.GET["drug"]
    condition = request.GET["condition"]

    models = DrugReviewModel.objects.filter(drugname=drug,condition=condition)

    positive = 0
    negative = 0
    neutral = 0

    for model in models:

        if model.sentiment == 'positive':
            positive = positive + 1

        if model.sentiment == 'negative':
            negative = negative + 1

        if model == 'neutral':
            neutral = neutral + 1

    return render(request, "viewsentiment.html", {"positive": positive,"negative":negative,"neutral":neutral})

def loaddataset(request):
    loadData()
    return HTTPResponse("success")