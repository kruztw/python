# https://zh-tw.coderbridge.com/@WeiHaoEric/0b2ced0696cc4c38a62d7b26fa7bbea0

all:
	mv simple.py Makefile ..
	rm * -rf
	mv ../simple.py ../Makefile .
	pyinstaller  simple.py
	rm build dist -rf
	pyinstaller -F -n simple simple.py
	mv dist/simple .
	rm build __pycache__ dist -rf

clean:
	rm simple simple.spec __pycache__ -rf
