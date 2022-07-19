import parse_homer


# prints to console the text with swapped characters read from xml

complete_text = parse_homer.swapper(parse_homer.text_reader())

sample_text = complete_text[:277]

# a generator can continuly carve off its first line until a list of lines depletes the text


def text_splitter(text):
    # sorts out the content found in parsed text 
    line_by_line = []
    bad_lines = []
    # ignores XML format mistakes on conversion
    for line in text.splitlines():
        if line != '':
            line_by_line.append(line)
        else:
            bad_lines.append(line)

    return (line_by_line, bad_lines)

# print(text_splitter(sample_text))

def hexameter_scanner(all_lines):
    # each line contains six metric feet
    # each foot is either two long spondee or one with a dactyl
    # The last syllable of the final foot is usually long, sometimes a single short
    # caesura is a natural break typically occuring in middle of foot 2 3 or 4
    # elision vs hiatus. The latter is rare since an -Xm ending followed by h- elides

    # Nature - a syllable is long by nature if it has a long vowel or diphthong
    # Position - a syllable is long by position if it precedes two consonants

    scan_lines = all_lines[0]

    






print(hexameter_scanner(text_splitter(sample_text)))
