import numpy as np

from .utils import seq_and_pad


def predict_sentences(sentence, model, tokenizer, labels, padding, maxlen):
    sentence_seq_pad = seq_and_pad(sentence, tokenizer, padding, maxlen)

    predictions = model.predict(sentence_seq_pad)
    percentage = {}

    for i in range(len(predictions[0])):
        percentage[labels[i]] = predictions[0][i]

    prediction_res_idx = np.argmax(predictions[0])

    result_tag = labels[prediction_res_idx]
    prediction_acc = percentage[result_tag]

    return result_tag, prediction_acc
