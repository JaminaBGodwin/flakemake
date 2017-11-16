import pygame, sys, math
from pygame.locals import *

pygame.init()
DSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('FlakeMake 0.00a')

WHITE = (255, 255, 255)
# or more explicitly: WHITE = pygame.Color(255, 255, 255)

ORIGIN = (400, 300)

# pygame.draw.line(DISPLAYSURF, WHITE, ORIGIN, (ORIGIN[0] - 50, ORIGIN[1]), 4) # left horizontal
# pygame.draw.line(DISPLAYSURF, WHITE, ORIGIN, (ORIGIN[0] + 50, ORIGIN[1]), 4) # right horizontal
# pygame.draw.line(DISPLAYSURF, WHITE, ORIGIN, (ORIGIN[0], ORIGIN[1] - 50), 4) # up vertical
# pygame.draw.line(DISPLAYSURF, WHITE, ORIGIN, (ORIGIN[0], ORIGIN[1] + 50), 4) # down vertical

def simple_lines(n, l):
    '''draws the simplest possible snowflake of n lines of length l.'''
    for i in range(n):
        x = math.sin(math.radians(i * 360 / n))
        y = math.cos(math.radians(i * 360 / n))
        dest = (ORIGIN[0] + x * l, ORIGIN[1] + y * l)
        pygame.draw.line(DSURF, WHITE, ORIGIN, dest, 2)


while True:
    n = 6
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    simple_lines(72, 200)
    pygame.display.update()




# make a snowflake.

    # get some parameters:
        # let n be the number of initial branches
        # let l be the length of a branch
        # let a be the min segment size
        # let b be the max segment size
        # let d be the branch density
        # let s be the RNG seed.

    # set up a screen space.
        # ORIGIN is in the centre of the screen

    # initialise with n branches radiating from the ORIGIN

    # populate the branches: for all branches,
        # seed rng with s
        # branch divides into segments
            # a given branch's segments are randomly in the range (a, b)
        # depending on d, start a new branch from a random point in the seg.
            # at an angle computed from n, ruling out vectors parallel to this.
            # recurse

    # functions:
        # segment(branch)
            # divides a branch's vector into a list of vectors
            # randomly call make_branch on each segment, depending on d
        # snowflake(n, l, a, b, d, s)
            # draws initial branches
            # returns an array of vectors from the ORIGIN
            # iterates over those vectors (branches)
                # seed rng with s
                # segment, starting the recursion
        # make_branch(branch, segment, n)
            # makes a new branch off this segment of this branch
            # pass to get_branch_vector for ORIGIN, direction
            # draw a branch with length derived from parent branch
            # segment that branch

        # get_branch_vector(segment)
            # given a segment, randomly generates an ORIGIN point and a vector
            # for a new branch.

        # some IO stuff I don't know how to do yet!

        # draw a line on the screen - easy enough, but we want to draw from
        # some ORIGIN point with a length, so we need to compute our start
        # and end screen coordinates. (eg if surface dim 800x600 then orig. is
        # (400, 300) but we might also be taking any point on any branch as orig.)
        # want to be able to draw with an ORIGIN, normalised direction vector
        # (which I think we can get from the trig functions) and then multiply
        # that by some length.