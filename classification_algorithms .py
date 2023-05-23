from math import inf
from math import sqrt


def division_into_classes(file_name, classes_count):
    with open(file_name) as file:
        file_data = [[int(element) for element in line.split()] for line in file.readlines()]
    max_value_in_last_column = -inf
    for raw in file_data:
        if raw[-1] > max_value_in_last_column:
            max_value_in_last_column = raw[-1]
    classes_dict = {}
    for raw in file_data:
        k = 1
        while k <= classes_count:
            #print(raw[-1], max_value_in_last_column / classes_count * k)
            if raw[-1] > max_value_in_last_column / classes_count * k:
                k += 1
            else:
                break
        if k in classes_dict.keys():
            classes_dict[k].append(raw)
        else:
            classes_dict[k] = [raw]
    for k in range(1, classes_count+1):
        coords = []
        for j in range(len(classes_dict[k][0])-1):
            coords.append(sum([arr[j] for arr in classes_dict[k]])/classes_count)
        classes_dict[k] = coords
    return classes_dict


class _Class:
    name = ""
    coords = []

    def __init__(self, name, coords):
        self.name = name
        self.coords = coords


class _Object:
    name = ""
    coords = []

    def __init__(self, name, coords):
        self.name = name
        self.coords = coords


class ClassificationAlgorithms:
    classes = []
    objects = []
    length = 0

    def __init__(self, _classes, _objects):
        self.classes = _classes
        self.objects = _objects
        self.length = len(_objects[0].coords)

    def distance(self, cls, obj):
        return sqrt(sum([(obj.coords[i] - cls.coords[i]) ** 2 for i in range(self.length)]))

    def distance_calculation_output(self, cls, obj):
        calculations = f"p({cls.name}, {obj.name}) = √"
        for i in range(self.length):
            calculations += f"({obj.coords[i]}-{cls.coords[i]})**2 +"
        result = sqrt(sum([(obj.coords[i] - cls.coords[i]) ** 2 for i in range(self.length)]))
        calculations = calculations[:len(calculations) - 1]
        calculations += f"= {result}"
        print(calculations)

    def distances(self):
        for obj in self.objects:
            min_distance = inf
            min_classes = []
            for cls in self.classes:
                distance = self.distance(cls, obj)
                if distance < min_distance:
                    min_classes.clear()
                    min_classes.append(cls.name)
                    min_distance = distance
                elif distance == min_distance:
                    min_classes.append(cls.name)
            print(f'Объект {obj.name} принадлежит классу {min_classes}')

    def scalar_product(self, cls, obj):
        return sum([obj.coords[i] * cls.coords[i] for i in range(self.length)])

    def scalar_product_calculation_output(self, cls, obj):
        calculations = f"b({cls.name}, {obj.name}) = "
        for i in range(self.length):
            calculations += f"{obj.coords[i]}*{cls.coords[i]} +"
        result = sum([obj.coords[i] * cls.coords[i] for i in range(self.length)])
        calculations = calculations[:len(calculations) - 1]
        calculations += f"= {result}"
        print(calculations)

    def scalar_products(self):
        for obj in self.objects:
            max_prod = -inf
            max_classes = []
            for cls in self.classes:
                scalar_prod = self.scalar_product(cls, obj)
                if scalar_prod > max_prod:
                    max_classes.clear()
                    max_classes.append(cls.name)
                    max_prod = scalar_prod
                elif scalar_prod == max_prod:
                    max_classes.append(cls.name)
            print(f'Объект {obj.name} принадлежит классу {max_classes}')

    def r(self, cls, obj):
        return self.scalar_product(cls, obj) - (sum(cls.coords) * sum(obj.coords) / self.length)

    def r_calculation_output(self, cls, obj):
        coords_sum_1 = "("
        for coord in cls.coords:
            coords_sum_1 += f"{str(coord)} +"
        coords_sum_1 = coords_sum_1[:len(coords_sum_1) - 1] + ")"
        coords_sum_2 = "("
        for coord in cls.coords:
            coords_sum_2 += f"{str(coord)} +"
        coords_sum_2 = coords_sum_2[:len(coords_sum_2) - 1] + ")"
        print(f"r({cls.name}, {obj.name}) = {self.scalar_product(cls, obj)} - "
              f"({coords_sum_1}*{coords_sum_2}/{self.length})")

    def correlation_methods(self):
        for obj in self.objects:
            max_r = -inf
            max_classes = []
            for cls in self.classes:
                r = self.r(cls, obj)
                if r > max_r:
                    max_classes.clear()
                    max_classes.append(cls.name)
                    max_r = r
                elif r == max_r:
                    max_classes.append(cls.name)
            print(f'Объект {obj.name} принадлежит классу {max_classes}')

    def main(self):
        print("\nКлассификация по расстояниям объектов от центров тяжести классов\n")
        self.distances()
        print("\nКлассификация по скалярным произведениям\n")
        self.scalar_products()
        print("\nКлассификация с использованием корреляционного метода\n")
        self.correlation_methods()


if __name__ == '__main__':
    n = int(input("Количество классов: "))
    cls_dict = division_into_classes('test_data_ca.txt', n)
    classes = []
    objects = []
    print("------\nКлассы\n------")
    for i in range(n):
        class_name = input("Имя класса:")
        #class_coords = cls_dict[i+1]
        class_coords = list(map(int, input(f"Координаты класса {class_name}:").split()))
        classes.append(_Class(class_name, class_coords))
    print("--------\nОбъекты\n--------")
    m = int(input("Количество объектов: "))
    for i in range(m):
        obj_name = f'M{i + 1}'  # input("Имя объекта:")
        obj_coords = list(map(int, input(f"Координаты объекта {obj_name}:").split()))
        objects.append(_Object(obj_name, obj_coords))

    algs = ClassificationAlgorithms(classes, objects)
    algs.main()
