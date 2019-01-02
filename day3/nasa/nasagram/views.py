from django.shortcuts import render
from django.http import HttpResponse
from IPython.display import Image
import requests
from nasagram.models import NasaComment
from datetime import date
from datetime import datetime
from django.shortcuts import redirect

comment_flag = "DEBUG>>> "

# Create your views here.
def date_selector(request):
    return render(request,'datepicker.html')

def nasa_detail(request,id):
    nasa_comment = NasaComment.objects.get(id=id)
    print(nasa_comment.url)
    return render(request,'detail_view.html',{'nasa_comment':nasa_comment})

def nasa_create(request):
    if (request.method == "GET"):
        print(comment_flag+"GET")
        # Get date from query parameters [check]
        date = request.GET.get('date_selected')
        # Get pic from nasa [check]
        api_key = "NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo"
        r = requests.get(f'https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}')
        url = r.json()["url"]
        # Render image []
        return render(request,'createcomment.html', {'picture': url,'date':date})
    elif (request.method == "POST"):
        print(comment_flag+"Post")
        date = datetime.strptime(request.POST.get('date','2018-01-01'),"%Y-%m-%d").date()
        nasacomment = NasaComment.objects.create(
            rating = request.POST.get('rating',5),
            favorite = request.POST.get('favorite', False) == "on",
            comment = request.POST.get('comment_section',''),
            date = date,
            url = request.POST.get('url','')
        )

        return redirect(f'comment/detail/{nasacomment.id}')
    else:
        return HttpResponse("EEp u Sh0ulD NOT b hEEr")

def nasa_list(request):
    nasa_comments = NasaComment.objects.all()
    return render(request, 'comment_list.html', { 'nasa_comments' : nasa_comments})
