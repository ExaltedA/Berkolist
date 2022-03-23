from django.shortcuts import render
from list.models import Nominee, DivTexts


# Create your views here.
def nominee_list(request):
    search_result = {}

    list_response = Nominee.objects.all().order_by('standings')
    search_result['list'] = list_response

    divs_response = DivTexts.objects.get(position="First Text")
    search_result['div1'] = divs_response

    divs_response = DivTexts.objects.get(position="Second Text")
    search_result['div2'] = divs_response

    return render(request, 'nominee_list.html', {'search_result': search_result})
