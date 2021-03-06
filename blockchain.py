from functools import reduce
from collections import OrderedDict
import hashlib
import json

# Reward given to a person who creates a new block
MINING_REWARD = 10

GENESIS_BLOCK = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}

# initializing our blockchain list
blockchain = [GENESIS_BLOCK]

# initializing list of outstanding transactions
open_transactions = []

owner = 'Wilhelm'

participants = {'Wilhelm'}


def get_last_blockchain_value():
    """ Returns the current value of the last blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """  Append a new value as well as the last blockchain value to the blockchain. 

        Arguments:
            :sender: The sender of the coins.
            :recipient: The recipient of the coins.
            :amount: The amount of coins sent with the transaction (default 1.0)
    """

    transaction = OrderedDict([
        ('sender', sender),
        ('recipient', recipient),
        ('amount', amount)
    ])

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])

    return sender_balance > transaction['amount']

    
def hash_block(block):
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0

    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    
    return proof




def mine_block():
    last_block = blockchain[-1]

    hashed_block = hash_block(last_block)

    proof = proof_of_work()

    reward_transaction = OrderedDict([
        ('sender', 'MINING'),
        ('recipient', owner),
        ('amount', MINING_REWARD)
    ])

    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions,
        'proof': proof
    }
    blockchain.append(block)
    return True


def get_balance(participant):
    tx_sender = [
        [tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] 
        for block in blockchain
    ]

    open_tx_sender = [
        tx['amount'] for tx in open_transactions if tx['sender'] == participant
    ]
    
    tx_sender.append(open_tx_sender)
    
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    
    tx_recipient = [
        [tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] 
        for block in blockchain
    ]

    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    
    return amount_received - amount_sent
    

def get_transaction_value():
    """ Returns the user's input (a new transaction amount). """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter the transaction amount: '))

    return tx_recipient, tx_amount


def get_user_choice():
    """ Returns the user's input (an action to perform). """
    return input('Your choice: ')



def print_blockchain_elements():
    # output blockchain list to the console 
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)


def verify_blockchain():
    """ Verify the current blockchain and return True if it's valid, False otherwise """
    for index, block in enumerate(blockchain):
        if index == 0:
            continue 
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of work is invalid')
            return False
    
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])
    

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the transaction blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        recipient, amount = get_transaction_value()
        if add_transaction(recipient, amount=amount):
            print('Added transaction')
        else:
            print('Transaction failed')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{
                    'sender': 'Rich',
                    'recipient': 'Wilhelm',
                    'amount': 100
                }]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
        continue
    
    if not verify_blockchain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break

    print(f'Balance of {owner}: {get_balance(owner) : 6.2f}')
    
print('Done!')
