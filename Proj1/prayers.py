
import sys
import string
import itertools
from collections import Counter



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


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    print(freqs)
    
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)


ciphyer2 = "DPODKFHTNGCFAQWCKBQBCKQJKXLBQQQHVFCGLBJOFVKVYTPLQXVMMGVXLZAQQVLKDJPVMSOZQEUKTOQSPNBQPCPTVRKZKNKUZJGMWHAGSOHVKNKVBCXFKWPDMUWYGJHBKWFVQPQKOIVOUJPQYNMCEUVOQUCWJSUDJPVMSOZQEUKTOQSPNBQPCPTVRKZKNKUZJGMWHAGSOHVKNKVBCXFKWPDMUWYGJHBKWFVQPQKOIVOUJPQYNMCEUVOQUCWJSUDJPVMSOZQEUKTOQSPNBQPCPTVRKZKNKUZJGMWHAGSOHVKNKVBCXFKWPDMUWYGJHBKWFVQPQKOIVOUJPQYNMCEUVOQUCWJSU"
ciphyer = "VPGMSMIXKHYWWYXZZDGMWYANNRBSXSVSUMLZMEQMIYWPRMIZCBMQTTNLEQPJHPZNOUYGPPFQTMHIDPMYQUWMTKXFBLDXMUTKBSXONRSELLOBNBOZGIFXVMSXIEIHPPJCRJBAGHQPJWVEAMQNGBLGKRXQZPTUVSUETMPCFGATHVFMSPLWIYWSIORPRFFLSXZFJBBPGKRYVZPXWSYVMAEILJFAEHJRJLMNNBRITWCAIINBOXBAFJRBSXQEYIZYLIAIGPPWQQSCBWBSRYVMWHWXTTBSBVTXOBLETNXHPPZIZJKIDBVFZQPNHVSZGQZGBUFHASXVRASZVGMJBVMEAMENHELLPRWHCCGWESCBDHAUJKMYMQAXSICVPBKVMCAMQLSPZZBUJVMOZMUTUELLMALOOPWQAFTQRABJNHPLGWGMSZSXLTJVWRPPVHVAPXURIHWLEQPJOVPQKRQZMYMWCUCZENVVYMNZKKETECPMQALCVPHNGMSUHBBUYVMZMPRWHPPHVYDRQQYQPZZBJPIFYVIEAMEKZIXBVTTKIDZWAJOKCHAFYCBSXWGMSZDBLRTTBSXONWRMYPPRWSIWBKRHCCWWARJWBEKGVSUQYTPRQDTPLAFTFBZYENDHWQEGHUWVEHIGWSMMRBUJHQXXAUJVIOVIHLVBEAMSQOUTGOBFBLMKWHLVBTMJNHYBSXNVLVBHTABASZLGLOTHPEAMUJROPAWTXKMCXWHYCNDBOUYPCEBBQTSAYMUNYHMCFCPMHPZNOUYOTTVMNXOTWMPRFFKSXANWSOZGMSWCUEAQFXWLPHNGMSOCHCAIGWDAMGZQSPWQGFKIJNVQJFPPKIERHPLMQGRWOSMVBYSANTXRFUITGIAIKMYMJNHYNZKIYNHBWXUBWSKZGDRWGIEBWABWBSAMEKFQPGLJMSVDAMTTHJLVSGTHPPVPRXVQCXKNYGPPPIFXIZAKQFJRBZYQAIECTMMNQOZRXKETKLNHTYJQBPWZBZBLTMBUJFMHTANIWAANBRLCQYZWAGSBHXMAYVMPQMPZHQZGMEYVMVBVTFBLEAMDZSMYPPBBSZPTTYYOTVBVTFHWYVMJMWTPTTYYVMCXAGBSZPJCVYSATEMAYOVOEWBPSLGXZLZBKZFNBWHIMEMGMSUZFMAYOTTVMNUDMLKMQXVMHTANUDMLEMQYCJJTTYYVZPXBBXSBEEMGMSYFXAGNCVLGLGMSGCXXRFHMOMPRNFICZCZJBBDMWUJFBSHCTMOAEAMLFZTDIWXJOBZGKRXVMQHCAIWBGXZLMOZOBVQJSLEHUNPSWFMMKFQBWREUFHBSXGFFWLEAMRCSKFMQBSSZDTZTZAMYMENXHPLMGBZQWFELAYQCEHNSFVMLWCAQSADMPRWSELLIOTRGEHKHYWBZYNSWCUEAIGMSPLWVRASZSTLGTRWDNKUFHPTGOOJTWCXIAIVMHTAAYUWTGOGTPMRBVNYVQDMQZJCNWBNRYVMVBVTXOZRNURSHELLBUFHIYRBUNBOEAIGMOLLAMNIQWFELOJPMSXIQJRIYWBUFHGZNERWSVEMWGFZSYHVFJBAPMPRVIMPGANWUCXXVGBOAEAIGNTAZFMGMWVRPIFSHLZGMNGCCEBBVSZMDLBUFBVZMQZJGPPWPNASMGXZLGCLJXFRHIBPWIYQFWFGLVYKIDMPVXZIDMZRROZVMPNYVIOFIQJHPPPPBQSXLKBLQCWVLWTWODPTVQFBFTHCFFZQNXKBZZLEAQAPCNYHBUNBOPEARYCALRJHYWBMXTBSUAEHBUJRCNAMFXMWFWJRYHMCTAXMSZLUWHYWBDAMFNBXCBABSHPPJCRJBALBLGTHPPXFRHIBTHVRWTMEVPUJFPPKMNSRBSXMKJQCEBWAJFEPGBBKTTTDMNSOZCHEGMSKLMAUJOLMXONSTIOBVTFKIJMPRRCUPGBUJKIDZWAJOVOUGGMSBTFMUJVIOVWZJPINDEVYVBSXLHHVMDLQGMOLPGBVWSTJWQFFDXPTZRIGWEAMXNBOLGLGMSMIXKHYWWYXZEFBETELYDIXLGLQT"
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def keyoflength(n, nthletters):

    #for i in range(1,n+1):
        #nthletters = ciphyer[::n]
        #print(nthletters)

        all_freq = {}
        freq_ci = {}
        sum = 0.0
        listmult =[]

        for l in nthletters:

            if l in all_freq:

                all_freq[l] += 1
                
            else:
                all_freq[l] = 1
                freq_ci[l] = 1

        for l in alphabet:
            if l not in all_freq:
                all_freq[l] =0
                freq_ci[l] = 0        
                
        #print(all_freq)
        for l in all_freq:
            freq_ci[l] = all_freq[l] / float(len(nthletters))
        print(freq_ci)
        for i in range(len(freq_ci)):
            sum=0
            for l in freq_ci:
                #print(letter_freqs[l])
                #print(freq_ci[l])
                sum += (letter_freqs[l] * freq_ci[l])
                
            freq_ci = shift1(letter_freqs,freq_ci,n)
            #print(sum)
            listmult.append(sum)

        maxy = max(listmult)
        inmax = listmult.index(maxy)


        
        print(listmult)
        print(inmax)
        #print(freq_ci)
        #print(all_freq)
        return inmax


def shift1(alfreq, chifreq, n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    listy = []
    temp =0.0 
    #print(chifreq)
    for i in alphabet:
        if i in chifreq :
            listy.append(chifreq[i])

    #print(listy)   
    temp = listy[0] 

    for i in range(len(listy)-2):
        listy[i]  = listy[i+1] 
    listy[len(listy)-1] = temp   

    x =0
    for i in alphabet:
        if i in chifreq:
            chifreq[i]= listy[x]
            x += 1 
    #print(listy)   
    #print(chifreq)
    return chifreq


def helper(n):
    keyofn = []
    key =[]
    for i in range(n):
        nthletters = ciphyer2[i::n]
        keyofn.append(keyoflength(n ,nthletters))
    
    for i in keyofn:
        key.append(alphabet[i])
    #print(key)
    #print(keyofn)
    return(key)


############################
############################    #using encypt and decrypt function from https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4 
############################    #author dssstr 

def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]  
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext


############################
############################
############################





if __name__ == "__main__":
    keyl =[]
    #test = "VYBMTUMXLMBNVVRPMLNEQHLIGAEWMCMONTUQECSWPMZSBSJREHXBBHBMXEMOFSNAJPSIYDADPGJNTMABHFBVTPVBMNATEVHJTWHOWHCTGHDGCAUIGDMHNNINYMOMNBWJWZYBWHEOWJRWBLBFJBEXJISJHBTLWI"
    #print(len(test))
    #print(6.0 / len(test))
    #for i in range(2,14):
         
     #    keyl.append("".join(helper(i)))
    #for i in keyl:
     #   print(decrypt(ciphyer,i))
    print(keyl)
    helper(5)
    #print(decrypt(ciphyer,'GEARBOX'))
    print(decrypt('EHPFSFEBHMHPF', 'LTOBEORNOTTOB'))
    