def update(win, turrets, active_enemys):
    new_bullets = []
    for i in turrets:
        i.draw(win)
        if val := i.update(active_enemys):
            new_bullets.append(val)

    return turrets, new_bullets
