
model:
	@python3 -m app.cnn.cnn_model


dev:
	@uvicorn app.main:app --reload


test:
	@pytest -v -s -x --disable-warnings

test-predictions:
	@pytest tests/test_02_predictions.py -v -s -x --disable-warnings