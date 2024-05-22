# syntax list
listContoh = ["hello", 1, 2, 3, True]

# access data list
print(listContoh)
print(listContoh[0])
print(listContoh[1])
print(listContoh[2])
print(listContoh[3])
print(listContoh[4])

# negative list syntax
print(listContoh[-1])
print(listContoh[-2])
print(listContoh[-3])
print(listContoh[-4])
print(listContoh[-5])

# range of indexes
print(listContoh[1:3])
print(listContoh[1:])
print(listContoh[:3])
print(listContoh[1:4:2])
print(listContoh[:])
print(listContoh[-4:-1])
print(listContoh[-5:2])
print(listContoh[0:-2])

# change data
listContoh[0] = "hi"
listContoh[-1] = False
print(listContoh)

# add data
listContoh.append("python")
listContoh.insert(1, "mari belajar python")
print(listContoh)

# delete data
del listContoh[0]
listContoh.remove("mari belajar python")
listContoh.pop()  # remove last element
# listContoh.clear() # delete all elements
print(listContoh)

# loop trough a list
newListDataItems = ["hello", 1, 2, 3, True]
for i in newListDataItems:
    print(i)

# check if list contains
newDataList = ["hello", False]
if "hello" in newDataList:
    print("hello is in list")
else:
    print("hello is not in list")

# length of list
lengthList = [1, 2, 3, "mari belajar python", True]
print(len(lengthList))

# copy list
listCopy = ["kita", "akan", "mencoba", "copy", "list", "ini"]
print(listCopy)

newList = listCopy
newList[1] = "test"

newList1 = listCopy.copy()
newList1[2] = "baru"

print(newList)
print(newList1)

# concat list
listConcat = ["sekarang", "kita", "akan", "menggabungkan", "suatu", "list"]
print(listConcat)

list1 = [1, 2, 3]
addedList = [True]

gabungkanList = list1 + listConcat
print(gabungkanList)

gabungkanList.extend(addedList)  # extend adalah gabungkan list dari paling belakang
print(gabungkanList)

# find index
nameList = ["chika", "adam", "fajar", "ibu rina", "bapak ikmal"]
findIndex = nameList.index("ibu rina")
print(findIndex)

# findIndex1 = nameList.index('nisa')
# print(findIndex1) # error tidak menemukan yang namanya nisa

# sort list / masih menggunakan nameList
nameList.sort()  # menyesuaikan dengan abjad ascending
print(nameList)
nameList.reverse()  # kebalikannya descending
print(nameList)

# 2d list
listTwoDimension = [
    ["laptop", "mobile", "pc"],
    ["bersepeda", "jalan", "makan"],
    ["sepatu", "jaket", "kaca mata"],
]

print(listTwoDimension)
print(listTwoDimension[2])
print(listTwoDimension[2][0])