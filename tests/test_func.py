import pytest
from src.last_operations_func import output_last_operations


@pytest.fixture
def sample_data():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"

        },

    ]


def test_output_last_operations(capsys, sample_data):
    expected_output = (
        "26.08.2019 Перевод организации\n"
        " Maestro 159683 ********** 5199 -> Счет **************** 9589\n"
        "31957.58 руб.\n"
    )

    output_last_operations(sample_data)

    captured = capsys.readouterr()
    actual_output = captured.out

    print("Expected Output:")
    print(expected_output)
    print("Actual Output:")
    print(actual_output)

    assert actual_output.strip() == expected_output.strip()

