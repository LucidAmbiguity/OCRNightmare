"""Model Unit TEST FILE"""
# pylint: disable=invalid-name


from unittest.mock import patch
from app.models import Customer, customer_schema, customers_schema
from app.interfaces.db_customer_if import DBCustomerI
from app.types.my_types import NewCustomerTup

from tests.helpers import attr_counter


def test_customer_has_expected_attributes():
    """test Customer() has expected attributes"""
    customer = Customer()
    assert hasattr(customer,'id')
    assert hasattr(customer,'project_id')
    assert hasattr(customer,'project')
    # query can only be checked within an app context the others come
    # with sqlalchemy
    # those above are user defined
    ## attr_counter counts query however looking at
    ## it triggers deep sql-alchemy code
    # assert hasattr(customer,'query')
    assert hasattr(customer,'metadata')
    assert hasattr(customer,'query_class')
    assert hasattr(customer,'registry')
    attr_count = attr_counter(customer)
    assert attr_count == 7  # count check will fail if attributes added to model.  # pylint: disable=line-too-long


@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
def test_customer_interface_returns_Customer(a,b,c): # pylint: disable=unused-argument
    project_id = 1
    new_customer_tuple = NewCustomerTup(project_id)
    new_customer = DBCustomerI().new_customer(new_customer_tuple)
    assert new_customer.project_id == project_id
    assert isinstance(new_customer,Customer)


def test_customer_schema(new_customer_1):
    """test text line schema"""

    assert customer_schema.dump(new_customer_1) == {'id': 1, 'project_id': 1}

def test_customers_schema(new_customer_1,new_customer_2):
    """test text lines schema"""
     # pylint: disable=line-too-long
    customers = [new_customer_1,new_customer_2]
    print(customers)
    assert customers_schema.dump(customers) == [
      {'id': 1, 'project_id': 1},
      {'id': 2, 'project_id': 1},
    ]
