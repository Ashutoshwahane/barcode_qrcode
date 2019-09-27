def productsku(str1, dict, l_dict=""):
    for i in dict:
        l_dict += dict[i][:3] + "-"
    return (str1[:3]+"-"+l_dict[:-1]).upper()


str1 = "apple"
dict = {"model": "iphone", "color": "red", "os": "ios13"}
print(productsku(str1, dict, l_dict=""))
