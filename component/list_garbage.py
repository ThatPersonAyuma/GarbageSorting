import pygame
from . import object

class GarbageList:
    def __init__(self, trash: list[object.ImageObject], max_show:int) -> None:
        self.inventory = trash
        self.max_show = max_show
        self.position = 0
        
    def pop(self, key:int) -> object.ImageObject:
        obj = self.inventory[key]
        self.inventory.pop(key)
        return obj
    
    def refill(self, trash:list[object.ImageObject])->bool:
        if (len(self.inventory)>0):
            return False
        self.inventory = trash
        return True
            
    def get(self)->list[object.ImageObject]:
        return self.inventory[self.position*self.max_show:(self.position+1)*self.max_show]
        
    def scroll(self, is_up:bool=False)->bool:
        if is_up:
            if self.position>0:
                self.position-=1
                return True
            else:
                return False
        else:
            if self.position < (len(self.inventory)//self.max_show):
                self.position+=1
                return True
            else:
                return False
        
    def draw(self, surface:pygame.Surface, start_pos:tuple[int,int], spacing:int=10, box_size:tuple[int,int]=(60,60)):
        """
        Draw inventory items as vertical boxes and update ImageObject positions.
        """
        x, y = start_pos
        for item in self.get():
            rect = pygame.Rect(x, y, box_size[0], box_size[1])
            pygame.draw.rect(surface, (200, 200, 200), rect)

            # Update posisi ImageObject
                # print("Runned")
            item.rect[0], item.rect[1] = rect.center  # simpan posisi tengah kotak di ImageObject
            surface.blit(item.pygame_surface, item.pygame_surface.get_rect(center=rect.center))
            y += box_size[1] + spacing

    