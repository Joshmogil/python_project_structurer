say_hello:
	@echo "Hello World"

build:
	go build -o bin/py-struct ./tool/*

run:
	go run ./tool/*