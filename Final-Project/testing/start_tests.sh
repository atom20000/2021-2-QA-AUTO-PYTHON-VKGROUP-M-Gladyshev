#! /bin/bash

pytest -m "${MARK}" -n "${N}" /tmp/testing/tests  --alluredir=/tmp/allure