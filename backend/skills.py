

class CombatSkills:

    def __init__(self, name: str = "", mp_cost: int = 0, hp_cost: int = 0, percentage_cost: bool = False,
                 damage: int = 0, skill_type: str = "skill", damage_type: str = "physical",
                 elemental_type: str = "none", affected: str = "enemy", aoe: bool = False):
        """
        Class for Creating new Skills. to Create debuffs use skill_type='buff' and affected='enemy'"
        :param name: Name of the Skill
        :param mp_cost: Mana Cost when casting Spell
        :param hp_cost: HP Cost when casting Spell or Skill
        :param percentage_cost: Bool to determine if the MP or HP cost is percentual or not
        :param skill_type:  Types of Skills are "buff", "skill", "spell", "ultimate"
        :param damage_type: types of Damage "physical", "magical".
        :param elemental_type: affected element:
        :param affected: The Affected Group, "enemy" or "ally"
        :param aoe: Area of Effect, True means whole Group False means single Target
        """
        self.__available_skill_types = ("buff", "skill", "spell", "ultimate")
        self.__available_special_skills = ("lycoris_radiata", "dantes_inferno")
        self.__available_damage_types = ("physical", "magical")
        self.__available_elements = ("none", "fire", "ice", "shock", "light", "dark")
        self.__available_affected = ("enemy", "ally")

        self.mp_cost = mp_cost
        self.hp_cost = hp_cost
        self.damage = damage
        self.name = name
        self.__percentage_cost = percentage_cost
        self.aoe = aoe

        self.skill_type = skill_type
        self.damage_type = damage_type
        self.elemental_type = elemental_type
        self.affected = affected

        if self.skill_type not in self.__available_skill_types:
            raise ValueError('Skill Type not available. Available Skill types: "buff", "attack", "special"')

        if self.skill_type == "ultimate" and self.name not in self.__available_special_skills:
            raise ValueError('Ultimate Skill under that name not available. Check Skilltree for Ultimate Skill Names')

        if self.damage_type not in self.__available_damage_types:
            raise ValueError('Damage Type not available. Available Damage types: "physical", "magical"')

        if self.elemental_type not in self.__available_elements:
            raise ValueError('Elemental Type not available. Available Elemental type: "none", "fire", '
                             '"ice", "shock", "light", "dark"')

        if self.affected not in self.__available_affected:
            raise ValueError('Affected not available. Affected has to be "enemy" or "ally')

    def lycoris_radiata(self):
        print("learnt Ultimate Skill Lycoris Radiata")

    def dantes_inferno(self):
        print("learnt Ultimate Skill Dantes Inferno")