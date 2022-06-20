import firebase_admin
from firebase_admin import credentials, firestore

from django import template

# Setup the connexion to the project
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


# CRUD HRS

def create_hr(name_hr, email_hr, mdp_hr, company_hr):
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    # A voir pour ajouter le doc avec un id auto généré
    new_hr = {
        'name': f'{name_hr}',
        'email': f'{email_hr}',
        'mdp': f'{mdp_hr}',
        'company': f'{company_hr}'
    }

    db.collection('hrs').add(new_hr)


def read_hr(name_hr):
    # Only get 1 document or hrs

    col_hrs = db.collection('hrs').where("name", '==', f'{name_hr}')
    hrs = col_hrs.stream()

    for hr in hrs:
        print(f'{hr.id} => {hr.to_dict()}')

def test(email_hr, mdp_hr):
    hr = db.collection('hrs').where("email", '==', f'{email_hr}').where("mdp", '==', f'{mdp_hr}').get()

    for h in hr:
        print(f'{h.id} => {h.to_dict()}')


def read_hrs():
    # Get the hole hrs collection
    col_hrs = db.collection('hrs')
    hrs = col_hrs.stream()

    for hr in hrs:
        print(f'{hr.id} => {hr.to_dict()}')



def read_job():

    collections = db.collection('hrs').document('op6uiPZV4zO5HCBIAzWE').collections()
    for collection in collections:
        for doc in collection.stream():
            print(f'{doc.id} => {doc.to_dict()}')


if __name__ == '__main__':
    # create_hr('Khalida', 'test@gmail.fr', 'azerty', 'ESGI')
    #read_hr('Test')
    test('test@test.fr', 'test')
