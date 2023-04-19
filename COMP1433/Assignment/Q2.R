# Q2
#(a)
infile <- "./Assignment_data/Q2/train_tweets_new.txt"
tweets <- read.csv(infile, header = FALSE, sep = "\t",col.names=c("tweetID", "userID", "sentiment","text"))
head(tweets)



#(b)
library("tokenizers")
tokens <- tokenize_words(tweets$text)
tokens
tweets$tokens <- tokens


#(c)
vocab <- c()
tokens_unlist <- unlist(tokens)
tokens_table <- table(tokens_unlist)
words <- names(tokens_table)

for (i in 1:21673){
  x <- words[i]
  count <- 0
  for (j in 1:8021){
    if (x %in% tweets$tokens[[j]]){
      count = count + 1
      if (count > 3){
        vocab <- c(vocab, x)
        break
      }
    }
  }
}
print(count)
print(vocab)

#(d)
#positive/negative/neutral texts
positive_text <- c()
negative_text <- c()
neutral_text <- c()

for (i in 1:8021){
  if (tweets$sentiment[i] == 'positive'){
    x <- tweets$tokens[i]
    positive_text <- c(positive_text, x)
  }
  else if (tweets$sentiment[i] == 'negative'){
    x <- tweets$tokens[i]
    negative_text <- c(negative_text, x)
  }
  else {
    x <- tweets$tokens[i]
    neutral_text <- c(neutral_text, x)
  }
}

#positive/negative/neutral words
positive_words <- c()
negative_words <- c()
neutral_words <- c()

for (i in 1:8021){
  if (tweets$sentiment[i] == 'positive'){
    x <- tweets$tokens[i]
    positive_words <-c (positive_words, x)
  }
  else if (tweets$sentiment[i] == 'negative'){
    x <- tweets$tokens[i]
    negative_words <-c (negative_words, x)
  }
  else {
    x <- tweets$tokens[i]
    neutral_words <-c (neutral_words, x)
  }
}

# positive 
tokens_positive_text <- unlist(positive_words)
tokens_positive_text_table <- table(tokens_positive_text)
o_positive_words <- names (tokens_positive_text_table)

words_in_positive <- c()
for(i in 1:(length(positive_words))){
  x = vocab[i]
  for (j in 1:(length(positive_words))){
    if (x == o_positive_words[j]){
      words_in_positive <- c(words_in_positive, x)
    }
  }
}

#negative
tokens_negative_text <- unlist(negative_words)
tokens_negative_text_table <- table(tokens_negative_text)
o_negative_words <- names (tokens_negative_text_table)

words_in_negative <- c()
for (i in 1:(length(negative_words))){
  x = vocab[i]
  for (j in 1:(length(negative_words))){
    if (x == o_negative_words[j]){
      words_in_negative <- c(words_in_negative, x)
    }
  }
}

#neutral
tokens_neutral_text <- unlist(neutral_words)
tokens_neutral_text_table <- table(tokens_neutrale_text)
o_neutral_words <- names(tokens_neutral_text_table)

words_in_neutral <- c()
for (i in 1:(length(neutral_words))){
  x = vocab[i]
  for (j in 1:(length(neutral_words))){
    if (x == o_neutral_words[j]){
      words_in_neutral <- c(words_in_neutral, x)
    }
  }
}


#p-positive
positivedf <- data.frame()
wordsdf <- data.frame()
for (i in 1:(length(vocab))){
  if (vocab[i] %in% tokens_positive_text){
    number = tokens_positive_text_table[vocab[i]]
    p_positive = number / (length(o_positive_words) + length(vocab))
    wordsdf <- data.fram(p_positive)
    positivedf <- rbind(positivedf,wordsdf)
  }
  else {
      p_positive <- 1 / (length(o_positive_words) + length(vocab))
      wordsdf <- data.frame(p_positive)
      row.names(wordsdf) <- vocab[i]
      positivedf <- rbind(positivedf, wordsdf)
  }
}

#p-negative
negativedf <- data.frame()
wordsdf <- data.frame()
for (i in 1:(length(vocab))){
  if (vocab[i] %in% tokens_negative_text){
    number = tokens_negative_text_table[vocab[i]]
    p_negative = number/(length(o_negative_words)+length(vocab))
    wordsdf <- data.fram(p_negative)
    negativedf <- rbind(negativedf,wordsdf)
  }
  else {
      p_negative <- 1/(length(o_negative_words)+length(vocab))
      wordsdf <- data.frame(p_negative)
      row.names(wordsdf) <- vocab[i]
      negativedf <- rbind(negativedf,wordsdf)
  }
}

#p-neutral
neutraldf <- data.frame()
wordsdf <- data.frame()
for (i in 1:(length(vocab))){
  if (vocab[i] %in% tokens_neutral_text){
    number = tokens_neutral_text_table[vocab[i]]
    p_neutral = number/(length(o_neutral_words)+length(vocab))
    wordsdf <- data.frame(p_neutral)
    neutraldf <- rbind(neutraldf,wordsdf)
  }
  else {
      p_neutral <- 1 / (length(o_neutral_words)+length(vocab))
      wordsdf <- data.frame(p_neutral)
      row.names(wordsdf) <- vocab[i]
      neutraldf <- rbind(neutraldf,wordsdf)
  }
}


#tweet sentiment test
tweet1 <- "I love the banner that was unfurled in the United end last night. It read: Chelsea - Standing up against racism since Sunday"
tweet2 <- "So Clattenburg's alleged racism may mean end of his career; Terry, Suarez, Rio use it and can’t play for a couple of weeks?"
tweet3 <- "In our busy lives in Dubai could we just spare a moment of silence this Friday morning for the people who still wear crocs."

#tweet 1
token_tweet1 <- unlist(tokenize_words(tweet1))

#tweet 2
token_tweet2 <- unlist(tokenize_words(tweet2))

#tweet 3
token_tweet3 <- unlist(tokenize_words(tweet3))

tweet_list <- c(token_tweet1, token_tweet2, token_tweet3)
type <- c("positive","negative","neutral")


#likelihood
#tweet1
#tweet1 positive
log_p_positive <- 0
for (i in 1: (length(token_tweet1))) {
  for (j in 1:(length(vocab))) {
    if (token_tweet1[i] %in% vocab[j]) {
      print(positivedf[token_tweet1[i], ])
      log_p_positive = log_p_positive + log(positivedf[token_tweet1[i], ])
    }
  }
}
likelihood_positive_tweet1 <- (length(positive_text)/8021) + log_p_positive


# tweet1 negative 
log_p_negatve <- 0
for (i in 1: (length(token_tweet1))) {
  for (j in 1:(length(vocab))) {
    if (token_tweet1[i] %in% vocab[j]) {
      print(negativedf[token_tweet1[i], ])
      log_p_negative = log_p_negative + log(negativedf[token_tweet1[i], ])
    }
  }
}
likelihood_negative_tweet1 <- (length(negative_text)/8021) + log_p_negative


# tweet1 neutral 
log_p_neutral  <- 0
for (i in 1: (length(token_tweet1))) {
  for (j in 1:(length(vocab))) {
    if (token_tweet1[i] %in% vocab[j]) {
      print(neutraldf[token_tweet1[i], ])
      log_p_neutral = log_p_neutral + log(neutraldf[token_tweet1[i], ])
    }
  }
}
likelihood_neutral_tweet1 <- (length(neutral_text) / 8021) + log_p_neutral 



#tweet2
#tweet2 positive
log_p_positive <- 0
for (i in 1: (length(token_tweet2))) {
  for (j in 1:(length(vocab))) {
    if (token_tweet2[i] %in% vocab[j]) {
      print(positivedf[token_tweet2[i], ])
      log_p_positive = log_p_positive + log(positivedf[token_tweet2[i], ])
    }
  }
}
likelihood_positive_tweet2 <- (length(positive_text)/8021) + log_p_positive


# tweet2 negative 
log_p_negatve <- 0
for (i in 1: (length(tokens_tweet2))) {
  for (j in 1:(length(vocab))) {
    if (token_tweet2[i] %in% vocab[j]) {
      print(negativedf[token_tweet2[i], ])
      log_p_negative = log_p_negative + log(negativedf[token_tweet2[i], ])
    }
  }
}
likelihood_negative_tweet2 <- (length(negative_text)/8021) + log_p_negative


# tweet2 neutral 
log_p_neutral  <- 0
for (i in 1: (length(tokens_tweet2))) {
  for (j in 1:(length(vocab))) {
    if (token_tweet2[i] %in% vocab[j]) {
      print(neutraldf[token_tweet2[i], ])
      log_p_neutral = log_p_neutral + log(neutraldf[token_tweet2[i], ])
    }
  }
}
likelihood_neutral_tweet2 <- (length(neutral_text) / 8021) + log_p_neutral 



#tweet3
#tweet3 positive
log_p_positive <- 0
for (i in 1: (length(token_tweet3))) {
  for (j in 1:(length(vocab))) {
    if (token_tweet3[i] %in% vocab[j]) {
      print(positivedf[token_tweet3[i], ])
      log_p_positive = log_p_positive + log(positivedf[token_tweet3[i], ])
    }
  }
}
likelihood_positive_tweet3 <- (length(positive_text)/8021) + log_p_positive


# tweet3 negative 
log_p_negatve <- 0
for (i in 1: (length(tokens_tweet3))) {
  for (j in 1:(length(vocab))) {
    if (token_tweet3[i] %in% vocab[j]) {
      print(negativedf[token_tweet3[i], ])
      log_p_negative = log_p_negative + log(negativedf[token_tweet3[i], ])
    }
  }
}
likelihood_negative_tweet3 <- (length(negative_text)/8021) + log_p_negative


# tweet3 neutral 
log_p_neutral  <- 0
for (i in 1: (length(tokens_tweet3))) {
  for (j in 1:(length(vocab))) {
    if (token_tweet3[i] %in% vocab[j]) {
      print(neutraldf[token_tweet3[i], ])
      log_p_neutral = log_p_neutral + log(neutraldf[token_tweet3[i], ])
    }
  }
}
likelihood_neutral_tweet3 <- (length(neutral_text) / 8021) + log_p_neutral 


#result
tweet1_result <- c(likelihood_positive_tweet1, likelihood_negative_tweet1 , likelihood_neutral_tweet1)
tweet1_result_type <- which.max(tweet1_result)

tweet2_result <- c(likelihood_positive_tweet2, likelihood_negative_tweet2 , likelihood_neutral_tweet2)
tweet2_result_type <- which.max(tweet2_result)

tweet3_result <- c(likelihood_positive_tweet3, likelihood_negative_tweet3 , likelihood_neutral_tweet3)
tweet3_result_type <- which.max(tweet3_result)


print("The likelihood of observing each words in tweet1 is ")
print(type[tweet1_result_type])
print("The likelihood of observing each words in tweet2 is ")
print(type[tweet2_result_type])
print("The likelihood of observing each words in tweet3 is ")
print(type[tweet1_result_type])

