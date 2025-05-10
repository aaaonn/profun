from tkinter import Tk, Canvas

root = Tk()
root.title("Keroro Face")
canvas = Canvas(root, width=500, height=500, bg='white')
canvas.pack()

# ===== ใบหน้า =====
canvas.create_oval(100, 100, 400, 400, fill="#6CBF00", outline="black", width=2)  # สีเขียวใบหน้า

# ===== ดวงตา =====
canvas.create_oval(120, 160, 240, 280, fill="white", outline="black", width=2)
canvas.create_oval(260, 160, 380, 280, fill="white", outline="black", width=2)

# ===== ตาดำ =====
canvas.create_oval(150, 190, 210, 250, fill="black")  # ตาซ้าย
canvas.create_oval(290, 190, 350, 250, fill="black")  # ตาขวา

# ===== ปาก =====
#canvas.create_arc(160, 220, 240, 280, start=0, extent=-180, style='arc', width=2)

# ===== หมวกเหลือง =====
canvas.create_arc(
    70, 40, 
    330, 200, 




    
    start=0, extent=180, fill="yellow", outline="black", width=2
)

# ===== ดาวกลางหน้าผาก =====
canvas.create_polygon(
    200, 80,   # จุดบนสุด
    210, 110,
    240, 110,
    215, 130,
    225, 160,
    200, 140,
    175, 160,
    185, 130,
    160, 110,
    190, 110,
    fill="gold", outline="black"
)

root.mainloop()
