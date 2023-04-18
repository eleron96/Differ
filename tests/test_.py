from gendiff.formaters.diff_plain import stringify, render
from gendiff.formaters.diff_stylish import render as stylish_render
from gendiff.formaters.diff_stylish import build_ident as stylish_build_ident
from gendiff.formaters.diff_stylish import stringify as stylish_stringify
import pytest


def test_stringify():
    assert stringify(None) == 'null'
    assert stringify(True) == 'true'
    assert stringify(False) == 'false'
    assert stringify(42) == '42'
    assert stringify("example") == "'example'"
    assert stringify([1, 2, 3]) == '[complex value]'
    assert stringify({"key": "value"}) == '[complex value]'


@pytest.mark.parametrize("tree, expected_output", [
    (
            {"type": "no_changes"},
            [],
    ),
    (
            {"type": "added", "key": "example", "value": "value"},
            ["Property 'example' was added with value: 'value'"],
    ),
    (
            {"type": "removed", "key": "example"},
            ["Property 'example' was removed"],
    ),
    (
            {"type": "changed", "key": "example", "value_1": "old_value",
             "value_2": "new_value"},
            ["Property 'example' was updated. From 'old_value' to 'new_value'"],
    ),
    (
            {
                "type": "nested",
                "key": "parent",
                "children": [
                    {"type": "added", "key": "child", "value": "value"}
                ]
            },
            ["Property 'parent.child' was added with value: 'value'"],
    ),
])
def test_render(tree, expected_output):
    assert render(tree) == expected_output


def test_stylish_build_ident():
    assert stylish_build_ident(0) == '  '
    assert stylish_build_ident(1) == '    '
    assert stylish_build_ident(2, marker='+') == '      + '


def test_stylish_stringify():
    assert stylish_stringify(None) == 'null'
    assert stylish_stringify(True) == 'true'
    assert stylish_stringify(False) == 'false'
    assert stylish_stringify(42) == '42'
    assert stylish_stringify({"key": "value"}) == (
        '{\n'
        '        key: value\n'
        '    }'
    )


@pytest.mark.parametrize("tree, expected_output", [
    (
            {"type": "no_changes", "key": "key", "value": "value"},
            "  key: value",
    ),
    (
            {"type": "added", "key": "key", "value": "value"},
            "+ key: value",
    ),
    (
            {"type": "removed", "key": "key", "value": "value"},
            "- key: value",
    ),
    (
            {
                "type": "changed",
                "key": "key",
                "value_1": "old_value",
                "value_2": "new_value",
            },
            "- key: old_value\n+ key: new_value",
    ),
    (
            {
                "type": "nest",
                "key": "parent",
                "children": [
                    {"type": "added", "key": "child", "value": "value"}
                ]
            },
            "  parent: {\n  + child: value\n  }",
    ),
    (
            {
                "type": "differ",
                "children": [
                    {"type": "added", "key": "child", "value": "value"}
                ]
            },
            "{\n  + child: value\n}",
    ),
])
def test_stylish_render(tree, expected_output):
    assert stylish_render(tree) == expected_output
