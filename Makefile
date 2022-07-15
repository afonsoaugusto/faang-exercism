MAKEFLAGS  	+= --silent
SHELL      	 = /bin/bash


elixir:
	@echo "Run tests in elixir..."
	cd exercism/0/elixir && \
	mix test