def update(win, enemys, player):
    new_dead = []
    for enemy in enemys:
        if not enemy.dead:
            res = enemy.draw(win)
            if res == "win":
                player.health -= 1
        else:
            new_dead.append(enemy)

        if enemy.dead:
            new_dead.append(enemy)

    dead_count = 0
    for enemy in new_dead:
        if enemy in enemys:
            dead_count += 1

            if enemy.killed:
                enemys.remove(enemy)

    return enemys, dead_count
