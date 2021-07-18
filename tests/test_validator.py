from baby_steps import then, when
from district42 import schema

from valera import eq


def test_validator_eq():
    with when:
        result = eq(schema.str, schema.str)

    with then:
        assert result is True


def test_validator_not_eq_schema():
    with when:
        result = eq(schema.str, schema.int)

    with then:
        assert result is False


def test_validator_not_eq_props():
    with when:
        result = eq(schema.str, schema.str.len(1))

    with then:
        assert result is False


def test_validator_not_eq_value():
    with when:
        result = eq(schema.str, 42)

    with then:
        assert result is False
