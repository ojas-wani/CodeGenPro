class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * (n + 1)
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        result = []
        while self.stream[idKey] != "":
            result.append(self.stream[idKey])
            idKey += 1
        return result