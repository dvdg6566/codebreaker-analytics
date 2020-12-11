# codebreaker-analytics
This repository represents the AWS code to run data analytics for <a href="https://codebreaker.xyz"> codebreaker online judge</a>.

Setup required:
<ul>
	<li>Installation of <a href="https://botocore.amazonaws.com/v1/documentation/api/latest/index.html">botocore</a> package</li>
	<li>Installatino of AWS Command Line Interface (<a href="https://aws.amazon.com/cli/">AWS CLI</a>) and required login credentials to access the databases for codebreaker.
</ul>

For the reference of future developers, here is the storage system for the judge. Database refers to <a href="https://docs.aws.amazon.com/dynamodb/index.html"> dynamoDB</a> and bucket refers to <a href="https://docs.aws.amazon.com/s3/index.html">S3</a>:
<ul>
	<li> Problem database "codebreaker-problems" </li>
	<li> Contests database "codebreaker-contests" </li>
	<li> Users database "codebreaker-users" </li>
	<li> Submissions database "codebreaker-submissions" </li>
	<li> Submissions bucket "codebreaker-submissions" (Stores ```.cpp``` submissions and binary compiled submissions for 2 days after submission)</li>
	<li> Testdata bucket "codebreaker-testdata" (Stores ```.in``` and ```.out``` testdata)</li>
	<li> Checkers bucket "codebreaker-checkers" (Stores binary checkers)</li>
	<li> Attachments bucket "codebreaker-attachments" (Stores ```.zip``` attachments)</li>
	<li> Statements bucket "codebreaker-statements" (Stores ```.pdf``` and ```.html``` statements)</li>
	<li> Graders bucket "codebreaker-graders" (Stores ```.cpp``` graders and ```.h``` header files)</li>
	<li> "codebreakers-submission-number" stores one single text file that indicates the number of submissions for faster assigning of subIds. </li>
</ul>

Lambda Functions
<ul>
	<li> ```codebreaker-problem-grader-3``` grades submission through testcase grader ```codebreaker-testcase-grader-2```. To facilitate parallel calls, the javascript function ```evenmorecringe``` is used.</li>
	<li> ```codebreaker-problem-upload-2``` syncs testcases from google drive, assisted by ```codebreaker-testcase-upload``` for parallel syncing. </li>
	<li> ```codebreaker-problem-verification``` allows admin panel to check whether or not their problem is valid and can be deployed. ```codebreaker-update-testcaseCount``` allows admin panel to check the status of their testdata upload. </li>
	<li> ```stopcontestwindow``` allows admin panel to stop the contest window for all contestants. </li>
	<li> ```codebreaker-submission-queue-response``` assigns submission numbers to users' submissions </li> 
</ul>

Current files present in this repository:
<ul> 
	<li	>```date.py``` helps to output the distribution of submissions with respect to date
	</li>
	<li> ```rank.py``` helps to generate a users ranking table based on analysis mode scores
	</li>
	<li> ```submissions.py``` helps to generate a list of users' submissions (to help ensure no users are maliciously submitting code)
</ul>