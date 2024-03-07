#lists and tuples

tupl = (1,2,8,["klsjd",'kkjsj'],'jks')

print(type(tupl))

tupl[3][0] = 55 #list in tuple is immutable but can't change range of list in tuple

k = tupl[0:2]

print(k)
print("type os k is ",type(k))

print(tupl)
print(tupl[3])

print((tupl[1])+(tupl[2])+tupl[3][1])