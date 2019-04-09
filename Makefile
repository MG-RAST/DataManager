BUILD_ID?=latest
REGISTRY?=mgrast

.PHONY: build_base
build_base:
	docker build -t ${REGISTRY}/django-base:${BUILD_ID} -f Dockerfile.base .
	@echo Image tag: ${REGISTRY}/django-base:${BUILD_ID}

build: build_base
