SHELL := /bin/bash
UV ?= uv

.DEFAULT_GOAL := help
.PHONY: help install sync convert docs docs-serve docs-clean clean lint

help: ## Display this help text
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Setup

install: ## Install all dependencies
	$(UV) sync

##@ Content Pipeline

sync: ## Sync raw HTML from wiki server
	./scripts/sync.sh

convert: ## Convert HTML to Markdown (requires sync first)
	$(UV) run --group convert python scripts/convert.py --wiki all --raw-dir _raw --out-dir .

##@ Documentation

docs: docs-clean ## Build Sphinx documentation
	$(UV) run sphinx-build -b html . _build/html -j auto --keep-going

docs-serve: ## Serve docs with live reload
	$(UV) run sphinx-autobuild . _build/html -j auto --port 8001

docs-clean: ## Clean built documentation
	rm -rf _build

##@ Code Quality

lint: ## Run pre-commit hooks
	$(UV) run prek run --all-files

##@ Utility

clean: docs-clean ## Clean all build artifacts
	rm -rf _raw
