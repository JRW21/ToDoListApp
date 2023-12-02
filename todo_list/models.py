from django.db import models
# This is where database stuff is managed
# Create your models here.
class List(models.Model):#This is a table. After we create this we must create a migration
    item = models.CharField(max_length=200) # CharField is a data type
    completed = models.BooleanField(default = False)
    
    def __str__(self):#This is important for the admin page. Always want for databases
        return self.item #Gives the name on the admin page for each entry in the table
