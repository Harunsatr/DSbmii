from django.http import HttpResponse # type: ignore
from django.shortcuts import render, redirect # type: ignore
from .forms import UploadFileForm
from .models import bmii
from sklearn.tree import DecisionTreeClassifier # type: ignore
from django.conf import settings # type: ignore
import numpy as np # type: ignore
import pandas as pd # type: ignore
import os
import joblib # type: ignore

# def logic_predict(request):
#     if request.method == 'POST':
#         try:
#             age = float(request.POST['age'])
#             height = float(request.POST['height'])
#             weight = float(request.POST['weight'])
#             bmi = float(request.POST['bmi'])
            
#             # Load model from file
#             model_path = 'media/decision_tree_model.joblib'  # Sesuaikan dengan path yang benar
#             model = joblib.load(model_path)

#             # Prediksi
#             X_new = np.array([[age, height, weight, bmi]])
#             prediction = model.predict(X_new)[0]


#             return render(request, 'pages/predict/hasil.html', {
#                 'age': age,
#                 'height': height,
#                 'weight': weight,
#                 'bmi': bmi,
#                 'hasil': prediction,
#             })
#         except (ValueError, TypeError) as e:
#             return render(request, 'pages/predict/hasil.html', {
#                 'error_message': "Input harus berupa angka. Kesalahan: {}".format(e)
#             })
#     return render(request, 'pages/predict/hasil.html')



def index(request):
    return render(request, 'pages/homepage.html')

def about(request):
    return render(request, 'templates/about.html')

def appoinment(request):
    return render(request, 'templates/appoinment.html')

def blog_sidebar(request):
    return render(request, 'blog-sidebar.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def example(request):
    return render(request, 'templates/dataset-example.html')

def contact(request):
    return render(request, 'templates/contact.html')

def department_single(request):
    return render(request, 'department-single.html')

def department(request):
    return render(request, 'templates/department.html')

def doctor_single(request):
    return render(request, 'doctor-single.html')

def doctor(request):
    return render(request, 'doctor.html')

def documentation(request):
    return render(request, 'templates/documentation.html')

def index_copy(request):
    return render(request, 'index-copy.html')

def index2(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            dataset_id = form.instance.id
            context['dataset_id'] = dataset_id
            return redirect('uploads:prepocessing', dataset_id=dataset_id)
    else:
        form = UploadFileForm()
        context['form'] = form
        return render(request, 'templates/service.html', context)



# def index(request):
#     table_html = None
#     selected_label = None
#     columns = []

#     if request.method == 'POST':
#         if 'upload' in request.POST:
#             form = UploadFileForm(request.POST, request.FILES)
#             if form.is_valid():
#                 file = request.FILES['file']
#                 file_path = os.path.join(settings.MEDIA_ROOT, file.name)
#                 id = form.instance.id
                
#                 # Save the file to the media directory
#                 with open(file_path, 'wb+') as destination:
#                     for chunk in file.chunks():
#                         destination.write(chunk)
                
#                 # Read the CSV file using Pandas
#                 df = pd.read_csv(file_path)
#                 columns = df.columns.tolist()
                
#                 # Sort the DataFrame by first column (assuming it's numeric)
#                 df.sort_values(by=df.columns[0], inplace=True)
                
#                 # Convert the DataFrame to HTML
#                 table_html = df.to_html(classes='table table-striped', index=False, escape=False)
                
#                 # Save the DataFrame to session
#                 request.session['table_data'] = df.to_dict(orient='list')
        
#         elif 'select_attributes' in request.POST:
#             selected_attributes = request.POST.getlist('attributes')
#             table_data = request.session.get('table_data')
#             df = pd.DataFrame(table_data)
#             df = df[selected_attributes]  # Filter DataFrame based on selected attributes
#             columns = df.columns.tolist()
            
#             # Sort the DataFrame by first column (assuming it's numeric)
#             df.sort_values(by=df.columns[0], inplace=True)
            
#             table_html = df.to_html(classes='table table-striped', index=False, escape=False)
#             request.session['selected_attributes'] = selected_attributes
        
#         elif 'select_label' in request.POST:
#             selected_label = request.POST.get('selected_label')
#             request.session['selected_label'] = selected_label
            
#             # Train Decision Tree model
#             table_data = request.session.get('table_data')
#             df = pd.DataFrame(table_data)
            
#             X = df.drop(columns=[selected_label])  # Mengambil semua atribut kecuali label
#             y = df[selected_label]  # Memilih label

#             model = DecisionTreeClassifier()
#             model.fit(X, y)

#             # Simpan model ke file
#             model_filename = 'decision_tree_model.joblib'  # atau 'decision_tree_model.pkl' jika menggunakan pickle
#             model_path = os.path.join(settings.MEDIA_ROOT, model_filename)
#             joblib.dump(model, model_path)  # atau 'pickle.dump(model, open(model_path, 'wb'))' jika menggunakan pickle

#             # Simpan lokasi file model ke dalam sesi
#             request.session['model_path'] = model_path
            
#             # Redirect to prediction page
#             return view_predict
            
#     else:
#         form = UploadFileForm()

#     return render(request, 'pages/index.html', {
#         'form': form,   
#         'table_html': table_html,
#         'selected_label': selected_label,
#         'columns': columns
#     })

# # httprespons test


# def predict(request):
#     prediction = None
#     error_message = None
    
#     if request.method == 'POST':
#         try:
#             # Load model from file
#             model_path = request.session.get('model_path')
#             model = joblib.load(model_path)  # atau 'model = pickle.load(open(model_path, 'rb'))' jika menggunakan pickle

#             age = float(request.POST.get('age'))
#             height = float(request.POST.get('height'))
#             weight = float(request.POST.get('weight'))
#             bmi = float(request.POST.get('bmi'))
            
#             X_new = np.array([[age, height, weight, bmi]])
#             prediction = model.predict(X_new)[0]
                
#         except (ValueError, TypeError):
#             error_message = "Input harus berupa angka."
    
#     return render(request, 'page/predict/predict.html', {'prediction': prediction, 'error_message': error_message})

