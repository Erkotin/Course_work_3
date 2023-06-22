from datetime import datetime
import re


def output_last_operations(data):
    for item in data[:5]:
        date_str = item.get("date", "")
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date.strftime("%d.%m.%Y")
        description = item["description"]
        from_account = item.get("from", "")

        # Extract card number and card name
        card_number = from_account[-16:]
        card_name = from_account.split()[:-1]  # Extract all words except the last one
        card_name = " ".join(card_name)  # Join the words with a space

        #hide card number
        visible_digits = 6
        hidden_part = "*" * (len(card_number) - visible_digits)
        masked_card = " ".join([card_number[:visible_digits], hidden_part, card_number[-4:]])

        to_account = item.get("to", "")

        #hide account number
        account_number = to_account[-20:]
        account_name = to_account.split()[:-1]  # Extract all words except the last one
        account_name = " ".join(account_name)
        visible_digits_account = 4
        hidden = "*" * (len(account_number) - visible_digits_account)
        masked_account = " ".join([account_name, hidden, account_number[-4:]])

        amount = item["operationAmount"]["amount"]
        currency = item["operationAmount"]["currency"]["name"]

        output = f"{formatted_date} {description}\n {card_name} {masked_card} -> {masked_account}\n{amount} {currency}"
        print(output)
        print()
