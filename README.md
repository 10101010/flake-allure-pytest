# flake8-allure-pytest

A flake8 plugin that checks for allure decorators in your pytest-based test code

By default, will expect to find `@allure.feature` and `@allure.story` tags on tests class, `@allure.description` on tests methods, but it's easy to customize the behavior

The following errors are reported:
* `AL001 class '{name}' should have {tags} tags`

* `AL002 method '{name}' should have 'description' tag`  

Installation:

`pip install -e git+https://github.com/10101010/flake-allure-pytest#egg=flake-allure-pytest`

