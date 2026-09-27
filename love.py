import math
import turtle

# ==========================================
# ⚙️ EKRAN VƏ QƏLƏM AYARLARI
# ==========================================
ekran = turtle.Screen()
ekran.bgcolor("black")  # Arxa fon qara (Hacker stili)
ekran.title("Mühəndis Romantikası")

qelem = turtle.Turtle()
qelem.speed(0)          # Çəkmə sürəti (ən sürətli)
qelem.color("#ff007f")  # Neon çəhrayı rəng
qelem.penup()           # Qələmi havaya qaldır (hələ yazma)

# ==========================================
# 🧮 ÜRƏYİN RİYAZİ FORMULU (Heart Equation)
# ==========================================
def urek_x(t):
    return 16 * math.sin(t) ** 3  

def urek_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

# ==========================================
# 🎨 ANİMASİYANI İŞƏ SAL (Zərrəciklər)
# ==========================================
for i in range(250):
    x = urek_x(i) * 15  # x oxu üzrə genişlik (15 dəfə böyüdürük)
    y = urek_y(i) * 15  # y oxu üzrə hündürlük
    qelem.goto(x, y)    # Qələmi o nöqtəyə apar
    qelem.pendown()     # Və həmin nöqtəni cız

# Ekranda "I Love You" mesajı yazmaq
qelem.penup()
qelem.goto(0, -50)
qelem.color("white")
qelem.write("SƏNİ SEVİRƏM", align="center", font=("Arial", 24, "bold"))

qelem.hideturtle()
turtle.done()