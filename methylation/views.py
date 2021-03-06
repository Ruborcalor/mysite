from __future__ import absolute_import, division, print_function, unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.staticfiles.templatetags.staticfiles import static 
from django.views.decorators.csrf import csrf_exempt

# from flask import render_template, request
# from app import app

import json
import plotly
#import plotly.plotly as py
#import chart_studio.plotly as py
import plotly.graph_objs as go

import pandas as pd
import numpy as np


def index(request):

    # cgs = ["cg02228185", "cg01511567", "cg02085507", "cg08370996", "cg04084157", "cg19761273", "cg17274064", "cg20692569", "cg24450312", "cg04528819", "cg06493994", "cg22736354", "cg01820374", "cg07158339", "cg27544190", "cg02479575", "cg03286783", "cg09809672", "cg05442902"]

    # cgs = ["cg24450312", "cg02085507", "cg02479575", "cg09809672", "cg06493994", "cg22736354", "cg04084157", "cg04528819", "cg20692569", "cg07158339", "cg01511567", "cg01820374", "cg03286783", "cg08370996", "cg02228185", "cg19761273", "cg17274064", "cg27544190", "cg05442902"]
    cgs = ['cg16867657', 'cg06639320', 'cg22454769', 'cg21572722', 'cg24079702', 'cg14361627', 'cg19283806', 'cg24724428', 'cg07553761', 'cg11649376', 'cg23500537', 'cg26290632', 'cg16008966', 'cg00329615', 'cg07082267', 'cg04875128', 'cg07547549', 'cg08262002', 'cg08128734', 'cg25410668', 'cg17110586', 'cg14556683', 'cg16054275', 'cg00481951', 'cg06874016'];


    np_valid_pred = np.load(static('/methylation/y_valid_pred.npy'))
    np_valid_real = np.load(static('/methylation/y_valid_real.npy'))

    # Create a trace
    trace = go.Scatter(
        x = np_valid_real,
        y = np_valid_pred,
        mode='markers',
        marker=dict(size=[16] * len(np_valid_real), color=["red"] * len(np_valid_real))
    )

    data = [trace]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render(request, "methylation/display.html", {'cgs':cgs, 'plot':graphJSON})

def about(request):
    return """
        <h1 style='color: red;'>I'm a red H1 heading!</h1>
        <p>This is a lovely little paragraph</p>
        <code>Flask is <em>awesome</em></code>
        """



# @app.route("/click_point", methods=['POST'])
@csrf_exempt
def click_point(request):
    print("CLICK POINT RECEIVED")

    body_unicode = request.body.decode('utf-8')

    body = json.loads(body_unicode)

    print(body)
    print(body["x"])

    if request.method == 'POST':

        # cgs = ["cg02228185", "cg01511567", "cg02085507", "cg08370996", "cg04084157", "cg19761273", "cg17274064", "cg20692569", "cg24450312", "cg04528819", "cg06493994", "cg22736354", "cg01820374", "cg07158339", "cg27544190", "cg02479575", "cg03286783", "cg09809672", "cg05442902"]
        # cgs = ['cg05442902', 'cg20692569', 'cg02228185', 'cg02085507', 'cg27544190', 'cg03286783', 'cg01820374', 'cg07158339', 'cg24450312', 'cg17274064', 'cg04084157', 'cg19761273', 'cg22736354', 'cg06493994', 'cg04528819', 'cg02479575', 'cg09809672', 'cg08370996', 'cg01511567']
        # cgs = ["cg24450312", "cg02085507", "cg02479575", "cg09809672", "cg06493994", "cg22736354", "cg04084157", "cg04528819", "cg20692569", "cg07158339", "cg01511567", "cg01820374", "cg03286783", "cg08370996", "cg02228185", "cg19761273", "cg17274064", "cg27544190", "cg05442902"]
        cgs = ['cg16867657', 'cg06639320', 'cg22454769', 'cg21572722', 'cg24079702', 'cg14361627', 'cg19283806', 'cg24724428', 'cg07553761', 'cg11649376', 'cg23500537', 'cg26290632', 'cg16008966', 'cg00329615', 'cg07082267', 'cg04875128', 'cg07547549', 'cg08262002', 'cg08128734', 'cg25410668', 'cg17110586', 'cg14556683', 'cg16054275', 'cg00481951', 'cg06874016'];





        # spots16 = ["cg19761273", "cg27544190", "cg03286783", "cg01511567", "cg07158339", "cg05442902", "cg24450312", "cg17274064", "cg02085507", "cg20692569", "cg04528819", "cg08370996", "cg04084157", "cg22736354", "cg06493994", "cg02479575"]
        # spots6 = ["cg09809672", "cg22736354", "cg02228185", "cg01820374", "cg06493994", "cg19761273"]
        # spots19 = list(set((spots6 + spots16)))
        # print("Spots 19:")
        # print(spots19)
        # cgs = ["cg19761273", "cg27544190", "cg03286783", "cg01511567", "cg07158339", "cg05442902", "cg24450312", "cg17274064", "cg02085507", "cg20692569", "cg04528819", "cg08370996", "cg04084157", "cg22736354", "cg06493994", "cg02479575"]
        # cgs += ["cg09809672", "cg22736354", "cg02228185", "cg01820374", "cg06493994", "cg19761273"]
        # cgs = list(set(cgs))
        print(cgs)

        np_x_test = np.load(static('/methylation/X_test.npy'))
        print(np_x_test[body['pointNumber']])
        return JsonResponse({
            'x': body["x"], 
            'y': body["y"], 
            'pointNumber': body["pointNumber"], 
            'methyl': np_x_test[body['pointNumber']].tolist(),
            'cgs': cgs,
            'success':True})

