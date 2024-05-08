#!/bin/bash

name='jordan'
# set -x

echo $name

whoami

id

# set+x

age=21

echo $name is $age years old

#_________________comment


#parameter
param1=$2

echo $param1



# echo Enter your name:
# read name
# echo Your name is $name

# echo Enter age, weight, height
# read age weight height
# echo $age $weight $height



#arrays____________---

transport=('car' 'train' 'bike' 'bus')
echo "${transport[@]}"
echo "${transport[1]}"

unset transport[1]
echo "${transport[@]}"

transport[1]='trainride'
echo "${transport[@]}"


# echo enter name
# read name0
# read name1
# read name2

# names=($name0,$name1,$name2)
# echo all names are "${names[@]}"



#condointionals____________
count=$1
# count=10

if [ $count -eq 10 ]
then 
    echo 'True'

else 
    echo 'false'

fi





filename=$2

if [ -f "$filename" ] && [ -w "$filename" ]
then
    echo testestest >> $filename
    echo file overwritten
else
    touch "$filename"
    echo "testestest" > $filename
    echo file created
fi
