import datetime
from enum import Enum
import base58

from core.blockchain.blockchain import Blockchain
from core.blockchain.pool import Pool, poolParam
from core.wallet.operation import Operation
from core.wallet.transaction import Transaction
from core.wallet.wallet import Wallet


class Core:
    HASH = '0000000000000000000000000000000000000000000000000000000000000000'
    CoreStats = Enum('CoreStats', ['STATE_OK', 'TOKEN_NOT_EXIST', 'USER_NOT_EXIST', 'WALLET_NOT_EXIST', 'USER_EXIST'])

    users_id = []
    wallets = []
    tokens = []
    blockchain = Blockchain()

    def contruct_wallets(self):
        wallet_id = 0
        now = datetime.datetime.now()

        for block in self.blockchain.blocks:
            for pool in block.pools:

                if pool.param == 3:
                    state, wallet = Wallet.construct(pool.id_1)

                    self.wallets.append(wallet)
                    self.users_id.append(pool.id_1)
                    wallet_id += 1

                elif pool.param == 0:
                    state, transaction1 = Transaction.construct(pool.id_1, pool.id_2, pool.amount, 'OUT', str(now))
                    state, transaction2 = Transaction.construct(pool.id_1, pool.id_2, pool.amount, 'IN', str(now))

                    index1 = [index for index in range(len(self.users_id)) if self.users_id[index] == pool.id_1]
                    index2 = [index for index in range(len(self.users_id)) if self.users_id[index] == pool.id_2]

                    Wallet.add_transaction(self.wallets[index1[0]], transaction1)
                    Wallet.add_transaction(self.wallets[index2[0]], transaction2)

                    Wallet.remove_amount(self.wallets[index1[0]], pool.amount)
                    Wallet.add_amount(self.wallets[index2[0]], pool.amount)

                elif pool.param == 1:
                    index2 = [index for index in range(len(self.users_id)) if self.users_id[index] == pool.id_2]
                    state, operation = Operation.construct(pool.id_2, 1, 'NEW TOKEN', str(now))
                    Wallet.add_operation(self.wallets[index2[0]], operation)
                    Wallet.add_amount(self.wallets[index2[0]], 1)
                    self.tokens.append(pool.id_1)

                elif pool.param == 2:
                    try:
                        self.tokens.remove(pool.id_1)
                        index2 = [index for index in range(len(self.users_id)) if self.users_id[index] == pool.id_2]
                        state, operation = Operation.construct(pool.id_2, 1, 'DEL TOKEN', str(now))
                        Wallet.add_operation(self.wallets[index2[0]], operation)
                        Wallet.remove_amount(self.wallets[index2[0]], 1)
                    except ValueError:
                        print()

        for i in range(0, len(self.wallets)):
            state = Wallet.save_wallet(self.wallets[i], i)

    def print_wallet(self, wallet):
        print("GENERAL OVERWIEV")
        state, str_ = Wallet.print_status(wallet)
        print(str_)
        print("TRANSACTIONS LIST")
        state, str_ = Wallet.print_transactions(wallet)
        print(str_)
        print("OPERATIONS LIST")
        state, str_ = Wallet.print_operations(wallet)
        print(str_)

    def add_transaction(self, user1_id, user2_id, amount):
        now = datetime.datetime.now()

        index1 = [index for index in range(len(self.users_id)) if self.users_id[index] == user1_id]
        index2 = [index for index in range(len(self.users_id)) if self.users_id[index] == user2_id]

        if index1 and index2:
            state, wallet1 = Wallet.read_wallet(index1[0])
            state, wallet2 = Wallet.read_wallet(index2[0])

            state = Wallet.remove_amount(wallet1, amount)

            if state.value == Wallet.WalletStats.STATE_OK.value:
                state = Wallet.add_amount(wallet2, amount)

                state, transaction1 = Transaction.construct(user1_id, user2_id, amount, 'OUT', str(now))
                state, transaction2 = Transaction.construct(user1_id, user2_id, amount, 'IN', str(now))

                state = Wallet.add_transaction(wallet1, transaction1)
                state = Wallet.add_transaction(wallet2, transaction2)

                state = Wallet.save_wallet(wallet1, index1[0])
                state = Wallet.save_wallet(wallet2, index2[0])

                self.wallets[index1[0]] = wallet1
                self.wallets[index2[0]] = wallet2

                state, new_pool = Pool.construct(user1_id, poolParam.SEND.value, user2_id, amount, str(now), self.HASH)
                state = self.blockchain.add_pool(new_pool)
                
                return (self.CoreStats.STATE_OK)
            else:
                return (self.CoreStats.WALLET_NOT_EXIST)

        else:
            return (self.CoreStats.USER_NOT_EXIST)

    def add_token(self, token, userID):
        now = datetime.datetime.now()

        index1 = [index for index in range(len(self.users_id)) if self.users_id[index] == userID]

        if index1:
            state, new_pool = Pool.construct(token, poolParam.nTOKEN.value, userID, 1, str(now), self.HASH)
            state = self.blockchain.add_pool(new_pool)

            state, wallet1 = Wallet.read_wallet(index1[0])
            state, operation1 = Operation.construct(userID, 1, 'NEW TOKEN', str(now))
            state = Wallet.add_operation(wallet1, operation1)
            state = Wallet.add_amount(wallet1, 1)
            state = Wallet.save_wallet(wallet1, index1[0])
            self.wallets[index1[0]] = wallet1
            self.tokens.append(token)

            return (self.CoreStats.STATE_OK)
        else:
            return (self.CoreStats.USER_NOT_EXIST)

    def delete_token(self, token, userID):
        now = datetime.datetime.now()

        index1 = [index for index in range(len(self.users_id)) if self.users_id[index] == userID]

        if index1:
            try:
                self.tokens.remove(token)

                state, new_pool = Pool.construct(token, poolParam.dTOKEN.value, userID, 1, str(now), self.HASH)
                state = self.blockchain.add_pool(new_pool)

                state, wallet1 = Wallet.read_wallet(index1[0])
                state, operation1 = Operation.construct(userID, 1, 'DEL TOKEN', str(now))
                state = Wallet.add_operation(wallet1, operation1)
                state = Wallet.remove_amount(wallet1, 1)
                state = Wallet.save_wallet(wallet1, index1[0])
                self.wallets[index1[0]] = wallet1

                return (self.CoreStats.STATE_OK)
            except ValueError:
                return (self.CoreStats.TOKEN_NOT_EXIST)
        else:
            return (self.CoreStats.USER_NOT_EXIST)

    def add_user(self, userID):
        index1 = [index for index in range(len(self.users_id)) if self.users_id[index] == userID]

        if not index1:
            now = datetime.datetime.now()
            state, wallet = Wallet.construct(userID)

            #################################################
            # wallet.add_amount(wallet, 0)
            #################################################

            self.wallets.append(wallet)
            self.users_id.append(userID)

            state = Wallet.save_wallet(wallet, len(self.wallets) - 1)

            state, new_pool = Pool.construct(userID, poolParam.nUSER.value, userID, 1, str(now), self.HASH)
            state = self.blockchain.add_pool(new_pool)

            return (self.CoreStats.STATE_OK)
        else:
            return (self.CoreStats.USER_EXIST)
            
    def wallet_to_json(self, coded_user_id):
        #try:
        real_user_id = base58.b58decode(coded_user_id).decode('utf-8')

        index1 = [index for index in range(len(self.users_id)) if self.users_id[index] == real_user_id]
        some = []
        
        if index1:
            return Wallet.to_json(self.wallets[index1[0]])
        else:
            return {"wallet": "No exist"}
        #except Exception:
        #    return {"wallet": "Invalid User"}

