from datetime import date
from django.shortcuts import render

# Create your views here.
all_data = [
    {
        "first_name": "De",
        "last_name": "X",
        "nickname": "",
        "birthday": date(2005, 3, 10),
        "address": "Some random address",
        "contact": "9153552447"
    },
    {
        "first_name": "He",
        "last_name": "X",
        "nickname": "Hexagon",
        "birthday": date(2006, 3, 10),
        "address": "Some other address",
        "contact": "6296538947"
    },
    {
        "first_name": "Te",
        "last_name": "X",
        "nickname": "Texagon",
        "birthday": date(2007, 3, 10),
        "address": "Some another address",
        "contact": "6296539548"
    }
]


def home(request):
    return render(request, 'contacts/home.html', {'data': all_data, })
