from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
import os
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import _utils

import firesql

from django import template


# from . import query_firestore


def index(request):
    return render(request, 'index.html')


def log(request):
    return render(request, 'log.html')


def log_form(request):
    # print("Inside View")
    if request.method == "POST":
        # print("Inside post")
        name_hr = request.POST.get("name_hr", None)
        email_hr = request.POST.get("email_hr", None)
        mdp_hr = request.POST.get("mdp_hr", None)
        company_hr = request.POST.get("company_hr", None)
        # print(email_hr)
        # print(os.getcwd())
        cred = credentials.Certificate("./website/serviceAccountKey.json")

        firebase_admin.initialize_app(cred)

        db = firestore.client()

        new_hr = {
            'name': f'{name_hr}',
            'email': f'{email_hr}',
            'mdp': f'{mdp_hr}',
            'company': f'{company_hr}'
        }

        db.collection('hrs').add(new_hr)

    return render(request, 'log.html')


def login_form(request):
    print("Inside View")
    if request.method == "GET":
        print("Inside get")

        email_hr = request.GET.get("email_hr", None)
        mdp_hr = request.GET.get("mdp_hr", None)

        cred = credentials.Certificate("./website/serviceAccountKey.json")

        firebase_admin.initialize_app(cred)

        db = firestore.client()

        hr = db.collection('hrs').where("email", '==', f'{email_hr}').where("mdp", '==', f'{mdp_hr}')
        hr.get()

        print(hr)

        context = {
            'email_hr': f'{email_hr}',
            'mdp_hr': f'{mdp_hr}'
        }

    return render(request, 'home.html', context)


def home(request, context):
    print("Inside Home")
    cred = credentials.Certificate("./website/serviceAccountKey.json")
    db = firestore.client()

    name_hr = request.GET.get("name_hr", None)
    email_hr = request.GET.get("email_hr", None)
    mdp_hr = request.GET.get("mdp_hr", None)

    hr = db.collection('hrs')
    hr.where("email", '==', f'{context.email_hr}').get()
    hr.where("mdp", '==', f'{context.mdp_hr}').get()
    hr.where("name", '==', f'{name_hr}').get()

    hr_id = hr.doc(id).get()

    print(name_hr)

    context = {
        'email_hr': f'{email_hr}',
        'mdp_hr': f'{mdp_hr}',
        'name_hr': f'{name_hr}'
    }

    #    collections = hr.document('$hr_id').collection('job_description')
    #    for collection in collections:
    #        for doc in collection.stream():
    #            print(f'{doc.id} => {doc.to_dict()}')

    # doc_hr = db.collection('hrs').document()
    # id = doc_hr.id

    return render(request, 'home.html', context)


def user_profile(request, context):
    cred = credentials.Certificate("./website/serviceAccountKey.json")
    db = firestore.client()

    name_hr = request.GET.get("name_hr", None)
    email_hr = request.GET.get("email_hr", None)
    mdp_hr = request.GET.get("mdp_hr", None)

    hr = db.collection('hrs')
    hr.where("email", '==', f'{context.email_hr}').get()
    hr.where("mdp", '==', f'{context.mdp_hr}').get()
    hr.where("name", '==', f'{name_hr}').get()

    context = {
        'email_hr': f'{email_hr}',
        'mdp_hr': f'{mdp_hr}',
        'name_hr': f'{name_hr}'
    }

    return render(request, 'user_profile.html', context)


def my_posts(request):
    return render(request, 'my_posts.html')


def post_generator(request):
    return render(request, 'post_generator.html')


def upload_post(request):
    return render(request, 'upload_post.html')


def get_profile(request):
    # TODO
    return None


def faq(request):
    return render(request, 'pages-faq.html')
