Currency Converter

list of files:

	README.md (you are here now)

	Currency.py
		initialized currency objects and compares using operands
		throws error if difference currencies are attempted to be added/subbed

	CurrencyConverter.py
		initializes a dictionary of rates of currencies compared to USD
		helps you convert from one currency to another
		determines ratio of currency when adjusted
		throws and error if you attempt to convert FROM or TO a currency not in dict

	currencyconverter_test.py
        using nosetests:
    		runs a series of tests to make sure code works.
    		all pass and the two with errors get caught
