from django.shortcuts import render
from .models import InfoDB
# Create your views here.

def indexRender(request):
    return render(request, 'index.html')

def noticeRender(request):
    return render(request, 'notice.html')

def signinRender(request):
    return render(request, 'signin.html')

def passwordCheck(request):
    password = request.POST['password']

    #密码检测
    print(password)
    standardPasswordList = ['80808000',
                            '80008080',
                            '123456']
    if password not in standardPasswordList:
        return render(request, 'passwordFalse.html')
    else:
        return render(request, 'skipping.html', context={'password': password})



def releaseRender(request):
    return render(request, 'release.html')

def postRelease(request):
    date = request.POST['date']
    entryTime = request.POST['entryTime']
    takeOffTime = request.POST['takeOffTime']
    SIDAps = request.POST['SIDAps']
    SIDApsICAO = request.POST['SIDApsICAO']
    STARAps = request.POST['STARAps']
    STARApsICAO = request.POST['STARApsICAO']
    flightDistance = request.POST['flightDistance']
    route = request.POST['route']
    planeType = request.POST['planeType']
    flightLevel = request.POST['flightLevel']
    cruiseSpeed = request.POST['cruiseSpeed']
    remarks = request.POST['remarks']

    print(date, entryTime, takeOffTime, SIDAps, SIDApsICAO,
          STARAps, STARApsICAO, flightDistance, route,
          planeType, flightLevel, cruiseSpeed, remarks,)

    InfoDB.objects.create(date=date,
                          entryTime=entryTime,
                          takeOffTime=takeOffTime,
                          SIDAps=SIDAps,
                          SIDApsICAO=SIDApsICAO,
                          STARAps=STARAps,
                          STARApsICAO=STARApsICAO,
                          flightDistance=flightDistance,
                          flightLevel=flightLevel,
                          route=route,
                          planeType=planeType,
                          cruiseSpeed=cruiseSpeed,
                          remarks=remarks,)

    return render(request, 'notice.html', context={'date': date,
                                                   'entryTime': entryTime,
                                                   'takeOffTime': takeOffTime,
                                                   'SIDAps': SIDAps,
                                                   'SIDApsICAO': SIDApsICAO,
                                                   'STARAps': STARAps,
                                                   'STARApsICAO': STARApsICAO,
                                                   'flightDistance': flightDistance,
                                                   'route': route,
                                                   'planeType': planeType,
                                                   'flightLevel': flightLevel,
                                                   'cruiseSpeed': cruiseSpeed,
                                                   'remarks': remarks,
                                                   })



