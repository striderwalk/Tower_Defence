class Player:
    """
    deal with health and money
    """

    def __init__(self, health=100, score=0):
        self.health = health
        self.score = score
        self.dead = False

    def update(self, dead_count):
        self.score += dead_count
        if self.dead:
            raise RuntimeError("player dead but ask to update")

        if self.health <= 0:
            self.dead = True

    def can_buy(self, cost) -> bool:
        if self.score >= cost:
            return True
        return False
