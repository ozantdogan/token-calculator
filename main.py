import tiktoken
import datetime

while True:
    enc = tiktoken.get_encoding("cl100k_base")

    my_input = input('\n')

    if my_input == '0':
        break

    word_count = len(my_input.split())

    encoded_tokens = enc.encode(my_input)
    decoded_tokens = [enc.decode([token]) for token in encoded_tokens]
    token_info = [(token, enc.decode([token])) for token in encoded_tokens]
    token_count = len(encoded_tokens)

    price_per_1m_tokens_input = 30.00 # cent
    price_per_1m_tokens_output = 60.00 # cent

    input_cost = (token_count / 1_000_000) * price_per_1m_tokens_input
    output_cost = (token_count / 1_000_000) * price_per_1m_tokens_output    

    output_content = f"\n"
    output_content += f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n"
    output_content += f"Input: {my_input}\n"
    output_content += f"Word count: {word_count}\n"
    output_content += f"Token count: {token_count}\n"
    output_content += f"Tokens: {encoded_tokens}\n"
    output_content += f"Tokenized breakdown: {decoded_tokens}\n"
    output_content += f"Token information (token, string): {token_info}\n"
    output_content += f"Cost (input): {input_cost}\n"
    output_content += f"Cost (output): {output_cost}\n"

    print(f"Word count: {word_count}")
    print(f"Token count: {token_count}")
    print(f"Tokens: {encoded_tokens}")
    print(f"Tokenized breakdown: {decoded_tokens}")
    print(f"Token information (token, string): {token_info}")
    print(f"Cost (input): {input_cost}") 
    print(f"Cost (output): {output_cost}")

    with open("output.txt", "a", encoding="utf-8") as file:
        file.write(output_content)