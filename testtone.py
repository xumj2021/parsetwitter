from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentences = ["$BHI - Baker Hughesorporated Stock Analysis - Doji Candlestick Pattern - http://t.co/OBWqUrHDbC",  # positive sentence example
             "Weekly Top S&amp;P100 #Stocks $NKE $GILD $AMGN $HPQ $ABT $LMT $MA $AMZN $MON $NOV $WAG $AVP $CMCSA $BHI $UNH $PEP $CL $INTC  #OEF #trading",  # punctuation emphasis handled correctly (sentiment intensity adjusted)
             "Inverse H&amp;S pattern developing on $BHI - Neckline around 48.50  http://t.co/HZZapgjK29", # booster words handled correctly (sentiment intensity adjusted)
             ]

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))