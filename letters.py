import polygon, turtle, math

def draw_a(t, l):
    t.lt(90)
    polygon.circle(t, l)
    t.fd(l)
    t.lt(180)
    t.fd(2*l)
    t.lt(90)

def draw_b(t, l):
    t.lt(90)
    t.fd(2*l)
    t.lt(180)
    t.fd(1.5*l)
    polygon.circle(t,l/2)
    t.lt(90)

def draw_c(t, l):
    t.lt(120)
    polygon.arc(t, l, 300)
    t.lt(-60)

def draw_d(t, l):
    t.lt(90)
    polygon.circle(t, l/2)
    t.fd(1.5*l)
    t.lt(180)
    t.fd(2*l)
    t.lt(90)

def draw_e(t,l):
    t.fd(2*l)
    t.lt(90)
    polygon.arc(t, l, 320)
    t.lt(-50)

def draw_f(t, l):
    t.lt(90)
    polygon.arc(t, l/2, 180)
    t.fd(2*l)
    t.lt(180)
    t.fd(l)
    t.lt(90)
    t.fd(l/2)
    t.lt(180)
    t.fd(l)

def draw_g(t, l):
    t.lt(90)
    polygon.circle(t, l)
    t.fd(l/2)
    t.lt(180)
    t.fd(2*l)
    polygon.arc(t,l, -180)
    t.rt(90)

def draw_h(t, l):
    t.lt(90)
    t.fd(l/2)
    polygon.arc(t, l/2, 180)
    t.fd(l/2)
    t.lt(180)
    t.fd(2*l)
    t.rt(90)

def draw_i(t, l):
    t.lt(90)
    t.fd(l)
    t.pu()
    t.fd(l/2)
    t.pd()
    polygon.circle(t, 2)
    t.rt(90)

def draw_j(t, l):
    t.lt(-90)
    polygon.arc(t, l/4, 180)
    t.fd(l)
    t.pu()
    t.fd(l/2)
    t.pd()
    polygon.circle(t, 2)
    t.rt(90)

def draw_k(t, l):
    t.lt(90)
    t.fd(2*l)
    t.lt(180)
    t.fd(1.5*l)
    t.lt(45)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(180)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(-90)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.rt(45)

def draw_l(t, l):
    t.lt(90)
    t.fd(2*l)
    t.rt(90)

def draw_m(t, l):
    t.lt(90)
    t.fd(l)
    polygon.arc(t, l, 180)
    t.fd(l)
    t.lt(180)
    t.fd(l)
    polygon.arc(t, l, 180)
    t.fd(l)
    t.lt(180)
    t.fd(2*l)
    t.rt(90)

def draw_n(t, l):
    t.lt(90)
    t.fd(l)
    polygon.arc(t, l, 180)
    t.fd(l)
    t.lt(180)
    t.fd(2*l)
    t.rt(90)

def draw_o(t, l):
    polygon.circle(t, l)

def draw_p(t, l):
    t.lt(90)
    polygon.circle(t, l/2)
    t.pu()
    t.lt(90)
    t.fd(l)
    t.rt(90)
    t.pd()
    t.fd(l/2)
    t.lt(180)
    t.fd(2*l)
    t.lt(90)

def draw_q(t, l):
    t.lt(90)
    polygon.circle(t, l/2)
    t.fd(0.5*l)
    t.lt(180)
    t.fd(2*l)
    t.lt(90)

def draw_r(t,l):
    t.lt(90)
    polygon.arc(t, l/4, 180)
    t.lt(180)
    t.fd(l/4)
    t.lt(180)
    t.fd(l)
    t.lt(90)

def draw_s(t, l):
    t.lt(90)
    polygon.arc(t, l / 4, 180)
    polygon.arc(t, l / 4, 90)
    polygon.arc(t, l / 4, -90)
    polygon.arc(t, l / 4, -180)
    t.rt(90)

def draw_t(t, l):
    t.lt(-90)
    polygon.arc(t, l / 4, -180)
    t.fd(3*l/2)
    t.lt(180)
    t.fd(l/2)
    t.lt(90)
    t.fd(l/4)
    t.lt(180)
    t.fd(l/2)
    t.lt(180)

def draw_u(t, l):
    t.lt(90)
    t.fd(l)
    t.lt(180)
    t.fd(l/2)
    polygon.arc(t, l/2, -180)
    t.fd(l/2)
    t.rt(90)

def draw_v(t, l):
    t.lt(45)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(180)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.rt(90)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.rt(135)

def draw_w(t, l):
    t.lt(45)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(180)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.rt(90)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(90)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.rt(90)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.rt(135)

def draw_x(t, l):
    t.lt(135)
    t.fd(2* ((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(180)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(90)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(180)
    t.fd(2 * ((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(135)

def draw_y(t, l):
    t.lt(135)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(180)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(90)
    t.fd(((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(180)
    t.fd(2 * ((l / 2) ** 2 + (l / 2) ** 2) ** 0.5)
    t.lt(135)

def draw_z(t, l):
    t.lt(180)
    t.fd(l)
    t.rt(135)
    t.fd((((l / 2) ** 2 + (l / 2) ** 2) - 2 * l * l * math.cos(math.radians(135)))** 0.5)
    t.lt(135)
    t.fd(l)
    t.lt(180)

bob = turtle.Turtle()

