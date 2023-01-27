#Import Neccessary Dependencies
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json


#Define Required State of Smart Appliances
all_lights_state =1

#DEF MAIN VIEW
def index(request):
     # GET SMART APPLIANCESES STATE
     global all_lights_state
     #GET DESIRED COMMAND WITH REFERENCES TO RELATIVE NFC TAG WAS TRIGGERED
     a = request.GET.get("command")
     
     #READ FILE TO GET PERSONAL BEARER TOKEN USER HAS SAVED
     #USER MUST DEFINE THEIR OWN FILE!!!!
     with open('/home/mahmoodtahir459/Programming/nfcTagServer/bearer_token.json','r') as bearer_token:
          data = json.load(bearer_token)
     print(data)
     #SET THE DESIRED TOKEN AS A HEADER
     hed = data

     #BASED ON THE REQUIRED COMMAND CONTROL SMART APPLIANCE     
     if(a == '1'):

          if (all_lights_state == 1):
               print("run")
               url = "https://api.smartthings.com/v1/scenes/e5a9f323-7dbc-4020-bc74-2213c661e71b/execute"
               x = requests.post(url,headers=hed)
               all_lights_state = 0
               print(x.text)
          else:
               print("run")
               url ="https://api.smartthings.com/v1/scenes/8f4ccdd6-77fe-4efc-abca-c9d82092cfaa/execute"
               x = requests.post(url,headers=hed)
               all_lights_state = 1
               print(x.text)
     else:
          print("NOT A VALID COMMAND")
     # RETURN HTML WHICH CLOSES THE SITE IF OPENDED VIA NFC TAG
     return render(request, 'index.html')