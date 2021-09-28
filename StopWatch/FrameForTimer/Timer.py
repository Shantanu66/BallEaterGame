from tkinter import Tk, Frame, ttk, font, StringVar
from collections import deque

class Timer(ttk.Frame):
    def __init__(self,parent,controller,show_Settings):
        super().__init__(parent)
        self["style"]="Background.TFrame"
        self.controller=controller
        controller.Container.configure(style="Timer.TFrame")
        self.pomodoro=int(controller.Pomodoro.get())
        self.longbreak=int(controller.LongBreak.get())
        self.shortbreak = int(controller.ShortBreak.get())
        self.current_time = StringVar(value=f"{self.pomodoro:02d}:00")
        self.timer_running = False
        self.CurrentTimer_Schedule = StringVar(value=controller.timer_schedule[0])
        self.DecrementJob=None

        self.CurrentTime_Schedule_Label = ttk.Label(self, textvariable=self.CurrentTimer_Schedule,style="LightText.TLabel")           #label
        Timer_Frame = ttk.Frame(self,height=200,style="Timer.TFrame")
        time_counter = ttk.Label(Timer_Frame, text="TIME", textvariable=self.current_time,style="TimerText.TLabel")
        Button_Container=ttk.Frame(self,padding=20,style="Background.TFrame")
        self.Start_Button=ttk.Button(Button_Container,text="Start",command=self.Start_Timer,cursor="hand2",style="PomodoroButton.TButton",padding=(30,5))
        self.Stop_Button = ttk.Button(Button_Container, text="Stop", command=self.Stop_Timer, cursor="hand2",style="PomodoroButton.TButton",padding=(30,5))
        self.Reset_Button=ttk.Button(Button_Container,text="Reset",command=self.Reset_Timer,cursor="hand1",style="PomodoroButton.TButton",padding=(30,5))
        self.Settings_Button=ttk.Button(self,text="Settings",command=show_Settings,cursor="hand2",style="PomodoroButton.TButton",padding=(30,5))

        self.CurrentTime_Schedule_Label.grid(row=0, column=0, sticky="W", padx=(10, 0), pady=(10, 0))  #packing into Gui
        self.Settings_Button.grid(row=0,column=1,sticky="E",padx=10,pady=(10,0))
        Timer_Frame.grid(row=1, column=0,pady=(10, 0), sticky="NSEW",columnspan=2)
        time_counter.place(relx=0.5,rely=0.5,anchor="center")
        Button_Container.grid(row=3, column=0,sticky="EW",columnspan=2)
        self.Start_Button.grid(row=0, column=0,sticky="EW")
        self.Stop_Button.grid(row=0, column=1,sticky="EW",padx=5)
        self.Reset_Button.grid(row=0,column=2,sticky="EW")

        for child in Button_Container.winfo_children():
            child.grid_configure(padx=5)

        Button_Container.columnconfigure((0,1,2),weight=1)

    def Start_Timer(self):
        self.timer_running=True
        self.Start_Button["state"]="disabled"
        self.Stop_Button["state"]="enabled"
        self.DecreaseTime()

    def Stop_Timer(self):
        self.timer_running=False
        self.Start_Button["state"]="enabled"
        self.Stop_Button["state"]="disabled"
        if self.DecrementJob:
            self.after_cancel(self.DecrementJob)
            self.DecrementJob=None

    def Reset_Timer(self):
        self.Stop_Timer()
        self.current_time.set(f"{int(self.controller.Pomodoro.get()):02d}:00")
        self.controller.timer_schedule=deque(self.controller.timer_order)
        self.CurrentTimer_Schedule.set(self.controller.timer_schedule[0])

    def DecreaseTime(self):
        CurrentTime = self.current_time.get()
        if self.timer_running and CurrentTime!= "00:00":
            minutes, seconds = CurrentTime.split(":")                               # also using split directly without tupple unpacking
            if int(seconds) > 0:
                seconds = int(seconds) - 1
                minutes = int(minutes)
            else:
                seconds = 59
                minutes = int(minutes) - 1
            self.current_time.set(f"{minutes:02d}:{seconds:02d}")
            self.DecrementJob=self.after(1000, self.DecreaseTime)                   #check for a job if we actually have a problem and cancel it
        elif self.timer_running and CurrentTime == "00:00":
            self.controller.timer_schedule.rotate(-1)
            next_up = self.controller.timer_schedule[0]
            self.CurrentTimer_Schedule.set(next_up)

            if next_up == "Pomodoro":
                pomodoro = int(self.controller.Pomodoro.get())
                self.current_time.set(f"{pomodoro:02d}:00")
            elif next_up == "Short Break":
                shortbreak = int(self.controller.ShortBreak.get())
                self.current_time.set(f"{shortbreak:02d}:00")
            elif next_up == "Long Break":
                longbreak = int(self.controller.LongBreak.get())
                self.current_time.set(f"{longbreak:02d}:00")

            self.DecrementJob=self.after(1000, self.DecreaseTime)
