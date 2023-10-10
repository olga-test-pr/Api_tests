"""methods for response checking"""
import json

from requests import Response


class Checking():
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Success! Status code = " + str(response.status_code))
        else:
            print("Failed! Status code = " + str(response.status_code))

#method of checking mandatory fields in response

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("all mandatory fields exist")

#method of checking values in mandatory fields in response

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " valid!")


#method of checking values in mandatory fields in response when use search word

    @staticmethod
    def check_json_search_word_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("word " + search_word + " exist!" )
        else:
            print("word " + search_word + " missing!")

