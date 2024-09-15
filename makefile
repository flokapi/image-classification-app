
model:
	@python3 -m app.cnn.cnn_model


dev:
	@uvicorn app.main:app --reload