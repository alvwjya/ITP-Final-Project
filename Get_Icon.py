# importing os and urllib libraries
import os
import urllib.request

# creating lists for icons
day = ["01d.png", "02d.png", "03d.png", "04d.png", "09d.png", "10d.png", "11d.png", "13n.png", "50d.png"]
night = ["01n.png", "02n.png", "03n.png", "04n.png", "09n.png", "10n.png", "11n.png", "13n.png", "50n.png"]


url = "https://openweathermap.org/img/w/"  # the url of the image
path = "./img/"  # save location of the file

# check if the path is already exist
if not os.path.exists(path):
    os.makedirs(path)

# saving the images from "day" list
for i in day:
    file_name = path + i
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(url + i, file_name)

# saving the images from "night" list
for i in night:
    file_name = path + i
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(url + i, file_name)

# opening the main file "Weather_Forecast.py"
os.system("python Weather_Forecast.py")
