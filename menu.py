import scoreboard
import health_bar


def draw(surf, player):
    # draw healthbar
    bar = health_bar.get(player.health / 100)
    bar_x = surf.get_width() - bar.get_width()
    bar_y = surf.get_height() - bar.get_height()

    surf.blit(bar, (bar_x, bar_y))

    # draw scoreboard
    board = scoreboard.get(player.score)
    board_x = surf.get_width() - board.get_width()
    board_y = bar_y - board.get_height()

    surf.blit(board, (board_x, board_y))
