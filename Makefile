
setup:
	pip install -r requirements.txt

save:
	pip freeze >  requirements.txt

test:
	pytest -v

