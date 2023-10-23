.PHONY: test

test:
	docker-compose run main pytest
