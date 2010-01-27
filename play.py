#!/usr/bin/env python

from game import Game
import config

if __name__ == "__main__":

    if config.PROFILE:
        import cProfile, pstats
        prof = cProfile.run("Game()", "profile.prof")
        stats = pstats.Stats("profile.prof")
        stats.sort_stats('cumulative', 'time', 'calls')
        stats.print_stats(30)
    else:
        Game()
