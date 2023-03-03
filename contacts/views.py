from datetime import date
from django.shortcuts import render

# Create your views here.
all_data = [
    {
        "id": 1,
        "first_name": "De",
        "last_name": "X",
        "image": "person_avatar.jpeg",
        "nickname": "",
        "birthday": date(2005, 3, 10),
        "address": "Some random address",
        "contact": {"Mobile": "9153552447"}
    },
    {
        "id": 2,
        "first_name": "He",
        "last_name": "X",
        "image":"person_avatar.jpeg",
        "nickname": "Hexagon",
        "birthday": date(2006, 3, 10),
        "address": "Some other address",
        "contact": {"Work":"6296538947", "Mobile":"9454785960"}
    },
    {
        "id": 3,
        "first_name": "Te",
        "last_name": "X",
        "image":"person_avatar.jpeg",
        "nickname": "Texagon",
        "birthday": date(2007, 3, 10),
        "address": "Some another address",
        "contact": {"Mobile":"6296539548"}
    }
]


def home(request):
    return render(request, 'contacts/home.html', {'data': all_data, })


def details(request, id):
    particular_detail = all_data[id-1]
    return render(request, 'contacts/details.html', {
        "title":f"{particular_detail['first_name']} {particular_detail['last_name']}",
        "contact":particular_detail['contact'],
        "address":particular_detail['address'] or None,
        "profile_image":particular_detail['image'] or None,
        "birthday":particular_detail['birthday'] or None,
        "nickname": particular_detail['nickname'] or None,
    })
