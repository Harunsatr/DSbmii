# apps/core/utils.py
import os
import pandas as pd
from django.conf import settings
from sklearn.tree import DecisionTreeClassifier

def handle_uploaded_file(file):
    file_path = os.path.join(settings.MEDIA_ROOT, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path

def read_csv(file_path):
    df = pd.read_csv(file_path)
    df.sort_values(by=df.columns[0], inplace=True)
    table_html = df.to_html(classes='table table-striped', index=False, escape=False)
    return df, table_html

def filter_attributes(df, selected_attributes):
    df = df[selected_attributes]
    df.sort_values(by=df.columns[0], inplace=True)
    table_html = df.to_html(classes='table table-striped', index=False, escape=False)
    return df, table_html

def train_model(df, selected_attributes, selected_label):
    X = df[selected_attributes]
    y = df[selected_label]
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model
