# codebreaker-analytics
This repository represents the AWS code to run data analytics for [codebreaker online judge](https://codebreaker.xyz).
___
Setup required:

- Installation of [botocore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html) package
- Installation of AWS Command Line Interface ([AWS CLI](https://aws.amazon.com/cli/)) and required login credentials to access the databases for codebreaker.

___
For the reference of future developers, here is the storage system for the judge. Database refers to [dynamoDB](https://docs.aws.amazon.com/dynamodb/index.html) and bucket refers to [S3](https://docs.aws.amazon.com/s3/index.html):

- Problem database "codebreaker-problems" 
- Contests database "codebreaker-contests" 
- Users database "codebreaker-users" 
- Submissions database "codebreaker-submissions" 
- Submissions bucket "codebreaker-submissions" (Stores `.cpp` submissions and binary compiled submissions for 2 days after submission)
- Testdata bucket "codebreaker-testdata" (Stores `.in` and `.out` testdata)
- Checkers bucket "codebreaker-checkers" (Stores binary checkers)
- Attachments bucket "codebreaker-attachments" (Stores `.zip` attachments)
- Statements bucket "codebreaker-statements" (Stores `.pdf` and `.html` statements)
- Graders bucket "codebreaker-graders" (Stores `.cpp` graders and `.h` header files)
- "codebreakers-submission-number" stores one single text file that indicates the number of submissions for faster assigning of subIds. 

___
Lambda Functions

- `codebreaker-problem-grader-3` grades submission through testcase grader `codebreaker-testcase-grader-2`. To facilitate parallel calls, the javascript function `evenmorecringe` is used.
- `codebreaker-problem-upload-2` syncs testcases from google drive, assisted by `codebreaker-testcase-upload` for parallel syncing. 
- `codebreaker-problem-verification` allows admin panel to check whether or not their problem is valid and can be deployed. `codebreaker-update-testcaseCount` allows admin panel to check the status of their testdata upload. 
- `stopcontestwindow` allows admin panel to stop the contest window for all contestants. 
- `codebreaker-submission-queue-response` assigns submission numbers to users' submissions  

___
Current files present in this repository:

- `date.py` helps to output the distribution of submissions with respect to date
- `rank.py` helps to generate a users ranking table based on analysis mode scores
- `submissions.py` helps to generate a list of users' submissions (to help ensure no users are maliciously submitting code)
