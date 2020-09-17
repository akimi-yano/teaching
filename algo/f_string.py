

students = [{'first_name':"Akimi",'last_name':"Yano"}]

def iterateDictionary(students):
    for i in range(0, len(students), 1):
        first = students[i]['first_name']
        last = students[i]['last_name']
        print(f"first_name - {first}, last_name - {last}.")

iterateDictionary(students)