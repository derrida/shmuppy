from character import Character

class Player(Character):
    """The sprite that the player controls."""

    def __init__(self, scene):
        size = (16,16)
        color = (255,0,0)
        name = "Player 1"
        speed = 2
        hp = 20
        Character.__init__(self, scene, size, color, name, speed, hp)

    def next_weapon(self):
        """Switch the player's weapon to the next one in their inventory."""

        self.weapon_id += 1
        self.weapon_id %= len(self.scene.weapon_list)
        self.weapon = self.scene.weapon_list[self.weapon_id]

    def switch_to_weapon(self, weapon):
        """Switch the player's weapon directly to any of the weapons."""

        #self.weapon_id == 1
        #result = {
            #'bow': lambda x: x * 5,
            #'pistol': lambda x: x + 7,
            #'laser': lambda x: x - 2
            #'rifle': lambda x: x - 2
        #}[value](x) 
