from django.contrib.auth.models import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def loan_request_view(request):
    person_type = request.data.get('person_type')
    document = request.data.get('document')
    name = request.data.get('name')
    debt_amount = float(request.data.get('debt_amount'))
    loan_amount = float(request.data.get('loan_amount'))

    # Verificar se o nome possui o tamanho adequado
    if len(name) < 3 or len(name) > 100:
        return Response({'message': 'Nome deve ter entre 3 e 100 caracteres.'})

    # Verificar se o valor do empréstimo solicitado é maior que R$50000,00
    if loan_amount > 50000.00:
        return Response({'message': 'Empréstimo negado. Valor solicitado é maior que R$50000,00.'})

    # Verificar se o valor do empréstimo solicitado é maior que a metade da dívida ativa
    if loan_amount > (debt_amount / 2):
        return Response({'message': 'Empréstimo negado. Valor solicitado é maior que a metade da dívida ativa.'})

    # Verificar se o documento é válido de acordo com o tipo de pessoa
    if person_type == 'PF' and not validate_cpf(document):
        return Response({'message': 'CPF inválido.'})
    elif person_type == 'PJ' and not validate_cnpj(document):
        return Response({'message': 'CNPJ inválido.'})

    # Caso contrário, aprovar o empréstimo
    return Response({'message': 'Empréstimo aprovado.'})

def validate_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    sum = 0
    for i in range(9):
        sum += int(cpf[i]) * (10 - i)
    remainder = sum % 11
    digit_1 = 0 if remainder < 2 else 11 - remainder
    if int(cpf[9]) != digit_1:
        return False

    sum = 0
    for i in range(10):
        sum += int(cpf[i]) * (11 - i)
    remainder = sum % 11
    digit_2 = 0 if remainder < 2 else 11 - remainder
    if int(cpf[10]) != digit_2:
        return False

    return True


def validate_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))

    if len(cnpj) != 14:
        return False

    if cnpj == cnpj[0] * 14:
        return False

    sum = 0
    weight = 5
    for i in range(12):
        sum += int(cnpj[i]) * weight
        weight = 9 if weight == 2 else weight - 1
    remainder = sum % 11
    digit_1 = 0 if remainder < 2 else 11 - remainder
    if int(cnpj[12]) != digit_1:
        return False

    sum = 0
    weight = 6
    for i in range(13):
        sum += int(cnpj[i]) * weight
        weight = 9 if weight == 2 else weight - 1
    remainder = sum % 11
    digit_2 = 0 if remainder < 2 else 11 - remainder
    if int(cnpj[13]) != digit_2:
        return False

    return True
