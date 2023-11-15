from backend import map_tiled
from backend.game import ScrunkleQuest

# tile_screen = map_tiled.WorldScreen()
# map_surface = tile_screen.render_map()

game = ScrunkleQuest((800, 600), debug=False)
game.main()