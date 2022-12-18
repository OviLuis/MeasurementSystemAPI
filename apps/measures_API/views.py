import pandas as pd

from django.shortcuts import render
from django.http import HttpResponse

from .models import Measure


def index(request):
    template = 'index.html'
    return render(request, template)


def download_csv_file(request):
    qs = Measure.objects.all().values('device_id', 'measure_value', 'measure_unit', 'measure_date')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="measures.csv"'

    df = pd.DataFrame.from_records(qs)

    df.to_csv(response)

    return response

