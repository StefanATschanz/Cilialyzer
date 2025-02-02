import tkinter as tk

class Menubar:

    """
    Constructs the menubar on top of parent (main window of the application)
    """

    def about_info(self):
        """
        Displays the 'About Cilialyzer' information in a toplevel window
        """

        self.about_window = tk.Toplevel(self.parent)
        self.about_window.title('About Cilialyzer')

        # open the toplevel window in the middle of the screen
        # get the screen dimensions first:

        sw = self.about_window.winfo_screenwidth()
        sh = self.about_window.winfo_screenheight()

        win_width = 600
        win_height = 450

        posx = int(0.5*sw - 0.5*win_width)
        posy = int(0.5*sh - 0.5*win_height)

        self.about_window.geometry("%dx%d+%d+%d" % (
            win_width, win_height, posx, posy))
        self.about_window.update()

        # text in about window
        self.textbox = tk.Text(self.about_window, height=5, width=400)

        text = """
        The Cilialyzer software is an easy-to-use, open source application 
        mainly intended for the clinical  assessment of the effectivity of the 
        mucociliary clearance mechanism inferred from recordings taken by 
        high-speed video microscopy 
        """

        self.textbox.pack()
        self.textbox.insert(tk.END, text)


    def link_tutorials(self):
        """
        opens the link to the tutorials in the default webbrowser
        """
        pass

    def open_doc(self):
        """
        Opens the documentation in the webbrowser
        """
        # webbrowser.open_new(r'./Doc/help.pdf')
        pass


    def __init__(self, parent):

        self.parent = parent
        self.myfont = ("TkDefaultFont", 10)

        # create the menubar of parent tk-window
        self.menubar = tk.Menu(self.parent, bg='gray30', fg='gray95', font=self.myfont)

        # create 'File'-tab in menubar
        self.mfile = tk.Menu(self.menubar)
        # create submenus of File-tab:
        self.mfile.add_command(label="Open sequence...", font=self.myfont)
        self.mfile.add_command(label="Open video...",font=self.myfont)

        # create 'Appearance'-tab 
        self.mapp = tk.Menu(self.menubar)
        # create submenus
        self.mapp.add_command(label="Configure...",font=self.myfont)

        # create 'Help'-tab 
        self.mhelp = tk.Menu(self.menubar)

        self.mhelp.add_command(label='Documentation', command=self.open_doc)
        self.mhelp.add_command(label='Watch tutorial videos',
                               command=self.link_tutorials)
        self.mhelp.add_command(label='About',
                               command=self.about_info, font=self.myfont)

        # create 'Exit'-tab
        self.mexit = tk.Menu(self.menubar)

        # add menus to menubar: 
        self.menubar.add_cascade(menu=self.mfile,label="File ",font=self.myfont)
        self.menubar.add_cascade(label=" Appearance ",font=self.myfont,menu=self.mapp)
        self.menubar.add_cascade(label=" Help ",font=self.myfont,menu=self.mhelp)
        self.menubar.add_cascade(label=" Exit ",font=self.myfont,menu=self.mexit)

if __name__ == "__main__":

    root = tk.Tk()
    root.geometry('300x200')
    mbar = Menubar(root)
    root.config(menu=mbar.menubar)
    root.mainloop()
