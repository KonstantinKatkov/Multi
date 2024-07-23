from multiprocessing import Pool, Manager

class WarehouseManager:
    def __init__(self):
        managers = Manager()
        self.data = managers.dict()
    def process_request(self, request):
        for i in request:
            product, action, amount = i
           
            if action == 'receipt':
                if product in self.data:
                    self.data[product] += amount
                else:
                    self.data[product] = amount
            elif action == 'shipment':
                if product in self.data and self.data[product] >= amount:
                    self.data[product] -= amount

    def run(self, request):
        with Pool(processes=2) as pool:
            result = pool.map(self.process_request, [request])

if __name__ == '__main__':
    manager = WarehouseManager()
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    manager.run(requests)
    print(manager.data)