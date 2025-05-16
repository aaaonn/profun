import random
from tkinter import HIDDEN, NORMAL, Tk, Canvas, Button, Frame, Label

root = Tk()
root.title("Patrick V2")
c = Canvas(root, width=500, height=500, bg='#20C5E1')
c.pack()
c.check =True
c.body_color = "#FA9AA3"
# ================================= Function ต่างๆ ========================================
# ===== กระพริบตา =====

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
    root.after(2500, blink)


# ===== ดีใจ (เอาเม้าเข้า) =====
def show_happy(event):
    if (200 <= event.x and event.x <= 300) and (50 <= event.y and event.y <= 220) :
        c.itemconfigure(devil_smile, state=NORMAL)

        c.itemconfigure(eyebrow_devil_left1, state=NORMAL)
        c.itemconfigure(eyebrow_devil_left2, state=NORMAL)
        c.itemconfigure(eyebrow_devil_right1, state=NORMAL)
        c.itemconfigure(eyebrow_devil_right2, state=NORMAL)

        c.itemconfigure(eyebrow_left1, state=HIDDEN)
        c.itemconfigure(eyebrow_left2, state=HIDDEN)
        c.itemconfigure(eyebrow_right1, state=HIDDEN)
        c.itemconfigure(eyebrow_right2, state=HIDDEN)
        c.itemconfigure(normal_smile, state=HIDDEN)
        c.itemconfigure(normal_smile1, state=HIDDEN)

        c.itemconfigure(sad_smile, state=HIDDEN)
        c.itemconfigure(sad_smile_left1, state=HIDDEN)
        c.itemconfigure(sad_smile_left2, state=HIDDEN)
        c.itemconfigure(sad_smile_right1, state=HIDDEN)
        c.itemconfigure(sad_smile_right2, state=HIDDEN)

        c.itemconfigure(eyebrow_sad_left1, state=HIDDEN)
        c.itemconfigure(eyebrow_sad_left2, state=HIDDEN)
        c.itemconfigure(eyebrow_sad_right1, state=HIDDEN)
        c.itemconfigure(eyebrow_sad_right2, state=HIDDEN)

        c.itemconfigure(tear_left, state=HIDDEN)
        c.itemconfigure(tear_right, state=HIDDEN)
        c.happy_level = 6
    return

# ===== ซ่อนดีใจ (เอาเม้าออก) =====
def hide_happy(event):
    c.itemconfigure(devil_smile, state=HIDDEN)
    c.itemconfigure(eyebrow_devil_left1, state=HIDDEN)
    c.itemconfigure(eyebrow_devil_left2, state=HIDDEN)
    c.itemconfigure(eyebrow_devil_right1, state=HIDDEN)
    c.itemconfigure(eyebrow_devil_right2, state=HIDDEN)

    c.itemconfigure(eyebrow_left1, state=NORMAL)
    c.itemconfigure(eyebrow_left2, state=NORMAL)
    c.itemconfigure(eyebrow_right1, state=NORMAL)
    c.itemconfigure(eyebrow_right2, state=NORMAL)
    c.itemconfigure(normal_smile, state=NORMAL) 
    c.itemconfigure(normal_smile1, state=NORMAL)

    c.itemconfigure(sad_smile, state=HIDDEN)
    c.itemconfigure(sad_smile_left1, state=HIDDEN)
    c.itemconfigure(sad_smile_left2, state=HIDDEN)
    c.itemconfigure(sad_smile_right1, state=HIDDEN)
    c.itemconfigure(sad_smile_right2, state=HIDDEN)
    
    return

# ===== เศร้า =====
def sad():
    if c.happy_level == 0:
        c.itemconfigure(devil_smile, state=HIDDEN)

        c.itemconfigure(eyebrow_devil_left1, state=HIDDEN)
        c.itemconfigure(eyebrow_devil_left2, state=HIDDEN)
        c.itemconfigure(eyebrow_devil_right1, state=HIDDEN)
        c.itemconfigure(eyebrow_devil_right2, state=HIDDEN)

        c.itemconfigure(normal_smile, state=HIDDEN)
        c.itemconfigure(normal_smile1, state=HIDDEN)
        c.itemconfigure(eyebrow_left1, state=HIDDEN)
        c.itemconfigure(eyebrow_left2, state=HIDDEN)
        c.itemconfigure(eyebrow_right1, state=HIDDEN)
        c.itemconfigure(eyebrow_right2, state=HIDDEN)

        c.itemconfigure(sad_smile, state=NORMAL)
        c.itemconfigure(sad_smile_left1, state=NORMAL)
        c.itemconfigure(sad_smile_left2, state=NORMAL)
        c.itemconfigure(sad_smile_right1, state=NORMAL)
        c.itemconfigure(sad_smile_right2, state=NORMAL)
        c.itemconfigure(eyebrow_sad_left1, state=NORMAL)
        c.itemconfigure(eyebrow_sad_left2, state=NORMAL)
        c.itemconfigure(eyebrow_sad_right1, state=NORMAL)
        c.itemconfigure(eyebrow_sad_right2, state=NORMAL)

        c.itemconfigure(tear_left, state=NORMAL)
        c.itemconfigure(tear_right, state=NORMAL)
    else:
        c.happy_level -= 3
    root.after(1500, sad)

def toggle_happy():
    if not c.happy_show:
        c.itemconfigure(normal_body, state=HIDDEN)

        c.itemconfigure(normal_smile, state=HIDDEN) 
        c.itemconfigure(normal_smile1, state=HIDDEN)

        c.itemconfigure(sad_smile, state=HIDDEN)
        c.itemconfigure(sad_smile_left1, state=HIDDEN)
        c.itemconfigure(sad_smile_left2, state=HIDDEN)
        c.itemconfigure(sad_smile_right1, state=HIDDEN)
        c.itemconfigure(sad_smile_right2, state=HIDDEN)
        c.itemconfigure(eyebrow_sad_left1, state=HIDDEN)
        c.itemconfigure(eyebrow_sad_left2, state=HIDDEN)
        c.itemconfigure(eyebrow_sad_right1, state=HIDDEN)
        c.itemconfigure(eyebrow_sad_right2, state=HIDDEN)
        c.itemconfigure(tear_left, state=HIDDEN)
        c.itemconfigure(tear_right, state=HIDDEN)

        c.itemconfigure(happy_body, state=NORMAL)

        c.itemconfigure(happy_smile, state=NORMAL)
        c.itemconfigure(happy_smile1, state=NORMAL)
        c.happy_show = True
    else:
        c.itemconfigure(normal_body, state=NORMAL)

        c.itemconfigure(normal_smile, state=NORMAL) 
        c.itemconfigure(normal_smile1, state=NORMAL)

        c.itemconfigure(happy_body, state=HIDDEN)

        c.itemconfigure(happy_smile, state=HIDDEN)
        c.itemconfigure(happy_smile1, state=HIDDEN)

        c.happy_show = False


def toggle_tongue():
    if not c.tongue_show:
        c.itemconfigure(tongue, state=NORMAL)
        c.itemconfigure(tongue_line, state=NORMAL)
        c.tongue_show = True
    else:
        c.itemconfigure(tongue, state=HIDDEN)
        c.itemconfigure(tongue_line, state=HIDDEN)
        c.tongue_show = False

def happy(event):
    toggle_tongue()
    toggle_happy()
    hide_happy(event)
    root.after(1100, toggle_tongue)
    root.after(1100, toggle_happy)
    c.happy_level = 6
    return

# ================================= Background ========================================
# ===== ชั้นบรรยากาศชั้นกลาง =====
c.create_polygon(
    0,500,0,500,0,100,0,100,500,100,500,100,500,500,500,500,
    fill="#10ADDE", smooth = 1,outline="#10ADDE"#17B6DE
)
# ===== ชั้นบรรยากาศชั้นล่าง =====
c.create_polygon(
    0,500,0,500,0,200,0,200,500,200,500,200,500,500,500,500,
    fill="#06A0E0", smooth = 1,outline="#06A0E0"
)

# ===== ทรายชั้นบน =====
c.create_polygon(
    0,500,0,500,0,280,0,280,50,270,120,280,300,280,380,260,440,280,500,270,500,270,500,500,500,500,
    fill="#869E88", smooth = 1,outline="#869E88"
)

# ===== ทรายชั้นกลาง =====
c.create_polygon(
    0,500,0,500,0,330,0,330,120,310,250,350,400,320,500,300,500,300,500,500,500,500,
    fill="#A4B29E", smooth = 1,outline="#A4B29E"
)

# ===== ทรายชั้นล่าง =====
c.create_polygon(
    0,500,0,500,0,380,0,380,100,350,250,400,400,380,500,420,500,420,500,500,500,500,
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
# ================ Normal Body ================
normal_body = c.create_polygon(
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

    fill="#FA9AA3", smooth = 1,outline="#FD341F", width=2 , 
)

# ================ Happy Body ================ state=HIDDEN
happy_body = c.create_polygon(
    285,25,
    220,120,
    190,250,

    130,140,

    112,130,

    110,150,

    120,220,

    150,270,

    160,271,
    145,340,
    150,350,
    240,380,

    345,350,

    335,310,    #335,315,
    
    350,270,

    380,240,

    410,150,

    400,140,

    390,140,

    315,240,
    300,140,

    fill="#FA9AA3", smooth = 1,outline="#FD341F", width=2 , state=HIDDEN
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
# ================ Sad Eyes ================  state=HIDDEN
# ===== Eye Left =====
tear_left = c.create_polygon(
    212,155,212,160,222,170,230,170,238,160,238,160,
    fill="#8aadea", smooth = 1, state=HIDDEN
)
# ===== Eye Right =====
tear_right = c.create_polygon(
    242,160,242,160,252,170,260,170,269,160,269,155,
    fill="#8aadea", smooth = 1, state=HIDDEN
)

# ================================= Mouth ===============================================
# ================ Normal Smile ================ 
normal_smile = c.create_line(
    220,210,
    240,230,
    270,190,
    fill="black", smooth = 1, width=2,capstyle='round' , 
)
normal_smile1 = c.create_line(
    265,185,
    270,190,
    275,190,

    fill="black", smooth = 1, width=2,capstyle='round' , 
)
# ================ Devil Smile ================ state = HIDDEN
devil_smile = c.create_polygon(
    210,180,
    206,178,

    240,210,

    274,182,
    270,180,

    240,230,

    fill="#6A0503", smooth = 1,outline="black", width=2, state = HIDDEN
)
# ================ Sad Smile ================ state=HIDDEN
sad_smile = c.create_line(
    210,210,    #Start 

    210,200,

    225,205,

    230,190,

    240,200,    #middle

    250,190,

    260,205,

    270,200,    #End
    275,210,

    fill="black", smooth = 1, width=2,capstyle='round', state = HIDDEN
)
sad_smile_left1 = c.create_line(
    214,180,208,185,203,200,
    fill="black", smooth = 1, width=2,capstyle='round', state = HIDDEN
)
sad_smile_right1 = c.create_line(
    270,178,278,185,280,200,
    fill="black", smooth = 1, width=2,capstyle='round', state = HIDDEN
)

sad_smile_left2 = c.create_line(
    205,205,200,220,215,212,
    fill="black", smooth = 1, width=2,capstyle='round', state = HIDDEN
)
sad_smile_right2 = c.create_line(
    275,200,290,222,265,213,
    fill="black", smooth = 1, width=2,capstyle='round', state = HIDDEN
)
# ================ Happy Smile ================ state = HIDDEN
happy_smile = c.create_polygon(
    215,190,215,195,240,200,278,184,255,230,210,220,210,220,215,220,225,195,220,197,
    fill="#821B29", outline = "black" , width = 2 ,smooth = 1  , state = HIDDEN
)
happy_smile1 = c.create_line(
    265,185,270,190,275,190,
    fill="black", smooth = 1, width=2,capstyle='round' , state = HIDDEN
)
# ================ tongue ================ state = HIDDEN
tongue = c.create_polygon(
    220,220,
    245,210,
    265,215,
    240,228,
    fill="#F7B8C0", outline = "black" , width = 2 , smooth = 1  , state = HIDDEN
)
tongue_line = c.create_line(
    255,214,
    245,215,
    244,218,
    fill="black" , width = 2 , smooth = 1  , state = HIDDEN
)


# ================================= คิ้ว ===============================================
# ================ คิ้วแบบปกติ ================
# ===== คิ้วซ้าย =====
eyebrow_left1 = c.create_line(
    215,108,237,104,width=3
)
eyebrow_left2 = c.create_line(
    215,112,237,108,width=3
)
# ===== คิ้วขวา =====
eyebrow_right1 = c.create_line(
    245,104,267,108,width=3
)
eyebrow_right2 = c.create_line(
    245,108,267,112,width=3
)

# ================ คิ้วแบบโกรธ ================  , state=HIDDEN
# ===== คิ้วซ้าย =====
eyebrow_devil_left1 = c.create_line(
    215,104,237,114,width=3 , state=HIDDEN
)
eyebrow_devil_left2 = c.create_line(
    215,108,237,118,width=3 , state=HIDDEN
)
# ===== คิ้วขวา =====
eyebrow_devil_right1 = c.create_line(
    245,114,267,104,width=3 , state=HIDDEN
)
eyebrow_devil_right2 = c.create_line(
    245,118,267,108,width=3 , state=HIDDEN
)

# ================ คิ้วแบบเศร้า ================ state=HIDDEN
# ===== คิ้วซ้าย =====
eyebrow_sad_left1 = c.create_line(
    215,124,237,114,width=3 , state=HIDDEN
)
eyebrow_sad_left2 = c.create_line(
    215,128,237,118,width=3 , state=HIDDEN
)
# ===== คิ้วขวา =====
eyebrow_sad_right1 = c.create_line(
    245,114,267,124,width=3 , state=HIDDEN
)
eyebrow_sad_right2 = c.create_line(
    245,118,267,128,width=3 , state=HIDDEN
)




# ================================= Grid ===============================================

"""# ===== Grid =====
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
"""

c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', happy)

c.happy_level = 6
c.happy_show = False
c.tongue_show = False

root.after(1000, blink)
root.after(2000, sad)
root.mainloop()