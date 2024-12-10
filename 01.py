import time
import pygame



width = 600
height = 600
velocidade = 5

tela = pygame.display.set_mode((width,height))
p = pygame.image.load('./assets/p.png')
p = pygame.transform.scale(p,(50,65))

player = p.get_rect()
player.right = width // 2
player.bottom = height -20

#configurando o inimigo
inimigo = pygame.image.load('./assets/i.png')
inimigo = pygame.transform.scale(inimigo , (30,30))

player2 = inimigo.get_rect()
player2.top=15
direcao = 0


pos_y = player.y
tiro =  pygame.Rect( player.x + 25,player.y+30,5,15)
shot = False


inimigo_ativo = True

loop = True
clock = pygame.time.Clock()
while loop:
    clock.tick(20)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:

            loop=False

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                loop=False


#Contrla os inputs do teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= velocidade
    if keys[pygame.K_DOWN]:
        player.y += velocidade
        print(f"v = {player.y}")
    if keys[pygame.K_LEFT]:
        player.x -=velocidade
    if keys[pygame.K_RIGHT]:
        player.x +=velocidade

    if keys[pygame.K_SPACE]:
        tiro.x = player.x + 25
        tiro.y = player.y + 30
        shot=True

    if inimigo_ativo:
        if player2.x >= 550:
            direcao -=1
            print(f'{direcao}')
        elif player2.x <= 0:
            direcao +=1
            print(f'{direcao}')

    player2.x+=direcao*5
    #print(f'Pos_Nav: {player2.x}')

    if inimigo_ativo and tiro.colliderect(player2):
        inimigo_ativo = False
        shot = False
        print("Acertou!")


    if shot == True:
        tiro.y-=15
        print(shot)

    if tiro.y==0:
        shot = False
        print(shot)
        tiro.x = player.x+25
        tiro.y = player.y+30




    tela.fill((0,0,0))

    pygame.draw.rect(tela,'white', tiro)
    tela.blit(p,player)
    if inimigo_ativo:
        tela.blit(inimigo,player2)
    pygame.display.flip()
