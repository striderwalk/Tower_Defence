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

    def draw(self, surf):
        bar = health_bar.get(self.health / 100)
        x = surf.get_width() - bar.get_width()
        y = surf.get_height() - bar.get_height()

        surf.blit(bar, (x, y))
