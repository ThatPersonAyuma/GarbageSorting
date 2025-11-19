import pygame
from . import objects

class ItemList:
    def __init__(self, trash: list[objects.TrashObject], start_pos:tuple[int,int], spacing:int, max_show:int, box_size:tuple[int,int]) -> None:
        self.inventory = trash
        self.max_show = max_show
        self.position = 0
        self.box_size = box_size
        self.start_pos = start_pos 
        self.spacing = spacing
        
        
    def pop(self, position:int) -> objects.TrashObject:
        obj = self.inventory.pop(position+(self.position*self.max_show))
        return obj
    
    def refill(self, trash:list[objects.TrashObject])->bool:
        if (len(self.inventory)>0):
            return False
        self.inventory = trash
        return True
            
    def get(self)->list[objects.TrashObject]:
        return self.inventory[self.position*self.max_show:(self.position+1)*self.max_show]
        
    def scroll_up(self)->bool:
        print(f"Up {self.position}")
        if self.position>0:
            self.position-=1
            return True
        else:
            return False
        
    def scroll_down(self)->bool:
        print(f"Down len:{len(self.inventory)} max:{self.max_show}, Position:{self.position}")
        if self.position < ((len(self.inventory)-1)//self.max_show):
            self.position+=1
            return True
        else:
            return False
        
    def draw(self, surface:pygame.Surface):
        """
        Draw inventory items as vertical boxes and update ImageObject positions.
        """
        x, y = self.start_pos
        y -= self.box_size[1] + self.spacing
        for item in self.get():
            y += self.box_size[1] + self.spacing
            if item.is_dragged:
                continue
            item.rect.x = x
            item.rect.y = y
            item.rect.width, item.rect.height = self.box_size
            # rect = pygame.Rect(x, y, box_size[0], box_size[1])
            # pygame.draw.rect(surface, (0, 0, 0), item.rect, 20)
            
            # # Update posisi ImageObject
            #     # print("Runned")
            # item.rect.x, item.rect.y = rect.center  # simpan posisi tengah kotak di ImageObject
            
            surface.blit(item.pygame_surface, item.pygame_surface.get_rect(center=item.rect.center))
            # pygame.draw.rect(surface, (0, 0, 0), item.rect, 2)
            # y += box_size[1] + spacing

    