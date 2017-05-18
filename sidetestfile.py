import math

# formula used to solve this
# logbaseX {I(p)/sqrt(n)} x X^m = M
"""
- - - -
- - - -
- m - -
- - - p
"""
"""
----
----
-m--
---p
"""



def ini(first_input):
    moveslist = []
    # ask first sec and third input


    # insert them into to a list
    list = []
    list.append(first_input)

    # create second list to furthr down list's list with a loop
    list2 = []

    for every_thing in list:
        for every_atom in every_thing:
            list2.append(every_atom)
    size_of_list2 = len(list2)
    sqrrt = math.sqrt(size_of_list2)
    # creat a list to match every atom in list2 with  number
    number_match_list = []
    i = 0

    try:
        for _ in list2:
            i += 1
            number_match_list.append(i)
        how_far_m_from_end = (size_of_list2 - list2.index('m'))
        how_far_p_from_end = (size_of_list2 - list2.index('p'))
        p_index = list2.index('p')
        m_index = list2.index('m')
        kmr = (list2.index('m') // sqrrt) + 1
        kpr = (list2.index('p') // sqrrt) + 1

        if kmr > kpr:
            print('up by2', kmr - kpr, 'steps')
            [moveslist.append("up") for _ in range(int(kmr - kpr))]

        elif kmr < kpr:

            print('down by1', kpr - kmr, 'steps')
            [moveslist.append("down") for _ in range(int(kpr - kmr))]

        temp = 0
        tt = list2.index('m')
        kttr = (tt // sqrrt) + 1


        if kpr * sqrrt != p_index:
            kpc = sqrrt - ((kpr * sqrrt) - p_index)

        else:
            kpc = sqrrt * kpr
        if kmr * sqrrt != p_index:
            kmc = sqrrt - ((kmr * sqrrt) - m_index)

        else:
            kmc = sqrrt * kmr

        # if kpc != kmc and kpr != kmr:
        #     if kpc > kmc:
        #         print('right by23', kpc - kmc, 'steps')
        #         [moveslist.append("right") for _ in range(int(kpc - kmc))]
        #     if kmc > kpc:
        #         print('left by34', kmc - kpc, 'steps')
        #         [moveslist.append("left") for _ in range(int(kmc - kpc))]

        if kpr == kmr:
            if tt > p_index:
                print('left by', m_index - p_index, 'steps')

                [moveslist.append("left") for _ in range(int(m_index - p_index))]

                print(moveslist, "6m")
                return moveslist  #ini()

            else:
                print('right by', p_index - m_index, 'steps')
                [moveslist.append("right") for _ in range(int(p_index - m_index))]

                print(moveslist, "5m")
                return moveslist  #ini()



        else:
            while temp < sqrrt:
                temp += 1

                if kpr > kmr:
                    tt += sqrrt
                    kttr = (tt // sqrrt) + 1

                    if kttr == kpr:
                        if p_index > tt:
                            print('right by', p_index - tt, 'steps')
                            [moveslist.append("right") for _ in range(int(p_index - tt))]

                            print(moveslist,"4m")
                            return moveslist#ini()


                        elif p_index < tt:
                            print('left by', tt - p_index, 'steps')
                            [moveslist.append("left") for _ in range(int(tt - p_index))]
                            print(moveslist,"3m")
                            return moveslist  #ini()


                else:
                    tt -= 4
                    kttr = (tt // sqrrt) + 1

                    if kttr == kpr:
                        if p_index > tt:
                            print('right by', p_index - tt, 'steps')
                            [moveslist.append("right") for _ in range(int(p_index - tt))]

                            print(moveslist,"2m")
                            return moveslist  #ini()

                        elif p_index < tt:
                            print('left by', tt - p_index, 'steps')
                            [moveslist.append("left") for _ in range(int(tt - p_index))]

                            print(moveslist,"1m")
                            return moveslist  #ini()

        print(moveslist)

    except ValueError:
        print('Value Error guy!')
        # ini()
    return moveslist

# ini()