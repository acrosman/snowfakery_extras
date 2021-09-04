from pprint import pprint
import json

class JsonReader:
    def heddepts():
        f = open('HigherEdDepartments.json')
        depts = json.load(f)
        deptnames = set()
        for item in depts:
            printme = item["title"]
            deptnames.add(printme)
        pprint(deptnames)
    pass

JsonReader.heddepts()