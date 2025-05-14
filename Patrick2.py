import random
from tkinter import HIDDEN, NORMAL, Tk, Canvas, Button, Frame, Label

root = Tk()
root.title("Keroro Face")
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
    root.after(2500, blink) #ทุกๆ 2.5 วิ

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
# ================================= Eyes ========================================
# ===== Eye Left =====
eye_left = c.create_oval(
    210,130,240,170,
    #250,130,280,170,

    fill="white", outline="black", width=2
)
# ===== Eye Left Ball =====
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
# ===== Eye Right Ball =====
pupil_right = c.create_oval(
    250,142,260,158,

    fill="black", outline="black"
)
pupil_right1 = c.create_oval(
    254,144,258,150,
    fill="white"
)


# ===== Smile =====
c.create_polygon(
    210,180,
    206,178,

    240,210,

    274,182,
    270,180,

    240,230,

    fill="#6A0503", smooth = 1,outline="black", width=2
)

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
)





# ================================= Grid ========================================

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

root.after(1000, blink)
root.mainloop()