from . import *


class AmosMsg:
    __host = None
    __port = None
    __v_host = None
    __exchange = None
    __queue = None

    __ca = None
    __crt = None
    __key = None
    __msg_connection = None
    __queue_name = None

    def __init__(self, msg_user, msg_pass, config_path=None, enable_ssl=False,
                 host=None, port=None, v_host=None, exchange=None, queue=None,
                 ca=None, crt=None, key=None
                 ):
        self.msg_user = msg_user
        self.msg_pass = msg_pass
        self.config_path = config_path
        self.enable_ssl = enable_ssl
        if not config_path:
            self.__host = host
            self.__port = port
            self.__v_host = v_host
            self.__exchange = exchange
            self.__queue = queue
            if enable_ssl:
                self.__ca = ca
                self.__crt = crt
                self.__key = key

    def __load_config(self):
        if self.config_path:
            try:
                with open(self.config_path, 'r') as config_reader:
                    conf = yaml.full_load(config_reader)
                    self.__host = conf['host']
                    self.__port = conf['port']
                    self.__v_host = conf['virtual_host']
                    self.__exchange = conf['exchange']
                    self.__queue = conf['queue']
                    if self.enable_ssl:
                        self.__ca = conf['ca']
                        self.__crt = conf['crt']
                        self.__key = conf['key']
            except FileNotFoundError:
                print("Please Check File of {0} exist!".format(self.config_path))
            except KeyError as e:
                print("Please check key of {0} in yaml file".format(e))

    def create_channel(self):
        if self.config_path:
            self.__load_config()
        credentials = pika.PlainCredentials(self.msg_user, self.msg_pass)
        if self.enable_ssl:
            context = ssl.create_default_context(cafile=self.__ca)
            context.load_cert_chain(self.__crt, self.__key)
            ssl_options = pika.SSLOptions(context, self.__host)
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=self.__host,
                    port=self.__port,
                    virtual_host=self.__v_host,
                    ssl_options=ssl_options,
                    credentials=credentials,
                )
            )

        else:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=self.__host,
                    port=self.__port,
                    virtual_host=self.__v_host,
                    credentials=credentials,
                )
            )
        self.__msg_connection = connection.channel()

    def create_queue(self, is_durable=False):
        result = self.__msg_connection.queue_declare(queue=self.__queue, durable=is_durable)
        self.__queue_name = result.method.queue

    def connect_exchange(self):
        self.__msg_connection.queue_bind(exchange=self.__exchange, queue=self.__queue_name)

    def run_consumer(self, func):
        self.__msg_connection.basic_consume(queue=self.__queue_name, on_message_callback=func)
        try:
            self.__msg_connection.start_consuming()
        except KeyboardInterrupt:
            print("Consumer is Stopped by manually")

