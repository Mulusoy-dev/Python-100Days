import json 


#JSON string to dict

info_user={"name":"melih", "city":["Ankara","Istanbul"]}

#result=json.loads(info_user)
# result=result["city"]
# print(result)


with open("info_user.json","w") as f:
    json.dump(info_user, f)





