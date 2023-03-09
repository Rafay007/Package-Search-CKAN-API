
def get_datasets_title(data:dict, key:str, items_count: int)-> list:
    records = list()
    for index, item in enumerate(data['result']['results'],1):
            # if index>items_count-1:
            #     break
            records.append(f'Index: {index} and Title: {item[key]}')

    return records