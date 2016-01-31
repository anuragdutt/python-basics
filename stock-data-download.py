from yahoo_finance import Share
yahoo = Share("YHOO")
print(yahoo.get_open())
print(yahoo.get_trade_datetime())
yahoo.refresh()
