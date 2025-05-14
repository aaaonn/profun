import random
from tkinter import HIDDEN, NORMAL, Tk, Canvas, Button, Frame, Label

root = Tk()
root.title("Keroro Face")
c = Canvas(root, width=500, height=500, bg='#20C5E1')
c.pack()
c.check =True
c.body_color = "#FA9AA3"

# ================================= Background ========================================
# ===== ชั้นบรรยากาศชั้นกลาง =====
c.create_polygon(
    0,500,#ตั้งแต่ข้างซ้ายล่าง
    0,500,

    0,100,#มุมซ้ายบน
    0,100,

    500,100,#มุมขวาบน
    500,100,

    500,500,#ตั้งแต่ข้างขวาล่าง
    500,500,
    fill="#10ADDE", smooth = 1,outline="#10ADDE"#17B6DE
)
# ===== ชั้นบรรยากาศชั้นล่าง =====
c.create_polygon(
    0,500,#ตั้งแต่ข้างซ้ายล่าง
    0,500,

    0,200,#มุมซ้ายบน
    0,200,

    500,200,#มุมขวาบน
    500,200,

    500,500,#ตั้งแต่ข้างขวาล่าง
    500,500,
    fill="#06A0E0", smooth = 1,outline="#06A0E0"
)


# ===== ทรายชั้นบน =====
c.create_polygon(
    0,500,#ตั้งแต่ข้างซ้ายล่าง
    0,500,

    0,280,#มุมซ้ายบน
    0,280,

    50,270,
    120,280,
    300,280,
    380,260,
    440,280,

    500,270,#มุมขวาบน
    500,270,

    500,500,#ตั้งแต่ข้างขวาล่าง
    500,500,
    fill="#869E88", smooth = 1,outline="#869E88"
)

# ===== ทรายชั้นกลาง =====
c.create_polygon(
    0,500,#ตั้งแต่ข้างซ้ายล่าง
    0,500,

    0,330,#มุมซ้ายบน
    0,330,

    120,310,
    250,350,
    400,320,

    500,300,#มุมขวาบน
    500,300,

    500,500,#ตั้งแต่ข้างขวาล่าง
    500,500,
    fill="#A4B29E", smooth = 1,outline="#A4B29E"
)
# ===== ทรายชั้นล่าง =====
c.create_polygon(
    0,500,
    0,500,

    0,380,
    0,380,

    100,350,
    250,400,
    400,380,

    500,420,
    500,420,

    500,500,
    500,500,
    fill="#DEE4C8", smooth = 1,outline="#DEE4C8"
)


# ===== ฟังก์ชันสร้างเม็ดสี 3 สี =====
def create_red_dot():
    radius = 1  # รัศมีเม็ดสี
    x0 = random.randint(radius, 500 - radius) #สีแดง
    y0 = random.randint(280, 500 - radius)
    x1 = random.randint(radius, 500 - radius) #สีเขียว
    y1 = random.randint(280, 500 - radius)
    x2 = random.randint(radius, 500 - radius) #สีเหลือง
    y2 = random.randint(280, 500 - radius)
    
    c.create_oval(  #สีแดง
        x0 - radius, y0 - radius, x0 + radius, y0 + radius, 
        fill="#87160D", outline="#87160D"
    )
    c.create_oval(  #สีเขียว
        x1 - radius, y1 - radius, x1 + radius, y1 + radius,
        fill="#07A27F", outline="#07A27F"
    )
    c.create_oval(  #สีเหลือง
        x2 - radius, y2 - radius, x2 + radius, y2 + radius,
        fill="#ECC112", outline="#ECC112"
    )

# สร้างเม็ดสีอย่างละ 50 เม็ด 
for _ in range(50):
    create_red_dot()

# ==== ร่ม ====
c.create_line(
    440,280,440,240,
    fill='black',width=3
)
c.create_polygon(
    440,210,400,240,420,240,430,250,
    fill="#BA9F1B"
)
c.create_polygon(
    440,210,430,250,440,240,460,250,
    fill="#BF8709"
)
c.create_polygon(
    440,210,460,250,460,240,475,235,
    fill="#A4750D"
)
# ==== ผ้าปู ====
c.create_polygon(
    430,280,390,290,400,310,440,300,
    fill="#408B89"
)
c.create_line(
    400,310,440,300,
    fill="black"
)


# ======================================== Body ===============================================
# ==== Upper Body ====
c.create_polygon(
    285,25,
    220,120,
    190,230,
    140,260,
    120,340,
    140,360,

    170,270,
    170,271,
    145,340,
    150,350,
    240,380,

    345,350,

    335,310,    #335,315,
    310,275,
    311,275,
    #310,275,
    335,315,    #335,315,
    350,355,
    365,370,
    380,330,
    380,280,
    315,225,
    300,140,

    fill="#FA9AA3", smooth = 1,outline="#FD341F", width=2
)
# ===== สะดือ =====
c.create_line(
    220,320,
    230,325,
    240,325,
    250,320,
    width=1
)
c.create_line(
    230,310,
    233,312,
    237,312,
    240,310,
    width=1
)

# ===== Legs =====
c.create_polygon(
    170,430,
    170,430,
    200,480,
    220,430,
    220,430,
    
    240,400,
    260,400,

    275,440,
    275,440,
    305,490,
    335,420,
    335,420,

    320,380,
    180,350,


    fill="#FA9AA3", smooth = 1,outline="#FD341F", width=2
)

# ===== Pant =====
c.create_polygon(
    151,332,    #ขอบกางเกง 145,340  150,330,
    149,332,
    145,360,    #150,360,

    160,425,
    160,425,

    195,435,
    235,430,
    235,420,
    236,419,

    215,415,
    195,410,

    196,409,
    215,414,
    236,419,
    250,420,
    270,415,
    271,416,
    260,420,

    259,419,
    260,440,
    305,440,
    345,430,
    335,400,

    345,330,
    330,340,
    220,350,

    fill="#CCE70B", smooth = 1,outline="black", width=2
)
c.create_line(
    150,338,
    208,352,

    230,353,

    295,350,
    342,342,
    width="2"
)

# ===== Pant Style =====
c.create_polygon(
    184,348,
    180,354,
    170,370,

    200,365,

    180,390,
    245,400,

    235,364,

    250,380,

    260,380,
    260,360,

    255,355,

    213,357,

    fill="#AF90C4", smooth = 1,outline="#757AB3", width=2
)
c.create_polygon(
    290,438,
    290,438,
    275,420,
    280,400,

    300,420,

    290,390,
    330,390,

    320,420,
    335,390,

    340,434,


    fill="#AF90C4", smooth = 1,outline="#757AB3", width=2
)
# ================================= Eyes ===============================================
# ================ Normal Eyes ================ 
# ===== Eye Left =====
eye_left = c.create_oval(
    210,130,240,170,
    fill="white", outline="black", width=2
)
# ===== Eye Left puppil =====
pupil_left = c.create_oval(
    220,142,230,158,
    fill="black", outline="black"
)
pupil_left1 = c.create_oval(
    224,144,228,150,
    fill="white"
)

# ===== Eye Right =====
eye_right = c.create_oval(
    240,130,270,170,
    fill="white", outline="black", width=2
)
# ===== Eye Right puppil =====
pupil_right = c.create_oval(
    250,142,260,158,
    fill="black", outline="black"
)
pupil_right1 = c.create_oval(
    254,144,258,150,
    fill="white"
)
# ================ Sad Eyes ================ 
# ===== Eye Left =====
c.create_polygon(
    212,155,
    212,160,
    222,170,
    230,170,
    238,160,
    238,160,
    fill="#8aadea", smooth = 1,
)
# ===== Eye Right =====
c.create_polygon(
    242,160,
    242,160,
    252,170,
    260,170,
    269,160,
    269,155,
    fill="#8aadea", smooth = 1,
)

# ================================= Mouth ===============================================
# ================ Normal Smile ================ state = HIDDEN
c.create_line(
    215,210,
    240,230,
    270,190,
    fill="black", smooth = 1, width=2,capstyle='round' , state = HIDDEN
)
c.create_line(
    265,185,
    270,190,
    275,190,

    fill="black", smooth = 1, width=2,capstyle='round' , state = HIDDEN
)
# ================ Devil Smile ================ state = HIDDEN
Devil_Smile = c.create_polygon(
    210,180,
    206,178,

    240,210,

    274,182,
    270,180,

    240,230,

    fill="#6A0503", smooth = 1,outline="black", width=2, state = HIDDEN
)
# ================ Sad Smile ================ 
Sad_Smile = c.create_line(
    210,210,    #Start 

    210,200,

    225,205,
                    #240,180,    #Middle
    230,190,

    240,200,    #middle

    250,190,

    260,205,

    270,200,    #End
    275,210,

    fill="black", smooth = 1, width=2,capstyle='round', #state = HIDDEN
)
Sad_Smile_Left1 = c.create_line(
    214,180,208,185,203,200,
    fill="black", smooth = 1, width=2,capstyle='round', #state = HIDDEN
)
Sad_Smile_Right1 = c.create_line(
    270,178,278,185,280,200,
    fill="black", smooth = 1, width=2,capstyle='round', #state = HIDDEN
)

Sad_Smile_Left2 = c.create_line(
    205,205,200,220,215,212,
    fill="black", smooth = 1, width=2,capstyle='round', #state = HIDDEN
)
Sad_Smile_Right2 = c.create_line(
    275,200,290,222,265,213,
    fill="black", smooth = 1, width=2,capstyle='round', #state = HIDDEN
)


# ================================= คิ้ว ===============================================
"""# ================ คิ้วแบบปกติ ================
# ===== คิ้วซ้าย =====
c.create_line(
    215,108,237,104,width=3
)
c.create_line(
    215,112,237,108,width=3
)
# ===== คิ้วขวา =====
c.create_line(
    245,104,267,108,width=3
)
c.create_line(
    245,108,267,112,width=3
)
"""
"""# ================ คิ้วแบบโกรธ ================
# ===== คิ้วซ้าย =====
c.create_line(
    215,104,237,114,width=3
)
c.create_line(
    215,108,237,118,width=3
)
# ===== คิ้วขวา =====
c.create_line(
    245,114,267,104,width=3
)
c.create_line(
    245,118,267,108,width=3
)"""

# ================ คิ้วแบบเศร้า ================
# ===== คิ้วซ้าย =====
c.create_line(
    215,124,237,114,width=3
)
c.create_line(
    215,128,237,118,width=3
)
# ===== คิ้วขวา =====
c.create_line(
    245,114,267,124,width=3
)
c.create_line(
    245,118,267,128,width=3
)


# ================================= Function ต่างๆ ========================================
"""# ===== กระพริบตา =====
def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_left1, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(pupil_right1, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(2500, blink) #ทุกๆ 2.5 วิ
"""
#แสดงหน้า Cry
def Cry():
    if not c.eyes_crossed:
        eyes_close()
        c.itemconfigure(heart_left, state=HIDDEN)
        c.itemconfigure(heart_right, state=HIDDEN)
        c.itemconfigure(eye_left_new, state=HIDDEN)
        c.itemconfigure(eye_right_new, state=HIDDEN)
        c.itemconfigure(eye_left_new2, state=NORMAL)
        c.itemconfigure(eye_right_new2, state=NORMAL)
        c.itemconfigure(eye_left_new3, state=HIDDEN)
        c.itemconfigure(eye_right_new3, state=HIDDEN)
        hide_happy(None)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_cry, state=NORMAL)
        c.itemconfigure(tear_left, state=NORMAL)
        c.itemconfigure(tear_right, state=NORMAL)
        c.eyes_crossed = True
    else:
        eyes_open()
        c.itemconfigure(heart_left, state=HIDDEN)
        c.itemconfigure(heart_right, state=HIDDEN)
        c.itemconfigure(eye_left_new, state=HIDDEN)
        c.itemconfigure(eye_right_new, state=HIDDEN)
        c.itemconfigure(eye_left_new2, state=HIDDEN)
        c.itemconfigure(eye_right_new2, state=HIDDEN)
        c.itemconfigure(eye_left_new3, state=HIDDEN)
        c.itemconfigure(eye_right_new3, state=HIDDEN)
        hide_happy(None)
        close_tear()
        c.eyes_crossed = False

# ================================= สร้างปุ่ม ===============================================
button_frame2 = Frame(root)
button_frame2.pack(side="bottom")
button_frame = Frame(root)
button_frame.pack(side="bottom")

#button1 = Button(button_frame, text="ANGRY", command=on_Love_click,bg="pink", fg="black",bd=3,padx=25, pady=10, font=("Arial Rounded MT Bold", 12, "bold"))
#button1.pack(side="left", padx=15, pady=5)
button2 = Button(button_frame, text="CRY", command=on_Cry_click,bg="pink", fg="black",bd=3,padx=30, pady=10, font=("Arial Rounded MT Bold", 12, "bold"))
button2.pack(side="right", padx=15, pady=5)


#กดปุ่ม CRY จะแสดงหน้า CRY เป็นเวลา 1 วินาที
def on_Cry_click():
    check_state()
    if c.check:
        Cry()
        stop_blinking()
        root.after(1000, Cry)
        start_blinking()
    return
#ตรวจสอบว่ามีการแสดงอารมณ์ต่างๆ
def check_state():
    current_state1 = c.itemcget(mouth_cry, 'state')
    #current_state2 = c.itemcget(mouth_love1, 'state')
    current_state3 = c.itemcget(mouth_angry, 'state')
    #current_state4 = c.itemcget(tongue_main, 'state')
    if current_state1 == HIDDEN and current_state3 == HIDDEN :
        c.check = True
    else:
        c.check = False
        
    return

# ================================= Grid ===============================================

""# ===== Grid =====
grid_size = 20  # ความถี่ของเส้นแบ่ง (10 พิกเซล)
for x in range(0, 501, grid_size):                   # วาดเส้นแนวตั้ง (แกน Y)
    c.create_line(x, 0, x, 500, fill="#383838")

for x in range(0, 501, 50):     #ทุกๆ 50
    c.create_line(x, 0, x, 500, fill="red")
    c.create_text(x + 2, 6, text=str(x), anchor="nw", font=("Arial", 10,"bold"), fill="purple")
    c.create_text(x + 2, 500 - 15, text=str(x), anchor="nw", font=("Arial", 10,"bold"), fill="purple")

for x in range(0, 501, 100):     #ทุกๆ 100
    c.create_line(x, 0, x, 500, fill="blue")

for y in range(0, 501, grid_size):                  # วาดเส้นแนวนอน (แกน X)
    c.create_line(0, y, 500, y, fill="#383838")

for y in range(0, 501, 50):
    c.create_line(0, y, 500, y, fill="red")
    c.create_text(5, y + 2, text=str(y), anchor="nw", font=("Arial Rounded MT", 10,"bold"), fill="black")
    c.create_text(500 - 25, y + 2, text=str(y), anchor="nw", font=("Arial", 10,"bold"), fill="black")

for y in range(0, 501, 100):
    c.create_line(0, y, 500, y, fill="blue")
""

#root.after(1000, blink)
root.mainloop()