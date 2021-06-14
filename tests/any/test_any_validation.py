from typing import Any

import pytest
from baby_steps import given, then, when
from district42 import schema
from th import PathHolder

from valera import validate
from valera.errors import SchemaMismatchValidationError


@pytest.mark.parametrize("value", [
    None,
    True,
    42,
    3.14,
    "banana",
    [],
    {},
    Exception,
])
def test_any_validation(value: Any):
    with when:
        result = validate(schema.any, value)

    with then:
        assert result.get_errors() == []


def test_any_type_validation():
    with when:
        result = validate(schema.any(schema.none), None)

    with then:
        assert result.get_errors() == []


def test_any_type_validation_error():
    with given:
        value = False
        types = (schema.none,)

    with when:
        result = validate(schema.any(*types), value)

    with then:
        assert result.get_errors() == [
            SchemaMismatchValidationError(PathHolder(), value, types)
        ]


@pytest.mark.parametrize("value", [42, "42"])
def test_any_types_validation(value: Any):
    with when:
        result = validate(schema.any(schema.int, schema.str), value)

    with then:
        assert result.get_errors() == []


def test_any_types_validation_error():
    with given:
        value = None
        types = (schema.int, schema.str)

    with when:
        result = validate(schema.any(*types), value)

    with then:
        assert result.get_errors() == [
            SchemaMismatchValidationError(PathHolder(), value, types)
        ]
