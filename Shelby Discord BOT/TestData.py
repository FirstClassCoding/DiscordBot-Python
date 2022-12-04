import pandas as pd

readData = pd.read_excel('Data.xlsx')
#อ่านข้อมูลที่มีอยู่ในไฟล์

#newData = pd.DataFrame({'Name' : ['Test'] , 'Date' : ['Test']})

#สร้างข้อมูลใหม่

#newData = readData.replace('Somchai' , 'Mari')
#แทนค่าข้อมูล

updateData = [readData , newData]
result = pd.concat(updateData)
#รวมข้อมูล

writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
#สร้างการเขียนไฟล์

result.to_excel(writeData,index = False)
writeData.save()

print(readData)
#print('******')
#readData = pd.read_excel('Data.xlsx')
#print(readData)
