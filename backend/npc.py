import pygame


class NPC(pygame.sprite.Sprite):

    def __init__(self, position: tuple, npc_type: str, inventory: dict, size: int = 25):
        """
        Class for Creating NPCs in pygame. Interactable if needed
        :param inventory: what inventory they have
        :param position: where on the map is the NPC
        :param race: choose one of the 9 Races
        :param npc_type: merchant, questgiver, villager, party member, enemy
        :param size: how big is the NPC
        """
        pygame.sprite.Sprite.__init__(self)

        self.type = npc_type
        self.inventory = inventory
        self.position = position
        self.image = pygame.Surface((25, 25))
        self.image.fill((0, 255, 10))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def interact(self):
        pass

    def talk(self):
        pass

    def trade(self):
        pass

    def fight(self):
        pass

    def move(self, x_pos, y_pos):
        self.rect.x += x_pos
        self.rect.y += y_pos

    def update(self):
        pass

