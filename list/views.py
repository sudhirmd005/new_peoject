from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request,'list/index.html')

def work(request):
    content = "We are still working on this!"
    return render(request, 'list/work.html',{'content':content})

def states(request):
    context = 'List of State in India'
    dict = {
         1: "Andhra_Pradesh",
         2: "Goa",
         3: "Himachal_Pradesh",
         4: "Karnataka",
         5: "Kerala",
         6: "Maharashtra",
         7: "Meghalaya",
         8: "Rajasthan",
         9: "Sikkim",
        10: "Uttar_Pradesh"
    }
    return render(request, 'list/list_state.html',{'dict':dict, 'context':context})

def city(request):
    # andhra pradesh
    dict1 ={
    1: "Visakhapatnam",
    2: "Nellore",
    3: "Guntur",
    4: "Amaravati",
    5: "Srikakulam",
    }
    return render(request, 'list/city.html', {'dict1':dict1})

def city1(request):
    #   goa
    dict2 ={
    1: "Panaji",
    2: "Margao",
    3: "Ponda",
    4: "Curchorem",
    5: "Canacona",
    }
    return render(request, 'list/city1.html', {'dict2':dict2})

def city2(request):
    # Himachal_Pradesh
    dict3 ={
    1: "Shimla",
    2: "Dharamsala",
    3: "Palampur",
    4: "Mandi",
    5: "Paonta Sahib",
    }
    return render(request, 'list/city2.html', {'dict3':dict3})

def city3(request):
    # karnataka
    dict4 ={
    1: "Bengaluru",
    2: "Dharwad",
    3: "Mysuru",
    4: "Belagavi",
    5: "Davanagere",
    }
    return render(request, 'list/city3.html', {'dict4':dict4})
def city4(request):
    # kerala
    dict5 ={
    1: "Kochi",
    2: "Thiruvananthapuram",
    3: "Kozhikode",
    4: "Thrissur",
    5: "Kollam",
    }
    return render(request, 'list/city4.html', {'dict5':dict5})


def city5(request):
    #  maha
    dict6 ={
    1: "Mumbai",
    2: "Pune",
    3: "Nagpur",
    4: "Kolhapur",
    5: "Nashik",
    }
    return render(request, 'list/city5.html', {'dict6':dict6})

def city6(request):
    #  mega
    dict7 ={
    1: "Shillong",
    2: "Tura",
    3: "Nongpoh",
    4: "Cherrapunji",
    5: "Nongstoin",
    }
    return render(request, 'list/city6.html', {'dict7':dict7})

def city7(request):
    #  rajas
    dict8 ={
    1: "Jaipur",
    2: "Jodhpur",
    3: "Kota",
    4: "Bhiwadi",
    5: "Bikaner",
    }
    return render(request, 'list/city7.html', {'dict8':dict8})

def city8(request):
    # sikkim
    dict9 ={
    1: "Gangtok",
    2: "Pelling",
    3: "Lachung",
    4: "Namchi",
    5: "Zuluk",
    }
    return render(request, 'list/city8.html', {'dict9':dict9})

def city9(request):
    # up
    dict10 ={
    1: "Lucknow",
    2: "Kanpur",
    3: "Agra",
    4: "Varanasi",
    5: "Meerut",
    }
    return render(request, 'list/city9.html', {'dict10':dict10})


