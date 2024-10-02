from tkinter import *

def show():
    personality = signDict.get(myRadio.get())
    result.config(text=personality, font=("roman", 50), bg="black", fg="yellow")


window = Tk()
window.title("My Astrological Sign App")
window.geometry("500x500")

signDict = {
    "Aries": "Fearless",
    "Taurus": "Persistent",
    "Gemini": "Energetic",
    "Cancer": "Compassionate",
    "Leo": "Confident",
    "Virgo": "Thoughtful",
    "Libra": "Friendly",
    "Scorpio": "Complex",
    "Sagittarius": "Free",
    "Capricorn":"Responsible",
    "Aquarius":"Innovative",
    "Pisces":"Intuitive",
    "Connor":"choopy"
        }







myRadio=StringVar()


for key in signDict.keys():
    r=Radiobutton(window, text=key, variable = myRadio, value = key, command=show)
    r.pack()


result = Label(window, text="Personality will show here")
result.pack()

mainloop()
