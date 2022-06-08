import pickle
from tensorflow import keras


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
        sequences, maxlen=maxlen, padding=padding)

    return padded_sequences


def load_tokenizer(tokenizer_file):
    with open(tokenizer_file, 'rb') as tokenizer:
        loaded_tokenizer = pickle.load(tokenizer)

    return loaded_tokenizer


def load_model(model_file):
    loaded_model = keras.models.load_model(model_file)

    return loaded_model
