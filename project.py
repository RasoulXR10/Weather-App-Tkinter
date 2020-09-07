import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import requests
HEIGHT = 600
WIDTH = 600


def format_weather(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nCondition: %s \nTemprature: %s (°C)' % (
            name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = '1708c9c264af3574982477a5bcf7a9d8'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    # injuti moshakhas mikonim koja mishe dataha ro koja represent konim
    label['text'] = format_weather(weather)


root = tk.Tk()
root.geometry("400x300")
root.title('Weather App')

# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)  # canvas is a container
# canvas.pack()

# background_image = ImageTk.PhotoImage(Image.open("background.jpg"))
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("background.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


e = Example(root)
e.pack()


frame = tk.Frame(root, bg='#80b3ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40,
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80b3ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
