from loguru import logger


class Weapon(object):
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense


class Player(object):
    def __init__(
        self,
        name,
        health=100,
        gold=100,
        defense=100,
        attack=100,
        level=1,
        weapon_list=[],
    ):
        self.name = name
        self.health = health
        self.gold = gold
        self.defense = defense
        self.attack = attack
        self.level = level
        self.weapon_list = weapon_list

    def attacker(self, defenser, weapon_index=None):
        if weapon_index is None:
            damage = self.attack - defenser.defense
        else:
            damage = self.weapon_list[weapon_index].attack - defenser.defense
        if damage > 0:
            defenser.health -= damage
            logger.info(f"{self.name}成功攻击了{defenser.name},造成了{damage}点伤害")
        else:
            logger.info(f"{self.name}的攻击被{defenser.name}防御了")

    def buy_weapon(self, weapon):
        self.weapon_list.append(weapon)
        logger.info(f"{self.name}购买装备{weapon.name}!")

    def level_up(self):
        self.level += 1
        self.gold += 100
        logger.info(f"{self.name}升级了,奖励金币100")


w1 = Weapon("屠龙刀", 800, 200)
yuan = Player("yuan")
alex = Player("alex")
yuan.buy_weapon(w1)
yuan.attacker(alex, 0)
