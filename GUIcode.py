import tkinter as tk
from PIL  import ImageTk,Image, ImageDraw,ImageFont
from tkinter import filedialog
import tkinter.font as font
LARGE_FONT= ("Verdana", 12)




class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage1, StartPage, PageOne, PageTwo, PageThree, PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

""""""""""""""""""""""""



class Exit_win(tk.Frame):
    def __init__(self, parent, controller):
        window=Tk()
        mylabel1=Label(window, text="Do you really want to exit this program?",font=('arial', 12,'bold')).place(x=35,y=30)
        quit=tk.Button(window, text="Yes", padx=30, pady=10, fg="black", command=self.quit)
        quit.place(x=40,y=100)
        quit=tk.Button(window, text="No", padx=30, pady=10, fg="black", command=window.destroy)
        quit.place(x=270,y=100)
        
class StartPage1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        start=tk.Button(self, text="Get Started", padx=25, pady=20, fg="white",bd=5, bg="saddle brown",command=lambda: controller.show_frame(StartPage))
        start.pack()

        button6=tk.Button(self, text="Exit", padx=30, pady=5, fg="white", bg="saddle brown", command=lambda: controller.show_frame(Exit_win))
        button6.pack()




""""""""""""""""""""""""


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, bg='IndianRed3',text="SMART CROWD ANALYZER", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self,height=2,width=30,bg='IndianRed3', text="People Count", command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self,height=2,width=30,bg='IndianRed3', text="Group Count", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = tk.Button(self,height=2,width=30,bg='IndianRed3', text="Age & Gender", command=lambda: controller.show_frame(PageThree))
        button3.pack()

        button4 = tk.Button(self,height=2,width=30,bg='IndianRed3', text="Customer Satisfaction", command=lambda: controller.show_frame(PageFour))
        button4.pack()

        button5 = tk.Button(self,height=2,width=30,bg='IndianRed3', text="Back to Start", command=lambda: controller.show_frame(StartPage1))
        button5.pack()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,bg='peach puff', text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10, fill="both", expand=True)

        button1 = tk.Button(self,bg='IndianRed3', text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,bg='peach puff', text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10, fill="both", expand=True)

        button1 = tk.Button(self,bg='IndianRed3', text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,bg='peach puff', text="Page Three!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10, fill="both", expand=True)

        button1 = tk.Button(self,bg='IndianRed3', text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,bg='peach puff', text="Page Four!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10, fill="both", expand=True)

        button1 = tk.Button(self,bg='IndianRed3', text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = SeaofBTCapp()
app.title('Smart Crowd Analysis')


app.mainloop()



