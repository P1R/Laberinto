import pygame
from pygame.locals import *
import math
import worldManager
import time
import lab
import matplotlib.pyplot as pyplot

#worldMap =[
#  [8,8,8,8,8,8,8,8,8,8,8,4,4,6,4,4,6,4,6,4,4,4,6,4],
#  [8,0,0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,0,0,0,0,0,0,4],
#  [8,0,3,3,0,0,0,0,0,8,8,4,0,0,0,0,0,0,0,0,0,0,0,6],
#  [8,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
#  [8,0,3,3,0,0,0,0,0,8,8,4,0,0,0,0,0,0,0,0,0,0,0,4],
#  [8,0,0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,6,6,6,0,6,4,6],
#  [8,8,8,8,0,8,8,8,8,8,8,4,4,4,4,4,4,6,0,0,0,0,0,6],
#  [7,7,7,7,0,7,7,7,7,0,8,0,8,0,8,0,8,4,0,4,0,6,0,6],
#  [7,7,0,0,0,0,0,0,7,8,0,8,0,8,0,8,8,6,0,0,0,0,0,6],
#  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,6,0,0,0,0,0,4],
#  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,6,0,6,0,6,0,6],
#  [7,7,0,0,0,0,0,0,7,8,0,8,0,8,0,8,8,6,4,6,0,6,6,6],
#  [7,7,7,7,0,7,7,7,7,8,8,4,0,6,8,4,8,3,3,3,0,3,3,3],
#  [2,2,2,2,0,2,2,2,2,4,6,4,0,0,6,0,6,3,0,0,0,0,0,3],
#  [2,2,0,0,0,0,0,2,2,4,0,0,0,0,0,0,4,3,0,0,0,0,0,3],
#  [2,0,0,0,0,0,0,0,2,4,0,0,0,0,0,0,4,3,0,0,0,0,0,3],
#  [1,0,0,0,0,0,0,0,1,4,4,4,4,4,6,0,6,3,3,0,0,0,3,3],
#  [2,0,0,0,0,0,0,0,2,2,2,1,2,2,2,6,6,0,0,5,0,5,0,5],
#  [2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,0,5,0,5,0,0,0,5,5],
#  [2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,5,0,5,0,5,0,5,0,5],
#  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
#  [2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,5,0,5,0,5,0,5,0,5],
#  [2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,0,5,0,5,0,0,0,5,5],
#  [2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,5,5,5,5,5,5,5,5,5]
#];

z=lab.maze(23,21)
worldMap=[None]*21
for i in range(21):
	worldMap[i]=[None]*23

i=0
for i in range(21):
	for j in range(23):
		if z[i][j] == True:
			worldMap[i][j]=2
			if i == 0:
				worldMap[i][j]=5
			if i == 20:
				worldMap[i][j]=5
			if j == 0:
				worldMap[i][j]=5
			if j== 22:
				worldMap[i][j]=5
		else:
			worldMap[i][j]=0

print worldMap
pyplot.figure(figsize=(10, 5))
pyplot.imshow(z, cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
'''

worldMap =[
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
];
'''

sprite_positions=[
  (20, 11.5, 3), #Bandera de Metai
];
#  (20, 11.5, 3), #green light in front of playerstart
  #green lights in every room
#  (18.5,4.5, 2),
#  (10.0,4.5, 2),
#  (10.0,12.5,2),
#  (3.5, 6.5, 2),
#  (3.5, 20.5,2),
#  (3.5, 14.5,2),
#  (14.5,20.5,2),
  
  #row of pillars in front of wall: fisheye test
#  (18.5, 10.5, 1),
#  (18.5, 11.5, 1),
#  (18.5, 12.5, 1),
  
  #some barrels around the map
#  (21.5, 1.5, 0),
#  (15.5, 1.5, 0),
#  (16.0, 1.8, 0),
#  (16.2, 1.2, 0),
#  (3.5,  2.5, 0),
#  (9.5, 15.5, 0),
#  (10.0, 15.1,0),
#  (10.5, 15.8,0),
#]

def load_image(image, darken, colorKey = None):
    ret = []
    if colorKey is not None:
        image.set_colorkey(colorKey)
    if darken:
        image.set_alpha(127)
    for i in range(image.get_width()):
        s = pygame.Surface((1, image.get_height())).convert()
        #s.fill((0,0,0))
        s.blit(image, (- i, 0))
        if colorKey is not None:
            s.set_colorkey(colorKey)
        ret.append(s)
    return ret

def main():
  
    t = time.clock() #time of current frame
    oldTime = 0. #time of previous frame
    pygame.mixer.init()
    pygame.mixer.music.load("one_last_thrill.mp3")
    pygame.mixer.music.play(-1)
    size = w, h = 640,480
    pygame.init()
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Laberinto")
    screen = pygame.display.get_surface()
    #pixScreen = pygame.surfarray.pixels2d(screen)
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    
    f = pygame.font.SysFont(pygame.font.get_default_font(), 18)
    
    wm = worldManager.WorldManager(worldMap,sprite_positions, 20, 11.5, -1, 0, 0, .66)

    while(True):
        clock.tick(60)
        
        wm.draw(screen)
        
        
        # timing for input and FPS counter
        
        frameTime = float(clock.get_time()) / 1000.0 # frameTime is the time this frame has taken, in seconds
        t = time.clock()
        text = f.render(str(clock.get_fps()), False, (255, 255, 0))
        screen.blit(text, text.get_rect(), text.get_rect())
        #weapon.draw(screen, t)
        pygame.display.flip()

        # speed modifiers
        moveSpeed = frameTime * 6.0 # the constant value is in squares / second
        rotSpeed = frameTime * 3.0 # the constant value is in radians / second
        
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                return 
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        print "camera dirx:".rstrip('\n')
        print wm.camera.dirx
        print "camera diry:".rstrip('\n')
        print wm.camera.diry
        print "camera planex:".rstrip('\n')
        print wm.camera.planex
        print "camera planey:".rstrip('\n')
        print wm.camera.planey
	print "rotSpeed:".rstrip('\n')
	print rotSpeed
	print "moveSpeed:".rstrip('\n')
	print moveSpeed
	keys = pygame.key.get_pressed()
	rot = math.pi/2

	
	moveX = wm.camera.x + wm.camera.dirx * moveSpeed
	if(worldMap[int(moveX)][int(wm.camera.y)]==0 and worldMap[int(moveX + 0.1)][int(wm.camera.y)]==0):wm.camera.x += wm.camera.dirx * moveSpeed
	else:
		pygame.time.delay(100)
		oldDirX = wm.camera.dirx
		wm.camera.dirx = wm.camera.dirx * math.cos(- rot) - wm.camera.diry * math.sin(- rot)
		wm.camera.diry = oldDirX * math.sin(- rot) + wm.camera.diry * math.cos(- rot)
		oldPlaneX = wm.camera.planex
		wm.camera.planex = wm.camera.planex * math.cos(- rot) - wm.camera.planey * math.sin(- rot)
		wm.camera.planey = oldPlaneX * math.sin(- rot) + wm.camera.planey * math.cos(- rot)

	moveY = wm.camera.y + wm.camera.diry * moveSpeed
	if(worldMap[int(wm.camera.x)][int(moveY)]==0 and worldMap[int(wm.camera.x)][int(moveY + 0.1)]==0):wm.camera.y += wm.camera.diry * moveSpeed
	else:
		pygame.time.delay(100)
		oldDirX = wm.camera.dirx
		wm.camera.dirx = wm.camera.dirx * math.cos(- rot) - wm.camera.diry * math.sin(- rot)
		wm.camera.diry = oldDirX * math.sin(- rot) + wm.camera.diry * math.cos(- rot)
		oldPlaneX = wm.camera.planex
		wm.camera.planex = wm.camera.planex * math.cos(- rot) - wm.camera.planey * math.sin(- rot)
		wm.camera.planey = oldPlaneX * math.sin(- rot) + wm.camera.planey * math.cos(- rot)

'''		
        if keys[K_UP]:
            # move forward if no wall in front of you
            moveX = wm.camera.x + wm.camera.dirx * moveSpeed
            if(worldMap[int(moveX)][int(wm.camera.y)]==0 and worldMap[int(moveX + 0.1)][int(wm.camera.y)]==0):wm.camera.x += wm.camera.dirx * moveSpeed
            moveY = wm.camera.y + wm.camera.diry * moveSpeed
            if(worldMap[int(wm.camera.x)][int(moveY)]==0 and worldMap[int(wm.camera.x)][int(moveY + 0.1)]==0):wm.camera.y += wm.camera.diry * moveSpeed
        if keys[K_DOWN]:
            # move backwards if no wall behind you
            if(worldMap[int(wm.camera.x - wm.camera.dirx * moveSpeed)][int(wm.camera.y)] == 0):wm.camera.x -= wm.camera.dirx * moveSpeed
            if(worldMap[int(wm.camera.x)][int(wm.camera.y - wm.camera.diry * moveSpeed)] == 0):wm.camera.y -= wm.camera.diry * moveSpeed
        if (keys[K_RIGHT] and not keys[K_DOWN]) or (keys[K_LEFT] and keys[K_DOWN]):
            # rotate to the right
            # both camera direction and camera plane must be rotated
            oldDirX = wm.camera.dirx
            wm.camera.dirx = wm.camera.dirx * math.cos(- rotSpeed) - wm.camera.diry * math.sin(- rotSpeed)
            wm.camera.diry = oldDirX * math.sin(- rotSpeed) + wm.camera.diry * math.cos(- rotSpeed)
            oldPlaneX = wm.camera.planex
            wm.camera.planex = wm.camera.planex * math.cos(- rotSpeed) - wm.camera.planey * math.sin(- rotSpeed)
            wm.camera.planey = oldPlaneX * math.sin(- rotSpeed) + wm.camera.planey * math.cos(- rotSpeed)
        if (keys[K_LEFT] and not keys[K_DOWN]) or (keys[K_RIGHT] and keys[K_DOWN]): 
            # rotate to the left
            # both camera direction and camera plane must be rotated
            oldDirX = wm.camera.dirx
            wm.camera.dirx = wm.camera.dirx * math.cos(rotSpeed) - wm.camera.diry * math.sin(rotSpeed)
            wm.camera.diry = oldDirX * math.sin(rotSpeed) + wm.camera.diry * math.cos(rotSpeed)
            oldPlaneX = wm.camera.planex
            wm.camera.planex = wm.camera.planex * math.cos(rotSpeed) - wm.camera.planey * math.sin(rotSpeed)
            wm.camera.planey = oldPlaneX * math.sin(rotSpeed) + wm.camera.planey * math.cos(rotSpeed)
'''
fps =8

         
if __name__ == '__main__':
    main()
