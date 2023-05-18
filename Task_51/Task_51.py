#�������� ������� same_by(characteristic, objects), ������� 
#���������, ��� �� ������� ����� ���������� �������� 
#��������� ��������������, � ���������� True, ���� ��� ���. 
#���� �������� �������������� ��� ������ �������� 
#���������� - �� False. ��� ������� ������ ��������, ������� 
#������ ���������� True. �������� characteristic - ��� 
#�������, ������� ��������� ������ � ��������� ��� 
#��������������.

values = [0, 1, 2, 10, 6]

def same_by(characteristic, objects):
    list_values=[characteristic(obj) for obj in objects ]
    return all(value for value in list_values)

characteristic=lambda x:x%2==0

if same_by(characteristic, values):
    print('same')
else:
    print('different')


     