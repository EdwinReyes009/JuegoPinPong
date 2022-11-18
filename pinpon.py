def main():
    pygame.init()
    win=pygame.display.set_mode((winHori,winVert))
    pygame.display.set_caption("Mi juego de pin pon")
    pelota = pelotaP("pon.png")
    fuente = pygame.font.Font(None,60)
    raqueta_1=raqueta()
    raqueta_1.x=60

    raqueta_2=raqueta()
    raqueta_2.x=winHori-60-raqueta_2.ancho

    jugando=True
    while jugando:
        pelota.movimiento()
        pelota.rebotar(pelota)
        raqueta_1.movimiento(pelota)
        raqueta_2.golpear_maqui(pelota)

        win.fill(white)
        win.blit(pelota.imagen,(pelota.x,pelota.y))
        win.blit(raqueta_1.imagen,(raqueta_1.x,raqueta_1.y))
        win.blit(raqueta_2.imagen,(raqueta_2.x,raqueta_2.y))
        text=f"{pelota.puntuacion}:{pelota.puntuacion_maqui}"
        letre=fuente.rendertes(text,False,negro)
        win.blit(letre,(winHori/2-fuente.size(text)[0]/2,50))
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando=False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y=-5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y=5
            if event.key == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y=0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y

        pygame.display.flip()
        pygame.time.Clock().tick(fps)
    pygame.quit()
if _name_=='_main_':
    main() 
            

        

