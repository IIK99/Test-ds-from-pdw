# syntax list
listContoh = ["hello", 1, 2, 3, True]

# access data list
print(listContoh)
print("This is a access data list")
print(listContoh[0])
print(listContoh[1])
print(listContoh[2])
print(listContoh[3])
print(listContoh[4])

# negative list syntax
print("This is a negative list")
print(listContoh[-1])
print(listContoh[-2])
print(listContoh[-3])
print(listContoh[-4])
print(listContoh[-5])

# range of indexes
print("This is a list range of indexes")
print(listContoh[1:3])
print(listContoh[1:])
print(listContoh[:3])
print(listContoh[1:4:2])
print(listContoh[:])
print(listContoh[-4:-1])
print(listContoh[-5:2])
print(listContoh[0:-2])

# change data
print("change data of a list")
listContoh[0] = "hi"
listContoh[-1] = False
print(listContoh)

# add data
print("add data of a list")
listContoh.append("python")
listContoh.insert(1, "mari belajar python")
print(listContoh)

# delete data
print("delete data of a list")
del listContoh[0]
listContoh.remove("mari belajar python")
listContoh.pop()  # remove last element
# listContoh.clear() # delete all elements
print(listContoh)

# loop trough a list
print("loop through a list")
newListDataItems = ["hello", 1, 2, 3, True]
for i in newListDataItems:
    print(i)

# check if list contains
print("check if list contains")
newDataList = ["hello", False]
if "hello" in newDataList:
    print("hello is in list")
else:
    print("hello is not in list")

# length of list
print("length of list")
lengthList = [1, 2, 3, "mari belajar python", True]
print(len(lengthList))

# copy list
print("copy list")
listCopy = ["kita", "akan", "mencoba", "copy", "list", "ini"]
print(listCopy)

newList = listCopy
newList[1] = "test"

newList1 = listCopy.copy()
newList1[2] = "baru"

print(newList)
print(newList1)

# concat list
print("concat list")
listConcat = ["sekarang", "kita", "akan", "menggabungkan", "suatu", "list"]
print(listConcat)

list1 = [1, 2, 3]
addedList = [True]

gabungkanList = list1 + listConcat
print(gabungkanList)

gabungkanList.extend(addedList)  # extend adalah gabungkan list dari paling belakang
print(gabungkanList)

# find index
print("find index")
nameList = ["chika", "adam", "fajar", "ibu rina", "bapak ikmal"]
findIndex = nameList.index("ibu rina")
print(findIndex)

# findIndex1 = nameList.index('nisa')
# print(findIndex1) # error tidak menemukan yang namanya nisa

# sort list / masih menggunakan nameList
print("sort list")
nameList.sort()  # menyesuaikan dengan abjad ascending
print(nameList)
nameList.reverse()  # kebalikannya descending
print(nameList)

# 2d list
print("2d list")
listTwoDimension = [
    ["laptop", "mobile", "pc"],
    ["bersepeda", "jalan", "makan"],
    ["sepatu", "jaket", "kaca mata"],
]

print(listTwoDimension)
print(listTwoDimension[2])
print(listTwoDimension[2][0])
