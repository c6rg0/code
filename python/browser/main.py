import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1080x720")
        self.title("App")
        ctk.set_appearance_mode("dark")
        
        self.entry = ctk.CTkEntry(self, placeholder_text="Name")
        self.entry.grid(row=0, column=1, columnspan=5, padx=20,
                        pady=50, sticky="ew")

        self.button = ctk.CTkButton(master=self, text="Enter",
                                    command=self.entry_callback)
        self.button.grid(row=0, column=0, columnspan=1, padx=20,
                        pady=20, sticky="ew")

        
    def entry_callback(self):
        self.entry_text = self.entry.get()
        print(self.entry_text)

if __name__ == "__main__":
    app = App()
    app.mainloop()


