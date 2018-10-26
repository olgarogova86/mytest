import csv
import os


class BaseCar:
    def __init__(self, car_type=None, photo_file_name=None, brand=None, carrying=0.0):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        result = os.path.splitext(self.photo_file_name)
        return result[1]


class Car(BaseCar):
    def __init__(self, car_type=None, photo_file_ext=None, brand=None, carrying=0.0, passenger_seats_count=0):
        super().__init__(car_type, photo_file_ext, brand, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(BaseCar):
    def __init__(self, car_type=None, photo_file_ext=None, body_params=None, brand=None, carrying=0.0):
        super().__init__(car_type, photo_file_ext, brand, carrying)
        self._body_params = body_params
        _body_whl = self._set_params(self._body_params)
        self.body_length = _body_whl[0]
        self.body_width = _body_whl[1]
        self.body_height = _body_whl[2]

    @staticmethod
    def _set_params(body_whl):
        try:
            return list(map(float, (body_whl.split('x'))))
        except ValueError:
            return [0.0]*3

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(BaseCar):
    def __init__(self, car_type=None, photo_file_ext=None, brand=None, carrying=0.0, extra=None):
        super().__init__(car_type, photo_file_ext, brand, carrying)
        self.extra = extra


class NewCar:
    def __init__(self, car):
        self._car_type = car[0]
        self._brand = car[1]
        self._passenger_seats_count = car[2]
        self._photo_file_name = car[3]
        self._body_whl = car[4]
        self._carrying = car[5]
        self._extra = car[6]
        self._new_car = None

        if self._car_type == 'car':
            self._new_car = Car(self._car_type, self._photo_file_name, self._brand, self._carrying,
                                self._passenger_seats_count)
        elif self._car_type == 'spec_machine':
            self._new_car = SpecMachine(self._car_type, self._photo_file_name, self._brand, self._carrying, self._extra)
        else:
            self._new_car = Truck(self._car_type, self._photo_file_name, self._body_whl, self._brand, self._carrying)

    @property
    def new_car(self):
        return self._new_car


class ImportCSV:
    def __init__(self, path=None):
        self.path = path
        self._csv_data = []

    def read(self):
        with open(self.path) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                self._csv_data.append(row)
        return self._csv_data


def get_car_list(csv_filename):
    list_of_cars = []
    importer = ImportCSV(csv_filename)
    cars = importer.read()
    for car in cars:
        try:
            new_car = NewCar(car).new_car
            list_of_cars.append(new_car)
        except IndexError:
            pass
    return list_of_cars

#print(Truck("car","1.jpg","1x2x3","b","2.1").__dict__)
#print(Car("carcar","2.jpg","b","2.5","1").__dict__)