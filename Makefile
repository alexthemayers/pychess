.PHONY: run client start all clean
run: client server/server start

all: client server/server

start:
	./server/server localhost &
	client

server/server:
	cd server && go vet
	cd server && go mod tidy -v
	go build -v -x -o server
	
build_client:
	pip install -r client/requirements.txt

clean: 
	rm server/server