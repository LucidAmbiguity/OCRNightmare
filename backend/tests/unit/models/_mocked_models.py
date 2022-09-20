"""Mocked Models"""


from unittest.mock import patch
import pytest

from app.types.my_types import NewUserTup
from app.interfaces.db_user_if import DBUserI
from app.interfaces.db_project_if import DBProjI
from app.types.my_types import NewProjTup
from app.interfaces.db_page_if import DBPageI
from app.models.models import Page
from app.types.my_types import NewPageTup
from app.interfaces.db_customer_if import DBCustomerI
from app.models.models import Customer
from app.types.my_types import NewCustomerTup



@pytest.fixture(scope='module')
@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
@patch('uuid.uuid4', return_value = '1b6dd37d-37f1-41c0-a441-c644f2d9525c')
def new_user1(m_u,m_dba,m_dbc,m_dbr):  # pylint: disable=unused-argument
    """
    Returns:
        User: User model with mock data
    """

    username,password = 'Rufus', '!password123'
    nut=NewUserTup(None,username,password,None)
    new_user = DBUserI().new_user(nut)
    new_user.id = 1
    print('mocked new_user1',new_user.id,new_user.public_id,new_user.password,new_user.admin)
    return new_user

@pytest.fixture(scope='module')
@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
@patch('app.models.models.uuid.uuid4', return_value = '4aac1ea8-f877-473e-b38b-e7bf27747c17')
def new_user2(m_u,m_dba,m_dbc,m_dbr):  # pylint: disable=unused-argument
    """
    Returns:
        User: User model with mock data
    """

    username,password = 'Murphy', '!password123'
    nut=NewUserTup(None,username,password,None)
    new_user = DBUserI().new_user(nut)
    new_user.id = 2
    print('mocked new_user1',new_user.id,new_user.public_id,new_user.password,new_user.admin)
    return new_user


@pytest.fixture(scope='module')
@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
def new_proj_1(m_dba,m_dbc,m_dbr):  # pylint: disable=unused-argument
    """
    Returns:
        Project: Project model with mock data
    """

    project_name, filename = 'filename', 'filename.pdf'
    new_project_tuple = NewProjTup(project_name, filename, 0)
    new_project = DBProjI().new_project(new_project_tuple)
    new_project.id = 1
    print('mocked new_proj_1',new_project.id,new_project.name,new_project.status,new_project.filename,new_project.pages,new_project.customers)
    return new_project


@pytest.fixture(scope='module')
@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
def new_proj_2(m_dba,m_dbc,m_dbr):  # pylint: disable=unused-argument
    """
    Returns:
        Project: Project model with mock data
    """

    project_name, filename = 'proj210304', 'proj210304.pdf'
    new_project_tuple = NewProjTup(project_name, filename, 1)
    new_project = DBProjI().new_project(new_project_tuple)
    new_project.id = 2
    print('mocked new_proj_1',new_project.id,new_project.name,new_project.status,new_project.filename,new_project.pages,new_project.customers)
    return new_project


@pytest.fixture(scope='module')
@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
def new_page_1(m_dba,m_dbc,m_dbr):  # pylint: disable=unused-argument
    """
    Returns:
        Page: Page model with mock data
    """

    project_id = 1
    new_page_tuple = NewPageTup(project_id)
    new_page = DBPageI().new_page(new_page_tuple)
    assert new_page.project_id == project_id
    assert isinstance(new_page,Page)
    new_page.id = 1
    print('mocked new_page_1',new_page.id,new_page.project_id )
    return new_page

@pytest.fixture(scope='module')
@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
def new_page_2(m_dba,m_dbc,m_dbr):  # pylint: disable=unused-argument
    """
    Returns:
        Page: Page model with mock data
    """

    project_id = 1
    new_page_tuple = NewPageTup(project_id)
    new_page = DBPageI().new_page(new_page_tuple)
    assert new_page.project_id == project_id
    assert isinstance(new_page,Page)
    new_page.id = 2
    print('mocked new_page_1',new_page.id,new_page.project_id )
    return new_page


@pytest.fixture(scope='module')
@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
def new_customer_1(m_dba,m_dbc,m_dbr):  # pylint: disable=unused-argument
    """
    Returns:
        Customer: Customer model with mock data
    """

    project_id = 1
    new_customer_tuple = NewCustomerTup(project_id)
    new_customer = DBCustomerI().new_customer(new_customer_tuple)
    assert new_customer.project_id == project_id
    assert isinstance(new_customer,Customer)
    new_customer.id = 1
    print('mocked new_customer_1',new_customer.id,new_customer.project_id )
    return new_customer

@pytest.fixture(scope='module')
@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
def new_customer_2(m_dba,m_dbc,m_dbr):  # pylint: disable=unused-argument
    """
    Returns:
        Customer: Customer model with mock data
    """

    project_id = 1
    new_customer_tuple = NewCustomerTup(project_id)
    new_customer = DBCustomerI().new_customer(new_customer_tuple)
    assert new_customer.project_id == project_id
    assert isinstance(new_customer,Customer)
    new_customer.id = 2
    print('mocked new_customer_1',new_customer.id,new_customer.project_id )
    return new_customer
