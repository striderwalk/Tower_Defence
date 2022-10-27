def update(win, enemys, player):
    new_dead = []
    for enemy in enemys:
        if not enemy.dead:
            res = enemy.draw(win)
            if res == "win":
                player.health -= 1
            elif res == "die":
                print(res)
                enemy.die()

    dead_count = 0
    update_enemys = enemys.copy()
    for enemy in enemys:
        if not enemy.dead:
            continue

        if enemy.killed:
            dead_count += 1
        update_enemys.remove(enemy)

    return update_enemys, dead_count
