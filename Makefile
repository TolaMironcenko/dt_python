all:
	@echo 'cleaning...'
	@make clean
	@echo 'cleaning successful'
	@echo 'building...'
	@make build
	@echo 'building siccessful'

build:
	@python setup.py py2app -A

clean:
	@rm -rf build dist