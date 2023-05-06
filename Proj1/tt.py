#!/usr/bin/python3

import sys
import string
import itertools
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}


ENGLISH_FREQ = (0.0749, 0.0129, 0.0354, 0.0362, 0.1400, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047,
                0.0357, 0.0339, 0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.0300, 0.0116,
                0.0169, 0.0028, 0.0164, 0.0004)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
citext = "VPGMSMIXKHYWWYXZZDGMWYANNRBSXSVSUMLZMEQMIYWPRMIZCBMQTTNLEQPJHPZNOUYGPPFQTMHIDPMYQUWMTKXFBLDXMUTKBSXONRSELLOBNBOZGIFXVMSXIEIHPPJCRJBAGHQPJWVEAMQNGBLGKRXQZPTUVSUETMPCFGATHVFMSPLWIYWSIORPRFFLSXZFJBBPGKRYVZPXWSYVMAEILJFAEHJRJLMNNBRITWCAIINBOXBAFJRBSXQEYIZYLIAIGPPWQQSCBWBSRYVMWHWXTTBSBVTXOBLETNXHPPZIZJKIDBVFZQPNHVSZGQZGBUFHASXVRASZVGMJBVMEAMENHELLPRWHCCGWESCBDHAUJKMYMQAXSICVPBKVMCAMQLSPZZBUJVMOZMUTUELLMALOOPWQAFTQRABJNHPLGWGMSZSXLTJVWRPPVHVAPXURIHWLEQPJOVPQKRQZMYMWCUCZENVVYMNZKKETECPMQALCVPHNGMSUHBBUYVMZMPRWHPPHVYDRQQYQPZZBJPIFYVIEAMEKZIXBVTTKIDZWAJOKCHAFYCBSXWGMSZDBLRTTBSXONWRMYPPRWSIWBKRHCCWWARJWBEKGVSUQYTPRQDTPLAFTFBZYENDHWQEGHUWVEHIGWSMMRBUJHQXXAUJVIOVIHLVBEAMSQOUTGOBFBLMKWHLVBTMJNHYBSXNVLVBHTABASZLGLOTHPEAMUJROPAWTXKMCXWHYCNDBOUYPCEBBQTSAYMUNYHMCFCPMHPZNOUYOTTVMNXOTWMPRFFKSXANWSOZGMSWCUEAQFXWLPHNGMSOCHCAIGWDAMGZQSPWQGFKIJNVQJFPPKIERHPLMQGRWOSMVBYSANTXRFUITGIAIKMYMJNHYNZKIYNHBWXUBWSKZGDRWGIEBWABWBSAMEKFQPGLJMSVDAMTTHJLVSGTHPPVPRXVQCXKNYGPPPIFXIZAKQFJRBZYQAIECTMMNQOZRXKETKLNHTYJQBPWZBZBLTMBUJFMHTANIWAANBRLCQYZWAGSBHXMAYVMPQMPZHQZGMEYVMVBVTFBLEAMDZSMYPPBBSZPTTYYOTVBVTFHWYVMJMWTPTTYYVMCXAGBSZPJCVYSATEMAYOVOEWBPSLGXZLZBKZFNBWHIMEMGMSUZFMAYOTTVMNUDMLKMQXVMHTANUDMLEMQYCJJTTYYVZPXBBXSBEEMGMSYFXAGNCVLGLGMSGCXXRFHMOMPRNFICZCZJBBDMWUJFBSHCTMOAEAMLFZTDIWXJOBZGKRXVMQHCAIWBGXZLMOZOBVQJSLEHUNPSWFMMKFQBWREUFHBSXGFFWLEAMRCSKFMQBSSZDTZTZAMYMENXHPLMGBZQWFELAYQCEHNSFVMLWCAQSADMPRWSELLIOTRGEHKHYWBZYNSWCUEAIGMSPLWVRASZSTLGTRWDNKUFHPTGOOJTWCXIAIVMHTAAYUWTGOGTPMRBVNYVQDMQZJCNWBNRYVMVBVTXOZRNURSHELLBUFHIYRBUNBOEAIGMOLLAMNIQWFELOJPMSXIQJRIYWBUFHGZNERWSVEMWGFZSYHVFJBAPMPRVIMPGANWUCXXVGBOAEAIGNTAZFMGMWVRPIFSHLZGMNGCCEBBVSZMDLBUFBVZMQZJGPPWPNASMGXZLGCLJXFRHIBPWIYQFWFGLVYKIDMPVXZIDMZRROZVMPNYVIOFIQJHPPPPBQSXLKBLQCWVLWTWODPTVQFBFTHCFFZQNXKBZZLEAQAPCNYHBUNBOPEARYCALRJHYWBMXTBSUAEHBUJRCNAMFXMWFWJRYHMCTAXMSZLUWHYWBDAMFNBXCBABSHPPJCRJBALBLGTHPPXFRHIBTHVRWTMEVPUJFPPKMNSRBSXMKJQCEBWAJFEPGBBKTTTDMNSOZCHEGMSKLMAUJOLMXONSTIOBVTFKIJMPRRCUPGBUJKIDZWAJOVOUGGMSBTFMUJVIOVWZJPINDEVYVBSXLHHVMDLQGMOLPGBVWSTJWQFFDXPTZRIGWEAMXNBOLGLGMSMIXKHYWWYXZEFBETELYDIXLGLQT"

def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    print(freqs)
    
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

#################################################################
#################################################################
#################################################################
def vigenere(plaintext, key, a_is_zero=True):
    key = key.lower()
    if not all(k in string.ascii_lowercase for k in key):
        raise ValueError("Invalid key {!r}; the key can only consist of English letters".format(key))
    key_iter = itertools.cycle(map(ord, key))
    return "".join(
        chr(ord('a') + (
            (next(key_iter) - ord('a') + ord(letter) - ord('a'))    # Calculate shifted value
            + (0 if a_is_zero else 2)                               # Account for non-zero indexing
            ) % 26) if letter in string.ascii_lowercase             # Ignore non-alphabetic chars
        else letter
        for letter in plaintext.lower()
    )

#################################################################
#################################################################
#################################################################

def vigenere_decrypt(ciphertext, key, a_is_zero=True):
    # Decryption is encryption with the inverse key
    key_ind = [ord(k) - ord('a') for k in key.lower()]
    inverse = "".join(chr(ord('a') +
            ((26 if a_is_zero else 22) -
                (ord(k) - ord('a'))
            ) % 26) for k in key)
    return vigenere(ciphertext, inverse, a_is_zero)

 #################################################################
#################################################################
#################################################################
#    
def compare_freq(text):
    """
    Compare the letter distribution of the given text with normal English. Lower is closer.
    Performs a simple sum of absolute difference for each letter
    """
    if not text:
        return None
    text = [t for t in text.lower() if t in string.ascii_lowercase]
    freq = [0] * 26
    total = float(len(text))
    for l in text:
        freq[ord(l) - ord('a')] += 1
    return sum(abs(f / total - E) for f, E in zip(freq, ENGLISH_FREQ))

#################################################################
#################################################################
#################################################################
def solve_vigenere(text,  a_is_zero=True):
    """
    Solve a Vigenere cipher by finding keys such that the plaintext resembles English
    Returns:
        the first and second best from the set of best keys for each length
    This is not a brute force solver; instead, it takes advantage of a weakness in the cipher to
    solve in O(n * K^2) where n is the length of the text to decrypt and K is the length of the
    longest key to try.
    The idea is that for any key length, the key is used repeatedly, so if the key is of length k
    and we take every k'th letter, those letters should have approximately the same distribution as
    the English language on a whole. Furthermore, since each letter in the key is independent, we
    can perform the analysis for each letter in the key by taking every k'th letter at different
    starting offsets. Then, since the letters in the key are independent, we can construct the best
    key for a given length by simply joining the best candidates for each position.
    """
    best_keys = []
    key_min_size = 2
    key_max_size = 13

    text_letters = [c for c in text.lower() if c in string.ascii_uppercase]

    for key_length in range(key_min_size, key_max_size):
        # Try all possible key lengths
        key = [None] * key_length
        for key_index in range(key_length):
            letters = "".join(itertools.islice(text_letters, key_index, None, key_length))
            shifts = []
            for key_char in string.ascii_lowercase:
                shifts.append(
                    (compare_freq(vigenere_decrypt(letters, key_char, a_is_zero)), key_char)
                )
            key[key_index] = min(shifts, key=lambda x: x[0])[1]
        best_keys.append("".join(key))
    best_keys.sort(key=lambda key: compare_freq(vigenere_decrypt(text, key, a_is_zero)))
    return best_keys[:2]






if __name__ == "__main__":
    citext = "VPGMSMIXKHYWWYXZZDGMWYANNRBSXSVSUMLZMEQMIYWPRMIZCBMQTTNLEQPJHPZNOUYGPPFQTMHIDPMYQUWMTKXFBLDXMUTKBSXONRSELLOBNBOZGIFXVMSXIEIHPPJCRJBAGHQPJWVEAMQNGBLGKRXQZPTUVSUETMPCFGATHVFMSPLWIYWSIORPRFFLSXZFJBBPGKRYVZPXWSYVMAEILJFAEHJRJLMNNBRITWCAIINBOXBAFJRBSXQEYIZYLIAIGPPWQQSCBWBSRYVMWHWXTTBSBVTXOBLETNXHPPZIZJKIDBVFZQPNHVSZGQZGBUFHASXVRASZVGMJBVMEAMENHELLPRWHCCGWESCBDHAUJKMYMQAXSICVPBKVMCAMQLSPZZBUJVMOZMUTUELLMALOOPWQAFTQRABJNHPLGWGMSZSXLTJVWRPPVHVAPXURIHWLEQPJOVPQKRQZMYMWCUCZENVVYMNZKKETECPMQALCVPHNGMSUHBBUYVMZMPRWHPPHVYDRQQYQPZZBJPIFYVIEAMEKZIXBVTTKIDZWAJOKCHAFYCBSXWGMSZDBLRTTBSXONWRMYPPRWSIWBKRHCCWWARJWBEKGVSUQYTPRQDTPLAFTFBZYENDHWQEGHUWVEHIGWSMMRBUJHQXXAUJVIOVIHLVBEAMSQOUTGOBFBLMKWHLVBTMJNHYBSXNVLVBHTABASZLGLOTHPEAMUJROPAWTXKMCXWHYCNDBOUYPCEBBQTSAYMUNYHMCFCPMHPZNOUYOTTVMNXOTWMPRFFKSXANWSOZGMSWCUEAQFXWLPHNGMSOCHCAIGWDAMGZQSPWQGFKIJNVQJFPPKIERHPLMQGRWOSMVBYSANTXRFUITGIAIKMYMJNHYNZKIYNHBWXUBWSKZGDRWGIEBWABWBSAMEKFQPGLJMSVDAMTTHJLVSGTHPPVPRXVQCXKNYGPPPIFXIZAKQFJRBZYQAIECTMMNQOZRXKETKLNHTYJQBPWZBZBLTMBUJFMHTANIWAANBRLCQYZWAGSBHXMAYVMPQMPZHQZGMEYVMVBVTFBLEAMDZSMYPPBBSZPTTYYOTVBVTFHWYVMJMWTPTTYYVMCXAGBSZPJCVYSATEMAYOVOEWBPSLGXZLZBKZFNBWHIMEMGMSUZFMAYOTTVMNUDMLKMQXVMHTANUDMLEMQYCJJTTYYVZPXBBXSBEEMGMSYFXAGNCVLGLGMSGCXXRFHMOMPRNFICZCZJBBDMWUJFBSHCTMOAEAMLFZTDIWXJOBZGKRXVMQHCAIWBGXZLMOZOBVQJSLEHUNPSWFMMKFQBWREUFHBSXGFFWLEAMRCSKFMQBSSZDTZTZAMYMENXHPLMGBZQWFELAYQCEHNSFVMLWCAQSADMPRWSELLIOTRGEHKHYWBZYNSWCUEAIGMSPLWVRASZSTLGTRWDNKUFHPTGOOJTWCXIAIVMHTAAYUWTGOGTPMRBVNYVQDMQZJCNWBNRYVMVBVTXOZRNURSHELLBUFHIYRBUNBOEAIGMOLLAMNIQWFELOJPMSXIQJRIYWBUFHGZNERWSVEMWGFZSYHVFJBAPMPRVIMPGANWUCXXVGBOAEAIGNTAZFMGMWVRPIFSHLZGMNGCCEBBVSZMDLBUFBVZMQZJGPPWPNASMGXZLGCLJXFRHIBPWIYQFWFGLVYKIDMPVXZIDMZRROZVMPNYVIOFIQJHPPPPBQSXLKBLQCWVLWTWODPTVQFBFTHCFFZQNXKBZZLEAQAPCNYHBUNBOPEARYCALRJHYWBMXTBSUAEHBUJRCNAMFXMWFWJRYHMCTAXMSZLUWHYWBDAMFNBXCBABSHPPJCRJBALBLGTHPPXFRHIBTHVRWTMEVPUJFPPKMNSRBSXMKJQCEBWAJFEPGBBKTTTDMNSOZCHEGMSKLMAUJOLMXONSTIOBVTFKIJMPRRCUPGBUJKIDZWAJOVOUGGMSBTFMUJVIOVWZJPINDEVYVBSXLHHVMDLQGMOLPGBVWSTJWQFFDXPTZRIGWEAMXNBOLGLGMSMIXKHYWWYXZEFBETELYDIXLGLQT"

    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    #cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()
    #cipher = input()
    #cipher = cipher.replace("\n", "").replace(" ", "").upper()
    cipher = citext.replace("\n", "").replace(" ", "").upper()
    #################################################################
    # Your code to determine the key and decrypt the ciphertext here
    #print(cipher)
    #print((pop_var(citext)))
    #print(pop_var(alphabet))


solve_vigenere(cipher, True)