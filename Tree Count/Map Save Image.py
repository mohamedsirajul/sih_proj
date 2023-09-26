from tkinter import *
import tkinter
import tkintermapview
from PIL import ImageGrab

window = Tk()
window.title("Map")
window.geometry("1000x800")

label = LabelFrame(window)
label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(label , width =800 , height = 600)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
map_widget.pack()



map_widget.set_position(8.7244041,77.7350118)


#map_widget.fit_bounding_box((<lat1>, <long1>), (<lat2>, <long2>))


def capture_and_save_image():
 
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    width = window.winfo_width()
    height = 630
    
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    
    screenshot.save("captured_image.jpg")


capture_button = tkinter.Button(window, text="Capture and Save Image", command=capture_and_save_image)
capture_button.pack()


window.mainloop()









