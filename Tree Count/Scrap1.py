from tkinter import *
import tkintermapview
from PIL import Image, ImageGrab

window = Tk()
window.title("Map")
window.geometry("1000x800")

label = LabelFrame(window)
label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(label, width=800, height=600)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
map_widget.pack()

# Variables to store selection coordinates
start_x, start_y = None, None
end_x, end_y = None, None

# Flag to indicate if selection is active
selection_active = False

# Function to start selecting an area
def start_selection(event):
    global start_x, start_y, selection_active
    if not selection_active:
        start_x, start_y = event.x, event.y
        selection_active = True

# Function to end selection and save the selected area
def end_selection(event):
    global end_x, end_y, selection_active
    if selection_active:
        end_x, end_y = event.x, event.y

        # Ensure that the end coordinates are greater than the start coordinates
        if end_x < start_x:
            start_x, end_x = end_x, start_x
        if end_y < start_y:
            start_y, end_y = end_y, start_y

        # Capture the area from the map widget
        screenshot = ImageGrab.grab(bbox=(map_widget.winfo_rootx() + start_x,
                                          map_widget.winfo_rooty() + start_y,
                                          map_widget.winfo_rootx() + end_x,
                                          map_widget.winfo_rooty() + end_y))

        # Save the selected area as an image
        screenshot.save("selected_area.png")

        # Reset selection flag
        selection_active = False

# Function to initiate area selection
def select_area():
    global selection_active
    selection_active = True

# Create a "Select Area" button
select_button = Button(window, text="Select Area", command=select_area)
select_button.pack()

# Bind mouse events to the map widget
map_widget.bind("<ButtonPress-1>", start_selection)
map_widget.bind("<ButtonRelease-1>", end_selection)

window.mainloop()
