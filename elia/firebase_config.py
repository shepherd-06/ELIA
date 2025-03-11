import os
import firebase_admin
from firebase_admin import credentials, firestore

# Absolute path to the service account key file
cert_path = os.path.join(os.path.dirname(__file__), 'awesome-elia-firebase-adminsdk-fbsvc-d927ee12b2.json')

cred = credentials.Certificate(cert_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

