# Given co-ordinates of a room (X, Y, Z) check if room is safe
# Room is NOT safe if any co-ordinate of room is prime number or 
# the sum of its digits is prime

class Room:
    def __init__(self, coords):
        self.coords = coords
    
    def isPrime(self, number):
        # Better way to check for prime numbers
        # Primality test
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i*i <= number:
            if number%i == 0 or number%(i+2) == 0:
                return False
            i += 6
        return True        

        # if number == 1:
        #     return False
        # for i in range(2, number - 1):
        #     if number % i == 0:
        #         return False
        # return True    


    def getSumOfDigits(self, number):
        sumDigits = 0
        while number // 10 != 0:
            sumDigits += number % 10
            number = number // 10
        sumDigits += number % 10
        return sumDigits
    
    def isSafe(self):
        for i in range(0, len(self.coords)):
            # print self.isPrime(self.coords[i])
            # print self.getSumOfDigits(self.coords[i])
            if not self.isPrime(self.coords[i]) and not self.isPrime(self.getSumOfDigits(self.coords[i])):
                continue
            else:
                print "Room is not safe!"
                return 
        print "Room is safe."


if __name__ == '__main__':
    r = Room([55, 10, 99])
    r.isSafe()
    r = Room([55, 10, 98])
    r.isSafe()
    r = Room([52, 13, 99])
    r.isSafe()
