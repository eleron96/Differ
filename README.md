### Hexlet tests and linter status:
[![Actions Status](https://github.com/eleron96/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/eleron96/python-project-50/actions)
### Maintainability Badge:
[![Maintainability](https://api.codeclimate.com/v1/badges/ae82db826b8a6d6f28f6/maintainability)](https://codeclimate.com/github/eleron96/python-project-50/maintainability)
### Test Coverage Badge:
[![Test Coverage](https://api.codeclimate.com/v1/badges/ae82db826b8a6d6f28f6/test_coverage)](https://codeclimate.com/github/eleron96/python-project-50/test_coverage)


# Вычислитель отличий

**Вычислитель отличий** - это программа, предназначенная для сравнения двух конфигурационных файлов и отображения различий между ними.

## Установка

TBD

## Использование

Для вывода справочной информации по утилите, выполните следующую команду:

Copy code

`gendiff -h` 

Программа принимает на вход два аргумента - пути до конфигурационных файлов, которые необходимо сравнить:

Copy code

`gendiff first_file second_file` 

Результат сравнения может выводиться в разных форматах. Чтобы указать формат вывода, используйте опцию `--format`:

Copy code

`gendiff -f FORMAT first_file second_file` 

## Пример

Сравнение плоских JSON-файлов:

Copy code

`gendiff filepath1.json filepath2.json` 

Результат:

yamlCopy code

`{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}` 

Здесь `-` означает, что ключ присутствует только в первом файле, `+` - что ключ присутствует только во втором файле. Если нет плюса или минуса, это означает, что ключ есть в обоих файлах и его значения совпадают.
