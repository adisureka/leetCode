import numpy as np
class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        
        # Python has built in functions to sort easily
        # heroes.sort()
        # monsters.sort()
        # print(heroes)
        # print(monsters)

        # def sort_index(lst):
        #     d = []
        #     for i in range(len(lst)):
        #         d.append([lst[i], i])
        #     return d
        # # print(sort_index(heroes))
        # # print(sort_index(monsters))
        # my_heroes = sort_index(heroes)
        # my_heroes.sort()
        # # print(my_heroes)

        hero_index = np.argsort(heroes)
        # print(hero_index)
        monster_index = np.argsort(monsters)
        # coin_index = np.argsort(coins)
        # print(monster_index)
        # print(coin_index)

        # sort coins by monster order
        heroes.sort()
        monsters.sort()
        coins = np.array(coins)[monster_index]
        # print(coins)
        # print(heroes)
        # print(monsters)
        # pointers for binary search
        left = 0
        right = 0
        # counter for loot
        loot = 0
        # list counter to hold thhe loot per hero
        bounty = []
        # not working as hero 2 is not taking into the loot for hero 1
        for i in range(len(heroes)):
            while(right < len(monsters) and heroes[i] >= monsters[right]):
                right += 1
            loot += sum(coins[left:right])
            bounty.append(loot)
            # since the hero list is sorted, wee need to move to the next hero who we know shall defeat the monsters the previous hero defeated as they are sorted on combat power
            left = right
        print(bounty)
        print(hero_index)

        # reverse the collected coins now to the hero list
        origional_index = np.argsort(hero_index)
        return(np.array(bounty)[origional_index])

        # Solves for 703 testcases

        # hero = heroes[0]
        # index = []
        # loot = 0
        # hero_bounty = []
        # # monster = monsters[0]

        # for j in range(len(heroes)):

        #     # This is the code for a single hero
        #     for i in range(len(monsters)):
        #         if(heroes[j] >= monsters[i]):
        #             loot += coins[i]
        #             print(monsters[i], coins[i])
        #     # this is working
        #     hero_bounty.append(loot)
        #     loot = 0
            
        # return(hero_bounty)


        