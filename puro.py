from math import inf as infinity


class PuroAlgorithm:
    objects = []
    D_max = 0
    expert_count = 0

    def one_expert_ranking_filling_manually(self, expert_number: int):
        print(f'Даны объекты {self.objects}. Провести ранжирование для эксперта {expert_number + 1}')
        one_expert_ranking = []
        for i in range(1, len(self.objects) + 1):
            val = input(f'{i}. ')
            if val in self.objects and val not in one_expert_ranking:
                one_expert_ranking.append(val)
            elif val not in self.objects:
                print('Объект не входит в список')
                return self.one_expert_ranking_filling_manually(expert_number)
            else:
                print('Объект уже был указан')
                return self.one_expert_ranking_filling_manually(expert_number)
        return one_expert_ranking

    def forming_ordering_matrix(self, one_expert_ranking: list):
        ordering_matrix = []
        for obj1 in self.objects:
            raw = []
            for obj2 in self.objects:
                if obj1 == obj2:
                    raw.append(0)
                elif one_expert_ranking.index(obj1) < one_expert_ranking.index(obj2):
                    raw.append(1)
                elif one_expert_ranking.index(obj1) > one_expert_ranking.index(obj2):
                    raw.append(-1)
            ordering_matrix.append(raw)
        for i in range(len(self.objects)):
            if i == 0:
                print("\t"+self.objects[i], end='\t')
            else:
                print(self.objects[i], end='\t')
        print('\n')
        for i in range(len(ordering_matrix)):
            print(self.objects[i], end="\t")
            for j in range(len(ordering_matrix[i])):
                print(ordering_matrix[i][j], end="\t")
            print("\n")
        return ordering_matrix

    def forming_difference_matrix(self, order_matrices: list):
        min_dif = infinity
        dif_sum = 0
        dif_matrix = []
        for i in range(self.expert_count):
            if i == 0:
                print("\tЭ1", end='\t')
            else:
                print(f"Э{i+1}", end='\t')
        print("\n")
        for i in range(self.expert_count):
            raw = []
            raw_sq_sum = 0
            print(f"Э{i + 1}", end='\t')
            for j in range(self.expert_count):
                dif = self.kemeni(order_matrices[i], order_matrices[j])
                print(dif, end="\t")
                raw.append(dif)
                raw_sq_sum += dif ** 2
                dif_sum += dif
            if raw_sq_sum < min_dif:
                min_dif = raw_sq_sum
            print("\n")
            dif_matrix.append(raw)
        return dif_matrix

    def create_relationship_graph(self, matrix: list):
        dporog = infinity
        m = []
        for i in range(self.expert_count):
            if i == 0:
                print("\tЭ1", end='\t')
            else:
                print(f"Э{i+1}", end='\t')
        print("\n")
        for i in range(self.expert_count):
            raw = []
            print(f"Э{i + 1}", end='\t')
            for j in range(self.expert_count):
                tmp = round(matrix[i][j] / self.D_max, 2)
                if len(str(tmp == 4)):
                    print(str(tmp), end=' ')
                else:
                    print(str(tmp), end='\t')
                raw.append(tmp)

                if 0 < tmp < dporog:
                    dporog = tmp
            print("\n")
            m.append(raw)
        print(f"d porog = {dporog} \n")
        for i in range(self.expert_count):
            if i == 0:
                print("\tЭ1", end='\t')
            else:
                print(f"Э{i+1}", end='\t')
        print("\n")
        for i in range(self.expert_count):
            raw = []
            print(f"Э{i + 1}", end='\t')
            for j in range(self.expert_count):
                if 0 < m[i][j] <= dporog:
                    raw.append(1)
                    print(1, end='\t')
                else:
                    raw.append(0)
                    print(0, end='\t')
            print("\n")

    def kemeni(self, matrix_1, matrix_2):
        if matrix_1 == matrix_2:
            return 0
        else:
            difference = 0
            for i in range(len(matrix_1)):
                for j in range(len(matrix_1[0])):
                    difference += abs(matrix_1[i][j] - matrix_2[i][j])
            return difference // 2

    def main(self, filling_choice, file_name=None):
        ranking_of_experts = []
        if filling_choice == 1:
            self.objects = input('Исходные объекты в строчку:').split()
            self.expert_count = int(input('Количество экспертов: '))
            for k in range(self.expert_count):
                ranking_of_experts.append(self.one_expert_ranking_filling_manually(k))
        else:
            with open(file_name) as file:
                lines = file.readlines()
                self.objects = lines.pop(0).strip().split()
                self.D_max = len(self.objects) * (len(self.objects) - 1)
                self.expert_count = len(lines)
                for line in lines:
                    ranking_of_experts.append(line.strip().split())
        order_matrices = []
        for k in range(self.expert_count):
            print(f'Матрица ранжирования эксперта {k + 1}')
            order_matrices.append(self.forming_ordering_matrix(ranking_of_experts[k]))
        dm = self.forming_difference_matrix(order_matrices)
        self.create_relationship_graph(dm)


def action_choice():
    variant = input("1.Провести следующий тур.\n2.Завершить работу программы.\nНомер действия:")
    if variant == "1":
        return 1
    if variant == "2":
        return 0
    else:
        print("Такого варианта нет")
        return action_choice()


def filling_choice():
    variant = input("1.Заполнить вручную.\n2.Извлечь данные из файла.\nНомер действия:")
    if variant == "1":
        return 1
    if variant == "2":
        return 2
    else:
        print("Такого варианта нет")
        return filling_choice()


if __name__ == '__main__':
    p = PuroAlgorithm()
    fl = 1
    while fl:
        selection = filling_choice()
        p.main(selection, 'test_data_puro.txt')
        fl = action_choice()

# b a c d h
# c b a h d
# c b a d h
