#Code to notify regarding air quality index of city over email

#Libraries and files required
import requests
import send_mail
import config

#Querying iQAir API to fetch current pollution and weather data
response = requests.get(f"http://api.airvisual.com/v2/city?city={config.city}&state={config.state}&country={config.country}&key={config.api_key}").json()

weather_ts = response["data"]["current"]["weather"]["ts"]
weather_temp = response["data"]["current"]["weather"]["tp"]
pollution_ts = response["data"]["current"]["pollution"]["ts"]
pollution_aqius = response["data"]["current"]["pollution"]["aqius"]

#Create message for email
message = f"""\
Subject: Weather and pollution report

Please find the weather and pollution report for {config.city} below: \n The current temperature in Celsius is  {weather_temp} \n The current air quality index recorded is {pollution_aqius}"""

#Calling function to send email
send_mail.send_email(message)

