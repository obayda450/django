import datetime
from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "sara/index.html", {
        "sara_pirthday": now.month == 10 and now.day == 14
    })
