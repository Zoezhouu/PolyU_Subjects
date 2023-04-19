##estimating pi
no_of_points = 1000

#runif samples from a uniform distribution
x = runif(no_of_points,-1,1)
y = runif(no_of_points,-1,1)

#compute distance of each point from (0,0)
distance = sqrt(x^2+y^2)

#boolean vector to indicate if each point is within the circle
within_circle = ifelse(distance<1,TRUE,FALSE)

#comute proportion of points within circle/outside circle with table()
v=table(within_circle)

#compute and print PI
pi = v["TRUE"]/(v["TRUE"]+v["FALSE"])*4
print(pi)


## simulating product demand
> x=c(10000,20000,40000,60000)
> probability = c(0.1,0.35,0.3,0.25)
> demand = sample(x,100,replace = TRUE, prob = probability)
> barplot(table(demand))
> sum(demand)
[1] 3590000




## simulating coin flipping
> n = 10 #no. of coin flips
> k = 4  #no. of heads
> runs = 10000 #no. of trials
> 
> #one trial simulates the flipping of a coin for 10 times
> trial = function(){
+ sum(sample(c(0,1),n,replace = TRUE))} # of heads

#conduct trials 10000 times
> result = replicate(runs,trial())
> t=table(result)
> print(t)
result
   0    1    2    3    4    5    6    7    8    9   10 
  13  119  461 1184 2007 2426 2075 1161  451   93   10 

#conduct trials 10000 times
result = replicate(runs,trial())
t=table(result)
barplot(table(result))
barplot(table(result)/runs) #probability

# binomial distribution
# dbinom(x,size,prob)
# pbinom(q,size,prob,lower.tail)

#stock price prediction