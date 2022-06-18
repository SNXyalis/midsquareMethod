class midsquare_method():


    #calculate Z according to midsquaremethod
    #parameter: 8 digit interger/string
    #return: 4 inner digits integer
    def getZ(self, z): 
        z = int(str(z)[2:-2]) #select 4 inner digits
        return z

    
    #transform 4 digits to 8
    #par: 4 digit integer seed
    def getZ8(self, z): 
        z = z ** 2

        while len(str(z)) < 8: #z_pow should have 8 digits
            z = "0" + str(z)
        return z

    #Calculate U of z
    #par: 4 or 8 digit integer
    #return: u
    def getU(self, z):
        u = int(z) / 10000
        return u

    #Print table i  Zi  Ui  Zi**2
    #par: Z seed, R range
    #return: -
    def getTable(self, z, r):
        print("i", "Zi", "Ui", "Zi**2", sep='\t')

        print(0, z, "- ", self.getZ8(z), sep='\t')
    
        z = self.getZ( self.getZ8(z) )

        for i in range(1, r):

            print(i, str(z).zfill(4), format(self.getU(z), ".4f"), self.getZ8(z), sep='\t')

            z = self.getZ(self.getZ8(z))
        return 


x = midsquare_method()
x.getTable(7182, 16)
