import pygame,time,math,random
pygame.init()
screen_size=(400,300)
screen=pygame.display.set_mode(screen_size)
isrunning=True
pygame.time.Clock().tick(60)

#Player vars
player_image = pygame.image.load("Player_Sprite.png")
player_image.set_colorkey((255,255,255))
playerPos=[200,150]
inputAxis=[0,0]
playerSpeed=150
prev_time = time.time()
player_rect=pygame.Rect(playerPos[0],playerPos[1],16,16)
dt = 0

pygame.mixer.music.load("A.wav")
def PlayMusic():
	if t%(72*60)==0:
		pygame.mixer.music.play()
class Bullet:
	def __init__(self,position,rotation,rect):
		self.position=position
		self.rotation=rotation
		self.rect=rect

#Bullet vars
bulletSpeed=180
bullets=[]
bullet_image=pygame.image.load("Bullet.png")
bullet_image.set_colorkey((255,255,255))
i=70
t=0
bs=40
def CreateBullet(bs):
	if t%bs==0:
		wall_index=random.randint(0,3)
		if wall_index==0:
			bullet_x=random.randint(0,screen_size[0])
			bullet_y=0
		elif wall_index==1:
			bullet_x=random.randint(0,screen_size[0])
			bullet_y=screen_size[1]
		elif wall_index==2:
			bullet_x=0
			bullet_y=random.randint(0,screen_size[1])
		elif wall_index==3:
			bullet_x=screen_size[0]
			bullet_y=random.randint(0,screen_size[1])



		bullet_rotation=[0,0]
		bullet_rotation[0]=-(bullet_x-200)/200
		bullet_rotation[1]=-(bullet_y-150)/200
		bullet_rotation=normalize(bullet_rotation)
		bullet=Bullet([bullet_x,bullet_y],bullet_rotation,pygame.Rect(bullet_x,bullet_y,9,9))
		bullets.append(bullet)

def MoveBullet():
	for bullet in bullets:
		bullet.position[0]+=bullet.rotation[0]*bulletSpeed*dt
		bullet.position[1]+=bullet.rotation[1]*bulletSpeed*dt
		bullet.rect.x=bullet.position[0]
		bullet.rect.y=bullet.position[1]

def RenderBullet():
	for bullet in bullets:
		screen.blit(bullet_image,bullet.position)

def normalize(inputVector):
	if inputVector[0] +inputVector[1]!=0:
		inputVector[0]/= math.sqrt(abs(inputVector[0])+abs(inputVector[1]))
		inputVector[1]/= math.sqrt(abs(inputVector[0])+abs(inputVector[1]))
	return inputVector

def PlayerMovement():

	key=pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		inputAxis[0]=-1
	elif not key[pygame.K_RIGHT]:
		inputAxis[0]=0
	if key[pygame.K_RIGHT]:
		inputAxis[0]=1
	elif not key[pygame.K_LEFT]:
		inputAxis[0]=0
	if key[pygame.K_DOWN]:
		inputAxis[1]=1
	elif not key[pygame.K_UP]:
		inputAxis[1]=0
	if key[pygame.K_UP]:
		inputAxis[1]=-1
	elif not key[pygame.K_DOWN]:
		inputAxis[1]=0

	playerPos[0]+=inputAxis[0]*playerSpeed*dt
	playerPos[1]+=inputAxis[1]*playerSpeed*dt
	player_rect.x=playerPos[0]+4
	player_rect.y=playerPos[1]+4

def PlayerCollision():
	for bullet in bullets:
		if player_rect.colliderect(bullet.rect):
			isrunning=False
			pygame.quit()

while isrunning:
	bulletSpeed+=0.1
	PlayMusic()
	pygame.time.Clock().tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isrunning=False
	t+=1
	normalize(inputAxis)
	now = time.time()
	dt = now - prev_time
	prev_time = now
	screen.fill((0,0,0))
	screen.blit(player_image,playerPos)
	i+=10
	CreateBullet(bs)
	RenderBullet()
	MoveBullet()
	PlayerMovement()
	PlayerCollision()
	try:
		pygame.display.update()
	except pygame.error:
		break
