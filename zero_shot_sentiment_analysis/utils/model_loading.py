import os

from transformers import pipeline


def get_model(model_name, logger):
    model_path = os.path.join("resources", model_name)
    # if there is model weights in local, load it directly
    if os.path.exists(os.path.join(model_path)):
        logger.info(f"Loading the model from local {model_path}...")
        model = pipeline("zero-shot-classification", model_path)

    # loading from hugging face transformers library
    else:
        logger.info("Downloading the model from hugging face...")
        model = pipeline("zero-shot-classification", "facebook/bart-large-mnli")
        model.save_pretrained(model_path)

    return model
