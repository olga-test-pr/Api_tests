import json
import allure
from requests import Response
from utils.checking import Checking
from utils.api import Google_maps_api


#Create, update and delete new location
@allure.epic("Test_create_location")
class Test_create_location():

    @allure.description("Create, update and delete new location")
    def test_create_new_location(self):
        print("POST")
        result_post: Response = Google_maps_api.create_new_location()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        print(result_post.status_code)
        Checking.check_json_token(result_post,['status', 'place_id', 'scope', 'reference', 'id'])
        token = json.loads(result_post.text)
        print(list(token))
        Checking.check_json_value(result_post,'status','OK')
        print("GET POST")
        result_get: Response = Google_maps_api.get_new_location(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
        print("PUT")
        result_put: Response = Google_maps_api.put_new_location(place_id)
        Checking.check_status_code(result_put, 200)
        # print(result_put.status_code)
        Checking.check_json_token(result_put,['msg'])
        token = json.loads(result_put.text)
        print(list(token))
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')
        print("GET PUT")
        result_get: Response = Google_maps_api.get_new_location(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Checking.check_json_value(result_get, 'address', '121 33 Johannesh, SE')
        print("DELETE")
        result_delete: Response = Google_maps_api.delete_new_location(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete,['status'])
        Checking.check_json_value(result_delete,'status','OK')
        print("GET DELETE")
        result_get: Response = Google_maps_api.get_new_location(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get,['msg'])
        Checking.check_json_search_word_value(result_get,'msg','failed')

        print("Test of creation, update and delete new location is successfully finished ")


