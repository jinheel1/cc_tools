import cc_data
import json



def make_level_from_json(json_file):

    cc_level = cc_data.CCLevel()
    cc_level.level_number = json_file["level_number"]
    #cc_level.optional_fields = make_optional_fields_from_json(json_datap["optional fields"])
    return cc_level

def make_cc_data_from_json(json_file):
    cc_data_file = cc_data.CCDataFile()
    with open(json_file, 'r') as reader:
        level_data = json.load(reader)
        #level_data and json_file are NOT the same
        for json_level in level_data:
            cc_level = make_level_from_json(json_level)
            cc_data_file.add_level(cc_level)
    return cc_data_file