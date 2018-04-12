from nsetools import Nse
import modules
from templates.quick_replies import add_quick_reply


from templates.text import TextTemplate

'''
 nsetools is a library for collecting real time data from National Stock Exchange (India).
'''
def process(input,entities):
    output = {}
    try:
        nse = Nse()
        symbol = " "
        #  symbol is the 'NSE symbol of the company'
        s= input.split(' ')
        for i in s:
            if nse.is_valid_code(str(i)):
                symbol = i
                break

        q = nse.get_quote(str(symbol))
        #  Getting Company name using variable symbol
        company_name  = q['companyName']
        company_symbol = q['symbol']
        # Getting open price of the day
        open_price = q['open']
        # Getting closing price of the day
        close_price = q['closePrice']
        # Getting average price of the day
        stock_price = q['faceValue']
        # Top gainers  for the last trading session
        # Top losers for the last trading session

        output['input'] = "Stock_price"
        msg = 'Company Name = '+company_name+" \n "+"Symbol = "+company_symbol+"\n "+"Open Price = "+str(open_price)+"\n"+"Close Price = "+str(close_price)+"\n"+"Stock Price = "+str(stock_price)
        msg_1={'text':msg}

        msg_1= add_quick_reply(msg_1, 'wipro stock', modules.generate_postback('stock_price'))
        msg_1 = add_quick_reply(msg_1, 'Tell me a joke.', modules.generate_postback('joke'))
        msg_1 = add_quick_reply(msg_1, 'roll a dice.', modules.generate_postback('dice'))
        output['output']=msg_1
        output['success']=True
    except:
        error_message = 'I couldn\'t understand the symbol '
        error_message += '\nPlease ask something like tcs stock_price etc.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False

    return output
