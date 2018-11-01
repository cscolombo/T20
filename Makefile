SHELL := /bin/bash
LOCALPATH := $(CURDIR)/$(PROJECT)
PYTHONPATH := $(LOCALPATH)/


help:
	@echo "    Executa"
	@echo "    Processa o arquivo arquivosaida no diretorio corrente."

all: 	executa

#compila:
#	python T20.py

executa:
	python T20.py

clear:
	rm -Rf arquivosaida
