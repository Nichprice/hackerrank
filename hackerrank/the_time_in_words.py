def timeInWords(h, m):
    # Write your code here
    nums = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen",
            "twenty", "twenty one", "twenty two",
            "twenty three", "twenty four",
            "twenty five", "twenty six", "twenty seven",
            "twenty eight", "twenty nine"];

    if (m == 0):
        return(f"{nums[h]} o' clock");
 
    elif (m == 1):
        return(f"one minute past {nums[h]}");
 
    elif (m == 59):
        return(f"one minute to {nums[(h % 12) + 1]}");
 
    elif (m == 15):
        return(f"quarter past {nums[h]}");
 
    elif (m == 30):
        return(f"half past {nums[h]}");
 
    elif (m == 45):
        return(f"quarter to {(nums[(h % 12) + 1])}");
 
    elif (m <= 30):
        return (f"{nums[m]} minutes past {nums[h]}");
 
    elif (m > 30):
        return (f"{nums[60 - m]} minutes to {nums[(h % 12) + 1]}");