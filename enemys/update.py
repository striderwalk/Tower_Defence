def update(enemys,health,  win):
    new_dead = []
    for enemy in enemys:
        if not enemy.dead:
            res = enemy.draw(win)
            if res == "win":
                health -= 1 
        else:
            new_dead.append(enemy)

        if enemy.dead:
            new_dead.append(enemy)

    for enemy in new_dead:
        if enemy in enemys:
            enemys.remove(enemy)

    return enemys, health
