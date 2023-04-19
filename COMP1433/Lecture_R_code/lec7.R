# install.packages("ggplot2") # nolint
# library("ggplot2") # nolint


###Barplot

#define chart
quiz = c(100,80,70,20,80)
exam = c(80,30,90,40,90)
name = c("Peter","Kenny","Tom","Tiffany","Susanna")
gender = c("male","male","male","female","female")
student_id = c(1:5)
record = data.frame(student_id,name,gender,quiz,exam)
ggplot(record,aes(x=gender))

# #frequency for student gender
# > chart<-ggplot(record,aes(x=gender))
# > bars<-geom_bar(fill="blueviolet",color="black")
# > chart+bars

# #frequency for student gender with label
# > xlabel<-xlab("Student's gender")
# > ylabel<-ylab("Frequency")
# > title<-ggtitle("Frequency Distribution of students' Gender")
# > chart+bars+xlabel+ylabel+title

# #scores for each students
# > ggplot(record,aes(x=name,y=quiz))+geom_bar(fill="blueviolet",color="black",stat="identity")+xlab("Student")+ylab("Quiz Mark")+ggtitle("Quiz marks for student")

# #with each gender, we breakdown the data into different students(with different color)
# > ggplot(record,aes(x=gender,y=quiz,fill=name))+geom_bar(color="black",stat="identity")+xlab("Student")+ylab("Quiz Mark")+ggtitle("Quiz marks for student")

# #creat interleaved bars
# > ggplot(record,aes(x=gender,y=quiz,fill=name))+geom_bar(color="black",stat="identity",position = "dodge")+xlab("Student")+ylab("Quiz Mark")+ggtitle("Quiz marks for student")



# ###Histogram



