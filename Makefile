all: install

install:
	ln -s `pwd`/dbq.py ~/.bin/dbq

uninstall:
	rm -f ~/.bin/dbq
