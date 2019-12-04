import json
student = {
    'id': 2002324,
    'name': '홍길동',
    'history' : [
        {
            'date':  '2018-03-11', 'lang':'java'
        },
        {
            'date': '2018-07-23','lang':'python'
        },
]
}

js = json.dumps(student, ensure_ascii=False, indent=4)
print(js)

student1 = json.load(js)
print(student1)

print(type(js))
#s ='"id": "{}", "name": "{}"'.format(student.get("id"),student.get("name")) :

#s = "{" + "}"
#print("s")