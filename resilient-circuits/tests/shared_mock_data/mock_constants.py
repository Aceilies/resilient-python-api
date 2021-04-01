#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Common constants used in tests"""

MOCK_PACKAGE_NAME = u"mock_function_package"

RESILIENT_MOCK = u"pytest_resilient_circuits.BasicResilientMock"

CONFIG_DATA = """[{0}]
url = https://www.example.com""".format(MOCK_PACKAGE_NAME)

MOCK_OPTS = {
    "host": "192.168.0.1",
    "org": "Test Organization",
    "email": "admin@example.com",
    "password": "123",
    "resilient_mock": RESILIENT_MOCK
}
