all:
	python3 setup.py bdist_egg
	unzip -l dist/demo-0.1.0-py*.egg
	python3 setup.py install
	python3 -c "from demo import test; test()"

clean:
	rm -rf build dist *.egg-info 
