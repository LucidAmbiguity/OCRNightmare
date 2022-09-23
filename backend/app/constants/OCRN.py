""" Constants for the AUTH Codes """
# # System Codes
# pylint: disable=invalid-name




from app.types import ApiResp



class OCRN:
    Realm = ApiResp('OCRN0001', 'OCRN by Lucid Ambiguity')
    ROOT =  ApiResp('OCRN0002', 'OCRN Main Application Root')
    Projects =  ApiResp('OCRN0003', 'OCRN Projects List')
    Project_ =  ApiResp('OCRN0004',  lambda x: f'Project {x} : Information')
    FAILinForm =  ApiResp('OCRN0005', 'FAIL form validation. PDF files only also be sure you selected/submitted a file for upload')
    FAILinDir = ApiResp('OCRN0006', 'Project or Filename already exists in filesystem rename your file or click home to start again')
    FAILinDB = ApiResp('OCRN0007', 'Project or Filename already exists in database rename your file or click home to start again')
    FAILinCreate = ApiResp('OCRN0008', 'Project or Filename already exists in database rename your file or click home to start again')
    S_C_Proj_ = ApiResp('OCRN00009', lambda x: f'Project {x} Has been created')

    class Extract:
        ROOT =  ApiResp('OCRN0010', 'OCRN Project Extract Root')


    # UserDel_ = ApiResp('OCRN0001', lambda x: f'User {x} : Has been deleted')
    # # UserDel_: tuple[str, Callable[[str],str]] = ('OCRN0001', lambda x: f'User {x} : Has been deleted')
