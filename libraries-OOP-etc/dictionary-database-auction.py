#create an empty dictionary
# empty_dictionary={}


# #Nesting a List in a Dictionary
travel_log={
     "France":["Paris","Lille","Dijon"],
     "Germany":["Berlin","Hamburg","Stuttgart"],
     "Turkey":["Ankara","İstanbul","İzmir"]
}

 #Nesting a Dictionary in a Dictionary
dict_travel_log={
     "France": {"cities_visited":["Paris","Lille","Dijon"], "total_visited":20},
     "Germany": {"cities_visited":["Berlin","Hamburg","Stuttgart"], "total_visited":25},
     "Turkey": {"cities_visited":["Ankara","İstanbul","İzmir"], "total_visited":50}
}

# #Nesting a Dictionary in a List
list_travel_log=[
     {
     "country": "France",
     "cities_visited":["Paris","Lille","Dijon"],
     "total_visited":20
     },

     {
     "country": "Germany",
     "cities_visited":["Berlin","Hamburg","Stuttgart"],
     "total_visited":25
     },
    
     {
     "country": "Turkey",
     "cities_visited":["Ankara","İstanbul","İzmir"],
     "total_visited":50
     }
]

#print(list_travel_log[0])


###############################################################################################
#New İtem add in Dictionary

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country,visits,cities):
#     travel_log.append({"country":country,"visits":visits,"cities":cities})


# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

###############################################################################################
# Auction Program

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
#name=input("What is your name?:")                                                # name -> Dict(Key)
#bid=input("What's your bid?: $")                                                 # bid -> Dict(Value)
#if_bid_else=input("Are there any other bidders? Type 'yes' or 'no'. ")
greater=0
auction_dict={}
while True:

    name=input("What is your name?:")                                                # name -> Dict(Key)
    bid=int(input("What's your bid?: $"))
    if_bid_else=input("Are there any other bidders? Type 'yes' or 'no'. ")
    if if_bid_else=="yes":
        auction_dict[name]=bid
        #print(auction_dict)

    elif if_bid_else=="no":
        auction_dict[name]=bid
        print(auction_dict)
        for key in auction_dict:
            if auction_dict[key]>greater:
                greater=auction_dict[key]
                new_name=key
        print(f"The winner is {new_name} with a bid of {greater}")
            
        break
    
    








