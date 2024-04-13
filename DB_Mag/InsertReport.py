import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

# Use a service account.
def InsertReport(id,name_en,author,public,year,img,subject,lang,isbn,feeling):
    n = 0
    cred = credentials.Certificate('DB_Mag/SDK.json')
    if not firebase_admin._apps:
        app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    docs = db.collection("LMS").document("Tables").collection("BookReport")
    data = {
        "AccID":id,
        "BookName_EN":name_en,
        "Author":author,
        "Publication":public,
        "Publication_Year":year,
        "img":img,
        "Subject":subject,
        "Language":lang,
        "ISBN":isbn,
        "Feeling":feeling,
        "Date":datetime.now()
    }

    docs.document().set(data, merge=True)
    