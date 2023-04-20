from app.service.user_service import UserService


class TransactionService:
    user_service = UserService()

    def create(self, transaction_body):
        # NOT WORKING
        return 0
        # if not self.user_service.verify(transaction_body.from_user_id, transaction_body.private_key):
        #     return 401, {"message": f"Cannot verify user {transaction_body.from_user_id} with private key"}
        #
        # # make transaction
        # return 201, {"message": "Transaction successful"}
