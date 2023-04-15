import sys

input_file_name = "day6_input_sample.txt" if "SAMPLE" in sys.argv else "day6_input.txt"


# The marker length of the starting communication
START_PACKET_FRAGMENT_MARKER_LENGTH = 14


def find_beginning_of_communication(datastream: str):
    datastream_length = len(datastream)

    # process datastream by 14 characters group
    for start_fragment in range(0, datastream_length-START_PACKET_FRAGMENT_MARKER_LENGTH):
        # define datastream fragment to check
        end_fragment = start_fragment + START_PACKET_FRAGMENT_MARKER_LENGTH
        datastream_fragment = datastream[start_fragment:end_fragment]
        different_characters_in_fragment_count = len(set(datastream_fragment))
        #print(f"{datastream_fragment}, {different_characters_in_fragment_count}")
        if different_characters_in_fragment_count == START_PACKET_FRAGMENT_MARKER_LENGTH:
            # communication starting
            beginning_of_communication = start_fragment + START_PACKET_FRAGMENT_MARKER_LENGTH
            break;

    print(f"last character of marker position = {beginning_of_communication}")


with open(input_file_name) as input_file:
    for datastream in input_file:
        find_beginning_of_communication(datastream.strip())
