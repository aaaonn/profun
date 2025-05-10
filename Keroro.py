from tkinter import Tk, Canvas, Button, Frame, Label

root = Tk()
root.title("Keroro Face")
c = Canvas(root, width=500, height=500, bg='#94EDFA')
c.pack()
c.check =True

# ===== หูซ้าย =====
c.create_polygon(
    140,70,
    30,340,     #50,320,
    60,380,
    160,400,    #150,380,
    150,320,    #200,350
    fill="#f9d75e", smooth = 1,outline="black", width=2
)

# ===== หูขวา =====
c.create_polygon(
    355,65,
    470,340,
    440,380,
    340,400,
    350,320,
    fill="#f9d75e", smooth = 1, outline="black",width=2
)

# ===== ใบหน้า =====
c.create_oval(100, 100, 400, 400, fill="#61b45f", outline="black", width=2)  # สีเขียวใบหน้า

# ===== ดวงตา =====
c.create_oval(120, 160, 240, 280, fill="white", outline="black", width=2)
c.create_oval(260, 160, 380, 280, fill="white", outline="black", width=2)

# ===== ตาดำ =====
c.create_oval(150, 190, 210, 250, fill="black", outline="white", width=3)  # ตาซ้าย
c.create_oval(290, 190, 350, 250, fill="black", outline="white", width=3)  # ตาขวา

# ===== หมวกเหลือง =====
c.create_arc(
    120, 90, 
    380, 220, 
    start=0, extent=180, fill="#f9d75e", outline="black", width=2
)
c.create_polygon(
    180, 140,
    130, 170,
    100, 200, 
    100, 190, 
    115, 150,
    130, 125,
    fill="#f9d75e", smooth = 1
)
c.create_polygon(
    360,120,
    390,150,
    400,200,
    370,170,
    330,140,

    fill="#f9d75e", smooth = 1
)

# ===== ดาวกลางหน้าผาก =====
c.star = '\u2605'
c.color = '#d24a55'
c.fs = 34
c.create_text(250,134,text=f'{c.star}', font=("Arial", c.fs, "bold"), fill=c.color,)


# ===== ปาก =====
c.create_polygon(
    140,368,
    225,355,#
    250,350,
    285,355,#
    360,368,
    250,412,

    fill="white", smooth = 1,outline="black", width=2
)
c.create_polygon(
    215,355,
    250,350,
    285,355,
    250,390,
    fill="#C86671", smooth = 1,outline="black", width=2
)

#===== เส้นเก็บงาน =====
c.create_line(
    120,140,140,120,
    fill='black',width=2
)
c.create_line(
    115,186,
    132,168,
    158,154,
    fill='black',width=2
)
c.create_line(
    350,155,
    358,160,
    370,169,
    388,190,
    fill='black',width=2
)
c.create_line(
    360,120,
    383,144,
    fill='black',width=2
)


"""# ===== Grid =====
grid_size = 20  # ความถี่ของเส้นแบ่ง (10 พิกเซล)
for x in range(0, 501, grid_size):                   # วาดเส้นแนวตั้ง (แกน Y)
    c.create_line(x, 0, x, 500, fill="#383838")

for x in range(0, 501, 50):     #ทุกๆ 50
    c.create_line(x, 0, x, 500, fill="red")

for x in range(0, 501, 100):     #ทุกๆ 100
    c.create_line(x, 0, x, 500, fill="blue")

for y in range(0, 501, grid_size):                  # วาดเส้นแนวนอน (แกน X)
    c.create_line(0, y, 500, y, fill="#383838")

for y in range(0, 501, 50):
    c.create_line(0, y, 500, y, fill="red")

for y in range(0, 501, 100):
    c.create_line(0, y, 500, y, fill="blue")
"""

root.mainloop()
