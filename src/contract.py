import grpc
import os
import sys

from protobuf import common_pb2, contract_pb2, contract_pb2_grpc

CreateContractTransactionType = 103
CallContractTransactionType = 104

AUTH_METADATA_KEY = "authorization"


class ContractHandler:
    def __init__(self, stub, connection_id):
        self.client = stub
        self.connection_id = connection_id
        return

    def start(self, connection_token):
        self.__connect(connection_token)

    def __connect(self, connection_token):
        # подключение
        request = contract_pb2.ConnectionRequest(
            connection_id=self.connection_id
        )
        metadata = [(AUTH_METADATA_KEY, connection_token)]  # данные
        for contract_transaction_response in self.client.Connect(request=request, metadata=metadata):
            self.__process_connect_response(contract_transaction_response)  # маршрутизатор методов

    def __process_connect_response(self, contract_transaction_response):
        print("receive: {}".format(contract_transaction_response))
        contract_transaction = contract_transaction_response.transaction  # получаем транзакцию
        if contract_transaction.type == CreateContractTransactionType:
            self.__handle_create_transaction(contract_transaction_response)
        elif contract_transaction.type == CallContractTransactionType:
            self.__handle_call_transaction(contract_transaction_response)
        else:
            print("Error: unknown transaction type '{}'".format(contract_transaction.type), file=sys.stderr)

    def __handle_create_transaction(self, contract_transaction_response):
        create_transaction = contract_transaction_response.transaction
        request = contract_pb2.ExecutionSuccessRequest(  # возвращаем успешный ответ
            tx_id=create_transaction.id,  # id транзакции
            results=[common_pb2.DataEntry(  # сохранение данных в блокчейн
                    key="sum",
                    int_value=0)]
        )
        metadata = [(AUTH_METADATA_KEY, contract_transaction_response.auth_token)]
        response = self.client.CommitExecutionSuccess(request=request, metadata=metadata)  # ответ, сохранение данных
        print("in create tx response '{}'".format(response))

    def __handle_call_transaction(self, contract_transaction_response):
        call_transaction = contract_transaction_response.transaction
        metadata = [(AUTH_METADATA_KEY, contract_transaction_response.auth_token)]

        # k = self.client.GetContractKey(call_transaction, "key")
        contract_key_request = contract_pb2.ContractKeyRequest(
            contract_id=call_transaction.contract_id,
            key="sum"
        )
        # получаем ключ, из которого можно взять данные
        contract_key = self.client.GetContractKey(request=contract_key_request, metadata=metadata)
        old_value = contract_key.entry.int_value # получаем данные по ключу

        request = contract_pb2.ExecutionSuccessRequest(  # возвращаем успешный ответ
            tx_id=call_transaction.id,  # id транзакции
            results=[common_pb2.DataEntry(  # сохранение данных в блокчейн
                key="sum",
                int_value=old_value + 10)]
        )
        response = self.client.CommitExecutionSuccess(request=request, metadata=metadata)
        print("in call tx response '{}'".format(response))

    # Блок регистации
    def client_registry(self, call_transaction, metadata):
        pass

    def maker_registry(self, call_transaction, metadata):
        pass

    def distributor_registry(self, call_transaction, metadata):
        pass

    def review_register(self, call_transaction, metadata):
        pass

    # Блок создание нового товара
    def create_product(self, call_transaction, metadata):
        pass

    def change_product(self, call_transaction, metadata):
        pass

    def review_product(self, call_transaction, metadata):
        pass

    # Блок создания заказа

    def create_order(self, call_transaction, metadata):
        pass

    def review_order(self, call_transaction, metadata):
        pass

    def accept_order(self, call_transaction, metadata):
        pass

    def cancel_order(self, call_transaction, metadata):
        pass

    # Блок получения данных

    def get_user(self, call_transaction, metadata):
        pass

    def get_all_user(self, call_transaction, metadata):
        pass

    def get_product(self, call_transaction, metadata):
        pass

    def get_all_products(self, call_transaction, metadata):
        pass

    def get_order(self, call_transaction, metadata):
        pass

    def get_all_orders(self, call_transaction, metadata):
        pass


def run(connection_id, node_host, node_port, connection_token):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('{}:{}'.format(node_host, node_port)) as channel:
        stub = contract_pb2_grpc.ContractServiceStub(channel)
        handler = ContractHandler(stub, connection_id) # Создание объекта контракта
        handler.start(connection_token) # запускаем смарт контракт


CONNECTION_ID_KEY = 'CONNECTION_ID'
CONNECTION_TOKEN_KEY = 'CONNECTION_TOKEN'
NODE_KEY = 'NODE'
NODE_PORT_KEY = 'NODE_PORT'

if __name__ == '__main__':
    if CONNECTION_ID_KEY not in os.environ:
        sys.exit("Connection id is not set")
    if CONNECTION_TOKEN_KEY not in os.environ:
        sys.exit("Connection token is not set")
    if NODE_KEY not in os.environ:
        sys.exit("Node host is not set")
    if NODE_PORT_KEY not in os.environ:
        sys.exit("Node port is not set")

    connection_id = os.environ['CONNECTION_ID']
    connection_token = os.environ['CONNECTION_TOKEN']
    node_host = os.environ['NODE']
    node_port = os.environ['NODE_PORT']

    run(connection_id, node_host, node_port, connection_token)