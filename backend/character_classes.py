
class CharacterClass:
    """Sets up the Character Class, also checks if Character Class is even available"""

    def __init__(self, skill_sheet: dict, current_class: str):
        self.existing_classes = [
            "melee",
            "knight", "grand_knight", "demon_knight", "demon_Lord",
            "barbarian", "barbarian_chief", "ursus_fighter", "ursus_alpha",
            "templar", "high_templar", "inquisitor", "judicor",

            "mage",
            "wizard", "grand_wizard", "wizard_lizzard", "king_gizzard",
            "priest", "high_priest", "corrupted_acolyte", "seductress",
            "necromancer", "occult_leader", "lich", "elder_lich",

            "rogue",
            "assassin", "master_assassin", "poison_expert", "poison_master"
            "thief", "thief_master", "goblin_pillager", "goblin_chief",
            "archer", "high_archer", "elven_archer", "high_elf"
        ]

        if current_class not in self.existing_classes:
            raise ValueError("Chosen Class does not Exist - please check if you typed in class name correctly")



