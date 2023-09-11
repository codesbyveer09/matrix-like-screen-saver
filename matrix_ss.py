import pygame,time,random

def init():
    global d_green, green, white, black
    d_green = 5, 150, 50
    green = 0,225,0
    white = 253, 251, 249
    black = 21, 23, 24

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
    l.append([" "]*(X//22))
for i in range(X//22):
    d[i] = []

ct = time.time()


while time.time() < ct+MIN*60:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            exit(0)

    #Creator
    for _ in range(15):
        y = random.randrange(0,X//22)
        dist = random.randint(3,14)
        if random.random() < 0.3 and l[0][y] == l[dist//2][y] == l[dist][y] == " ":
            d[y].append([-random.randint(20,30)-1,-1])            #tail, head
    
    render()

    #Proceeder
    dlt=[]
    for i in d:
        for j in range(len(d[i])):
            for k in range(len(d[i][j])):
                d[i][j][k] += 1
            if d[i][j][0] > len(l):
                dlt.append([i,d[i][j]])
            elif d[i][j][0] < len(l):
                l[d[i][j][0]][i] = " "
                if d[i][j][1] < len(l):
                    if i in range(X//44 - len(time.ctime())//2, X//44 + len(time.ctime())//2):
                        l[d[i][j][1]][i] = time.ctime()[i - X//44 + len(time.ctime())//2]
                    else:
                        l[d[i][j][1]][i] = random.choice(s)
                    if d[i][j][1]+1 < len(l) and l[d[i][j][1]+1][i] != "-":
                        prt(l[d[i][j][1]][i], 18*i + 9, 20*d[i][j][1] - 20, white)

    #Time
    for i in range(-1,2):
        prt(" ".join(list((("|"+time.ctime()+"|").replace("  ", " ")).replace(" ", "|"))), (18*(X//44 - len((("|"+time.ctime()+"|").replace("  ", " ")).replace(" ", "|"))//2) + 9), 20*(Y//40 - 5 - i), d_green)


    for i in dlt:
        d[i[0]].remove(i[1])

