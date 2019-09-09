import utils.my_logging as my_logging
import re
log = my_logging.my_console_logger(__name__)


def fun1():    
    pattern = re.compile(r"\w+")
    word = "Hello World "
    result = re.match(pattern=pattern, string=word)
    log.info(type(result))
    log.info(result.group(0))
    log.info(result.groups())
    # print(type(re.search(pattern=pattern, string=word)))


def single_char():
    log.info(re.match("c", "abcdef"))
    log.info(re.search("c{\w}2c", "abcdecf"))


def sentence_match():
    pattern = re.compile(r'(.*) are (\w*)')
    line = "Things are awesome in this world"
    match = re.match(pattern, line)
    if match:
        log.info(match.group())


def single_char_match_digit():
    pattern = r'\d'
    line = "123"
    log.info(re.match(pattern, line))


def single_char_match_word():
    pattern = r'\w'
    line = 'abc'
    log.info(re.match(pattern=pattern, string=line))


def test_match():
    pattern = r'[a-zA-Z0-9]+'  # r'\w+'
    line = 'abc'
    log.info(re.match(pattern=pattern, string=line))


def quanitifers():
    pattern = r'^[0-9]*.[a-z]$'
    pattern2 = r'\d{2}+'
    line = '123Aa'
    log.info(re.match(pattern2, line))


def start_end():
    pattern = r'^\d.{4}$'
    word = "q1235Kq"
    log.info(re.match(pattern, word))


def not_char():
    pattern = r'.[^2][^3]'
    word = ["12310", "word"]
    for item in word:
        log.info(re.match(pattern, item))


def search_ex():
    pattern = r'\w+'
    word = "\n YogaSadhana"
    log.info(re.search(pattern=pattern, string=word))


def split_ex():
    pattern = r'\s+'
    word = """Hello
                World!
                This is beautiful :)"""
    result = re.split(pattern=pattern, string=word)
    for item in result:
        print(item, len(item))


def find_all():
    pattern = r'\d'
    word = " 10023456 23 55 awerdef 332 1 srasrw45fdsdfgdg45 gdfgdg"
    result = re.findall(pattern=pattern, string=word)
    log.info(len(result))


def sub_ex():
    pattern = re.compile(r'(?=\s)[0-9]{2}(?=\s)')
    log.info(pattern.sub("**", "There are 7 continents, 10 monkeys, 100 of countries and 1000s of states in this world"))


def look_ahead_ex(word):
    pattern = re.compile(r'a(?=[bcd])')
    return pattern.sub('*', string=word)


if __name__ == "__main__":
    log.info(look_ahead_ex("This should match ac, ab, ad but not bac, bad, bab, and not a , abdc"))
