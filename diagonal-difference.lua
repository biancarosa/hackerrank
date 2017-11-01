// PROBLEM: https://www.hackerrank.com/challenges/diagonal-difference/problem
n = io.read("*number", "*l")
a = {}
for a_i = 1,n do
   a_temp = io.read()
   a_j = 1
   a[a_i] = {}
   for token in string.gmatch(a_temp, "[^%s]+") do
      a[a_i][a_j] = token
      a_j = a_j + 1
   end
end
sum = 0
sum2 = 0
for x = 1,n do
    sum = sum + a[x][x]
    sum2 = sum2 + a[x][n+1-x] 
end
print(math.floor(math.abs(sum-sum2)))