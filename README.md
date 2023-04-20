
# Вычислитель отличий

#### Hexlet tests and linter status:
[![Actions Status](https://github.com/eleron96/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/eleron96/python-project-50/actions)
#### Maintainability Badge:
[![Maintainability](https://api.codeclimate.com/v1/badges/ae82db826b8a6d6f28f6/maintainability)](https://codeclimate.com/github/eleron96/python-project-50/maintainability)
#### Test Coverage Badge:
[![Test Coverage](https://api.codeclimate.com/v1/badges/ae82db826b8a6d6f28f6/test_coverage)](https://codeclimate.com/github/eleron96/python-project-50/test_coverage)

**Вычислитель отличий** - это программа, предназначенная для сравнения двух конфигурационных файлов и отображения различий между ними.

## Установка

TBD

## Использование

Для вывода справочной информации по утилите, выполните следующую команду:

`gendiff -h` 

Программа принимает на вход два аргумента - пути до конфигурационных файлов, которые необходимо сравнить:

`gendiff first_file second_file` 

Результат сравнения может выводиться в разных форматах. Чтобы указать формат вывода, используйте опцию `--format`:

`gendiff -f FORMAT first_file second_file` 

## Пример

Сравнение плоских JSON-файлов:

`gendiff filepath1.json filepath2.json` 

Результат:

    `{
      - follow: false
        host: hexlet.io
      - proxy: 123.234.53.22
      - timeout: 50
      + timeout: 20
      + verbose: true
    }` 

Здесь `-` означает, что ключ присутствует только в первом файле, `+` - что ключ присутствует только во втором файле. Если нет плюса или минуса, это означает, что ключ есть в обоих файлах и его значения совпадают.


## Плоский формат

Помимо стандартного формата вывода, программа поддерживает плоский формат (`plain`). Он удобен для интеграции с другими системами или для упрощенного восприятия разницы между файлами.

Чтобы использовать плоский формат, укажите опцию `--format plain`:

`gendiff --format plain filepath1.json filepath2.json` 

Результат:

    Property 'common.follow' was added with value: false
    Property 'common.setting2' was removed
    Property 'common.setting3' was updated. From true to null
    Property 'common.setting4' was added with value: 'blah blah'
    Property 'common.setting5' was added with value: [complex value]
    Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
    Property 'common.setting6.ops' was added with value: 'vops'
    Property 'group1.baz' was updated. From 'bas' to 'bars'
    Property 'group1.nest' was updated. From [complex value] to 'str'
    Property 'group2' was removed
    Property 'group3' was added with value: [complex value]

В плоском формате:

-   Если новое значение свойства является составным, выводится `[complex value]`.
-   Если свойство вложенное, отображается весь путь до корня, а не только с учетом родителя (например, `common.setting6.ops`).
