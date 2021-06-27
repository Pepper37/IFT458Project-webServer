from django.db import models


# the model User represents any user in the system
# a model is a column in the database
# the fields are the necessary data on the `signup.html` page
# the fields are the rows
class User(models.Model):

    # each of these is a column in the database
    userName = models.CharField(max_length=8, primary_key=True, default='janeDoe')
    password = models.CharField(max_length=8, default='password')
    fName = models.CharField(max_length=30, default='Jane')
    mName = models.CharField(max_length=30, blank=True, default='Janet')
    lName = models.CharField(max_length=30, default='Doe')
    gender = models.CharField(max_length=30, choices=[('f', 'Female'), ('m', 'Male'), ('nb', 'Non Binary'),
                                                    ('other', 'Other'), ('preferNot', 'Prefer Not To Say')], default=('f', 'Female'))
    streetAddr = models.CharField(max_length=50, default='123 Fake Street')
    city = models.CharField(max_length=30, default='Springfield')
    #below list obtained from https://pythoncircle.com/post/161/list-of-usa-states-in-python-django-format/
    state = models.CharField(max_length=30, choices=[("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode Island","Rhode Island"),("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming")], default='Oregon')
    zipCode = models.CharField(max_length=5, default=12345)
    email = models.EmailField(max_length=256, default='email@example.com')
    phoneNum = models.CharField(max_length=10, default='5555551234')
    country = models.CharField(max_length=30, default='United States')
    dob = models.CharField(max_length=10, default='3-19-1991')
    org = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.userName
