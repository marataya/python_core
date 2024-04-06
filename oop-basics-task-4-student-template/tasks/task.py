class HistoryDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history = []

    def set_value(self, key, value):
        self[key] = value
        self.history.append(key)
        if len(self.history) > 5:
            self.history.pop(0)

    def get_history(self):
        return self.history

if __name__ == '__main__':
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    print(d.get_history())
