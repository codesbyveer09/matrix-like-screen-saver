import pygame,time,random

def init():
    global blue, red, d_green, green, yellow, cyan, lime,\
       orange, white, black, grey, night_blue

    blue = 100, 120, 180
    red = 200, 0, 0
    d_green = 1, 50, 32
    green = 0,225,0
    yellow = 210, 210, 50
    cyan = 85, 150, 200
    lime = 60, 200, 120
    orange = 255, 69, 0
    white = 253, 251, 249
    black = 21, 23, 24
    grey = 150, 150, 150
    night_blue = 0, 0, 30

    global screen, X, Y, f_sz, font, MIN
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    X,Y = 1920,1080
    f_sz = 15
    pygame.font.init()
    font = pygame.font.Font("SourceCodePro.ttf", f_sz)
    MIN = 10
    pygame.draw.rect(screen, black, pygame.Rect(0, 0, X, Y))
    pygame.mouse.set_visible(False)


def prt(v_nm, x_var, y_var, f_clr):
    text = font.render(v_nm, True, f_clr, black)
    textRect = text.get_rect()
    textRect = (int(x_var), int(y_var))
    screen.blit(text, textRect)


def render():
    pygame.display.flip()
    time.sleep(0.05)
    x = 0
    for i in l:
        prt(" " + " ".join(i),0,20*x,green)
        x+=1


init()

s = "".join([chr(x) for x in range(33,127)])
l = []
d = {}
for i in range(Y//20):
    a = []
    for j in range(X//22):
        a.append(" ")
    l.append(a)

for i in range(X//22):
    d[i] = []


ct = time.time()

while time.time() < ct+MIN*60:
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            exit(0)


    #Creator
    for _ in range(5):
        y = random.randrange(0,X//22)
        dist = random.randint(4,10)
        if random.random() < 0.2 and l[0][y] == l[dist//2][y] == l[dist][y] == " ":
            sz = random.randint(9,24)
            d[y].append([-sz-1,-1])            #tail, head

    render()

    #Proceeder
    dlt=[]
    for i in d:
        for j in range(len(d[i])):
            for k in range(len(d[i][j])):
                d[i][j][k] += 1
            if d[i][j][0] >= len(l):
                dlt.append([i,d[i][j]])
            if d[i][j][0] < len(l):
                l[d[i][j][0]][i] = " "
                if d[i][j][1] < len(l):
                    l[d[i][j][1]][i] = random.choice(s)
                    prt(l[d[i][j][1]][i], 18*i + 9, 20*d[i][j][1] - 20, white)
    

    for i in dlt:
        d[i[0]].remove(i[1])

