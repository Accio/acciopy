import fuzzywuzzy
import os.path

def fuzzmatch_filenames(input_list, to_be_mapped):
    res_str = []
    for istr in input_list:
        lev_sim = [fuzzywuzzy.fuzz.ratio(istr, st) for st in to_be_mapped]
        ind_max = lev_sim.index(max(lev_sim))
        res_str.append(to_be_mapped[ind_max])
    return res_str


def _unique_first(alist):
    return list(set(alist))[0]


def _unique_dirname(alist):
    return _unique_first([os.path.dirname(x) for x in alist])


def basenames(alist):
    return [os.path.basename(s) for s in alist]


def print_fuzzmatch_filenames(input_list, mapped_list):
    input_dir = _unique_dirname(input_list)
    mapped_dir = _unique_dirname(mapped_list)
    print("# Input directory: " + input_dir)
    print("# Mapped directory: " + mapped_dir)
    ibase = basenames(input_list)
    mbase = basenames(mapped_list)
    imdict = dict(zip(ibase, mbase))
    print("# File mapping:")
    print(imdict)
    return None
