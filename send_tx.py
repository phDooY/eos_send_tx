from config import *

import eospy.keys
import eospy.cleos

#ce = eospy.cleos.Cleos(url='http://api.pennstation.eosnewyork.io:7001')
ce = eospy.cleos.Cleos(url='https://api.eosdetroit.io:443')

# to check if chain is active
#ce.get_chain_lib_info()

key1 = eospy.keys.EOSKey(ACC_PK)

memo_txt = "EOSpy sucks! Mhahahahah"

payload = [
        {
            'args': {
                "from": ACC_NAME_FROM,  # sender
                "to": ACC_NAME_TO,  # receiver
                "quantity": '1.0000 EOS',  # In EOS
                "memo": memo_txt,
            },
            "account": "eosio.token",
            "name": "transfer",
            "authorization": [{
                "actor": ACC_NAME_FROM,
                "permission": "active",
            }],
        }
    ]


data=ce.abi_json_to_bin(payload[0]['account'],payload[0]['name'],payload[0]['args'])

payload[0]['data']=data['binargs']

payload[0].pop('args')

trx = {"actions":[payload[0]]}

tx1 = ce.push_transaction(trx, [key1])

print('------------------------------------------------')
print(tx1)
print('------------------------------------------------')