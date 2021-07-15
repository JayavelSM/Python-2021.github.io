from tkinter import Tk, Label, Entry, ttk


class GUI:  # Requirement ID [Section B --> Note (ii)]
    """Library Class for GUI and Declare the Global parameters for Widgets
    1.Configure WindowSetup Parameters like as TitleName,Geometry and Configuration
    2.Create a EntryBox with Label and Configure the parameters like as Name ,Width and Position of EntryBox"
    3.Create a button and configure the parameters like as buttonName,Width and Position of button
    4.Create a Dropdown(Combobox) and Configure the parameters like as Name,Width,list of items and position of comboBox
    5.Create a Quantity(SpinBox) and Configure the parameters like as Name,Width and Position of Spinbox"""
    # Specify the Global Variables for Widgets as Font,Size,BackGround Color and ForeGround Color.Once Changed here its
    # Applicable for all the Widgets defines in this library
    # Requirement ID [Section B --> Note (i)]
    widget_font = 'Helvetica'
    widget_text_size = 14
    widget_background = 'white'
    widget_foreground = 'navy blue'

    def __init__(self):
        """Self initialisation of Tkinter window library functions"""
        # Create the Root Object as Tkinter Profiles
        self.window = Tk()

    def windowSetup(self, titleName, windowSize):
        """ WindowSetup Parameters Initialisation .User Set TitleName,Geometry and Configure Main widows"""
        # Setup the Windows for this Project.Set TitleName,Size of Window and Window BackGround Color
        self.window.title(titleName)
        self.window.geometry(windowSize)
        self.window.configure(background='white')

    def userInput(self, lblName, width, posX, posY):  # Requirement ID [Section B --> 1]
        """UserInput Function defined as EntryBox .The user can set parameters for labelName,Width of EntryBox,
        Location of EntryBox(X & Y)format"""
        # Label is used here to create the name of the EntryBox and User configure the LabelName Dynamically and
        # Set the Font and Color globally for all widgets
        Label(self.window, text=lblName, font=(GUI.widget_font, GUI.widget_text_size),
              foreground=GUI.widget_foreground, background=GUI.widget_background).place(x=posX, y=posY)
        # EntryBox Widget creation and Set the Font,Color globally as defined in the GUI Class during the initialisation
        entryBox = Entry(self.window, width=width, font=(GUI.widget_font, GUI.widget_text_size),
                         foreground=GUI.widget_foreground, background=GUI.widget_background)
        # EntryBox Creation The Pack geometry manager packs widgets in rows or columns.
        # We can use options like fill, expand, and side to control this geometry manager.
        entryBox.pack(side="left")
        # Location of EntryBox Dynamically Configure based on the Call arguments
        entryBox.place(x=posX + 180, y=posY)
        # Return the EntryBox to the Calling Script
        return entryBox

    def button(self, btnName, posX, posY):  # Requirement ID [Section B --> 2]
        """Button function is defined to create the button on the UI screen for user interaction .Arguments during
        function as buttonName,Location(X & Y)"""
        # Call for the Button Style
        style = ttk.Style()
        # Configure the Style of button and Configure the Font and Size use of globally Widget settings
        # defined in the GUI Class
        style.configure('W.TButton', font=(GUI.widget_font, GUI.widget_text_size),
                        foreground=GUI.widget_foreground, background=GUI.widget_background)
        # Assign the button to the predefined arguments
        button1 = ttk.Button(self.window,
                             text=btnName, style='W.TButton')
        # Get the Position arguments and Pass it to the function
        button1.place(x=posX, y=posY)
        # Return the button arguments to the calling script
        return button1

    def dropDown(self, lblName, List, posX, posY):  # Requirement ID [Section B --> 3]
        """DropDown function is defined to create the ComboBox on the UI screen for user interaction .Arguments during
        function as ComboBox Name(Label),List of Items,Location of ComboBox(X & Y)"""
        # Label is used here to create the name of the ComboBox and User configure the LabelName Dynamically and
        # Set the Font and Color globally for all widgets
        ttk.Label(text=lblName, font=(GUI.widget_font, GUI.widget_text_size),
                  background=GUI.widget_background,
                  foreground=GUI.widget_foreground).place(x=posX, y=posY)
        # ComboBox Widget creation and Set the Font,Color globally as defined in the GUI Class during the initialisation
        dropdown = ttk.Combobox(self.window, width=15, font=(GUI.widget_font, GUI.widget_text_size),
                                foreground=GUI.widget_foreground, background=GUI.widget_background)
        # Adding combobox drop down list of items based on the Arguments passed from the script
        dropdown['values'] = List
        # Location of ComboBox based on the Arguments
        dropdown.place(x=posX + 125, y=posY)
        # Used to assign the Default index as dropDown.current(0)
        dropdown.current(0)
        # Return the comboBox reference to the calling script
        return dropdown

    def quantity(self, lblName, posX, posY):  # Requirement ID [Section B --> 4]
        """Quantity function is defined to create the SpinBox on the UI screen for user interaction .Arguments during
                function as SpinBox Name(Label),Location of SpinBox(X & Y)"""
        # Label is used here to create the name of the SpinBox and User configure the LabelName Dynamically and
        # Set the Font and Color globally for all widgets
        ttk.Label(self.window,
                  text=lblName, font=(GUI.widget_font, GUI.widget_text_size),
                  background=GUI.widget_background, foreground=GUI.widget_foreground).place(x=posX,
                                                                                            y=posY)
        # SpinBox Widget creation and Set the Font,Color globally as defined in the GUI Class during the initialisation
        spinbox = ttk.Spinbox(self.window,
                              width=15, from_=0, to=21456987563, increment=1,
                              font=(GUI.widget_font, GUI.widget_text_size),
                              background=GUI.widget_background, foreground=GUI.widget_foreground,
                              )
        # Set the SpinBox Default Value to 0(Zero)
        spinbox.set(0)
        #  Location of SpinBox based on the Arguments
        spinbox.place(x=posX + 125, y=posY)
        # Return the SpinBox reference to the calling script
        return spinbox


if __name__ == '__main__':
    """Call During the Single Instance of GUI Library Functions"""
    # Assign the Class GUI to particular instance
    gui = GUI()
    # Assign the Arguments to the UserInput A Function and Check it
    a = gui.userInput('Key in value for a : ', 15, 0, 90)
    # Assign the Arguments to the UserInput B Function and Check it
    b = gui.userInput('Key in value for b : ', 15, 0, 130)
    # Assign the Arguments to the button Function and Check it
    c = gui.button('Swap', 50, 165)
    # Assign the Arguments to the DropDown Function with the list of items and check the function
    d = gui.dropDown('Select Fruit : ', ('-select-', 'Apple', 'Orange', 'Pear', 'Grape', 'Kiwi'), 380, 90)
    # Assign the Arguments to the Quantity Function and Check it
    spinner = gui.quantity('Quantity :  ', 380, 130)
    # Run the Main Window loop Continuously
    gui.window.mainloop()
