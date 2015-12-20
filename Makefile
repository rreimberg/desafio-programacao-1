clean:
	find -iname *.pyc -delete
	find -iname *.pyo -delete

setup:
	$(test) -d .venv || virtualenv -p python2.7 .venv
	.venv/bin/pip install -r requirements.txt

test:
	nosetests --rednose
