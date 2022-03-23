all:
	swig -python -keyword simple.i
	python3 setup.py build_ext --inplace

init:
	sudo apt install swig

run:
	python3 main.py

clean:
	rm *.so simple_wrap.c __pycache__ build -rf FOO.py

