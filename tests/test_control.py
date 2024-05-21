CORRECT_DATA = {
    'nome': 'Generic Name',
    'data_nasc': '08/07/2004',
    'endereco': 'Generic Address',
    'email': 'generic@mail.com',
    'tel': '88 94426422',
    'cpf': '12312312345',
    'rg': '12312312345'
}

def test_validate_form_correct_data(control_obj):
    # When/Then
    assert control_obj.validate_form(CORRECT_DATA) is None


def test_validate_form_missing_data(control_obj):
    # Given
    missing_data = CORRECT_DATA | {'rg': ''}

    # When/Then
    assert control_obj.validate_form({}) == 'Preencha todos os campos!'
    assert control_obj.validate_form(missing_data) == 'Preencha todos os campos!'


def test_validate_form_invalid_name(control_obj):
    # Given
    invalid_name_data = CORRECT_DATA | {'nome': 'Generic'}

    # When/Then
    assert control_obj.validate_form(invalid_name_data) == 'Digite seu nome completo!'


def test_validate_form_invalid_email(control_obj):
    # Given
    invalid_email_data_1 = CORRECT_DATA | {'email': 'noatsymbol.gmail.com'}
    invalid_email_data_2 = CORRECT_DATA |  {'email': 'no@domaingmailcom'}
    invalid_email_data_3 = CORRECT_DATA |  {'email': 'an@ empty.spacegmail.com'}
    invalid_email_data_4 = CORRECT_DATA |  {'email': '@.'}
    invalid_email_data_5 = CORRECT_DATA |  {'email': 'verybigemail@.' + '.' * 256}

    # When
    expected_result = 'Email inválido!'

    # Then
    assert control_obj.validate_form(invalid_email_data_1) == expected_result
    assert control_obj.validate_form(invalid_email_data_2) == expected_result
    assert control_obj.validate_form(invalid_email_data_3) == expected_result
    assert control_obj.validate_form(invalid_email_data_4) == expected_result
    assert control_obj.validate_form(invalid_email_data_5) == expected_result


def test_validate_form_invalid_tel(control_obj):
    # Given
    invalid_tel_data_1 = CORRECT_DATA | {'tel': '1'}
    invalid_tel_data_2 = CORRECT_DATA |  {'tel': '1' * 15}

    # When
    expected_result = 'Telefone inválido!'

    # Then
    assert control_obj.validate_form(invalid_tel_data_1) == expected_result
    assert control_obj.validate_form(invalid_tel_data_2) == expected_result

def test_validate_form_invalid_cpf(control_obj):
    # Given
    invalid_cpf_data_1 = CORRECT_DATA | {'cpf': '123.123.123-45'}
    invalid_cpf_data_2 = CORRECT_DATA | {'cpf': '1231231234'}

    # When/Then
    assert control_obj.validate_form(invalid_cpf_data_1) == 'Digite apenas os dígitos do CPF!'
    assert control_obj.validate_form(invalid_cpf_data_2) ==  'CPF inválido!'


def test_validate_form_invalid_rg(control_obj):
    # Given
    invalid_rg_data_1 = CORRECT_DATA | {'rg': '123123123-4'}
    invalid_rg_data_2 = CORRECT_DATA | {'rg': '123123123'}

    # When/Then
    assert control_obj.validate_form(invalid_rg_data_1) == 'Digite apenas os dígitos do RG!'
    assert control_obj.validate_form(invalid_rg_data_2) ==  'RG inválido!'


def test_check_credentials(control_obj):
    # Given
    login = 'NotCorrectLogin'
    password = 'NotCorrectPassword'

    # When/Then
    assert control_obj.check_credentials(login, password) == False
