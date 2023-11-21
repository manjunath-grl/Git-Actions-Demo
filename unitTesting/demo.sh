#!/bin/bash


declare -a filesChanged
filesChanged=("samplePythonfiles/demo_1.py" "samplePythonfiles/demo_3.py" "samplePythonfiles/demo_5.py" "samplePythonfiles/demo_6.py" "samplePythonfiles/demo_2.py" )

declare -a tests_list
tests_list=("samplePythonfiles/demo_1.py" "samplePythonfiles/demo_2.py")

text="samplePythonfiles/"

for key in "${!tests_list[@]}" ;
do
   #echo "tests_list: "${tests_list[$key]} "and index:" $key
   for value in "${!filesChanged[@]}" ;
   do
       #echo "filesChanged: "${filesChanged[$value]} "and index:" $value
       if [[ ${filesChanged[$value]} == ${tests_list[$key]} ]] ;
       then
           test=${tests_list[$key]}
           test_name="${test#*$text}"
           #echo ${test_name}
           #Runs unit tests
           python3 -m unittest ${test_name} -v
           break
       fi
   done
done
