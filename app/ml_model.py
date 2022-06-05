import numpy as np

from .utils import seq_and_pad

# Still hardcoded, consider to change it
labels = [
        'opsi', 
        'deactivateAccount', 
        'unknownPasswordReset', 
        'addEmailHp', 
        'payBooking', 
        'checkPaymentStatus', 
        'travelokaBankAccount', 
        'unsuccessfulTransaction', 
        'resendOTP', 
        'unlockAccount', 
        'paidWrongAmount', 
        'BookFlight', 
        'ActivateFlightPriceAlerts', 
        'PaySelectSeat', 
        'ReschedulingFlightHotelBooking', 
        'BookFlightHotel', 
        'confirmingTrainBooking', 
        'CancelAndGetRefundTrainBooking', 
        'TrainETicket', 
        'RescheduleRerouteTrainBooking', 
        'kaiTravelRegulationUpdate', 
        'rescheduleHotelBooking', 
        'bookAHotel', 
        'cancelAndGetRefundHotel', 
        'villaAndApartemen', 
        'BookingVillaAndApartment'
    ]

def predict_sentences(sentence, model, tokenizer, padding, maxlen):
    sentence_seq_pad = seq_and_pad(sentence, tokenizer, padding, maxlen)

    predictions = model.predict(sentence_seq_pad)
    percentage = {}

    for i in range(len(predictions[0])):
        percentage[labels[i]] = predictions[0][i] 

    # prediction_sorted_by_percentage = sorted(percentage.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

    prediction_res_idx = np.argmax(predictions[0])

    return labels[prediction_res_idx]