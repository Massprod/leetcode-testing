

def int_to_roman(num: int) -> str:
    # 49.88% 66.41% my brute_force with no thinking about anything
    # values = {
    #     1: "I",
    #     5: "V",
    #     10: "X",
    #     50: "L",
    #     100: "C",
    #     500: "D",
    #     1000: "M",
    # }
    # roman = ""
    # print(num)
    # while num != 0:
    #     if num >= 1000:
    #         num -= 1000
    #         roman += values[1000]
    #     elif 900 <= num < 1000:
    #         num -= 900
    #         roman += values[100] + values[1000]
    #     elif 500 <= num < 900:
    #         num -= 500
    #         roman += values[500]
    #     elif 400 <= num < 500:
    #         num -= 400
    #         roman += values[100] + values[500]
    #     elif 100 <= num < 400:
    #         num -= 100
    #         roman += values[100]
    #     elif 90 <= num < 100:
    #         num -= 90
    #         roman += values[10] + values[100]
    #     elif 50 <= num < 90:
    #         num -= 50
    #         roman += values[50]
    #     elif 40 <= num < 50:
    #         num -= 40
    #         roman += values[10] + values[50]
    #     elif 10 <= num < 40:
    #         num -= 10
    #         roman += values[10]
    #     elif 9 <= num < 10:
    #         num -= 9
    #         roman += values[1] + values[10]
    #     elif 5 <= num < 9:
    #         num -= 5
    #         roman += values[5]
    #     elif 4 <= num < 5:
    #         num -= 4
    #         roman += values[1] + values[5]
    #     elif 1 <= num < 4:
    #         num -= 1
    #         roman += values[1]
    # return roman
    # 64.63% 97.93% my not_brute
    values = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    roman = ""
    for key, value in values.items():
        while num >= key:
            num -= key
            roman += value
    return roman


# Instantly tried to solve it and think about better solution after.
# Brute force is working, and can be easily changed if we use 6 options in values.
# Both works fine.
