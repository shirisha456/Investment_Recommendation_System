from tkinter import *
import os
from PIL import Image, ImageTk  # Requires: pip install pillow

def main():
    ######################## Basic Structure
    frame2 = Tk()
    windowWidth = 1058
    windowHeight = 595
    frame2.geometry(f'{windowWidth}x{windowHeight}')

    # Center window on screen
    screen_w = frame2.winfo_screenwidth()
    screen_h = frame2.winfo_screenheight()
    position_x = int(screen_w/2 - windowWidth/2)
    position_y = int(screen_h/2 - windowHeight/2)
    frame2.geometry(f"+{position_x}+{position_y}")

    frame2.title('Investment Options')

    ######################## Functions
    def changeOnHover(button, colorOnHover="gray", colorOnLeave='#252525'):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover, cursor="hand2"))
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    def f1():
        # Adjust the command as needed; here it runs a separate Python script
        os.system('python stock_market.py')

    def f2():
        os.system('python mutual_funds.py')

    def f3():
        os.system('python gold_investment.py')

    def f4():
        os.system('python real_estate.py')

    ######################## Load JPEG background via Pillow
    # Build absolute path to your JPEG file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bg_filename = 'bg2.jpg'  # change if your filename differs
    image_path = os.path.join(script_dir, bg_filename)

    if not os.path.exists(image_path):
        # If file not found, raise or fallback to plain background
        raise FileNotFoundError(f"Background image not found at {image_path}")

    try:
        img = Image.open(image_path)
        # Optionally resize to exactly fit the window:
        img = img.resize((windowWidth, windowHeight), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        background = Label(frame2, image=photo)
        # Keep a reference so GC doesn’t remove it
        background.image = photo
        background.place(x=0, y=0)
    except Exception as e:
        print("Error loading background image:", e)
        # Fallback: solid background color
        frame2.configure(bg='#252525')

    ######################## Text Box (Title)
    text = Text(frame2, height=1, width=16, bg='#252525', fg='red', font=('', 34), bd=-2)
    text.insert(5.0, "Investment Options")
    text.config(state='disabled')
    # Adjust placement as desired
    text.place(x=340, y=70)

    ######################## Buttons
    back_button = Button(frame2, text='BACK', command=frame2.destroy,
                         font=('', 25), bd=-2, fg='red', bg='#252525', borderwidth=5)
    back_button.place(x=470, y=450)

    b1 = Button(frame2, text='Stock\nMarket', font=('', 27), width=10,
                fg='red', bg='#252525', borderwidth=5, command=f1)
    b1.place(x=50, y=250)

    b2 = Button(frame2, text='Mutual\nFunds', font=('', 27), width=10,
                fg='red', bg='#252525', borderwidth=5, command=f2)
    b2.place(x=300, y=250)

    b3 = Button(frame2, text='Gold\nInvestment', font=('', 27), width=10,
                fg='red', bg='#252525', borderwidth=5, command=f3)
    b3.place(x=550, y=250)

    b4 = Button(frame2, text='Real\nEstate', font=('', 27), width=10,
                fg='red', bg='#252525', borderwidth=5, command=f4)
    b4.place(x=800, y=250)

    for btn in (b1, b2, b3, b4, back_button):
        changeOnHover(btn)

    frame2.mainloop()

if __name__ == '__main__':
    main()
