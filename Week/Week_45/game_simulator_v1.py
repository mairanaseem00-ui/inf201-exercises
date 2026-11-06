
from items import Weapon


class Character:
    """Represents a character in the RPG."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
    ) -> None:
        """
        Initialize a Character.

        Args:
            name (str): The name of the character.
            hp_max (int): Maximum hit points (default: 100).
            damage (int): Base attack damage (default: 10).
            weapon (Weapon | None): Optional equipped weapon (default: None).

        Raises:
            ValueError: If maximum HP is not positive or damage is negative.
        """
        if hp_max <= 0:
            raise ValueError("Maximum HP must be greater than zero.")

        if damage < 0:
            raise ValueError("Damage cannot be negative.")

        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> None:
        """
        Reduce the character's HP when taking damage.

        Args:
            amount (int): Amount of damage received.

        Raises:
            ValueError: If the damage amount is negative.
        """
        if amount < 0:
            raise ValueError("Damage cannot be negative.")

        self._hp = max(0, self._hp - amount)

    def heal(self, amount: int) -> None:
        """
        Restore HP without exceeding the maximum HP.

        Args:
            amount (int): Amount of HP to restore.

        Raises:
            ValueError: If the healing amount is negative.
        """
        if amount < 0:
            raise ValueError("Healing amount cannot be negative.")

        self._hp = min(self.hp_max, self._hp + amount)

    def attack(self, target: "Character") -> None:
        """
        Attack another character.

        Use weapon dice damage if a weapon is equipped.
        Otherwise, use the character's base damage.
        """
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage

        target.take_damage(damage)

    def introduce(self) -> None:
        """Introduce the character."""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Return a representation of the character."""
        return (
            f"<Character name={self.name} "
            f"hp={self._hp} damage={self.damage}>"
        )

    def __str__(self) -> str:
        """Return a readable description of the character."""
        return (
            f"Character: {self.name} with "
            f"{self._hp} HP and {self.damage} damage"
        )

    @property
    def hp(self) -> int:
        """Return the character's current HP (read-only)."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Return True if the character is alive."""
        return self._hp > 0



class Warrior(Character):
    """A defensive character whose armor reduces incoming damage."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
        armor: int = 5,
    ) -> None:
        """
        Initialize a Warrior.

        Args:
            name (str): The warrior's name.
            hp_max (int): Maximum HP (default: 100).
            damage (int): Base attack damage (default: 10).
            weapon (Weapon | None): Optional equipped weapon.
            armor (int): Damage reduction (default: 5).

        Raises:
            ValueError: If armor is negative.
        """
        super().__init__(name, hp_max, damage, weapon)

        if armor < 0:
            raise ValueError("Armor cannot be negative.")

        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """
        Reduce incoming damage by the warrior's armor.

        Args:
            amount (int): Incoming damage.

        Raises:
            ValueError: If the incoming damage is negative.
        """
        if amount < 0:
            raise ValueError("Damage cannot be negative.")

        damage_after_armor = max(0, amount - self.armor)

        super().take_damage(damage_after_armor)



class Mage(Character):
    """A magic character that uses mana to perform powerful attacks."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
        mana: int = 30,
        mana_max: int = 30,
    ) -> None:
        """
        Initialize a Mage.

        Args:
            name (str): The mage's name.
            hp_max (int): Maximum HP (default: 100).
            damage (int): Base attack damage (default: 10).
            weapon (Weapon | None): Optional equipped weapon.
            mana (int): Starting mana (default: 30).
            mana_max (int): Maximum mana (default: 30).

        Raises:
            ValueError: If mana is outside the valid range.
        """
        super().__init__(name, hp_max, damage, weapon)

        if mana_max < 0:
            raise ValueError("Maximum mana cannot be negative.")

        if mana < 0 or mana > mana_max:
            raise ValueError("Mana must be between 0 and maximum mana.")

        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target: Character) -> None:
        """
        Attack using magic when enough mana is available.

        If mana >= 10:
            - Spend 10 mana.
            - Deal double base damage.
            - Ignore the equipped weapon.

        If mana < 10:
            - Use the inherited attack method.
            - Restore 5 mana without exceeding mana_max.
        """
        if self.mana >= 10:
            self.mana -= 10

            magic_damage = self.damage * 2
            target.take_damage(magic_damage)

        else:
            super().attack(target)

            self.mana = min(self.mana + 5, self.mana_max)



class Battle:
    """Manages turn-based combat between two characters."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialize a Battle.

        Args:
            hero (Character): The hero participating in the battle.
            enemy (Character): The enemy participating in the battle.
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """
        Play one round of battle.

        The hero attacks first.
        The enemy attacks back only if still alive.
        """
        if not self.hero.is_alive or not self.enemy.is_alive:
            return

        self.hero.attack(self.enemy)

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """
        Continue battle rounds until one character is no longer alive.
        """
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()
