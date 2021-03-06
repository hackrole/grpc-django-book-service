# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import app_pb2 as app__pb2


class GRPCBookServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.QueryBooksPost = channel.unary_stream(
            '/grpc_protos.GRPCBookService/QueryBooksPost',
            request_serializer=app__pb2.QueryBooksRequest.SerializeToString,
            response_deserializer=app__pb2.Book.FromString,
        )
        self.GetBookPost = channel.unary_unary(
            '/grpc_protos.GRPCBookService/GetBookPost',
            request_serializer=app__pb2.GetBookRequest.SerializeToString,
            response_deserializer=app__pb2.Book.FromString,
        )


class GRPCBookServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def QueryBooksPost(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBookPost(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GRPCBookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'QueryBooksPost': grpc.unary_stream_rpc_method_handler(
            servicer.QueryBooksPost,
            request_deserializer=app__pb2.QueryBooksRequest.FromString,
            response_serializer=app__pb2.Book.SerializeToString,
        ),
        'GetBookPost': grpc.unary_unary_rpc_method_handler(
            servicer.GetBookPost,
            request_deserializer=app__pb2.GetBookRequest.FromString,
            response_serializer=app__pb2.Book.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'grpc_protos.GRPCBookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
