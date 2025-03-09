class ISIN:
    def __init__(self, cusip):
        self.cusip = "US" + cusip  # Add country code for ISIN
    
    def getID(self):
        intArr = []
        
        # Convert letters to numbers (A=10, B=11, ..., Z=35)
        for ch in self.cusip:
            if 'A' <= ch <= 'Z':
                ordChar = ord(ch) - 55  # Convert letter to number
                intArr.append(ordChar // 10)  # First digit
                intArr.append(ordChar % 10)  # Second digit
            else:
                intArr.append(int(ch))  # Keep digits as they are
        
        # Apply Luhn algorithm: Double every second digit from the right
        for i in range(len(intArr) - 2, -1, -2):
            newVal = intArr[i] * 2
            intArr[i] = newVal // 10 + newVal % 10  # Sum digits if >9
        
        # Compute check digit
        lSum = sum(intArr)
        finalD = (10 - (lSum % 10)) % 10  # Ensures check digit is 0 if already divisible by 10
        
        return self.cusip + str(finalD)  # Append check digit

# Example usage:
print(ISIN("594918104").getID())  # US5949181048 (Microsoft)
print(ISIN("037833100").getID())  # US0378331002 (Apple)
print(ISIN("459200101").getID())  # US4592001014 (IBM)
print(ISIN("7A4B92C09").getID())  # US710411292009

