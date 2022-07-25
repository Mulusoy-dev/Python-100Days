
import os 
import datetime




####################################################################################
# current1=os.chdir('C:\Program Files (x86)\Adobe\Adobe Digital Editions 4.5')
# #print(os.getcwd())

# print(os.listdir(current1))
# os.startfile('DigitalEditions.exe')
#####################################################################################
# current2=os.chdir('C:\ST\STM32CubeIDE_1.10.0\STM32CubeIDE')
# #print(os.getcwd())

# print(os.listdir(current2))
# os.startfile('stm32cubeide.exe')
###########################################################################################################################

os.chdir("C:\melihExcel\melih")
print(os.getcwd())
#os.startfile("measurement123.xlsx")
result2=os.stat("measurement123.xlsx")
print(result2)

print(f'Dosya boyutu: {(result2.st_size/1024)}')                                 #Dosya Boyutu (Kb)

create_file_date=datetime.datetime.fromtimestamp(result2.st_ctime)              #Dosya oluşturulma tarihi
print(f'Dosya oluşturulma tarihi: {create_file_date}')


access_file_date=datetime.datetime.fromtimestamp(result2.st_atime)               #Dosyaya en son erişilme tarihi
print(f'Dosyaya en son erişilme tarihi: {access_file_date}')


modify_file_date=datetime.datetime.fromtimestamp(result2.st_mtime)                #Dosya değiştirlme tarihi
print(f'Dosya degiştirilme tarihi: {modify_file_date}')

##Dosyada yapılan değişikliklerin zamanını göstermek için dosyayı açmaya gerek yok. Zamandan tasarruf, kod verimliliği
#############################################################################################################################


# current=os.chdir('C:\Program Files (x86)\Adobe\Adobe Digital Editions 4.5')
# result=os.stat('DigitalEditions.exe')
# os.startfile('DigitalEditions.exe')
# print(f'Dosya boyutu: {(result.st_size/1024)}')                               #Dosya Boyutu (Kb)
# #print(result.st_ctime)                                                 

# create_file_date=datetime.datetime.fromtimestamp(result.st_ctime)             #Dosya oluşturulma tarihi
# print(f'Dosya oluşturulma tarihi: {create_file_date}')                        

# access_file_date=datetime.datetime.fromtimestamp(result.st_atime)             #Dosyaya en son erişilme tarihi
# print(f'Dosyaya en son erişilme tarihi: {access_file_date}')

# modify_file_date=datetime.datetime.fromtimestamp(result.st_mtime)             #Dosya değiştirlme tarihi
# print(f'Dosya degiştirilme tarihi: {modify_file_date}')

###################################################################################################################################








