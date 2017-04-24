install: install-dev install-prod

install-prod:
	pip install -Ur requirements.txt -t libs

install-dev:
	pip install -Ur requirements-dev.txt

unit: clean
	nosetests -A "speed!='slow'" ${ARGS}

clean:
	find . -name "*.py[co]" -delete

fix_gae:
	@echo "Attempting install of gae.pth"
	bash fix_gae.sh
	@echo "Install complete"

run:
	dev_appserver.py demo/app.yaml
