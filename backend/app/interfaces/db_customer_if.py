""" DB Customer Interface Thingy """


from app.types.my_types import NewCustomerTup
from app.extensions import db
from app.models import  Customer


class DBCustomerI:
    """ Customer Interface """

    def get_all(self)->list[Customer]:
        result: list[Customer] = Customer.query.all()  # type: ignore[misc]
        return result

    def new_customer(self,new_customer:NewCustomerTup)->Customer:

        new_customer_db = Customer(
                project_id = new_customer.project_id,
        )

        db.session.add(new_customer_db) # type: ignore[misc] # pylint: disable=no-member
        db.session.commit() # type: ignore[misc] # pylint: disable=no-member
        db.session.refresh(new_customer_db) # type: ignore[misc]
        return new_customer_db