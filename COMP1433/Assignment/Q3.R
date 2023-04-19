library("ggplot2")
infile <- "./Assignment_data/Q3/points.txt"
data <- read.table(infile, header = FALSE, sep = ",")
head(data)

# x, y, points, distance
x <- c(data$V1)
y <- c(data$V2)
point <- data.frame(x,y)

distance_a <- c()
distance_b <- c()
distance_c <- c()

# (0,100)
for (i in 1:90) { 
    xa = 0
    ya = 100
    x_variable <- x[i]
    y_variable <- y[i]
    da = sqrt((x_variable-xa)^2+(y_variable-ya)^2)
    distance_a <- c(distance_a,da)

}

#(40, 40)
for (i in 1:90) { 
    xb = 40
    yb = 40
    x_variable <- x[i]
    y_variable <- y[i]
    db = sqrt((x_variable-xb)^2+(y_variable-yb)^2)
    distance_b <- c(distance_b,db)
}

#(100, 0)
for (i in 1:90) { 
    xc = 100
    yc = 0
    x_variable <- x[i]
    y_variable <- y[i]
    dc = sqrt((x_variable-xc)^2+(y_variable-yc)^2)
    distance_c <- c(distance_c,dc)
}


count_a <- c()
count_b <- c()
count_c <- c()
point$type <- c()
col <- c()

# compare distance
for(i in 1:90) {
  if (distance_a[i] > distance_b[i]) {
    if (distance_b[i] > distance_c[i]) {
      col <- c(col, "c")
      count_c <- c(count_c, i)
    } 
    else if (distance_b[i] < distance_c[i]) {
      col <- c(col, "b")
      count_b <- c(count_b, i)
    }
  } 
  else if (distance_a[i] < distance_b[i]){
    if (distance_a[i] > distance_c[i]) {
      col <- c(col, "c")
      count_c <- c(count_c, i)
    } 
    else if (distance_a[i] < distance_c[i]) {
      col <- c (col, "a")
      count_a <- c(count_a, i)
    }
  }  
}



#iteration 999 times
for (q in 1:999){
  # a
  sum_x <- 0
  sum_y <- 0
  for (j in 1: (length(count_a))){
    sum_x = sum_x + x[count_a[j]]
    sum_y = sum_y + y[count_a[j]]
  }
  xa = sum_x / j
  ya = sum_y / j

  #b
  sum_x <- 0
  sum_y <- 0
  for (j in 1:(length(count_b))){
    sum_x = sum_x + x[count_b[j]]
    sum_y = sum_y + y[count_b[j]]
  }
  xb = sum_x / j
  yb = sum_y / j

  #c
  j <- 1
  sum_x <- 0
  sum_y <- 0
  for (j in 1:(length(count_c))){
    sum_x = sum_x + x[count_c[j]]
    sum_y = sum_y + y[count_c[j]]
    j = j + 1
  }
  xc = sum_x / j
  yc = sum_y / j

  distance_a <- c()
  distance_b <- c()
  distance_c <- c()

  #a
  for (i in 1:90) {
    x_variable <- x[i]
    y_variable <- y[i]
    d_a = sqrt((x_variable-xa)^2+(y_variable-ya)^2)
    distance_a <- c(distance_a, d_a)
  }

  #b
  for (i in 1:90) {
      x_variable <- x[i]
      y_variable <- y[i]
      d_b = sqrt((x_variable-xb)^2+(y_variable-yb)^2)
      distance_b <- c(distance_b, d_b)
  }

  #c
  for (i in 1:90){
      x_variable <- x[i]
      y_variable <- y[i]
      d_c = sqrt((x_variable-xc)^2+(y_variable-yc)^2)
      distance_c <- c(distance_c, d_c)
  }


  count_a <- c()
  count_b <- c()
  count_c <- c()
  point$type <- c()
  col <- c()
  

  for(i in 1:90) {
    if (distance_a[i] > distance_b[i]) {
      if (distance_b[i] > distance_c[i]) {
        col <- c(col, "c")
        count_c <- c(count_c, i)
      } 
      else if (distance_b[i] < distance_c[i]) {
        col <- c(col, "b")
        count_b <- c(count_b, i)
      }
    } 
    else if (distance_a[i] < distance_b[i]){
      if (distance_a[i] > distance_c[i]) {
        col <- c(col, "c")
        count_c <- c(count_c, i)
      } 
      else if (distance_a[i] < distance_c[i]) {
        col <- c(col, "a")
        count_a <- c(count_a, i)
      }
    }  
  }
}

point$type <- c(col)

graph <- ggplot(point, aes(x, y, color = type)) + geom_point(size = 1)

print(graph)