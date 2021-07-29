from pip._vendor import requests 


print("---------------------")
print("| TruckersMp Python |")
print("---------------------")
print("This is a program to access and display data from the TruckersMP API.")
print("------------------------------------------------")
print("| Pick one of the options from the list below: |")
print("| 1 | Lookup an event                          |")
print("| 2 | Lookup a player                          |")
print("| 3 | Lookup a player's bans                   |")
print("| 4 | View the tmp rules                       |")
print("------------------------------------------------")
print("Pick an option now")
picked_option = input("")



# if statements for options above 
if picked_option == '1':
    print("-------------------------------------------------------")
    print("Please say the ID of the event.")
    event_ID = input("")
    if event_ID == "":
        print("-------------------------------------------------------")
        print("Please say an EventID.")
    else:
     try: 
         geteventinfo = f"https://api.truckersmp.com/v2/events/{event_ID}"
         r = requests.get(geteventinfo)
         data = r.json()["response"]
         print("-------------------------------------------------------")
         print(f"The event info for {event_ID} will follow soon.")
         print("-------------------------------------------------------")
     
         message_2 = print("Do you want to do a basic lookup? Yes / No")
         type = input("")
         print("-------------------------------------------------------")
         # make the request to the api here
         if type == "no": 
          print("----------------------------------------------")
          print("| This will print all info found on the api! |")
          print("----------------------------------------------")
          print(data)
          
         elif type == "yes":
            print("---------------------")
            print(f"Basic Info for {event_ID}")
            print("---------------------") 
            print(f"Event Name: {data['name']}")
            print(f"Event Type: {data['event_type']['name']}")
            print(f"Event Game: {data['game']}")
            print(f"Event Server: {data['server']['name']}")
            print(f"Departure Location: {data['departure']['location']} | Departure City: {data['departure']['city']}")
            print(f"Arrival Location: {data['arrive']['location']} | Arrival City: {data['arrive']['city']}")
            print(f"Event Starts At (time/date): {data['start_at']}")  
            print("----------------------------------------------------------------------------------------------------------------------------------")
            print(
                f"| End of basic infomation. To find more visit https://truckersmp.com/events/{event_ID} or say no to 'Do you want to do a basic lookup'. |")
            print("----------------------------------------------------------------------------------------------------------------------------------")
         else: 
             print("Please say yes or no. ")
     except:
         print("-------------------------------------------------------")
         print("There is no event for that ID. Please try again!!")
         print("-------------------------------------------------------")

                
elif picked_option == '2':
    print("Please say the TruckersmpID of the player.")
    tmp_ID = input("")
    try: 
        getplayerinfo = f"https://api.truckersmp.com/v2/player/{tmp_ID}"
        r = requests.get(getplayerinfo)
        data = r.json()["response"]
        print("-------------------------------------------------------------")
        print(f"The Player info for {tmp_ID} will follow soon.")
        print(f"------------------------------------------------------------")
        
    # make request to the api here
elif picked_option == '3':
    print("Please say the TruckersmpID of the player.")
    tmp_ID_2 = input("")
    # make request to the api here 

elif picked_option == '4':
    print("The Rules will print below") 

else: 
    print("Sorry that is not an option.")          
   
