##simulate standard normal random numbers
> x<-rnorm(10)
> x
 [1] -1.2416951 -0.5271872  0.1598143  0.2418747  1.3654045 -0.4488002 -0.5551028  1.9699810 -1.4626256 -0.7058569

## generate random number from N(20,2^2)
> x<-rnorm(10,20,2)
> x
 [1] 21.15729 21.57717 24.92311 20.72628 16.77985 20.58035 17.21989 18.28065 20.37361 19.79298
> summary(x)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  16.78   18.66   20.48   20.14   21.05   24.92 

##random number seed
# initialize a pseudorandom number generator as a starting point
> set.seed(1)
> rnorm(5)
[1] -0.6264538  0.1836433 -0.8356286  1.5952808  0.3295078
> rnorm(5)
[1] -0.8204684  0.4874291  0.7383247  0.5757814 -0.3053884

##Simulating a Linear model
> set.seed(20)##always set your seed!
> x<-rnorm(100) # simulate predictor variable
> e<-rnorm(100,0,2)  #simulate the error term
> y<-0.5+2*x+e   #compute the outcome via model
> summary(y)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
-6.4084 -1.5402  0.6789  0.6893  2.9303  6.5052 
> plot(x,y)  ## draw scatter plot

#simulate binary random variable
> set.seed(!0)
> x=rbin(100,1,0.5)
# Error in rbin(100, 1, 0.5) : 没有"rbin"这个函数
> x=rbinom(100,1,0.5)
> str(x)
 int [1:100] 0 0 1 1 0 1 1 1 1 0 ...
 
> ## proceed the rest
> e=rnorm(100,0,2)
> y = 0.5+2*x+e
> plot(x,y)

##Random sampling
#sample numbers
> set.seed(1)
> sample(1:10,4)
[1] 9 4 7 1
> sample(1:10,4)
[1] 2 7 3 6

sample letters
> sample(letters,5)
[1] "r" "s" "a" "u" "w"

# random permutation
> sample(1:10)
 [1] 10  6  9  2  1  5  8  4  3  7
> sample(1:10)
 [1]  5 10  2  8  6  1  4  3  9  7

#sample with replacement
> sample(1:10,replace = TRUE)
 [1]  3  6 10 10  6  4  4 10  9  7
> 

> library(datasets)
> data(airquality)
> head(airquality)
  Ozone Solar.R Wind Temp Month Day
1    41     190  7.4   67     5   1
2    36     118  8.0   72     5   2
3    12     149 12.6   74     5   3
4    18     313 11.5   62     5   4
5    NA      NA 14.3   56     5   5
6    28      NA 14.9   66     5   6

> set.seed(20)

> ##index vector
> idx=seq_len(nrow(airquality))   ##a vector from 1 to 153(recorded number)

> ##sample from index vector
> samp = sample(idx,6)    ##generate 6 random number

> airquality[samp, ]   ## sample 6 rows according to random number generated
    Ozone Solar.R Wind Temp Month Day
107    NA      64 11.5   79     8  15
120    76     203  9.7   97     8  28
130    20     252 10.9   80     9   7
98     66      NA  4.6   87     8   6
29     45     252 14.9   81     5  29
45     NA     332 13.8   80     6  14

