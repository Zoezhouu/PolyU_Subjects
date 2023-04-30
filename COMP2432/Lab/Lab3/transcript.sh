#!/bin/bash
# ./transcript namesOfSubjectFiles .... student(marker) studentID

position=0
courseInfo=()
courseGrade=()
datafile=()
input_id=()
id_name=()

getGrade(){
    grades=() # array for grades
    for file in "${datafile[@]}"; do
        # read -r -p "${input_id[@]}"
        grep -q "$ID" "$file"
        if ! grep -q "$ID" "$file"; then
            continue
        fi

        # read lines in file to array
        fileContent=()
        while read -r line; do
            fileContent+=("$line")
        done < "$file"
        # echo "File content: ${fileContent[*]}"
        # echo "File content: ${fileContent[0]}"
        # echo "File content: ${fileContent[@]:1}"


        # split fileContents[0] - first line array(course information)
        read -r -a courseInfo <<< "${fileContent[0]}"
        # rest of them
        read -r -a courseGrade <<< "${fileContent[@]:1}"

        # loop go through courseInfo array
        indexInfo=0
        
        for element in "${courseInfo[@]}"; do
            if [ "$element" == "Subject" ]; then
                printf " "
            elif [ "$indexInfo" == 3 ]; then
                gradeIndex=0
                printf "Sem $element\t"
                # loop go through courseGrade
                for grade in "${courseGrade[@]}"; do
                    if [ "$grade" == "$ID" ]; then
                        grade_level="${courseGrade[$gradeIndex+1]}"
                        grades+=("$grade_level")
                        if [[ 
                        ("$grade_level" = "A+") || ("$grade_level" = "A") || ("$grade_level" = "A-") || 
                        ("$grade_level" = "B+") || ("$grade_level" = "B") || ("$grade_level" = "B-") || 
                        ("$grade_level" = "C+") || ("$grade_level" = "C") || ("$grade_level" = "C-") ||
                        ("$grade_level" = "D+") || ("$grade_level" = "D") || ("$grade_level" = "F")]]; then
                            printf "$grade_level\t"
                        else
                            continue
                        fi
                    fi
                    gradeIndex=$((gradeIndex+1))
                done
            else
                printf "$element\t"
            fi
            indexInfo=$((indexInfo+1))
        done
        printf "\n"         
    done

    # loop through grades array(convert to numbers)
    integer_gpa=0 # convert to integer(integer calc)
    numberOfSubject="${#grades[@]}"

    for grade in "${grades[@]}"; do
        case "$grade" in
            "A+") ((integer_gpa+=430));;
            "A" ) ((integer_gpa+=400));;
            "A-") ((integer_gpa+=300));;
            "B+") ((integer_gpa+=330));;
            "B" ) ((integer_gpa+=300));;
            "B-") ((integer_gpa+=270));;
            "C+") ((integer_gpa+=230));;
            "C" ) ((integer_gpa+=200));;
            "C-") ((integer_gpa+=170));;
            "D+") ((integer_gpa+=130));;
            "D" ) ((integer_gpa+=100));;
            "F") numberOfSubject=$((numberOfSubject-1));;
            *) numberOfSubject=$((numberOfSubject-1))
            continue
        esac
    done
    
    printf " GPA for %s subjects \t" "$numberOfSubject"
    # echo $integer_gpa
    GPA_number=$(($integer_gpa / $numberOfSubject))
    echo "scale=2;$GPA_number/100"| bc
}


# Loop through the given args looking for "student" keyword
for arg in "$@"; do
    if [ "$arg" == "student" ]; then
        # echo "The 'student' argument is in position $position"
        break
    fi
    position=$((position + 1))   
done
# echo "Position of 'student': $position"

# store all data file from given args in array(data)
for filename in "${@:1:$position}"; do
    if grep "*" "$filename"; then
        datafile=($(find -name "$filename.dat"))
        break
    else
        datafile+=("$filename")
    fi 
done
# echo "input file name: ${datafile[*]}"

# store input student ID in input_id array
for arg in "${@:$position+2:$#}"; do
    input_id+=("$arg")
done
# echo "input student ID: ${input_id[*]}"


# loop through every ID, student.dat,store in id_name
# printf "Lines:"
while read -r line; do
    id_name+=("$line")
    # printf "$line"
done < "student.dat"
# echo "id_name array:"
# echo "${id_name[@]}"

for ID in "${input_id[@]}"; do
    i=0
    for info in "${id_name[@]}"; do
        if [ "$i" -ge "${#id_name[@]}" ]; then
            break
        fi
        read -r -a all_value <<< "${id_name[$i]}"
        if [ "$all_value" == "$ID" ]; then
            printf "Transcript for %s \n" "${id_name[i]}"
            # echo "get grade here:..."
            getGrade # export transcript
            printf "\n"
        fi
        i=$((i+1))
    done
done