import pandas as pd

readData = pd.read_excel('Locker.xlsx')

Test = str(readData.iloc[18,0])

i = int(Test[5:])
print(i)

x = i + 10

editData = str('Test_%d' %x)

print(readData)
print(Test)
print(editData)

fixData = readData.replace([Test],[editData])

print(fixData)


writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')

fixData.to_excel(writeData,index = False)
writeData.save()
