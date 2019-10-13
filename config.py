class Config:
    '''
    General Configuration parent class
    '''
    pass


class ProdConfig(Config):
    '''
    production configuration child class

    Args:
        Config: parent configuration class with general configuration
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True