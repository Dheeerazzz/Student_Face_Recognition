import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': #paste URL of your DB here
})
 
ref = db.reference('Students')
 
data = {
            "11111":
    {
         "name": "tHe WeeKnD",
            "major": "singer",
            "starting_year":2,
            "standing": "2458584930",
            "year": "",
            "last_attendance_time": "2022-12-11 00:54:34"
    },
        "2255":
    {
         "name": "Dheeraj",
            "major": "AI&DS",
            "starting_year":2,
            "standing": "2458584930",
            "year": "",
            "last_attendance_time": "2022-12-11 00:54:34"
    },
    "1234":
    {
         "name": "pspk",
            "major": "Arts",
            "starting_year": 2,
            "standing": "1234566779",
            "year": "",
            "last_attendance_time": "2022-12-11 00:54:34"
    },
       "169":
    {
         "name": "Benedict cumberbatch",
            "major": "Black Magic",
            "starting_year": 1,
            "standing": "6969696969",
            "year": "",
            "last_attendance_time": "2022-12-11 00:54:34"
    },
    
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 3,
            "standing": "575849393",
            "year": "",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 1,
            "standing": "1234546",
            "year": "",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "21L31A54B1":
        {
            "name": "Dheeraj Surakasula",
            "major": "AI & DS",
            "starting_year": 4,
            "standing": "9247169668",
            "year": "",
            "last_attendance_time": "2022-12-11 00:54:34"
        },

}
 
for key, value in data.items():
    ref.child(key).set(value)
