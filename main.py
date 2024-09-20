import random
import re


def load_data(file_path):
    data_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data_list.append(line.strip())
    return data_list


def dump_data(data_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for data in data_list:
            f.write(data + '\n')


def make_fake_english_name(data_list, size=100):
    names_list = []
    for _ in range(size):
        names = random.sample(data_list, 2)
        names_list.append(' '.join(names))
    return names_list


def make_fake_chinese_name(data_list, size=100):
    from pypinyin import pinyin, lazy_pinyin, Style
    names_list = []
    original_names = random.sample(data_list, size)
    for name in original_names:
        last_name = str.capitalize(''.join(lazy_pinyin(name[0])))  # 只考虑单字姓
        first_name = str.capitalize(''.join(lazy_pinyin(name[1:])))
        names_list.append(first_name + ' ' + last_name)
    return names_list


def make_test_names_data(file_path):
    en_names = load_data('English_names.txt')
    fake_names = make_fake_english_name(en_names)
    cn_names = load_data('Chinese_names.txt')
    cn_names = make_fake_chinese_name(cn_names)
    mixtures = fake_names + cn_names
    random.shuffle(mixtures)
    dump_data(mixtures, file_path)


def is_pinyin(letter_combination, pinyin_list):
    if letter_combination in pinyin_list:
        return True
    return False


def is_pinyin_name(name_str, pinyin_list):
    # 如果 name_str 为空字符串，直接返回 False
    if not name_str:
        return False
    
    # 如果 name_str 可以被完全分解为拼音组合，则返回 True
    # 单个拼音最长为6个字母，因此只检查至多前6个字符
    for iSep in range(1, 7):
        # 获取可能的拼音组合
        letter_combination = name_str[:iSep]
        # 如果是拼音组合
        if is_pinyin(letter_combination, pinyin_list):
            # 如果当前组合正好分解了整个字符串，返回 True
            if iSep == len(name_str):
                return True
            # 递归检查剩余的字符串
            if is_pinyin_name(name_str[iSep:], pinyin_list):
                return True
    return False


def name_preprocess(name_str):
    name_str = str.lower(name_str.strip())
    name_seps = re.split(r'[,\s-]+', name_str)  # 以空格、逗号、短横线分割
    return name_seps


def find_pinyin_names(data_list):
    pinyin_names = []
    non_pinyin_names = []
    for name in data_list:
        name_seperated = name_preprocess(name)
        is_pinyin = True
        for single_name in name_seperated:
            if not is_pinyin_name(single_name, pinyin_list):
                is_pinyin = False
                break
        if is_pinyin:
            pinyin_names.append(name)
        else:
            non_pinyin_names.append(name)
    return pinyin_names, non_pinyin_names


if __name__ == '__main__':
    random.seed(0)
    pinyin_list = load_data('pinyin.txt')
    print(pinyin_list)
    # make_test_names_data('test_names_data.txt')
    test_names_data = load_data('test_names_data.txt')
    found_pinyin_names, non_pinyin_names = find_pinyin_names(test_names_data)
    print('Found PinYin names:', found_pinyin_names)
    print('Found Non-PinYin names:', non_pinyin_names)

