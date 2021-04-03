# coding: utf-8
import pytest
import allure
from report_demo.constans import case_data


# noinspection PyUnusedLocal
@allure.feature("needs_module")
@allure.severity(allure.severity_level.NORMAL)
class TestNeed:
    """需求模块"""

    @allure.story("needs")
    @pytest.mark.supply
    @pytest.mark.parametrize('need', [1, 2, 3])
    def test_need(self, need, fix_login, something):
        print("fix_login: ", fix_login, need)
        print("fix_login_json: ", fix_login.text, need)
        case_data.assert_handle.assert_equal_value(1, 1)

    pass
