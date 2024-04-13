import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

# Use a service account.
def Login(id,pwd):
    login = False
    n = 0
    cred = credentials.Certificate('DB_Mag/SDK.json')
    if not firebase_admin._apps:
        app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    docs = db.collection("LMS").document("Tables").collection("Account")
    records = docs.where(filter=FieldFilter("AccID", "==", id)).where(filter=FieldFilter("Password", "==", pwd)).get()
    account = []
    for doc in records:
        account.append(doc.to_dict())
    return account