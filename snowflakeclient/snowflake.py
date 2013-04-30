#! /usr/bin/env python

import sys
import traceback
from optparse import OptionParser

from snowflakeclient.client import Client


host = "localhost"
port = 7610
agent = "SN"
n = 1


def main():
    global host, port, agent, n

    usage = "Usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-s", "--host",
                      default=host,
                      help="The snowflake server host.")
    parser.add_option("-p", "--port",
                      default=port,
                      type="int",
                      help="The snowflake server port.")
    parser.add_option("-a", "--agent",
                      default=agent,
                      help="The snowflake server agent.")
    parser.add_option("-c", "--count",
                      default=n,
                      type="int",
                      help="Number of snowflake ids to get from the server.")
    (options, args) = parser.parse_args()

    if options.host:
        host = options.host
    if options.port:
        port = options.port
    if options.agent:
        agent = options.agent
    if options.count:
        n = options.count

    print n
    print '"' + agent + '"'
    print host + ":" + str(port)

    client = Client(host, port)
    if client:
        print client.n_times(agent, n)
    else:
        print "Unable to create snowflake server client."


if __name__ == "__main__":
    main()
