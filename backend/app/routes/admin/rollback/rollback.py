"""ocrnightmare Admin API Rollback Route Controller"""


from app.routes.admin._my_format import _my_format
from app.routes.admin.rollback import rollback

from app.interfaces.db_project_rollback_if import DBProjRollbackInterface
from app.constants.ADMIN import ADMIN

Rollback = ADMIN.Rollback

@rollback.route('', methods=['GET', 'POST'])  # type: ignore[attr-defined,misc]
def home():
    return 'hello world'

@rollback.route('/<proj_name>/delete/0', methods=['DELETE']) # type: ignore[attr-defined,misc]
def delete_project_by_name(proj_name:str)->dict:
    """ Delete Project and source material"""

    db_int = DBProjRollbackInterface()
    success = db_int.del_proj_by_name(proj_name)
    if success:
        return _my_format(Rollback.Delete_,code=200,x=proj_name)

    return _my_format(Rollback.Error_,code=200,x=proj_name)

@rollback.route('/<proj_name>/rollback/1', methods=['DELETE']) # type: ignore[attr-defined,misc]
def rollback_from_1(proj_name:str)->dict:
    """ old tutorial function"""

    proj_int = DBProjRollbackInterface()
    success = proj_int.rollback_from_1(proj_name)
    if success:
        return _my_format(Rollback.RB_1_,code=200,x=proj_name)

    return _my_format(Rollback.Error_,code=200,x=proj_name)



# @rollback.route('/<proj_name>/rollback/2', methods=['DELETE']) # type: ignore[attr-defined,misc]
# def rollback_from_2(proj_name:str)->dict:
#     """ old tutorial function"""

#     success = False
#     proj_int = DBProjRollbackInterface(proj_name)
#     success = proj_int.rollback_from_2()

#     return _my_format(
#         success,
#         m_code='RB0002',
#         m_text=f'Roll Back {proj_name} from 2: Successful.',
#     )

# @rollback.route('/<proj_name>/rollback/3', methods=['DELETE']) # type: ignore[attr-defined,misc]
# def rollback_from_3(proj_name:str)->dict:
#     """ old tutorial function"""

#     success = False
#     proj_int = DBProjRollbackInterface(proj_name)
#     success = proj_int.rollback_from_3()

#     return _my_format(
#         success,
#         m_code='RB0003',
#         m_text=f'Roll Back {proj_name} from 3: Successful.',
#     )

# @rollback.route('/<proj_name>/rollback/4', methods=['DELETE']) # type: ignore[attr-defined,misc]
# def rollback_from_4(proj_name:str)->dict:
#     """ old tutorial function"""

#     success = False
#     proj_int = DBProjRollbackInterface(proj_name)
#     success = proj_int.rollback_from_4()

#     return _my_format(
#         success,
#         m_code='RB0004',
#         m_text=f'Roll Back {proj_name} from 4: Successful.',
#     )

# @rollback.route('/<proj_name>/rollback/5', methods=['DELETE']) # type: ignore[attr-defined,misc]
# def rollback_from_5(proj_name:str)->dict:
#     """ old tutorial function"""

#     success = False
#     proj_int = DBProjRollbackInterface(proj_name)
#     success = proj_int.rollback_from_5()

#     return _my_format(
#         success,
#         m_code='RB0005',
#         m_text=f'Roll Back {proj_name} from 5: Successful.',
#     )

# @rollback.route('/<proj_name>/rollback/6', methods=['DELETE']) # type: ignore[attr-defined,misc]
# def rollback_from_6(proj_name:str)->dict:
#     """ old tutorial function"""

#     success = False
#     proj_int = DBProjRollbackInterface(proj_name)
#     success = proj_int.rollback_from_6()

#     return _my_format(
#         success,
#         m_code='RB0006',
#         m_text=f'Roll Back {proj_name} from 6: Successful.',
#     )

# @rollback.route('/<proj_name>/rollback/7', methods=['DELETE']) # type: ignore[attr-defined,misc]
# def rollback_from_7(proj_name:str)->dict:
#     """ old tutorial function"""

#     success = False
#     proj_int = DBProjRollbackInterface(proj_name)
#     success = proj_int.rollback_from_7()

#     return _my_format(
#         success,
#         m_code='RB0007',
#         m_text=f'Roll Back {proj_name} from 7: Successful.',
#     )


# @rollback.route('/<proj_name>/rollback/form_data', methods=['DELETE']) # type: ignore[attr-defined,misc]
# def rollback_form_data(proj_name:str)->dict:
#     """ old tutorial function"""

#     success = False
#     proj_int = DBProjRollbackInterface(proj_name)
#     success = proj_int.rollback_form_data()

#     return _my_format(
#         success,
#         m_code='D00002',
#         m_text=f'Roll Back {proj_name} Successful.',
#     )

