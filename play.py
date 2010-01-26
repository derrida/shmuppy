#!/usr/bin/env python

from constants import *
from game import Game

if __name__ == "__main__":

    if PROFILE:
        import cProfile, pstats
        prof = cProfile.run("Game()", "profile.prof")
        stats = pstats.Stats("profile.prof")
        stats.sort_stats('cumulative', 'time', 'calls')
        stats.print_stats(30)
    else:
        Game()
