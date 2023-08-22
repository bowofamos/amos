# Amos
## AmosMsg is a MQ consumer
### 1. MQ Consumer
your code
```python
import json
from AmosMsg.AmosMsg import AmosMsg


def call_back(ch, method, properties, body):
    message = json.loads(body.decode())
    print(message)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("%r" % body)


if __name__ == '__main__':
    amos = AmosMsg(
        msg_user='consumer_user', 
        msg_pass='consumer_password', 
        enable_ssl=False, # disable SSL
        host="your.rabbitmq.host", 
        port=5672,  # MQ default port is 5672
        v_host="your_virtual_host",
        exchange="your_exchange", 
        queue="your_queue",
    )
    amos.create_channel()
    amos.create_queue()
    amos.connect_exchange()
    amos.run_consumer(call_back)
```
### 2. Use SSL
your code
```python
import json
from AmosMsg.AmosMsg import AmosMsg


def call_back(ch, method, properties, body):
    message = json.loads(body.decode())
    print(message)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("%r" % body)


if __name__ == '__main__':
    amos = AmosMsg(
        msg_user='consumer_user', 
        msg_pass='consumer_password', 
        enable_ssl=True, # enable SSL
        host="your.rabbitmq.host", 
        port=5671,  # MQ SSL default port is 5671
        v_host="your_virtual_host",
        exchange="your_exchange", 
        queue="your_queue",
        ca="your/path/to/ca",
        crt="your/path/to/crt", 
        key="your/path/to//key"
    )
    amos.create_channel()
    amos.create_queue()
    amos.connect_exchange()
    amos.run_consumer(call_back)
```
### 3. Use config file
your code
```python
import json
from AmosMsg.AmosMsg import AmosMsg


def call_back(ch, method, properties, body):
    message = json.loads(body.decode())
    print(message)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("%r" % body)


if __name__ == '__main__':
    amos = AmosMsg(
        msg_user='consumer_user', 
        msg_pass='consumer_password', 
        config_path="path/to/your/config.yaml",
        enable_ssl=False, # disable SSL
    )
    amos.create_channel()
    amos.create_queue()
    amos.connect_exchange()
    amos.run_consumer(call_back)
```
config.yaml
```yaml
host: "your.rabbitmq.host"
port: 5672 # Non-SSL default port is 5672
virtual_host: "your_virtual_host"
exchange: "your_exchange"
queue: "your_queue"
```
### 4. Use config file with SSL
your code
```python
import json
from AmosMsg.AmosMsg import AmosMsg


def call_back(ch, method, properties, body):
    message = json.loads(body.decode())
    print(message)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("%r" % body)


if __name__ == '__main__':
    amos = AmosMsg(
        msg_user='consumer_user', 
        msg_pass='consumer_password', 
        config_path="path/to/your/config.yaml",
        enable_ssl=True, # enable SSL
    )
    amos.create_channel()
    amos.create_queue()
    amos.connect_exchange()
    amos.run_consumer(call_back)
```
config.yaml
```yaml
host: "your.rabbitmq.host"
port: 5671 # SSL default port is 5672
virtual_host: "your_virtual_host"
exchange: "your_exchange"
queue: "your_queue"
ca: "your/path/to/ca"
crt: "your/path/to/crt"
key: "your/path/to/key"
```
