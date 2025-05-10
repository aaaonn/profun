from tkinter import HIDDEN, NORMAL, Tk, Canvas, Button, Frame, Label
# สร้างหน้าต่างหลัก
root = Tk()
root.title("Patrick Star - Minimal Triangle Version")
canvas = Canvas(root, width=500, height=500, bg="skyblue")
canvas.pack()
canvas.ss = '\u2606' #269d 2730 2606(emoji)
canvas.fs = 50
canvas.cc = "#FFF3C3"

background_elements = []
for i in range(5):
    bg = canvas.create_text(250, 50 + i * 100, text=f'{canvas.ss} {canvas.ss} {canvas.ss} {canvas.ss} {canvas.ss}', font=("Arial", canvas.fs, "bold"), fill=canvas.cc)
    background_elements.append(bg)

# หัวสามเหลี่ยม (หัว Patrick)
canvas.create_polygon(250, 30, 100, 420, 400, 420, fill="#f4a7b9", outline="black", width=3)

# ตาซ้าย
canvas.create_oval(150, 190, 240, 300, fill="white", outline="black") #ซ้าย บน ขวา ล่าง
canvas.create_oval(170, 225, 195, 260, fill="black")
canvas.create_oval(170, 225, 185, 245, fill="white")

# ตาขวา
canvas.create_oval(235, 190, 320, 300, fill="white", outline="black")
canvas.create_oval(250, 225, 275, 260, fill="black")
canvas.create_oval(250, 225, 265, 245, fill="white")

# ปาก
canvas.create_arc(200, 280, 300, 340, start=0, extent=-180, style="arc", width=3)
#canvas.create_oval(240, 310, 260, 330, fill="red")  # ลิ้น

# คิ้ว (เส้น)
# ซ้าย
canvas.create_line(170, 190, 230, 180, width=4)
canvas.create_line(170, 185, 230, 175, width=4)

# ขวา
canvas.create_line(270, 180, 310, 190, width=4)
canvas.create_line(270, 175, 310, 185, width=4)

# จบการแสดงผล
root.mainloop()