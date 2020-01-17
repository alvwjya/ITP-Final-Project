

# importing tkinter, request, PIL, CSV, and pygeoip Libraries
from tkinter import *
import requests
from PIL import Image, ImageTk
import csv

## relx, rely, relwidth, relheight have the maximum value of 1 ##
## those things control the percentage of the image size ##

root = Tk()
# define the window size(canvas)
screen_width, screen_height = 800, 600
canvas = Canvas(root, width=screen_width, height=screen_height)
canvas.pack()

# set the background image of the canvas
bg_image = PhotoImage(file='Main_BG.png')
bg_label = Label(root, image=bg_image)  # placing the image to the canvas
bg_label.place(relwidth=1, relheight=1)


root.title("Weather Forecast")  # set the title bar name of tkinter window


# function that define format of the weather
def format_weather(weather):

    # try if the name of the city exists
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]
        wind_speed = weather["wind"]["speed"]
        country = weather["sys"]["country"]

        # opening the csv file to convert the country name
        with open("country_ID.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                if line[1] == country:
                    country = line[0]

        output_str = "City: %s \nCountry: %s \nConditions: %s \nTemperature: %s°C \nWind Speed: %sm/s"\
                     % (name, country, desc, temp, wind_speed)  # control the layout of the output string

    # run when the name of the city is not valid / cannot be found
    except:
        output_str = "Please make sure you input a valid name"
    return output_str


# class that create upper and lower frame
class Frame_dev:
    wmo_key = "7330008269a5c19a5f0824086266eb3d"  # Open Weather Map key
    url = "http://api.openweathermap.org/data/2.5/weather"  # the url of where the data is taking from

    def __init__(self, master):



        # UPPER FRAME #
        upper_frame = Frame(master, bg="dark red", bd=5)
        upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

        # placing a text box for user input
        self.entry = Entry(upper_frame, font=("Dubai Medium", 18))
        self.entry.place(relwidth=0.65, relheight=1)

        # placing a button where the user can click and search the weather
        self.button = Button(upper_frame, text="Search", font=("Dubai Medium", 18), bg="black", fg="white",
                             command=lambda: self.get_weather(self.entry.get()))
        self.button.place(relx=0.7, relheight=1, relwidth=0.3)

        # LOWER FRAME #
        self.lower_frame = Frame(master, bg="dark red", bd=5)
        self.lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

        # placing the label field and weather icon
        self.label = Label(self.lower_frame, bg="white", font=("Dubai", 14), anchor="nw", justify="left", bd=4)
        self.label.place(relwidth=1, relheight=1)
        self.weather_icon = Canvas(self.lower_frame, bg="white", bd=0, highlightthickness=0)
        self.weather_icon.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.5)

    def get_weather(self, city):  # function that get the weather situation from the text box
        params = {"APPID": self.wmo_key, "q": city, "units": "metric"}
        response = requests.get(self.url, params=params)
        weather = response.json()
        print(weather)
        # try if the user input is valid or not
        try:
            icon_name = weather["weather"][0]["icon"]
            self.open_image(icon_name)
        except:
            pass
        self.label["text"] = format_weather(weather)

    def open_image(self, icon):  # function that open the image icons.
        size = int(self.lower_frame.winfo_height() * 0.20)
        img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
        self.weather_icon.delete("all")
        self.weather_icon.create_image(0, 0, anchor="nw", image=img)
        self.weather_icon.image = img


Frame_dev(root)  # calling the class
root.mainloop()
