import pygame

# stats
"""
i think the stats could be inspired by Fallout with the special stats. but 10 shouldnt just be the maximum but,
should go even higher
They choose the proficiency of the character with weapon types

Strength would mean more melee based damage: Swords, Hammers and needed for two handed
Perception higher crit chance: Daggers, Bows, 
Endurance more mana or special points
Charisma could help in recruiting party members
Intelligence more magic based damage: Staves or Charms.
Agility faster turn speed
Luck better item drops and gambling chances

health would be according to level and class.
"""
# classes
"""
i think there are only 3 classes the rest are specializations:
Warrior: melee damage first
Mage: magic damage
Rogue: critical damage & turn speed

Maybe 3 different class specializations for each still with their specialization but different skill set/damage type
Warrior having:
- Barbarian: raw strength, no think just hit, maybe higher crit chance.
- Knight: more defence, build like a tank with more defence based skills
- Templar: has more magic based skills. Intelligence should be smart for the build. light based damage should be must

Mage having:
- Wizard: Should get Swag. Heavier Magic Attacks
- Necromancer: Undead Damage meaning Dark Type. Summon Undead get more turns with them
- Light Mage: Healer. has limited light damage magic

Rogue:
- Thief: more luck based but less crit chance. Higher probability of escaping fights. gets items after fight
- Assassin: Higher Crit Chance. Better melee damage
- Archer: Main Focus on Archery. higher chance to avoid damage. Higher Crit chance. Unable to use Swords

Classes should then again be able to specialize deeper or broaden their skill set.
"""
# skills
"""
Skills should be abilities the character can choose when leveling up. Should be saved in a dictionary. Encryption for



"""
example_stat_sheet = {
    "strength": 1,
    "perception": 1,
    "endurance": 1,
    "charisma": 1,
    "intelligence": 1,
    "agility": 1,
    "luck": 1
}


class Player(pygame.sprite.Sprite):

    def __init__(self, player_class: str, stats: dict, position: tuple, pixel_size: int = 25, walking_speed: int = 4):
        """
        Player class. Player only moves one pixel at a time with a standard speed of 4
        :param player_class: class for the Created Character. Classes are named in the skilltree
        :param stats: player stats. needs to be modelled after the S.P.E.C.I.A.L system from the Fallout series
        :param position: where on the Screen does the player start
        :param pixel_size: how big is the player and also how big one pixel on the screen is
        :param walking_speed: how many pixels the character should move in a second
        """
        pygame.sprite.Sprite.__init__(self)

        self.stats = stats
        self.player_class = player_class
        self.player_exp = 0
        self.player_skills = {}
        self.character_data = {
            "race": "Human",
            "class": "Melee",
            "stats": self.stats,
            "stat_points": 0,
            "skills": self.player_skills,
            "level": 1,
            "exp": 0,
            "skill_points": 0,
            "exp_cap": 50
        }
        self.pixel_size = pixel_size
        self.image = pygame.Surface((self.pixel_size, self.pixel_size))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.move_flag = False

        self.move_right_flag = True
        self.move_left_flag = True
        self.move_up_flag = True
        self.move_down_flag = True

        self.right_movement = False
        self.left_movement = False
        self.up_movement = False
        self.down_movement = False

        self.walking_speed = walking_speed
        self.last_move_time = 0
        self.move_delay = 1/self.walking_speed * 1000  # Delay between each movement in milliseconds
        print(f'current move_delay: {self.move_delay}')

    def place_character(self, x_coord: int, y_coord: int) -> None:
        self.rect.x = x_coord
        self.rect.y = y_coord

    def get_player_placement(self) -> tuple:
        return self.rect.x, self.rect.y

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        move_speed = self.pixel_size  # Number of pixels to move per click

        current_time = pygame.time.get_ticks()
        # Check for movement keys
        if current_time - self.last_move_time >= self.move_delay:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if self.move_left_flag:
                    self.rect.x -= move_speed
                self.last_move_time = current_time
                self.move_flag = True
                self.left_movement = True

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if self.move_right_flag:
                    self.rect.x += move_speed
                self.last_move_time = current_time
                self.move_flag = True
                self.right_movement = True

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                if self.move_up_flag:
                    self.rect.y -= move_speed
                self.last_move_time = current_time
                self.move_flag = True
                self.up_movement = True

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                if self.move_down_flag:
                    self.rect.y += move_speed
                self.last_move_time = current_time
                self.move_flag = True
                self.down_movement = True

        else:
            self.move_flag = False
            self.left_movement = False
            self.right_movement = False
            self.up_movement = False
            self.down_movement = False

