class Config:
    _use_remote = False
    _host = 'localhost'
    _port = 8086

    @staticmethod
    def set_remote(flag):
        Config._use_remote = flag

    @staticmethod
    def set_host(value):
        Config._host = value

    @staticmethod
    def get_host():
        return Config._host

    @staticmethod
    def get_port():
        return Config._port
    
    @staticmethod
    def set_port(port):
        Config.port = port

    @staticmethod
    def is_remote():
        return Config._use_remote
