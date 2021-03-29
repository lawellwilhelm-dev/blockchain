genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}

# initializing our blockchain list
blockchain = [genesis_block]

# initializing list of outstanding transactions
open_transactions = []

owner = 'Wilhelm'


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

    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]

    hashed_block = '-'.join([str(value) for key, value in last_block.items()])
    print(hashed_block)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)

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
    is_valid = True

    for block_index, block in enumerate(blockchain):
        if block_index == 0:
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break

    return is_valid
        


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the transaction blocks')
    print('h: Manipulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        recipient, amount = get_transaction_value()
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
        continue

    
    # if not verify_blockchain():
    #     print_blockchain_elements()
    #     print('Invalid blockchain')
    #     break

print('Done!')
    