"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"

        if number > 10_000_000:
            return "number exceeds the maximum supported range (10,000,000)"

        THAI_NUMBERS = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        THAI_PLACES = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

        if number == 0:
            return THAI_NUMBERS[0]
        
        if number == 10_000_000:
            return "สิบล้าน"
        
        num_str = str(number)
        num_len = len(num_str)
        result = []

        for i, digit in enumerate(num_str):
            digit = int(digit)
            place_index = num_len - 1 - i

            if digit == 0 and place_index != 0:
                continue

            if place_index == 6:
                if digit > 0:
                    result.append(THAI_NUMBERS[digit])
                result.append(THAI_PLACES[place_index])
                num_len = 6
                continue
            
            if digit > 0:
                if place_index == 0 and digit == 1 and num_len > 1 and int(num_str[-2]) != 0 and num_len != 7 : 
                    result.append("เอ็ด")
                
                elif place_index == 1 and digit == 2:
                    result.append("ยี่")
                    result.append(THAI_PLACES[place_index])
                
                elif place_index == 1 and digit == 1:
                    result.append(THAI_PLACES[place_index])
                
                else:
                    result.append(THAI_NUMBERS[digit])
                    if place_index > 0:
                        result.append(THAI_PLACES[place_index])
            
        return "".join(result)