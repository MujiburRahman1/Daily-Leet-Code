class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0  # Start altitude 0 hai
        highest = 0   # Sabse syada altitude ko track karne ke liye

        for g in gain:  # Gain array ke har element par loop
            altitude += g  # Current altitude update karo 
            highest = max(highest, altitude)  # Sabse zyada altitude ko check karo

        return highest   # final highest altitude return karo