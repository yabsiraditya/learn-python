import pygame

# init
pygame.init()

# membuat displat surface object
window_l = 500
window_p = 500
window = pygame.display.set_mode((window_l,window_p))

isRun = True

# Object game 
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak 
speed = 1

while isRun:
    # User input, Database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # Ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    # kanan
    if keys[pygame.K_RIGHT] and x < window_l-lebar:
        x += speed

    # bawah
    if keys[pygame.K_DOWN] and y < window_p-panjang:
        y += speed

    # atas
    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # Update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,0,0),(x,y,lebar,panjang))

    # render ke display
    pygame.display.update()

pygame.quit()