# 參考: https://dzone.com/articles/executable-package-pip-install

all:
	python3 setup.py bdist_wheel

local:
	sudo python3 -m pip install dist/*.whl

upload:
	sudo python3 -m twine upload dist/*

clean:
	rm build dist kruztw_py1.egg-info -rf 
