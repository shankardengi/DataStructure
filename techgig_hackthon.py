class patient:
    virus_composition = None
    virus_composition_index = {}
    patient_count = 1
    def __init__(self,composition,patient_number):
        self.patient_number = patient_number
        self.composition = composition
        self.result = None
    @staticmethod
    def virus_composition_index_method():
        dicts ={}
        count = 0
        for ch in patient.virus_composition:
            lists = []
            if ch in dicts:
                lists = dicts[ch]
                lists.append(count)
                dicts[ch]=lists
                count +=1
            else:
                lists.append(count)
                dicts[ch] = lists
                count += 1
        patient.virus_composition_index = dicts

if __name__=="__main__":
    patient.virus_composition = input().lower()
    patient.virus_composition_index_method()
    n = int(input())
    patient_list = []
    for i in range(n):
        composition = input().lower()
        patient.patient_count +=1
        pat = patient(composition,patient.patient_count)
        patient_list.append(pat)
    for patient in patient_list:
        list_temp = []
        result_composition_index = {}
        for ch in patient.composition:
            if ch in patient.virus_composition_index:
                lists = patient.virus_composition_index[ch]
                if ch in result_composition_index:
                    count = result_composition_index[ch]
                    if count < len(lists):
                        if len(lists)>1 and len(list_temp)>=1:
                            temp_list = list(filter(lambda x:x >= list_temp[len(list_temp)-1],lists))
                            if len(temp_list)>0:
                                list_temp.append(temp_list[0])
                                count +=1
                                result_composition_index[ch] = count
                            else:
                                patient.result = 'NEGATIVE'
                                break
                        else:
                            list_temp.append(lists[count])
                            count += 1
                            result_composition_index[ch]=count
                    else:
                        patient.result = 'NEGATIVE'
                        break
                else:
                    count = 1
                    if len(lists) > 1 and len(list_temp) >= 1:
                        temp_list = list(filter(lambda x: x >= list_temp[len(list_temp) - 1], lists))
                        result_composition_index[ch] = count
                        list_temp.append(temp_list[0])
                    else:
                        result_composition_index[ch] = count
                        list_temp.append(lists[0])
            else:
                patient.result = 'NEGATIVE'
                break
        if patient.result == None:
            temp_elements = list_temp.copy()
            list_temp.sort()
            if temp_elements == list_temp:
                patient.result = 'POSITIVE'
            else:
                patient.result = 'NEGATIVE'
    for patient in patient_list:
        print(patient.result)
