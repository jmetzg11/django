from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name='home.html'

import pandas as pd
import joblib
linear_model=joblib.load('mysite/models/linear.pkl')

def linear_default(request):
    features={}
    features['displacement']=int(190)
    features['horsepower']=int(100)
    features['weight']=int(2900)



    context={'features': features}
    return render(request, 'linear.html', context)

def linear_predict(request):
    if request.method=='POST':
        features={}
        features['displacement']=request.POST.get('disVal')
        features['horsepower']=request.POST.get('hrsVal')
        features['weight']=request.POST.get('weiVal')


    input_frame=pd.DataFrame({'x':features}).transpose()
    prediction=linear_model.predict(input_frame)
    context={'prediction': prediction, 'features': features}
    return render(request, 'linear.html', context)

from .graph_functions import blank_map, filled_map

def view_blank_map(request):
    blank=blank_map()
    return render(request, 'view_map.html', {'blank': blank})

def view_filled_map(request):
    filled=filled_map()
    return render(request, 'view_map.html', {'filled': filled})


class InfoPageView(TemplateView):
    template_name='info.html'