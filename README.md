---
title: python-snowflakeclient
description: Another python snowflake client. But this works.
author: J. Matt Peterson
created:  2013 Apr 30
modified: 2013 Apr 30

---
python-snowflakeclient
======================

Another python snowflake client.

This library works, with the current release (1.0.2) of Twitter's
snowflake. It's part of iPlantCollaborative's infrastructure. It
includes a script so snowflake can accessed from the console.

# Install
```bash
pip install git+git://github.com/jmatt/python-snowflakeclient
```

# Python
```python
In [1]: host = "localhost"

In [2]: port = 7610

In [3]: from snowflakeclient.client import Client

In [4]: client = Client(host, port)

In [5]: client.get_id("rahr")
Out[5]: 329372919094317056
```

# Console script
```bash
user@server:~> snowflake --help
Usage: snowflake [options]

Options:
  -h, --help            show this help message and exit
  -s HOST, --host=HOST  The snowflake server host.
  -p PORT, --port=PORT  The snowflake server port.
  -a AGENT, --agent=AGENT
                        The snowflake server agent.
  -c COUNT, --count=COUNT
                        Number of snowflake ids to get from the server.

user@server:~> snowflake -h localhost -p 7610 -a awesome
1
"awesome"
localhost:7610
[329361097121337344]

user@server:~> snowflake --count=5 -h localhost -p 7610
5
"SN"
localhost:7610
[329361740158472192, 329361740158472193, 329361740158472194, 329361740162666496, 329361740162666497]
```
