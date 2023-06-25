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

    def __init__(self, player_class: str, stats: dict, position: tuple):
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

        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

