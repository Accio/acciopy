from fuzzywuzzy import fuzz
from os.path import dirname, basename


def fuzzmatch_filenames(input_list, to_be_mapped):
    '''
    Returns a permuted list of to_be_mapped that fuzzy match input_list

    Args:
        input_list (list of str): A list of strings, for instance file names
        to_be_mapped (list of str): Another list of string that will be
        reordered

    Returns:
        mapped_list (list of str): A permuted version of to_be_mapped of the
        same length of input_list, each of which is most similar to the
        matching element in the input_list judged by the Levenshtein distance.
    '''

    res_str = []
    for istr in input_list:
        lev_sim = [fuzz.ratio(istr, st) for st in to_be_mapped]
        ind_max = lev_sim.index(max(lev_sim))
        res_str.append(to_be_mapped[ind_max])
    return res_str


def _unique_first(alist):
    return list(set(alist))[0]


def _unique_dirname(alist):
    return _unique_first([dirname(x) for x in alist])


def basenames(alist):
    return [basename(s) for s in alist]


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


def _sim_filename(ind):
    res = str(ind) + '_S' + str(ind) + '.fq'
    return(res)


def _sim_complex_filename(ind):
    res = '/tmp/' + str(ind) + '_S' + str(ind) + '_L001.fastq.gz'
    return(res)


if __name__ == '__main__':
    print("An example of fuzzmatch_filenames")
    alist = [_sim_filename(i) for i in range(1, 5)]
    blist = [_sim_complex_filename(i) for i in reversed(range(1, 5))]
    print('The input list:' + ','.join(alist))
    print('The observed list:' + ','.join(blist))
    matched_list = fuzzmatch_filenames(alist, blist)
    print('The matched list:')
    print_fuzzmatch_filenames(alist, matched_list)
