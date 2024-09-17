
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

test-predictions:
	@pytest tests/test_02_predictions.py -v -s -x --disable-warnings


test:
	@pytest -v -s -x --disable-warnings



################## Dev

dev:
	@uvicorn app.main:app --reload
