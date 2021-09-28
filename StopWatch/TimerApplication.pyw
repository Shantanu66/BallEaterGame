from tkinter import Tk, Frame, ttk, font, StringVar
from collections import deque
from FrameForTimer import Timer,Settings
from Windows import setprocessdpi
setprocessdpi()

COLOUR_PRIMARY="#201438"
COLOUR_SECONDARY = "#160d27"
COLOR_FADE="#301e50"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOR_TIMER_LABEL="#140c21"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"

class PomodoroTimer(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style=ttk.Style(self)
        style.theme_use("clam")
        style.configure("Timer.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure(
            "TimerText.TLabel",
            background=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            font=("Century Gothic",90,"bold")
        )

        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
            font=("Segoe UI",15,"bold")
        )

        style.configure(
            "PomodoroButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT,
            borderwidth=0,
            font=("BEBAS NEUE",15)
        )

        style.map(
            "PomodoroButton.TButton",
            background=[("active", COLOR_FADE), ("disabled", COLOUR_PRIMARY)])

        self["background"] = COLOUR_PRIMARY
        self.resizable(False,False)
        self.title("POMODORO TIMER")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.Pomodoro=StringVar(value=25)
        self.LongBreak=StringVar(value=15)
        self.ShortBreak=StringVar(value=5)
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)
        self.Container = ttk.Frame(self)
        self.Container.grid()
        self.Container.columnconfigure(0, weight=1)

        self.frames=dict()
        TimerFrame = Timer(self.Container,self,lambda : self.show_frame(Settings))
        TimerFrame.grid(row=0, column=0, sticky="NSEW")
        SettingFrame=Settings(self.Container,self,lambda : self.show_frame(Timer))
        SettingFrame.grid(row=0, column=0, sticky="NSEW")

        self.frames[Timer]= TimerFrame
        self.frames[Settings]=SettingFrame

        self.show_frame(Timer)
    def show_frame(self,container):
        frame=self.frames[container]
        frame.tkraise()


Gui = PomodoroTimer()
Gui.mainloop()
