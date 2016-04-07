
ne = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
by_ten = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninty"}
millions_and_billions = {1:"", 2:"thousand", 3:"million", 4:"billion", 5:"trillion" }

ck_at = float(raw_input("Enter Amount:"))


def num_to_words(num1):
    whole_amount = ""

    def hundo_column(num2):
         num2 = abs(num2)
         if num2 > 9:
            print "how did this even happen"
         elif num2 <= 0:
            return ""
         elif num2 < 9:
            return by_one[num2] + " " + "hundred"




    def tens_column(num3):
        num3 = abs(num3)
        tens_string = ""
        if num3 >= 0 and num3 < 20:
            return by_one[num3]

        else:
            first_digit = round(num3 % 10)
            second_digit = num3 // 10
            f_dgt = by_one[first_digit]
            s_dgt = by_ten[second_digit]
            tens_string =s_dgt + "-" + f_dgt
            return tens_string
    #print tens_column(ck_at)

     # isolate decimal, convert to sting and add to string : whole_amount
    num1 = abs(num1)
    cents = num1 % 1
    cents = cents * 100
    whole_amount = whole_amount + "and " + tens_column(cents) + " cents"
    num1 = num1 // 1

    counter = 0
    while num1 > 0:
        counter = counter + 1
         #bring all seperate pieces together
        first_three =  num1 % 1000
        hundred = first_three // 100
        hrd = hundo_column(hundred)
        tens = first_three % 100
        tns = tens_column(tens)
        whole_amount = hrd + " " +  tns + " " +  millions_and_billions[counter] + " " + whole_amount
        num1= num1 // 1000


    return whole_amount

print num_to_words(ck_at)


