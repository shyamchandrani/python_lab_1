subjects=["java","python","c++","j2ee","math"]
marks=[]
for subject in subjects:
    mark=float (input(f"enter the marks for{subject}:"))
    marks.append(mark)

total=sum(marks)
average=total/len(subject)

if average >= 80:
    grade='A'
elif average >= 70:
    grade='B' 
elif average >= 60:
    grade='C'
elif average >= 50:
    grade='D'
else:
    grade='F'

print(f"total marks:{total}")
print(f"average marks:{average}")
print(f"grade:{grade}")
