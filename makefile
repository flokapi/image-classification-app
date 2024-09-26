
################## Install

install:
	pip install -r requirements.txt
	pip install tensorflow
	pip install pytest
	npm install tailwindcss


################## Build

build-model:
	@python3 -m app.cnn.cnn_model


build-static-files:
	@echo "====== Downloading htmx"
	curl https://unpkg.com/htmx.org@1.6.1/dist/htmx.min.js -o ./static/htmx.min.js

	@echo "====== Generating the css file"
	npx tailwindcss -o ./static/styles.css


build: build-static-files build-model



################## Test

PYTEST_FLAGS = -v -s -x --disable-warnings


test-cnn:
	@pytest tests/test_01_cnn $(PYTEST_FLAGS)

test-api:
	@pytest tests/test_02_api $(PYTEST_FLAGS)

test-ui:
	@pytest tests/test_03_ui $(PYTEST_FLAGS)


test:
	@pytest $(PYTEST_FLAGS)



################## Dev

dev:
	@uvicorn app.main:app --reload
