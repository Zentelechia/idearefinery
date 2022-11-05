import sys
from sqlservice import *
from matching import *

initSQL()

# mentorMatch("cla4846c00002sl8bnu2khur8")

if sys.argv[1] == 1:
    mentorMatch(sys.argv[2])

close()