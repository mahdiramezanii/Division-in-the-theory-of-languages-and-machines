from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .division import division_operation
from Automata.models import AutomataModel

class HomeView(View):



    def post(self,request):

        L1=request.POST.get("L1")
        L2=request.POST.get("L2")

        division_operation(L1=L1,L2=L2)



        return redirect("Automata:result")

    def get(self,request):


        return render(request,"Automata/index.html")


class ResultView(View):

    def get(self,request):

        automata=AutomataModel.objects.all().last()

        return render(request,"Automata/result.html",{"automata":automata})