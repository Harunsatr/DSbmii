from django.shortcuts import render
import pandas as pd
import os
from django.conf import settings
from main.models import bmii

# Create your views here.
def prepocessing(request, dataset_id):
    context = {}
    dataset = bmii.objects.get(id=dataset_id)
    dataset_path = os.path.join(settings.MEDIA_ROOT, dataset.file.name)
    df = pd.read_csv(dataset_path)
    columns = df.columns.tolist()
    show_data = df.head(10).to_html(classes='table table-striped', index=False, escape=False)
    context['columns'] = columns
    context['dataset_id'] = dataset_id
    context['show_data'] = show_data
    return render(request, 'pages/uploads/index.html', context)
