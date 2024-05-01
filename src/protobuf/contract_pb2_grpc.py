# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protobuf.contract_pb2 as contract__pb2

class ContractServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Connect = channel.unary_stream(
                '/wavesenterprise.ContractService/Connect',
                request_serializer=contract__pb2.ConnectionRequest.SerializeToString,
                response_deserializer=contract__pb2.ContractTransactionResponse.FromString,
                )
        self.CommitExecutionSuccess = channel.unary_unary(
                '/wavesenterprise.ContractService/CommitExecutionSuccess',
                request_serializer=contract__pb2.ExecutionSuccessRequest.SerializeToString,
                response_deserializer=contract__pb2.CommitExecutionResponse.FromString,
                )
        self.CommitExecutionError = channel.unary_unary(
                '/wavesenterprise.ContractService/CommitExecutionError',
                request_serializer=contract__pb2.ExecutionErrorRequest.SerializeToString,
                response_deserializer=contract__pb2.CommitExecutionResponse.FromString,
                )
        self.GetContractKeys = channel.unary_unary(
                '/wavesenterprise.ContractService/GetContractKeys',
                request_serializer=contract__pb2.ContractKeysRequest.SerializeToString,
                response_deserializer=contract__pb2.ContractKeysResponse.FromString,
                )
        self.GetContractKey = channel.unary_unary(
                '/wavesenterprise.ContractService/GetContractKey',
                request_serializer=contract__pb2.ContractKeyRequest.SerializeToString,
                response_deserializer=contract__pb2.ContractKeyResponse.FromString,
                )


class ContractServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Connect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommitExecutionSuccess(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommitExecutionError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetContractKeys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetContractKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContractServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Connect': grpc.unary_stream_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=contract__pb2.ConnectionRequest.FromString,
                    response_serializer=contract__pb2.ContractTransactionResponse.SerializeToString,
            ),
            'CommitExecutionSuccess': grpc.unary_unary_rpc_method_handler(
                    servicer.CommitExecutionSuccess,
                    request_deserializer=contract__pb2.ExecutionSuccessRequest.FromString,
                    response_serializer=contract__pb2.CommitExecutionResponse.SerializeToString,
            ),
            'CommitExecutionError': grpc.unary_unary_rpc_method_handler(
                    servicer.CommitExecutionError,
                    request_deserializer=contract__pb2.ExecutionErrorRequest.FromString,
                    response_serializer=contract__pb2.CommitExecutionResponse.SerializeToString,
            ),
            'GetContractKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.GetContractKeys,
                    request_deserializer=contract__pb2.ContractKeysRequest.FromString,
                    response_serializer=contract__pb2.ContractKeysResponse.SerializeToString,
            ),
            'GetContractKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetContractKey,
                    request_deserializer=contract__pb2.ContractKeyRequest.FromString,
                    response_serializer=contract__pb2.ContractKeyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'wavesenterprise.ContractService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ContractService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/wavesenterprise.ContractService/Connect',
            contract__pb2.ConnectionRequest.SerializeToString,
            contract__pb2.ContractTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommitExecutionSuccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wavesenterprise.ContractService/CommitExecutionSuccess',
            contract__pb2.ExecutionSuccessRequest.SerializeToString,
            contract__pb2.CommitExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommitExecutionError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wavesenterprise.ContractService/CommitExecutionError',
            contract__pb2.ExecutionErrorRequest.SerializeToString,
            contract__pb2.CommitExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetContractKeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wavesenterprise.ContractService/GetContractKeys',
            contract__pb2.ContractKeysRequest.SerializeToString,
            contract__pb2.ContractKeysResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetContractKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wavesenterprise.ContractService/GetContractKey',
            contract__pb2.ContractKeyRequest.SerializeToString,
            contract__pb2.ContractKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)