class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        heaviest = len(people)-1
        lightest = 0
        boats = 0
        
        while lightest <= heaviest:
            if(people[lightest] > limit):
                break
            elif(lightest == heaviest and people[lightest]<=limit):
                boats+=1
                heaviest-=1
            elif(people[lightest]+people[heaviest]<= limit):
                boats+=1
                lightest+=1
                heaviest-=1
            elif(people[heaviest] <= limit):
                boats+=1
                heaviest-=1
            print(heaviest,lightest,boats)


        return boats
            
