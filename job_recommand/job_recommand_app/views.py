from django.shortcuts import render, HttpResponse
from job_recommand_app.models import Account


# Create your views here.
def test(request):
    # user = Account(name="chinlly", pwd="123456")
    # user.save()
    test_user = Account.objects.all()
    return render(request, "test.html", {'user': test_user})
