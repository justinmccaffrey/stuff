import sys,os
import curses
import random
from time import sleep

def draw_menu(stdscr):
	k = 0
	cursor_x = 0
	cursor_y = 0

    # Clear and refresh the screen for a blank canvas
	stdscr.clear()
	stdscr.refresh()


	curses.curs_set(0)
    # Loop where k is the last character pressed

	# Initialization
	stdscr.clear()
	height, width = stdscr.getmaxyx()


	cursor_x = max(0, cursor_x)
	cursor_x = min(width-1, cursor_x)

	cursor_y = max(0, cursor_y)
	cursor_y = min(height-1, cursor_y)


	# Rendering some text
	cat1 = "curses test"
	stdscr.addstr(0, 0, cat1)
	cat2 = "stuff : "
	stdscr.addstr(1, 0, cat2)

	# Render status bar
	stdscr.attron(curses.color_pair(3))
	stdscr.addstr(height-1, 0, statusbarstr)
	stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
	stdscr.attroff(curses.color_pair(3))


	# Refresh the screen
	stdscr.refresh()
	while(1):
		for i in range(1,21):
			stdscr.addstr(i, len(cat2),'0x'+ ''.join('{:08X}'.format(random.randrange(1,0x100000000))))
		stdscr.refresh()
		sleep(0.0)
def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()