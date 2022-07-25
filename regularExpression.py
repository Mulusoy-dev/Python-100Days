import re

str1="melih ulusoy 27500"

#result=re.findall("melih",str)                                   # str içinde melih'i arar ve liste tipinde değer döndürür
#result_count=len(result)                                         # melih string sayısını verir 
#print(result)
#print(result_count)

##################################################################################################################

# result=re.split(" ",str)                                        # split() metodu ayırma işlemi yapar
# print(result)

##################################################################################################################

# result=re.sub(" ","-",str)                                      # sub() metodu değiştirme işlemi yapar
# print(result)

###################################################################################################################

# result=re.search("melih",str)                                   # search() arama işlemi yapar ve sonucunda bir MATCH objesi döndürür
# print(result)                                                   # span(0,5) demek, aramanan ifadenin 0. karakterden 5. karaktere kadar
#                                                                 # olduğunu gösterir
# result_place=result.span()
# print(result_place)

###################################################################################################################

# result=re.findall("[a-k]",str)                                  # regular expression ifadesi. str içinde a-k arasındaki karakterleri arar ve yazdırır
# print(result)

###################################################################################################################

# result=re.findall("..",str)                                     # str içinde iki basamaklı karakterleri arar
# result2=re.findall("...",str)                                   # str içinde üç basamaklı karakterleri arar
# print(result)
# print(result2)

###################################################################################################################

# result=re.findall("^ul",str)                                    # ^ -> Belirtilen karakterle başlıyor mu?
# print(result)

###################################################################################################################

# result=re.findall("soy$",str)                                   # $ -> Belirtilen karakterle bitiyor mu?
# print(result)

###################################################################################################################

result=re.findall("[0-9]",str1)                                   # Bu projede kullanılabilir. 
# s=[str(integer) for integer in result]                          # Rakamlar bulunup list tipinden int tipine dönüşümü sağlanarak
# s_string="".join(s)                                             # projede kullanılabilir hale getirilir.
# res=int(s_string)

print(result)
print(type(result))

###################################################################################################################



























