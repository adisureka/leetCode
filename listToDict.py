lst = [1, 1, 1, 7, 8, 5, 5, "hello"]
dict_ = {}
for i in range(len(lst)):
 	print(lst[i])
 	if(lst[i] not in dict_):
 		dict_[lst[i]] = 1
 	else:
 		dict_[lst[i]] += 1 
print(dict_)