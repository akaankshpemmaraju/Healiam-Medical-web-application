from django.forms import Form, CharField, PasswordInput

class DrugReview(Form):
    drugname=CharField(max_length=500)
    condition=CharField(max_length=500)
    review=CharField(max_length=5000)


class PatientForm(Form):
    name=CharField(max_length=50)
    mobile=CharField(max_length=50)
    drug=CharField(max_length=50)

class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())
