z =700
x =900
c =1200
def setup():
    frameRate(50)
    size(1000,1000)
def draw():
    global z,x,c
    imv=loadImage("bbb.png")
    image(imv,700,700,300,300)
    imv=loadImage("bbbb.png")
    image(imv,700,700,300,300)
    imv=loadImage("bbbbb.jpg")
    image(imv,z,700,100,100)
    imv=loadImage("bbbbbb.jpg")
    image(imv,x,700,100,100)
    imv=loadImage("bbbbbbb.jpg")
    image(imv,c,700,100,100)
    z -=10
    x -=10
    c -=10
