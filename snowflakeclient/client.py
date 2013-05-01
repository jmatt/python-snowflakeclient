"""
Another python snowflake client.

This library works, with the current release (1.0.2) of Twitter's
snowflake. It's part of iPlantCollaborative's infrastructure. It
includes a script so snowflake can accessed from the console.
"""
import sys
import traceback

from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.transport import THttpClient
try:
    from thrift.protocol import TBinaryProtocolAccelerated as TBinaryProtocol
except ImportError:
    from thrift.protocol import TBinaryProtocol

from snowflakeclient.Snowflake import Snowflake
from snowflakeclient.Snowflake import ttypes
from snowflakeclient.Snowflake import constants

class Client(object):

    client = None

    def __init__(self, host, port):
        self.client = Client.factory(host, port)

    @classmethod
    def factory(cls, host, port):
        """
        Returns an open Snowflake client instance.
        """
        try:
            socket = TSocket.TSocket(host, port)
            transport = TTransport.TFramedTransport(socket)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = Snowflake.Client(protocol)
            client.socket = socket
            client.transport = transport
            client.protocol = protocol
            transport.open()
            return client
        except Exception as e:
            traceback.print_exc(file=sys.stdout)

    def get_id(self, agent):
        return self.client.get_id(agent)

    def n_ids(self, agent, n):
        i = 0
        ids = []
        while i < n:
            ids.append(self.client.get_id(agent))
            i += 1
        return ids

    def get_datacenter_id():
        return self.client.get_datacenter_id()

    def get_timestamp():
        return self.client.get_timestamp()

    def get_worker_id():
        return self.client.get_worker_id()
