import urllib.parse
import requests
from colorama import Fore, Back, Style
from datetime import datetime, date

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "San Francisco, CA"
dest = "Los Angeles, CA"
key = "PL3t1O9pauSij1Lk1GYAYNwbGeRVlXT4"
now = date.today()


name = input("What's your name?: ")
vehicle = input("What's your vehicle?: ")
plate = input("What's your plate number?: ")

while True:
   orig = input("Source Location: ")
   if orig == "quit" or orig == "q":
        break

   dest = input("End Location: ")
   if dest == "quit" or dest == "q":
        break
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

   print("URL: " + (url))

   json_data = requests.get(url).json()

   json_status = json_data["info"]["statuscode"]

   if json_status == 0:

       
       print(Fore.RED +"API Status: " +  str(json_status) + " = A successful route call.\n")
       print(Fore.BLUE +"=============================================")
       print(Fore.RED +"Welcome to Group 3, 4ITH")
       print(Fore.RED+"The Date Today is: " + (now))
       
       print(Fore.BLUE +"**********************************************")
       print("                                              ")
       print( Fore.GREEN +"Welcome, " +(name))
       print(Fore.RED + "Directions from " +  (orig) + " to " + (dest))
       print("                                              ")
       print(Fore.RED+"Vehicle Used: "+(vehicle))
       print(Fore.RED+"Plate no.: "+(plate))
       print( Fore.RED +"Trip Duration:   " + (json_data["route"]["formattedTime"]))
       print(Fore.RED + "Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       print(Fore.RED +"Fuel Used (Liter): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
       print("                                              ")
       print(Fore.BLUE +"=============================================")
   elif json_status == 402:
          print(Fore.BLUE +"**********************************************")

          print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")

          print(Fore.BLUE +"**********************************************\n")

   elif json_status == 611:
         print("**********************************************")

         print(Fore.RED +"Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")

         print("**********************************************\n")
   else:
         print("************************************************************************")

         print(Fore.RED +" For Staus Code: " + str(json_status) + "; Refer to:")

         print("https://developer.mapquest.com/documentation/directions-api/status-codes")

         print("************************************************************************\n")


