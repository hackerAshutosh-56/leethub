class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product=1
            for i in (str(n)):
                product*=int(i)
            if product%t==0:
                return n
            n=n+1        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna