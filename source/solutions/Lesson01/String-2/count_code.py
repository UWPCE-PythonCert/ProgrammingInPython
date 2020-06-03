def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i:i + 2] == "co" and str[i + 3] == "e":
            count += 1
    return count


assert count_code('aaacodebbb') == 1
assert count_code('codexxcode') == 2
assert count_code('cozexxcope') == 2
assert count_code('cozexxcope') == 2
assert count_code('cozfxxcope') == 1
assert count_code('xxcozeyycop') == 1
assert count_code('cozcop') == 0



print("all checks passed")

