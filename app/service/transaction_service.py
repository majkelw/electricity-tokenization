
class TransactionService:

    def __init__(self, core):
        self.core = core

    def create(self, transaction_body):
        
        index1 = [index for index in range(len(self.core.users_id)) if self.core.users_id[index] == transaction_body.id_from]
        index2 = [index for index in range(len(self.core.users_id)) if self.core.users_id[index] == transaction_body.id_to]
        
        if index1:
            if index2:
                state = self.core.add_transaction(self.core.users_id[index1[0]], self.core.users_id[index2[0]], float(transaction_body.amount))
                if state.value == self.core.CoreStats.STATE_OK.value:
                    return 201, {"transaction": "OK"}
                else:
                    return 401, {"transaction": "Negative_amount_or_negative_bilance"}
            else:
                return 401, {"transaction": "User to not exist."}
        else:            
            return 401, {"transaction": "User from not exist."}

