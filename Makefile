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

kill:
	lsof -P | grep ':8080' | awk '{print $2}' | xargs kill -9
