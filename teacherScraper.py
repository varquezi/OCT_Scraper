from helpers import Degree, Teacher
import requests
from pathlib import Path
import json
import csv

def getData(octID: int, octcsid: str):
    payload1 = {
        'id': octID,
        'csid': octcsid
    }
    req1Status = requests.get('https://apps.oct.ca/FindATeacherWebApiWrapper/api/publicregister/clientinfo', params = payload1)
    if (not req1Status.ok):
        return -1
    req1JSON = req1Status.json()
    if (not req1JSON):
        return -2
    req1 = req1JSON['value'][0]
    teacher = Teacher(octID, req1["phoenix_firstname"], req1["phoenix_middlename"], req1["phoenix_surname"])
    payload2 = {
        'id': octID,
        'guid': req1["contactid"],
        'csid': octcsid
    }

    req2Status = requests.get('https://apps.oct.ca/FindATeacherWebApiWrapper/api/publicregister/degreeCredentials', params = payload2)
    if (not req2Status.ok):
        return -1
    req2JSON = req2Status.json()
    if (not req2JSON):
        return -2
    req2 = req2JSON['value']
    for deg in req2:
        degree = Degree(deg["phoenix_degree_name"],(int(deg["phoenix_issueddate"][:4]), int(deg["phoenix_issueddate"][5:7]), int(deg["phoenix_issueddate"][8:])), deg["phoenix_institution_name"])
        teacher.addDegree(degree)
    
    return teacher

def getTeachers(start: int, end: int, octcsid: str):
    teacherDict = {"data":[]}
    for i in range(start, end + 1):
        data = getData(i, octcsid)
        if type(data) is not int:
            teacherDict["data"].append(data.__dict__)

    if (len(teacherDict["data"]) < 1):
        return -1
    
    with open("oct_data.csv", "w", newline='') as f:
        fieldnames = teacherDict["data"][0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for teacher in teacherDict["data"]:
            writer.writerow(teacher)
            
    return 0
        