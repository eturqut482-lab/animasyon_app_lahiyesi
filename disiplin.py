import turtle
import time

# ==========================================
# ⚙️ EKRAN AYARLARI (Canlı Animasiya üçün)
# ==========================================
ekran = turtle.Screen()
ekran.bgcolor("black")
ekran.title("Motive - Discipline")
# Diqqət: Bu dəfə tracer(0) YOXDUR ki, hərəkəti canlı görə bilək!

# ==========================================
# ✍️ MƏRKƏZİ YAZI: DISCIPLINE
# ==========================================
yazi = turtle.Turtle()
yazi.hideturtle()
yazi.penup()
yazi.goto(0, -15) # Yazını tam mərkəzə oturtmaq üçün
yazi.color("white")
yazi.write("DISCIPLINE", align="center", font=("Arial", 36, "bold"))

yazi.goto(0, -45)
yazi.color("#00f3ff") # Neon Mavi
yazi.write("Consistency is the key", align="center", font=("Courier", 14, "italic"))

# ==========================================
# 🌀 HƏRƏKƏTLİ ANİMASİYA (Neon Tor)
# ==========================================
qelem = turtle.Turtle()
qelem.speed(0)     # Ən sürətli qələm, amma gözlə görünən hərəkət
qelem.pensize(2)
qelem.hideturtle()

# Kiber rənglər (Mavi, Ağ, Bənövşəyi, Firuzəyi)
rengler = ["#00f3ff", "#ffffff", "#8a2be2", "#00ffcc"]

for i in range(250):
    qelem.color(rengler[i % 4])
    
    # Yazının üstündən keçməmək üçün əvvəlcə mərkəzdən 85 piksel uzaqlaşırıq
    qelem.penup()
    qelem.forward(85)  
    
    # Cızmağa başlayırıq
    qelem.pendown()
    qelem.forward(i)   # Xətti çəkirik (hər dövrdə xətt uzanır)
    qelem.left(59)     # Ulduz formalı kəskin dönüş
    
    # Qələmi qaldırıb yenidən mərkəzə qaytarırıq ki, növbəti xətti atsın
    qelem.penup()
    qelem.goto(0, 0)
    qelem.left(2)      # Növbəti xətt üçün fırlanma bucağı

# Animasiya bitəndən sonra ekran dərhal bağlanmasın deyə 10 saniyə gözləyir
time.sleep(10)