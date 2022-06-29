# """test scratch pad
#     a place for uncategorized feature  tests
#     Will likely be moved in refactor phase 
# """

# # def test_():
# #   assert True

# """Test the default home route '/'"""

# from app import create_app


# def test_home_page_get():
#     """
#     GIVEN a Flask application
#     WHEN the '/' page is requested (GET)
#     THEN check that a '200' status code is returned

#     """

#     # created_app = create_app(test_config=True)
#     created_app = create_app()

#     with created_app.test_client() as testing_client:
#         # Establish an application context
#         with created_app.app_context():
#             response = testing_client.get('/')
#             print(response.json)
#             assert response.status_code == 200
#             assert b"Microblog" not in response.data
#             assert b"Index Page" in response.data


