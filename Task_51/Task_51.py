#�������� ������� same_by(characteristic, objects), ������� 
#���������, ��� �� ������� ����� ���������� �������� 
#��������� ��������������, � ���������� True, ���� ��� ���. 
#���� �������� �������������� ��� ������ �������� 
#���������� - �� False. ��� ������� ������ ��������, ������� 
#������ ���������� True. �������� characteristic - ��� 
#�������, ������� ��������� ������ � ��������� ��� 
#��������������.


def same_by(characteristic, objects):
    list_values=[characteristic(obj) for obj in objects ]#������ �����������
    return all(value for value in list_values)#��� ���������� � ������ = True


values = [0, 2, 10, 6]#������ �������� ��� ��������
characteristic=lambda x:x%2==0 #������� ��������(��������� ����)


if same_by(characteristic, values):
    print('same')
else:
    print('different')


     