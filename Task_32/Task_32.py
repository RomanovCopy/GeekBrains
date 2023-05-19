#���������� ������� ��������� ������� (������),
#�������� ������� ����������� ��������� ��������� (�.�. ��
#������ ��������� �������� � �� ������ ���������
#���������)


from random import randint


array=list(map(lambda x: randint(-100,100), range(20)))
print(array)


def find_indexes1(arr, min_val, max_val):
    indexes = []
    is_in_range = lambda x: min_val <= x <= max_val
    for i in range(len(arr)):
        if is_in_range(arr[i]):
            indexes.append(i)
    return indexes

def find_indexes2(arr, min_val, max_val):
    indexes = []
    filtered_arr = list(filter(lambda x: min_val <= x <= max_val, arr))
    for i in range(len(arr)):
        if arr[i] in filtered_arr:
            indexes.append(i)
    return indexes

min_val = 1
max_val = 100
indexes = find_indexes1(array, min_val, max_val)
print(indexes) 


indexes = find_indexes2(array, min_val, max_val)
print(indexes)