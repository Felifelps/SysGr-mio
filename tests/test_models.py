from source.models import db, Cliente

def test_db_connection():
    assert db.is_closed() is False

def test_table_creation():
    assert db.table_exists('cliente')
    assert db.table_exists('data')

def test_cliente_model():
    cliente = Cliente(
        nome='John Doe',
        data_nasc='1990-01-01',
        tel='1234567890',
        email='johndoe@example.com',
        endereco='123 Main St',
        cpf='12345678909',
        rg='1234567890'
    )
    cliente.save()
    cliente_id = getattr(cliente, 'id')
    assert str(cliente) == 'John Doe'
    assert cliente.get_data() == {
        'id': cliente_id,
        'nome': 'John Doe',
        'data_nasc': '1990-01-01',
        'tel': '1234567890',
        'email': 'johndoe@example.com',
        'endereco': '123 Main St',
        'cpf': '12345678909',
        'rg': '1234567890'
    }
    cliente.delete_instance()
    assert Cliente.get_or_none(id=cliente_id) is None