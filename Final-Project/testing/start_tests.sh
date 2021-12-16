#! /bin/bash

pytest -m "${MARK}" -n "${N}" /tmp/testing  --alluredir=/tmp/allure