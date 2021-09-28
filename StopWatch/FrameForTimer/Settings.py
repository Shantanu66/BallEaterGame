import tkinter as tk
from tkinter import ttk,StringVar

class Settings(ttk.Frame):
    def __init__(self,parent,controller,show_timer):
        super().__init__(parent)
        self["style"]="Background.TFrame"
        self.columnconfigure(0,weight=1)
        self.rowconfigure(2,weight=1)

        settings_container=ttk.Frame(self,padding="30 15 30 15",style="Background.TFrame")
        settings_container.grid(row=0,column=0,sticky="EW",padx=10,pady=10)
        settings_container.columnconfigure(1,weight=1)
        settings_container.rowconfigure(1,weight=1)

        Pomodoro_Label=ttk.Label(settings_container,text="Pomodoro time:  ",style="LightText.TLabel")
        Pomodoro_Label.grid(row=0,column=0,sticky="W")
        Pomodoro_Input=tk.Spinbox(settings_container,textvariable=controller.Pomodoro,
                                       from_=0,to=120,justify="center",width=10)
        Pomodoro_Input.grid(row=0,column=1,sticky="EW")
        Pomodoro_Input.focus()

        LongBreak_Label = ttk.Label(settings_container, text="Long Break time:  ",style="LightText.TLabel")
        LongBreak_Label.grid(row=1, column=0, sticky="W")
        LongBreak_Input = tk.Spinbox(settings_container, textvariable=controller.LongBreak,
                                    from_=0, to=120, justify="center", width=10)
        LongBreak_Input.grid(row=1, column=1, sticky="EW")

        ShortBreak_Label = ttk.Label(settings_container, text="Short Break time:  ",style="LightText.TLabel")
        ShortBreak_Label.grid(row=2, column=0, sticky="W")
        ShortBreak_Input = tk.Spinbox(settings_container, textvariable=controller.ShortBreak,
                                     from_=0, to=120, justify="center", width=10)
        ShortBreak_Input.grid(row=2, column=1, sticky="EW")

        Button_Container=ttk.Frame(self,style="Background.TFrame")
        Button_Container.grid(row=3,column=0,sticky="EW",padx=10)
        Button_Container.columnconfigure(0,weight=1)

        Timer_Button=ttk.Button(Button_Container,text= "<- Back",command=show_timer,cursor="hand2",style="PomodoroButton.TButton")
        Timer_Button.grid(row=0,column=0,sticky="EW",pady=(0,12),padx=20)

        for child in settings_container.winfo_children():
            child.grid_configure(padx=7,pady=7)




