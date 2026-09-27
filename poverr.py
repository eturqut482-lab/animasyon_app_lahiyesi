import turtle
import colorsys
import time

# ==========================================
# ⚙️ EKRAN AYARLARI
# ==========================================
ekran = turtle.Screen()
ekran.bgcolor("black")
ekran.title("Arzular Portalı")

# ==========================================
# ✍️ MƏRKƏZİ YAZI (Tam qorunan zonada)
# ==========================================
yazi = turtle.Turtle()
yazi.hideturtle()
yazi.penup()

# Birinci sətir (Ağ rəng)
yazi.goto(0, 15)
yazi.color("white")
yazi.write("ARZULARINI", align="center", font=("Arial", 28, "bold"))

# İkinci sətir (Qızılı rəng - Uğur simvolu)
yazi.goto(0, -35)
yazi.color "#C3FF00") 
yazi.write("GERÇƏKLƏŞDİR", align="center", font=("Arial", 36, "bold"))

# ==========================================
# 🌌 3D PORTAL ANİMASİYASI (Yazıya toxunmur!)
# ==========================================
qelem = turtle.Turtle()
qelem.speed(0)
qelem.pensize(2)
qelem.hideturtle()

# Portalı çəkməyə başlayırıq
for i in range(250):
    # Rənglərin axıcı dəyişməsi (Göy qurşağı effekti)
    reng = colorsys.hsv_to_rgb(i / 250, 1.0, 1.0)
    qelem.pencolor(reng)
    
    qelem.penup()
    qelem.goto(0, 0)
    
    # Qələmi fırladırıq (11 dərəcə çox qəşəng 3D spiral yaradır)
    qelem.setheading(i * 11) 
    
    # ❗️ ƏSAS HİYLƏ: Qələmi mərkəzdən 170 piksel uzağa atırıq ki, yazıya toxunmasın!
    qelem.forward(170) 
    
    qelem.pendown()
    # Dairələr çəkərək 3D "Donut" (Torus) forması yaradırıq
    qelem.circle(i * 0.6)

# Animasiya bitdikdən sonra pəncərə dərhal bağlanmasın
time.sleep(10)