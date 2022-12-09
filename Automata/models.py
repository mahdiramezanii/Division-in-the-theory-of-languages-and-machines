from django.db import models

class AutomataModel(models.Model):
    l1=models.CharField(max_length=50,null=True,blank=True)
    l2=models.CharField(max_length=50,null=True,blank=True)
    result=models.CharField(max_length=100)

    def __str__(self):


        return "Automata"