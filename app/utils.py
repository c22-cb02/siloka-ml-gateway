import json
import time
import pickle
import logging
import functools
from pyclbr import Function

from tensorflow import keras
from google.cloud import storage


def microbenchmark(func: Function):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_microbenchmark(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        logging.info(
            "Function %s(%s, %s) ran in %.4f seconds",
            func.__name__,
            args,
            kwargs,
            run_time,
        )
        return value

    return wrapper_microbenchmark


@microbenchmark
def download_blob_from_bucket(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    logging.info(
        "Downloaded storage object %s from bucket %s to local file %s.",
        source_blob_name,
        bucket_name,
        destination_file_name,
    )


def load_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as file:
        loaded_json = json.load(file)

    logging.info("")

    return loaded_json


def seq_and_pad(sentences, tokenizer, padding, maxlen):
    """
    Generates an array of token sequences and pads them to the same length

    Args:
        sentences (list of string): list of sentences to tokenize and pad
        tokenizer (object): Tokenizer instance containing the word-index dictionary
        padding (string): type of padding to use
        maxlen (int): maximum length of the token sequence

    Returns:
        padded_sequences (array of int): tokenized sentences padded to the same length
    """

    # Convert sentences to sequences
    sequences = tokenizer.texts_to_sequences(sentences)

    # Pad the sequences using the correct padding and maxlen
    padded_sequences = keras.preprocessing.sequence.pad_sequences(
        sequences, maxlen=maxlen, padding=padding
    )

    return padded_sequences


def load_tokenizer(tokenizer_file):
    with open(tokenizer_file, "rb") as tokenizer:
        loaded_tokenizer = pickle.load(tokenizer)

    return loaded_tokenizer


@microbenchmark
def load_model(model_file):
    loaded_model = keras.models.load_model(model_file)

    return loaded_model
