import cc_dat_utils
import cc_json_utils
import cc_data
import json

#Below is submission for Part 1, Phase 3

def make_optional_fields_from_json(json_optional_fields):
    cc_fields = []

    for json_field in json_optional_fields:
        #This iterates through the optional fields in the json data,
        #first comparing the integer value "type" to a certain class in cc_data

        #Each class has its unique requirements, and all redefine cc_field,
        #which appends to the list cc_fields.

        field_type = json_field["type"]
        if field_type == cc_data.CCMapTitleField.TYPE:
            cc_field = cc_data.CCMapTitleField(json_field["title"])
            #Simple. In the json data, it just looks for the key
            # "title" and takes the value (level name)

            cc_fields.append(cc_field)
        elif field_type == cc_data.CCTrapControlsField.TYPE:
            cc_traps = []
            for json_trap in json_field["traps"]:
                bx = json_trap["button"][0]
                by = json_trap["button"][1]
                tx = json_trap["button"][0]
                ty = json_trap["button"][1]
                cc_traps.append(cc_data.CCTrapControl(bx,by,tx,ty))
            cc_field = cc_data.CCTrapControlsField(cc_traps)
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCCloningMachineControlsField.TYPE:
            cc_machines = []
            for json_machine in json_field["cloning_machines"]:
                bx = json_machine["button"]["0"]
                by = json_machine["button"]["1"]
                tx = json_machine["machine"]["0"]
                ty = json_machine["machine"]["1"]
                cc_machines.append(cc_data.CCCloningMachineControl(bx,by,tx,ty))
            cc_field = cc_data.CCTrapControlsField(cc_traps)
            #I don't believe the above line ultimately does anything.

            cc_field = cc_data.CCCloningMachineControlsField(cc_machines)
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCEncodedPasswordField.TYPE:
            #Similar to the title. Only we're grabbing a list of four elements
            # instead of a string value.

            cc_field = cc_data.CCEncodedPasswordField(json_field["password"])
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCMapHintField.TYPE:
            #Ditto to the title. Grabbing a string value.

            cc_field = cc_data.CCMapHintField(json_field["hint"])
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCMonsterMovementField.TYPE:
            #A little trickier. json_field["monsters"] is a list itself, and
            # we need to go through each element. Each element is also
            # a list.

            cc_monsters = []
            for json_monster in json_field["monsters"]:
                #A monster is given a list with two elements, denoting x and y coordinates

                x = json_monster[0]
                y = json_monster[1]
                cc_monsters.append(cc_data.CCCoordinate(x,y))
            cc_field = cc_data.CCMonsterMovementField(cc_monsters)
            cc_fields.append(cc_field)
        else:
            #I admittedly have no idea what's going on below.

            if __debug__:
                raise AssertionError("Unsupported field type: " + str(field_type))
            return None
    return cc_fields


def make_level_from_json(json_data):

    cc_level = cc_data.CCLevel()
    #initating in cc_data.py, cc_level is defined as the eventual level data
    #Below, the properties of each level in the json data are assigned to the cc_level

    cc_level.level_number = json_data["level_number"]
    cc_level.time = json_data["time"]
    cc_level.num_chips = json_data["num_chips"]
    cc_level.upper_layer = json_data["upper_layer"]
    cc_level.lower_layer = json_data["upper_layer"]
    cc_level.optional_fields = make_optional_fields_from_json(json_data["optional_fields"])
    return cc_level


def make_cc_data_from_json(json_file):
    """Reads a JSON file and constructs a CCDataFile object out of it
    This code assumes a valid JSON file and does not error check for invalid data
    Args:
        json_file (string) : the filename of the JSON file to read in
    Returns:
        A CCDataFile object constructed with the data from the given file
    """
    cc_data_file = cc_data.CCDataFile()
    with open(json_file, 'r') as reader:
        json_data = json.load(reader)
        for json_level in json_data:
            cc_level = cc_data.CCLevel()
            # cc_level = make_level_from_json(json_level)
            cc_data_file.add_level(cc_level)
    return cc_data_file

#End of submission for Part 1, Phase 3


json_data = cc_json_utils.make_cc_data_from_json("data/jinheel1_testData.json")
cc_dat_utils.write_cc_data_to_dat(json_data, "data/jinheel1_testData.dat")
dat_data = cc_dat_utils.make_cc_data_from_dat("data/jinheel1_testData.dat")
# print(dat_data)

# data = make_cc_data_from_json("data/jinheel1_testData.json")
# print(data)