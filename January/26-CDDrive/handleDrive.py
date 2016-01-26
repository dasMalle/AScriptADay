import pygame.cdrom as cdr

cdr.init()
cd = cdr.CD(0)  # 0 = first drive
cd.init()
cd.eject()
cd.quit()
cdr.quit()
