
import requests
import json                               ## Siteden gelen veriler json formatında olduğundan dolayı verileri direk alamıyoruz
                                          ## bunun için Json dan Dict (Dictionary) veri tipine dönüşüm yapılması gerekmektedir


res=requests.get("https://karabuk-loko.tmstechnic.com/manifest.json")             # get() fonksiyonu ile talep iletilir 
res=json.loads(res.text)                                                          # res.text-> json formatında loads() metodu ile Dict tipine dönüşüm yapılır
                                                                                  # Böylece verileri alabiliriz   

for i in res:                                                                     # bilgiler alındı
    print(res)                                                                                    
#print(res["name"])
#print(type(res))

