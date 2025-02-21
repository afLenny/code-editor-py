import customtkinter as ctk

class App(ctk.CTk):

    """
    Main application window that handles primary window setup and navigation.
    """

    def __init__(self):
        super().__init__()

        self.title("Code Editor in Python") 
        self.geometry("800x600") 

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = MainFrame(self)
        self.main_frame.grid(row=0, column=0, sticky="nsew")


class MainFrame(ctk.CTkFrame):
    """
    Main frame class, contains all UI elements and functionality.
    """

    def __init__(self, master: ctk.CTk):
        super().__init__(master)
        self.master = master

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="blue")

        self.create_widgets()
        self.setup_layout()



    def create_widgets(self) -> None:


        self.menu_frame = ctk.CTkFrame(self, fg_color="yellow", height=30)
        self.content_frame = ctk.CTkFrame(self, fg_color="red")


        self.text_widget = ctk.CTkTextbox(
            master=self.content_frame,
            corner_radius=0,
            wrap="none"
        )


        self.menu = ctk.CTkOptionMenu(
            master=self.menu_frame,
            values=["Open","Save"],
            command=self.option_menu_callback,
            variable=ctk.StringVar(value="File")
        )

    def setup_layout(self) -> None:
        
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=0)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.menu_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20,0))
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))


        self.menu.pack(side="left")
        self.text_widget.pack(expand=True, fill="both")

    def option_menu_callback(self, choice):
        print(f"Choice: {choice}")








