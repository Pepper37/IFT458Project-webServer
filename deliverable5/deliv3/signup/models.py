from django.db import models


# the model User represents any user in the system
# a model is a column in the database
# the fields are the necessary data on the `signup.html` page
# the fields are the rows
class User(models.Model):

    # each of these is a column in the database
    userName = models.CharField(max_length=8, primary_key=True)
    password = models.CharField(max_length=8)
    fName = models.CharField(max_length=30)

    def __str__(self):
        return self.userName
