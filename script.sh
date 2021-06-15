#!/bin/bash
read -p "Enter Problem Name: "  problemName
echo "Gathering files for $problemName"

mkdir $problemName
cd $problemName
# Testdata, recursive since getting folder
aws s3 cp s3://codebreaker-testdata/$problemName testdata --recursive 

# If grader exists
aws s3 cp s3://codebreaker-graders/$problemName/grader.cpp grader.cpp
aws s3 cp s3://codebreaker-graders/$problemName/$problemName.h $problemName.h

# If checker exists
aws s3 cp s3://codebreaker-checkers/source/$problemName.cpp checker.cpp

# If attachments exists
aws s3 cp s3://codebreaker-attachments/$problemName.zip attachments.zip

# Statement
aws s3 cp s3://codebreaker-statements/$problemName.pdf statement.pdf
aws s3 cp s3://codebreaker-statements/$problemName.html statement.html

cd ..
zip -r $problemName.zip $problemName