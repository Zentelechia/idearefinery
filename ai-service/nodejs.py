import sys
from sqlservice import *
from matching import *

initSQL()

# mentorMatch("cla4846c00002sl8bnu2khur8")

if sys.argv[1] == 1:
    print(mentorMatch(sys.argv[2]))
    sys.stdout.flush()

close()