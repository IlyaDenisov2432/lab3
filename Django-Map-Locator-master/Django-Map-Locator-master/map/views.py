from django.shortcuts import render, redirect
from django.http import HttpResponse
from folium.plugins import FastMarkerCluster

from .models import Obj
#from .forms import ObjForm
import folium
import geocoder
import pandas as pd
import numpy as np
from folium import IFrame
import base64
df = pd.read_csv('map/polnyy_perechen_sportivnyh_obek_0.csv',encoding='WINDOWS-1251', sep=';')
# Create your views here.

np1  = df['Яндекс координата объекта X:'].to_numpy()
newdf=df['Яндекс координата объекта X:'].values.tolist()
newdf2=df['Яндекс координата объекта Y:'].values.tolist()

newdf3=np.array(np.c_[newdf2, newdf])
def is_nan(x):
    return (x != x)
def index(request):
    labels=[]
    data=[]


    objec = Obj.objects.all()
    k=1
    m = folium.Map(location=[58, 38], zoom_start=5)
    for coordinates in objec:
        if coordinates.coordinatex!="" and coordinates.coordinatey!="":
            if all((is_nan((coordinates.coordinatey)),is_nan((coordinates.coordinatex)) ))==False:
                html = '<br>' + coordinates.name + coordinates.address + '<br>' + coordinates.status+'<br>'+coordinates.objtype+'<br>'+coordinates.sporttype
                iframe = folium.IFrame(html)
                popup = folium.Popup(iframe,
                                     min_width=300,
                                     max_width=300)
                folium.Marker(location=[coordinates.coordinatey,coordinates.coordinatex], control_scale=True ,tooltip='Click for more',
                     popup=(popup)).add_to(m)
        k+=1
    m = m._repr_html_()
    context = {
        'm': m,

    }
    context2 = {'labels':labels,'data':data}
    return render(request, 'index.html', context)
