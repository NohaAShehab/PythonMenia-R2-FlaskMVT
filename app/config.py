

## developemt , production
class Config:
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"


class ProductionConfig(Config):
    DEBUG= False
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"



projectConfig= {
    'dev': DevelopmentConfig,
    'prd': ProductionConfig
}