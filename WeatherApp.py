import tkinter as tk
import requests
from PIL import Image, ImageTk


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)

    file = open("key.txt", "r")
    weather_key = file.read()

    def get_weather(city, weather_key):
        url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {'APPID': weather_key, 'q':city, 'units': 'Metric'}
        response = requests.get(url,params=params)
        weather = response.json()
        print(weather)
        name = city.title()
        label['text'] = "City: "+ str(name)
        try:
            for i in range(0,5):
                desc = weather['list'][i]['weather'][0]['description']
                icon = weather['list'][i]['weather'][0]['icon']
                temp = weather['list'][i]['main']['temp']
                label['text'] = label['text']+ "\n\nConditions: "+ str(desc)+ "\nTemperature (C): "+ str(temp)

                size = int(lower_frame.winfo_height() * 0.20)
                img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
                if i==0:
                    weatherIcon0.create_image(0, 0, anchor='nw', image=img)
                    weatherIcon0.image = img
                elif i==1:
                    weatherIcon1.create_image(0, 0, anchor='nw', image=img)
                    weatherIcon1.image = img
                elif i==2:
                    weatherIcon2.create_image(0, 0, anchor='nw', image=img)
                    weatherIcon2.image = img
                elif i==3:
                    weatherIcon3.create_image(0, 0, anchor='nw', image=img)
                    weatherIcon3.image = img
                elif i==4:
                    weatherIcon4.create_image(0, 0, anchor='nw', image=img)
                    weatherIcon4.image = img

        except:
            label['text'] = "There was a problem retrieving data"

    canvas = tk.Canvas(root,height = 700, width = 800)
    canvas.pack()

    background_image = tk.PhotoImage(file="background.png")
    background_label = tk.Label(root, image = background_image)
    background_label.place(relwidth=1,relheight=1)

    frame = tk.Frame(root, bg = "#80c1ff", bd = 5)
    frame.place(relx=0.5,rely=0.1,relwidth = 0.75, relheight = 0.1, anchor="n")

    entry = tk.Entry(frame,font=("courier New Greek",15), bg = "white")
    entry.place(relwidth = 0.65,relheight=1)

    button =  tk.Button(frame, text = "Search City",font=("courier New Greek",20), bg = "purple", fg = "white" , command = lambda: get_weather(entry.get(),weather_key))
    button.place(relx=0.7,relheight=1,relwidth = 0.3)

    lower_frame = tk.Frame(root, bg = "#80c1ff", bd = 10)
    lower_frame.place(relx = 0.5, rely=0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

    label = tk.Label(lower_frame, font=("courier New Greek",15), anchor="nw",justify="left",bd=4,bg="white")
    label.place(relwidth=1,relheight=1)

    weatherIcon0 = tk.Canvas(label, bg="white", bd=0, highlightthickness=0)
    weatherIcon0.place(relx=.75, rely=0.07, relwidth=1, relheight=0.5)
    weatherIcon1 = tk.Canvas(label, bg="white", bd=0, highlightthickness=0)
    weatherIcon1.place(relx=.75, rely=0.25, relwidth=1, relheight=0.5)
    weatherIcon2 = tk.Canvas(label, bg="white", bd=0, highlightthickness=0)
    weatherIcon2.place(relx=.75, rely=0.42, relwidth=1, relheight=0.5)
    weatherIcon3 = tk.Canvas(label, bg="white", bd=0, highlightthickness=0)
    weatherIcon3.place(relx=.75, rely=0.6, relwidth=1, relheight=0.5)
    weatherIcon4 = tk.Canvas(label, bg="white", bd=0, highlightthickness=0)
    weatherIcon4.place(relx=.75, rely=0.78, relwidth=1, relheight=0.5)



    # print(tk.font.families())

    root.mainloop()