from datetime import datetime


def output_last_operations(data):
    for item in data[:5]:
        date_str = item.get("date", "")
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date.strftime("%d.%m.%Y")
        description = item["description"]
        from_account = item.get("from", "")
        to_account = item.get("to", "")
        amount = item["operationAmount"]["amount"]
        currency = item["operationAmount"]["currency"]["name"]

        output = f"{formatted_date} {description}\n{from_account} -> {to_account}\n{amount} {currency}"
        print(output)
