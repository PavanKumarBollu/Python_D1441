anp_d1441 = {
    "labs":70,
    "mcq":60,
    "ichart":50,
    "attendance":91.56,
    "batchcode":"ANP-D1441",
    "topics":["Excel","PowerBI","Python", "SQL", "FinalProject"],
    "managementNames":{
        "domain":"Pavan",
        "softSkills":"Sushmitha",
        "Pro":"Ganesh",
        "Manager":"Dinesh"
    },
    "timings":"01:00 pm - 04:00 pm",
    "totalstudentcount":100,
    "supporter":"Accenture",
    "location":"madhapur"
}

# print(anp_d1441)


#clear() method it will remove all the key-values pairs from the dictionary and makes it empty dictionary
# anp_d1441.clear()
# print(anp_d1441)

#get() method is used to get the values associated with the key means we need input the key then it will returns the value
# of that key if the key is not found then it will returns the None as the result if we want to give our own output when
# key not found then we can modify the default parameter like shown in below

# center_loation = anp_d1441.get("supporter","key not found")
# print(center_loation)
#
# print(anp_d1441.get("loc",)) # returns None because the loc key not available in the dict
# print(anp_d1441.get("loc", "key not found"))


#copy() method is used to create the copy of the original dict
# anp_d1441_copy = anp_d1441.copy()
# print(anp_d1441_copy)
# anp_d1441_copy["totalstudentcount"] = 50
# print(anp_d1441_copy)

#items() keys() values()
# items() method is used to get all the items as key-values pairs
# keys() method is used to get all the keys present inside the dictionary
# values() method is used to get all the values present inside the dictionary

# print(anp_d1441.items())
# print(anp_d1441.keys())
# print(anp_d1441.values())

# anp_d1441.update({"completion":70})
# print(anp_d1441)

# anp_d1441["labs"]=80
# print(anp_d1441)

# for key in anp_d1441.keys():
#     print(anp_d1441[key])

# print(anp_d1441.keys(), type(anp_d1441.keys()))

# count = len(anp_d1441)-1
# keys = anp_d1441.keys()
# keys_list = list(keys)
# while count >= 0:
#     print(anp_d1441[keys_list[count]])
#     count -= 1

def cal_sum(dict):
    list = []
    for i in dict:
        # print(i)
        list.append(dict[i])
        # print(list)
    results = sum(list)
    return results

my_dict = {"a":10,"b":20,"c":30,"d":40}

print(cal_sum(my_dict))#100

