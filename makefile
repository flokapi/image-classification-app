
model:
	@python3 -m app.cnn.cnn_model


api:
	@uvicorn app.main:app --reload