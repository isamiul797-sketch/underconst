from django.shortcuts import render
from uc.models import UnderConstruction
from decouple import config

class UnderConstructionMidlleware:
    def __init__(self,get_reponse):
        self.get_response = get_reponse
        print("One Time Initialization")


    def __call__(self, request):
        if request.user.is_staff:
            return self.get_response(request)
        
        uc_key = config("MAINTAINCE_BYPASS_KEY")
        if 'u' in request.GET and request.GET['u'] == uc_key:
            request.session['bypass_maintainance'] = True
            request.session.set_expiry(0)

        if request.session.get('bypass_maintainance'):
            return self.get_response(request)
        
        try:
            uc = UnderConstruction.objects.first()
            if uc and uc.is_under_construction:
               context ={
                   "uc_note": uc.uc_note,
                   "uc_duration":uc.uc_duration
               }
               return render (request,'uc/underc.html',context)
        except:
            pass
        return self.get_response(request)