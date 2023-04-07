# Given a string s, return the longest palindromic substring in s.

# A string U is a substring of a string T if there exist two strings P and S such that
# T = PUS. The empty string is a substring of every string
# P and S can be empty strings
#

def longest_subpal(s: str) -> str:
    s_values = {}
    for key, value in enumerate(s):
        s_values[key] = str(value)
    max_len = len(s_values)
    if max_len == 1:
        return s
    elif max_len == 0:
        return ""
    back = max_len - 1
    pal = ""
    pal_list = {}
    pal_len = 1
    for x in range(max_len):
        symbol = (s_values[x])
        pal_list[len(symbol)] = symbol
        if max_len - x <= pal_len:  # skipping all if len exceeds or equal half of max
            break
        if symbol not in s[:back]:  # skipping if not in left symbols slice
            back -= 1
            continue
        for y in range(x + 1, max_len):
            symbol = symbol + s_values[y]
            if len(symbol) <= pal_len:  # skipping palindrome check for lesser lengths
                continue
            for z in range(len(symbol)):
                if symbol[z] == symbol[(z * -1) - 1]:
                    pal = True
                    continue
                else:
                    pal = False
                    break
            if pal:
                pal_list[len(symbol)] = symbol
                pal_len = max(pal_list)
    return pal_list[pal_len]



test1 = "babad"
test2 = "cbbd"
test3 = "d"
test4 = "aa"
test5 = "d d"
test6 = "12344321"
test7 = "ac"
test8 = "boqylncwfahjzvawrojyhqiymirlkfzkhtvmbjnbfjxzewqqqcfnximdnrxtrbafkimcqvuprgrjetrecqkltforcudmbpofcxqdcirnaciggflvsialdjtjnbrayeguklcbdbkouodxbmhgtaonzqftkebopghypjzfyqutytbcfejhddcrinopynrprohpbllxvhitazsjeyymkqkwuzfenhphqfzlnhenldbigzmriikqkgzvszztmvylzhbfjoksyvfdkvshjzdleeylqwsapapduxrfbwskpnhvmagkolzlhakvfbvcewvdihqceecqhidvwecvbfvkahlzlokgamvhnpkswbfrxudpapaswqlyeeldzjhsvkdfvyskojfbhzlyvmtzzsvzgkqkiirmzgibdlnehnlzfqhphnefzuwkqkmyyejszatihvxllbphorprnyponircddhjefcbtytuqyfzjpyhgpobektfqznoatghmbxdouokbdbclkugeyarbnjtjdlaisvlfggicanricdqxcfopbmducroftlkqcertejrgrpuvqcmikfabrtxrndmixnfcqqqwezxjfbnjbmvthkzfklrimyiqhyjorwavzjhafwcnlyqob"
test9 = "lphntrsqudccteewsdmpjmgmfnxegawjclzobpnxdrvxeygafiwyqsvsecictqkmiqvrdjajfngvlhdezdpqpzjjzbhoyggrbkuzeocrpzqishvfairdvvabopyubfisxbrgnlughbrzunitwowvnsqhdtnkotitgxwzjhbgltksorygpdberdgzgvogrvwluhixfbrfhliedjylxuspjpitwlhdkneonreqrueqphirmgxtqumllqropaefddplspkrtkbmuvwkyryworojlvwzdlacuoqzokrmcgmwkopsbqjjkaoqjqbrderwzmhbhfgwvrjakyfeqcbtvlcgbsxkngymxyievihiskdmmppmmdksihiveiyxmygnkxsbgclvtbcqefykajrvwgfhbhmzwredrbqjqoakjjqbspokwmgcmrkozqoucaldzwvljorowyrykwvumbktrkpslpddfeaporqllmuqtxgmrihpqeurqernoenkdhlwtipjpsuxlyjdeilhfrbfxihulwvrgovgzgdrebdpgyrosktlgbhjzwxgtitokntdhqsnvwowtinuzrbhgulngrbxsifbuypobavvdriafvhsiqzprcoezukbrggyohbzjjzpqpdzedhlvgnfjajdrvqimkqtcicesvsqywifagyexvrdxnpbozlcjwagexnfmgmjpmdsweetccduqsrtnhpl"
test10 = "jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"
# print(longest_subpal(test1))
# print(longest_subpal(test2))
# print(longest_subpal(test3))
# print(longest_subpal(""))
# print(longest_subpal(test4))
# print(longest_subpal(test5))
# print(longest_subpal(test6))
# print(longest_subpal(test7))
# print(longest_subpal(test8))
# print(longest_subpal(test9))
print(longest_subpal(test10))


# fails:
#  - didn't count that palindrome is SYMBOL_ITSELF if len more than 1
#  - test8 failed but on SECOND try it works fine. Timelimit but no always. Hmmmm??
#  - test9 Timelimit
#  - test10 again works fine but TimeLimit overall