class Sun:
    _instance = None  # Private class attribute to store the singleton instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def inst(cls):
        """Method to access the singleton instance"""
        if not cls._instance:
            cls._instance = cls()
        return cls._instance
