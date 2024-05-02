import grpc
import os
import sys
import logging

logging.basicConfig(
    filename='contract_handler.log',  # Укажите имя файла, куда будут записываться логи
    level=logging.INFO,  # Уровень логгирования (INFO, DEBUG, ERROR и т. д.)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат записи логов
)


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
            results=[common_pb2.DataEntry(key="users", int_value=0),
                     common_pb2.DataEntry(key="makers", int_value=0),
                     common_pb2.DataEntry(key="distributors", int_value=0),
                     common_pb2.DataEntry(key="products", int_value=0),
                     common_pb2.DataEntry(key="orders", int_value=0)]
        )
        metadata = [(AUTH_METADATA_KEY, contract_transaction_response.auth_token)]
        response = self.client.CommitExecutionSuccess(request=request, metadata=metadata)  # ответ, сохранение данных
        print("in create tx response '{}'".format(response))

    def __handle_call_transaction(self, contract_transaction_response):
        call_transaction = contract_transaction_response.transaction
        metadata = [(AUTH_METADATA_KEY, contract_transaction_response.auth_token)]

        data = self.client_registry(call_transaction, metadata)
        # match tx_type:
        #     case "client_registry":
        #         request = self.client_registry(call_transaction, metadata)
        #     case "maker_registry":
        #         request = self.maker_registry(call_transaction, metadata)
        #     case "distributor_registry":
        #         request = self.distributor_registry(call_transaction, metadata)
        #     case "review_register":
        #         request = self.review_register(call_transaction, metadata)
        #     case "create_product":
        #         request = self.create_product(call_transaction, metadata)
        #     case "review_product":
        #         request = self.review_product(call_transaction, metadata)
        #     case "change_product":
        #         request = self.change_product(call_transaction, metadata)
        #     case "create_order":
        #         request = self.create_product(call_transaction, metadata)
        #     case "review_order":
        #         request = self.review_order(call_transaction, metadata)
        #     case "accept_order":
        #         request = self.accept_order(call_transaction, metadata)
        #     case "cancel_order":
        #         request = self.cancel_order(call_transaction, metadata)
        #     case "get_user":
        #         pass
        #     case "get_all_user":
        #         pass
        #     case "get_product":
        #         pass
        #     case "get_all_products":
        #         pass
        #     case "get_order":
        #         pass
        #     case "get_all_orders":
        #         pass

        request = contract_pb2.ExecutionSuccessRequest(
            tx_id=call_transaction.id,
            results=data
        )

        response = self.client.CommitExecutionSuccess(request=request, metadata=metadata)
        print("in call tx response '{}'".format(response))

    @staticmethod
    def get_string_value(call_transaction, key):
        res = ''
        for param in call_transaction.params:
            if param.key == key:
                res = param.str_value
                break
        return res

    @staticmethod
    def get_int_value(call_transaction, key):
        res = 0
        for param in call_transaction.params:
            if param.key == key:
                res = param.int_value
                break
        return res

    @staticmethod
    def get_bool_value(call_transaction, key):
        res = False
        for param in call_transaction.params:
            if param.key == key:
                res = param.bool_value
                break
        return res

    # Блок регистации
    def client_registry(self, call_transaction, metadata):
        # получаем ключ, из которого можно взять данные

        try:
            contract_key_request = contract_pb2.ContractKeyRequest(
                contract_id=call_transaction.contract_id,
                key="users"
            )
            contract_key = self.client.GetContractKey(request=contract_key_request, metadata=metadata)
            user_id = contract_key.entry.int_value

            data = [
                common_pb2.DataEntry(key=f"request_user_{user_id + 1}",
                                     str_value=self.get_string_value(call_transaction, "user")),
                common_pb2.DataEntry(key="users", int_value=user_id + 1)
            ]

            return data
        except Exception as error:
            logging.info(f'{error}')

    def maker_registry(self, call_transaction, metadata):
        try:
            contract_key_request = contract_pb2.ContractKeyRequest(
                contract_id=call_transaction.contract_id,
                key="makers"
            )
            contract_key = self.client.GetContractKey(request=contract_key_request, metadata=metadata)
            maker_id = contract_key.entry.int_value

            data = [
                common_pb2.DataEntry(key=f"request_maker_{maker_id + 1}",
                                     str_value=self.get_string_value(call_transaction, "maker")),
                common_pb2.DataEntry(key="makers", int_value=maker_id + 1)
            ]

            return data
        except Exception as error:
            logging.info(f'{error}')

    def distributor_registry(self, call_transaction, metadata):
        try:
            contract_key_request = contract_pb2.ContractKeyRequest(
                contract_id=call_transaction.contract_id,
                key="distributors"
            )
            contract_key = self.client.GetContractKey(request=contract_key_request, metadata=metadata)
            distributor_id = contract_key.entry.int_value

            data = [
                common_pb2.DataEntry(key=f"request_distributor_{distributor_id + 1}",
                                     str_value=self.get_string_value(call_transaction, "distributor")),
                common_pb2.DataEntry(key="distributors", int_value=distributor_id + 1)
            ]

            return data
        except Exception as error:
            logging.info(f'{error}')

    def review_register(self, call_transaction, metadata): # !!!!!!!!!!
        """одобряем регистрацию"""

        distributor_id = self.get_int_value(call_transaction, key="distributor")
        maker_id = self.get_int_value(call_transaction, key="maker")
        if distributor_id != 0:
            get_key = f"request_distributor_{distributor_id}"
        elif maker_id != 0:
            get_key = f"request_maker_{maker_id}"
        else:
            user_id = self.get_int_value(call_transaction, key="user")
            get_key = f"request_user_{user_id}"

        contract_key_request = contract_pb2.ContractKeyRequest(
            contract_id=call_transaction.contract_id,
            key=get_key
        )

        contract_key = self.client.GetContractKey(request=contract_key_request, metadata=metadata)
        _id = contract_key.entry.str_value

        data = [
            common_pb2.DataEntry(key=get_key,str_value=""), # меняем флаг на true
        ]

        return data

    # Блок создание нового товара
    def create_product(self, call_transaction, metadata):
        try:
            contract_key_request = contract_pb2.ContractKeyRequest(
                contract_id=call_transaction.contract_id,
                key="products"
            )
            contract_key = self.client.GetContractKey(request=contract_key_request, metadata=metadata)
            product_id = contract_key.entry.int_value

            data = [
                common_pb2.DataEntry(key=f"product_{product_id + 1}",
                                     str_value=self.get_string_value(call_transaction, "product")),
                common_pb2.DataEntry(key="products", int_value=product_id + 1)
            ]

            return data
        except Exception as error:
            logging.info(f'{error}')

    def review_product(self, call_transaction, metadata): # !!!!!!!!!!
        """Добавляем данные в продукт и публикуем его"""
        product_id = self.get_int_value(call_transaction, key="product")
        contract_key_request = contract_pb2.ContractKeyRequest(
            contract_id=call_transaction.contract_id,
            key=f"product_{product_id}"
        )

        contract_key = self.client.GetContractKey(request=contract_key_request, metadata=metadata)
        product = contract_key.entry.str_value

        data = [
            common_pb2.DataEntry(key=f"product_{product_id}",
                                 value="product") # работаем со значением
        ]

        return data

    # Блок создания заказа

    def create_order(self, call_transaction, metadata):
        try:
            contract_key_request = contract_pb2.ContractKeyRequest(
                contract_id=call_transaction.contract_id,
                key="orders"
            )
            contract_key = self.client.GetContractKey(request=contract_key_request, metadata=metadata)
            order_id = contract_key.entry.int_value

            data = [
                common_pb2.DataEntry(key=f"request_product_{order_id + 1}",
                                     str_value=self.get_string_value(call_transaction, "order")),
                common_pb2.DataEntry(key="orders", int_value=order_id + 1)
            ]

            return data
        except Exception as error:
            logging.info(f'{error}')

    def review_order(self, call_transaction, metadata):
        pass

    def user_order_review(self, call_transaction, metadata):
        pass


    # Блок получения данных

    # def get_user(self, call_transaction, metadata):
    #     pass
    #
    # def get_all_user(self, call_transaction, metadata):
    #     pass
    #
    # def get_product(self, call_transaction, metadata):
    #     pass
    #
    # def get_all_products(self, call_transaction, metadata):
    #     pass
    #
    # def get_order(self, call_transaction, metadata):
    #     pass
    #
    # def get_all_orders(self, call_transaction, metadata):
    #     pass


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