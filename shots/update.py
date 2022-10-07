def update(bullets, active_enemys, win):
    dead = []
    for bullet in bullets:
        if bullet.dead:
            dead.append(bullet)
            continue
        bullet.draw(win)
        bullet.update(active_enemys)
        if bullet.dead:
            dead.append(bullet)

    for i in dead:
        bullets.remove(i)

    return bullets
