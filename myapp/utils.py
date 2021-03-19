import base64
from io import BytesIO
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import requests
import bs4
import re
import matplotlib.patches as mpatches
from datetime import datetime
today=datetime.today().strftime('%Y-%m-%d')

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('sample graph')
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.tight_layout()
    graph=get_graph()
    return graph

def blank_map():
    world=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world=world[(world.pop_est>0)&(world.name!='Antarctica')]
    fig, ax=plt.subplots(1, figsize=(12,12))
    ax=world.plot(ax=ax,color='lightgray', edgecolor='black', linewidth=.15)
    ax.set_axis_off()
    map = get_graph()
    return map


# def filled_map()