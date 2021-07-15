from tkinter import messagebox, Message, Tk, Canvas, PhotoImage, SW, N, W, E, S  # Import Specific Tkinter Widget Used
from time import strftime  # To display the system date & time
import os.path  # To be used for file related stuffs
import shutil  # use to get the Free Disk Space from the PC
import Analysis  # Import the customised widget library required for this assessment
import gui_lib  # Import the Analysis related stuffs its a customised functionality


def __init__(self):
    """ Call for the root window and assign to the current script"""
    # Assign the Tkinter Window to the Current Script
    self.window = Tk()


# Call the Section A Function and get the return data and display into the message widget
# Requirements ID --> Section C : (iii)
def swap(event):
    """ When the user press the Swap button on the UI Screen . The Following Event will perform the Operation.
    Swap Event : It will get the data from the Value A and Value B Entry Box .
    Send the data to swap function call in Analysis.py and get the returned value and display onto the message box"""
    # Check the number available on a and b entryBox
    if EntryA.get() != '' and EntryB.get() != '':
        # Try cache method is user to check the user whether enter the integer values or not in both the Entry Boxes
        try:
            # Call the Swap Function in Analysis.py and get the return value to print on the Message Widget
            SwapOutput = Analysis.swap_func(1, int(EntryA.get()), int(EntryB.get()))  # RequirementID -->Section C:(ii)
            # Implement the message widget on the UI Screen and Set the Parameters to the Widget
            Msg = Message(None, text=SwapOutput, foreground='White', background='Black',
                          font=('Arial', 12), justify='right', aspect=50, width=250)
            # Message grid property is used to locate the widget in the exact location of UI Screen
            Msg.grid(row=0, sticky=(N, W, E, S), padx=200, pady=180)
        except ValueError:
            # Handle the exception
            messagebox.showerror('Swap Function', 'Please Enter the Integer Values for a & b')
    else:
        # If number not available software will prompt the message box as a error to user.
        messagebox.showerror('Swap Function', 'Please Enter the value for a & b')


def lookFunc(event):
    """Lookup Function Event is used to calculate the total cost based on the Fruit Selection on the DropDown
    and Quantity Entry on the SpinBox"""
    # Check the Fruit Dropdown is Empty or not
    if DropDownFruit.get() != '':
        # Call the Lookup Function in the Analysis.py script and get the return values of total cost
        totalVal = Analysis.lookup_func(1, DropDownFruit.get(), SpinBoxQuantity.get())
        # Assign the Values to another string function to display on the UI
        totalVal = "Total Price = " + "$" + str(totalVal)
        # Display the total cost on the UI with the help of message widget.
        # Message Widget configured the below parameters
        lookupMsg = Message(None, text=totalVal, foreground='White', background='Black',
                            font=('Arial', 12), justify='right', aspect=100, width=500)
        # Place property of message is used to assign the location on the UI Screen
        lookupMsg.place(x=525, y=165)
    else:
        # If the user doesn't select the fruit. it will display the warning Message to the user
        messagebox.showwarning('Lookup Function', 'Please select the Fruit Name')


def time():
    """Time Function call is used to display the real time system clock on the User Interface Screen"""
    # strftime function is used to convert to convert the timeFormat into the string
    string = strftime('%d/%m/%Y %H:%M:%S %p')
    # Real time system clock configured into the Message Widget
    clock = Message(None, width=1000, foreground='Black', background='white')
    # Message Widget place property is used to place the widget as per the location defined into the Arguments
    clock.place(x=550, y=200)
    # Config Property is used to configured the widget as a string format
    clock.config(text=string)
    # run the clock thread every 250ms
    clock.after(250, time)
    # Call the Ver_PCMem function call.
    # It used to display the dyson logo on the UI Screen and also get the System Free space
    Ver_PCMem()


def Ver_PCMem():
    """ Display the Dyson logo on the User interface screen on the Top Left Position
    and also this function display the System Free space"""
    # Software Version and System Memory display with the help of Message Widget.
    # Message widget are configured based on the property
    ver = Message(None, width=200, foreground='Black', background='white')
    # Placement of the Message Widget to display the Version and System Free Space
    ver.place(x=10, y=200)
    # Call the Shutil library to get the system total space,Free Space and used Space
    total, used, free = shutil.disk_usage("/")
    # Message widget Config property is used to append the information for display purposes
    ver.config(text=("Ver1.0.0  " + "Disk:%d/%d GB" % (total // (2 ** 30), free // (2 ** 30))))
    # To Display the Header of the Script using the Message Widget
    Message(None, text="Python Assessment", width=500, foreground='navy blue', background='white',
            font=('calibre light', 20, 'bold')).place(x=250, y=5)


gui = gui_lib.GUI()
"""Assign the Class GUI to the Specific Parameters helps to call the root window for the UI Design"""
# Window Setup geometry assign to fit the size of screen
gui.windowSetup('Python GUI Assessment', '700x250')
# Assign the EntryBox A and Call the GUI library UserInput Function call
EntryA = gui.userInput('Key in value for a : ', 15, 0, 90)
EntryB = gui.userInput('Key in value for b : ', 15, 0, 130)
# Assign the ButtonSwap and Call the GUI library Button Function call
ButtonSwap = gui.button('Swap', 50, 165)
# Assign the DropDownFruit and Call the GUI library DropDown Function call
DropDownFruit = gui.dropDown('Select Fruit : ', ('-select-', 'Apple', 'Orange', 'Pear', 'Grape', 'Kiwi'), 380, 90)
# Assign the SpinBoxQuantity and Call the GUI library Quantity Function call
SpinBoxQuantity = gui.quantity('Quantity :  ', 380, 130)
# Capture the Event for button press and assign to the swap function call
ButtonSwap.bind('<Button-1>', swap)
# Capture the Event for DropDown ValueChange and assign to the lookup function call
DropDownFruit.bind('<<ComboboxSelected>>', lookFunc)
# Capture the Event for Quantity ValueChange and assign to the lookup function call
SpinBoxQuantity.bind('<ButtonRelease-1>', lookFunc)
SpinBoxQuantity.bind('<Return>', lookFunc)
# Call the Time Function call and assign to the Thread to run every 250ms
time()
# Get the Dyson logo and assign to the left corner of the screen
# Check the Dyson Logo file Exists or not
if os.path.isfile("Dyson.png"):
    # Read the image and assign to the graphical widget(CANVAS) in Tkinter
    canV = Canvas(gui.window, width=110, height=50, background='white', bd=0, highlightthickness=0, relief='ridge')
    # Placement of the logo on the UI Screen
    canV.place(x=5, y=2)
    # Read the logo image and assign to the another variable
    img = PhotoImage(file="Dyson.png")
    # Set the Image properties
    canV.create_image(0, 50, anchor=SW, image=img)
# Call the Screen and Run Continuously
gui.window.mainloop()
