version 2.9.0.2 - 16.01.2021

Added this from like 58 in the class win after self.expand_widgets to control the menubar:

        self.define_menu()
        self.menu_voices()
        
    def define_menu(self):
        "17.01.2021 - added menubar to the root"
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        
    def add_menu(self, text, command=None):
        "17.01.2021 - self.add_menu to add a menu to the menubar"
        # ex: add_menu("New", self.new) # it adds a new menu called New
        self.menubar.add_command(label=text, command=command)

    def menu_voices(self):
        "List of all the voices of the menubar"

        voices = [
            # voice, command
            [ # popup with info about the app
            "About",
            lambda: popup("Credits", "pythonprogramming.altervista.org \nv.2.9.0.2", parent=self.root)], 
            # next voice
            ["Blog",
            lambda: os.startfile("https://pythonprogramming.altervista.org/wp-admin")]
        ]

        def show_voices():
            "Shows the menu items above in the list voices"
            for v in voices:
                self.add_menu(v[0], v[1])
        show_voices()


