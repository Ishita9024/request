import requests
import json
course_url=requests.get('http://saral.navgurukul.org/api/courses')
course_file=course_url.json()

with open("courses.json","w") as file:
    json.dump(course_file,file,indent=4)
course=0
while course<len(course_file["availableCourses"]):
    print(course+1,":",course_file["availableCourses"][course]["name"],"ID:",course_file["availableCourses"][course]["id"])
    course+=1
print("")

course_id=int(input("enter the course no. :-"))
print(course_id,":",course_file["availableCourses"][course_id-1]["name"])
Id=course_file["availableCourses"][course_id-1]["id"]
Url='http://saral.navgurukul.org/api/courses/'+str(Id)+'/exercises'
parents_url=requests.get(Url)
parents_file=parents_url.json()

with open("parents.json","w") as file1:
    json.dump(parents_file,file1,indent=4)
serial_no=0
for parent in parents_file["data"]:
    if parent["childExercises"]==[]:
        print(serial_no+1,parent["name"])
        print("     ",parent["slug"])
    else:
        print(serial_no+1,parent["name"])
        k=0
        while k<len(parent["childExercises"]):
            print("     ",k+1,":",parent["childExercises"][k]["name"])
            k+=1
    serial_no+=1
print("")

parent_id=int(input("enter the parent no. :- "))
print(parent_id,":",parents_file["data"][parent_id-1]["name"])
if parents_file["data"][parent_id-1]["childExercises"]==[]:
    print(parents_file["data"][parent_id-1]["slug"])
    pid=parents_file["data"][parent_id-1]["id"]
    pslug=parents_file["data"][parent_id-1]["slug"]
    parent_api='http://saral.navgurukul.org/api/courses/'+str(pid)+'/exercise/getBySlug?slug='+pslug
    slug_url=requests.get(parent_api)
    slug_file=slug_url.json()
    with open("slug.json","w") as file3:
        json.dump(slug_file,file3,indent=4)
    print(slug_file["content"])
else:
    k=0
    while k<len(parents_file["data"][parent_id-1]["childExercises"]):
        print("     ",k+1,":",parents_file["data"][parent_id-1]["childExercises"][k]["name"])
        k+=1
    child_id=int(input("enter the child no.:- "))
    slug=parents_file["data"][parent_id-1]["childExercises"][child_id-1]["slug"]
    id1=parents_file["data"][parent_id-1]["childExercises"][child_id-1]["id"]
    child='http://saral.navgurukul.org/api/courses/'+str(id1)+'/exercise/getBySlug?slug='+slug
    child_url=requests.get(child)
    child_file=child_url.json()
    with open("child.json","w") as file2:
        json.dump(child_file,file2,indent=4)
    print(child_file["content"])
    
    