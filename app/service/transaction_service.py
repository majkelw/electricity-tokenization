
class TransactionService:

    def __init__(self, core):
        self.core = core

    def create(self, transaction_body):
        
        index1 = [index for index in range(len(self.core.users_id)) if self.core.users_id[index] == transaction_body.user_id_from]
        index2 = [index for index in range(len(self.core.users_id)) if self.core.users_id[index] == transaction_body.user_id_to]
        
        if index1:
            if index2:
                state = self.core.add_transaction(self.core.users_id[index1[0]], self.core.users_id[index2[0]], float(transaction_body.amount))
                if state.value == self.core.CoreStats.STATE_OK.value:
                    return 201, {"message": "Wysłano"}
                else:
                    return 400, {"message": "Niepoprawna liczba tokenów"}
            else:
                return 401, {"message": "Taki odbiorca nie istnieje"}
        else:            
            return 401, {"message": "Taki nadawca nie istnieje"}

