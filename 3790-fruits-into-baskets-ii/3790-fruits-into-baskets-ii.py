class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        F = len(fruits)     # fruits ki total quantity
        B = len(baskets)    # baskets ki total quantity
        used = [False] * B  # har basket pehle unused hai
        count = 0           # unplaced fruits count karne ke liye

        for i in range(F):          # har fruit ke liye
            for j in range(B):      # har basket check karo
                if not used[j] and fruits[i] <= baskets[j]:  # agar basket empty ho aur fruit fit aa jaye
                    used[j] = True     # basket ab use ho gayi
                    break              # agli fruit pe chalo
            else:
                count += 1  # koi bhi basket available nahi thi, fruit place nahi ho saka

        return count  # jitne fruits place nahi ho sake
