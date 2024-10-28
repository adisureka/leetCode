lst = [80, 80, 66, 81, 72, 73, 80, 84, 48, 47, 67, 94, 87, 69, 61, 69, 81, 64, 77, 49]

grade = []
dict_ = {}
for i in range(len(lst)):
       if(lst[i] > 90):
              grade.append("A")
       elif(lst[i] <= 90 and lst[i] > 80):
              grade.append("B")
       elif(lst[i] <= 80 and lst[i] > 70):
              grade.append("C")
       elif(lst[i] <= 70 and lst[i] > 60):
              grade.append("D")
       else:
              grade.append("F")
print(grade)

for i in range(len(grade)):
       key = grade[i]
       if key in dict_:
              dict_[key] = dict_[key] + 1
       else:
              dict_[key] = 1
              
print(dict_)