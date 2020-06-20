import pprint

def parser(list_of_db_records):
    # list_of_db_records is a list of lists

    parsed_records = []
    for record in list_of_db_records:
        new_record = {}
        new_record['id'] = record[0]
        new_record['Strain'] = record[1]
        new_record['Type'] = record[2]
        new_record['Rating'] = record[3]
        new_record['Effects'] = record[4]
        new_record['Flavor'] = record[5]
        new_record['Description'] = record[6]

        parsed_records.append(new_record)

    pprint.pprint(parsed_records)

    return parsed_records
