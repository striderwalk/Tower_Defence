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

            if enemy.killed:
                dead_count += 1
                enemys.remove(enemy)

    return enemys, dead_count
