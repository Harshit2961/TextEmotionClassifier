from django.shortcuts import render
import pickle as pkl
# Create your views here.

# for calling index page
def index(request):
    return render(request, 'index.html')


# for loading model
def load(filename):
    file = open(filename, 'rb')
    data = pkl.load(file)
    file.close()
    return data


# for predicting
def predict(request):
    model = load('model.pkl')
    Text = request.GET['text']

    pred = model.predict([Text])[0]
    return render(request, 'predict.html', {'prediction': pred})
    