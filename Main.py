from tkinter import HIDDEN, NORMAL, Tk, Canvas, Button, Frame, Label
# สร้างหน้าต่างหลัก
root = Tk()
root.title("Patrick Star - Minimal Triangle Version")
c = Canvas(root, width=500, height=500, bg="skyblue")
c.pack()
c.ss = '\u2606' #269d 2730 2606(emoji)
c.fs = 50
c.cc = "#FFF3C3"

"""background_elements = []
for i in range(5):
    bg = c.create_text(250, 50 + i * 100, text=f'{c.ss} {c.ss} {c.ss} {c.ss} {c.ss}', font=("Arial", c.fs, "bold"), fill=c.cc)
    background_elements.append(bg)"""

# หัวสามเหลี่ยม (หัว Patrick)
c.create_polygon(250, 30, 100, 420, 400, 420, fill="#f4a7b9", outline="black", width=3)

# ตาซ้าย
c.create_oval(150, 190, 240, 300, fill="white", outline="black") #ซ้าย บน ขวา ล่าง
c.create_oval(170, 225, 195, 260, fill="black")
c.create_oval(170, 225, 185, 245, fill="white")

# ตาขวา
c.create_oval(235, 190, 320, 300, fill="white", outline="black")
c.create_oval(250, 225, 275, 260, fill="black")
c.create_oval(250, 225, 265, 245, fill="white")

# ปาก
c.create_arc(200, 280, 300, 340, start=0, extent=-180, style="arc", width=3)
#canvas.create_oval(240, 310, 260, 330, fill="red")  # ลิ้น

# คิ้ว (เส้น)
# ซ้าย
c.create_line(170, 190, 230, 180, width=4)
c.create_line(170, 185, 230, 175, width=4)

# ขวา
c.create_line(270, 180, 310, 190, width=4)
c.create_line(270, 175, 310, 185, width=4)




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


root.after(1000, blink)
root.mainloop()