import pygame

class Camera(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    
    self.offset = pygame.math.Vector2()
    
    self.camera_borders = {"left": 300, "right": 300, "top": 150, "bottom": 150}
    l = self.camera_borders["left"]
    t = self.camera_borders["top"]
    w = self.display_surface.get_width() - self.camera_borders["right"] - self.camera_borders["left"]
    h = self.display_surface.get_height() - self.camera_borders["top"] - self.camera_borders["bottom"]
    self.camera_rect = pygame.Rect(l, t, w, h)
    
    self.ground_surf = pygame.Surface((self.display_surface.get_width(), self.display_surface.get_height()))
    self.ground_surf.fill("#00ff00")
    self.ground_rect = self.ground_surf.get_rect(topleft = (0, 0))
  
  def box_center_camera(self, player):
    
    if player.rect.left < self.camera_rect.left:
      self.camera_rect.left = player.rect.left
    if player.rect.right > self.camera_rect.right:
      self.camera_rect.right = player.rect.right
    if player.rect.top < self.camera_rect.top:
      self.camera_rect.top = player.rect.top
    if player.rect.bottom > self.camera_rect.bottom:
      self.camera_rect.bottom = player.rect.bottom
      
    self.offset.x = self.camera_rect.left - self.camera_borders["left"]
    self.offset.y = self.camera_rect.top - self.camera_borders["top"]
  
  def custom_draw(self, player):
    
    self.box_center_camera(player)
    
    ground_offset = self.ground_rect.topleft - self.offset
    self.display_surface.blit(self.ground_surf, ground_offset)
    
    for sprite in self.sprites():
      offset_pos = sprite.rect.topleft - self.offset
      self.display_surface.blit(sprite.image, offset_pos)