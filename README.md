# CTC Coding Challenge 2020

At Code the Change, we're dedicated to high-quality and efficient engineering practices to build great technology for nonprofits.

To achieve this goal, our project teams organize our work into sprints. A sprint is a time period (usually 1 week) during which every member on a team is assigned a ticket (coding task) to complete. Sprints help us rapidly iterate on the product and ensure we are always making forward progress. If you're not familiar with this, think of it like a to-do list for multiple teams!

You will be building a simplified sprint planner. Your program will take in a list of tickets in our proprietary CTC format and output a sprint plan for the semester.

A ticket has a ticket ID, a description, a team ID (0, 1, ...), a priority level (LOW, MED, or HIGH), and optionally, a sprint ID, which corresponds to the sprint number during which the relevant team should complete that ticket (0 = 1st sprint, 1 = 2nd sprint, etc.).

The input ticket format will be as follows: <ticket ID>/ <description>/ <team ID>/ <priority>.

For the sprint plan, you should figure out which tickets will be completed during which sprints and print out the tickets, in order of the sprint number during which they will be completed. You should append the sprint ID at the end of the ticket, like so: <ticket ID>/ <description>/ <team ID>/ <priority> / <sprint ID>

Every week, a team should work on the highest priority ticket assigned to it. If there are multiple candidate tickets, the team works on the ticket with the lowest ticket ID. Tickets that will be completed during the same sprint should be ordered by ticket ID.

Tickets that will not be completed during the specified number of sprints should be printed out at the end and should be ordered by ticket ID.

# Here is an example input:

(2 is the number of teams, 3 is the number of sprints in the semester, and 7 is the number of tickets to be processed.)

```
2
3
7
0/ User authentication/ 1/ HIGH
1/ Delete user route/ 1/ HIGH
2/ Search bar component/ 0/ HIGH
3/ Admin model/ 0/ MED
4/ More unit tests/ 0/ HIGH
5/ Standardize CSS styles/ 0/ HIGH
6/ Push notifications/ 1/ LOW
```

And here is the corresponding output:

```
0/ User authentication/ 1/ HIGH/ 0
2/ Search bar component/ 0/ HIGH/ 0
1/ Delete user route/ 1/ HIGH/ 1
4/ More unit tests/ 0/ HIGH/ 1
5/ Standardize CSS styles/ 0/ HIGH/ 2
6/ Push notifications/ 1/ LOW/ 2
3/ Admin model/ 0/ MED
```

Notice that each team completes the highest priority tickets first, breaking ties based on the ticket ID. Ticket 3 (3/ Admin model/ 0/ MED) cannot be completed during the semester so it does not have an assigned sprint ID.

We are looking for critical thinking and attention to detail. Even if you do not pass all cases, we encourage you to submit something to show your thinking process. No time limit, infinite tries, feel free to google syntax!

# Input Format

Read from stdin  
1st line is the number of teams  
2nd line is the number of sprints in the semester  
3rd line is the number of tickets  
Remaining lines are the actual tickets:  
A ticket follows this format: `<id>/ <description>/ <team id>/ <priority>`  
All IDs (ticket ID, team ID, sprint ID, etc.) are zero-indexed! (0, 1, 2, ...)

# Constraints

Write to stdout  
The max number of tickets will be in the hundreds.  
The max number of teams will be 10.

# Output Format

Print to stdout  
One ticket per line  
IF a ticket will be completed during the semester, append the sprint ID at the end like so: `<id>/ <description>/ <team id>/ <priority>/ <sprint ID>`.

# Sample Input 0

```
2
3
7
0/ User authentication/ 1/ HIGH
1/ Delete user route/ 1/ HIGH
2/ Search bar component/ 0/ HIGH
3/ Admin model/ 0/ MED
4/ More unit tests/ 0/ HIGH
5/ Standardize CSS styles/ 0/ HIGH
6/ Push notifications/ 1/ LOW
```

# Sample Output 0

```
0/ User authentication/ 1/ HIGH/ 0
2/ Search bar component/ 0/ HIGH/ 0
1/ Delete user route/ 1/ HIGH/ 1
4/ More unit tests/ 0/ HIGH/ 1
5/ Standardize CSS styles/ 0/ HIGH/ 2
6/ Push notifications/ 1/ LOW/ 2
3/ Admin model/ 0/ MED
```

# Sample Input 1

```
2
4
12
0/ Create boilerplate/ 0/ HIGH
1/ User model/ 1/ MED
2/ User model/ 0/ HIGH
3/ Create user route/ 0/ MED
4/ Delete user route/ 0/ HIGH
5/ Login page/ 0/ MED
6/ Search bar component/ 0/ MED
7/ Admin panel UI/ 0/ MED
8/ Form validation/ 1/ MED
9/ Refactor backend/ 0/ HIGH
10/ Track user metrics/ 1/ HIGH
11/ Migrate from MongoDB to PostgreSQL/ 0/ LOW
```

# Sample Output 1

```
0/ Create boilerplate/ 0/ HIGH/ 0
10/ Track user metrics/ 1/ HIGH/ 0
1/ User model/ 1/ MED/ 1
2/ User model/ 0/ HIGH/ 1
4/ Delete user route/ 0/ HIGH/ 2
8/ Form validation/ 1/ MED/ 2
9/ Refactor backend/ 0/ HIGH/ 3
3/ Create user route/ 0/ MED
5/ Login page/ 0/ MED
6/ Search bar component/ 0/ MED
7/ Admin panel UI/ 0/ MED
11/ Migrate from MongoDB to PostgreSQL/ 0/ LOW
```

# Sample Input 2

```
3
5
23
0/ Create boilerplate/ 0/ MED
1/ Setup CI/CD/ 1/ MED
2/ User model/ 2/ HIGH
3/ User authentication/ 2/ HIGH
4/ Create user route/ 2/ LOW
5/ Delete user route/ 0/ HIGH
6/ Delete user route/ 2/ LOW
7/ Login page/ 0/ LOW
8/ Progress bar UI/ 1/ LOW
9/ Progress bar UI/ 2/ LOW
10/ Admin panel UI/ 2/ MED
11/ More unit tests/ 2/ MED
12/ Refactor backend/ 1/ MED
13/ Refactor backend/ 1/ MED
14/ Standardize CSS styles/ 1/ HIGH
15/ Track user metrics/ 2/ MED
16/ Data visualization/ 0/ MED
17/ Push notifications/ 1/ HIGH
18/ Push notifications/ 0/ HIGH
19/ Push notifications/ 2/ LOW
20/ Bug fixes/ 1/ LOW
21/ Bug fixes/ 0/ MED
22/ Deploy on Heroku/ 0/ HIGH
```

# Sample Output 2

```
2/ User model/ 2/ HIGH/ 0
5/ Delete user route/ 0/ HIGH/ 0
14/ Standardize CSS styles/ 1/ HIGH/ 0
3/ User authentication/ 2/ HIGH/ 1
17/ Push notifications/ 1/ HIGH/ 1
18/ Push notifications/ 0/ HIGH/ 1
1/ Setup CI/CD/ 1/ MED/ 2
10/ Admin panel UI/ 2/ MED/ 2
22/ Deploy on Heroku/ 0/ HIGH/ 2
0/ Create boilerplate/ 0/ MED/ 3
11/ More unit tests/ 2/ MED/ 3
12/ Refactor backend/ 1/ MED/ 3
13/ Refactor backend/ 1/ MED/ 4
15/ Track user metrics/ 2/ MED/ 4
16/ Data visualization/ 0/ MED/ 4
4/ Create user route/ 2/ LOW
6/ Delete user route/ 2/ LOW
7/ Login page/ 0/ LOW
8/ Progress bar UI/ 1/ LOW
9/ Progress bar UI/ 2/ LOW
19/ Push notifications/ 2/ LOW
20/ Bug fixes/ 1/ LOW
21/ Bug fixes/ 0/ MED
```

# Sample Input 3

```
3
5
11
0/ Create boilerplate/ 0/ MED
1/ Setup CI/CD/ 2/ HIGH
2/ User model/ 0/ MED
3/ Delete user route/ 2/ HIGH
4/ Login page/ 0/ MED
5/ Progress bar UI/ 1/ MED
6/ Admin panel UI/ 1/ HIGH
7/ Email notifications/ 2/ LOW
8/ Email notifications/ 1/ MED
9/ Bug fixes/ 1/ MED
10/ Deploy on Heroku/ 2/ LOW
```

# Sample Output 3

```
0/ Create boilerplate/ 0/ MED/ 0
1/ Setup CI/CD/ 2/ HIGH/ 0
6/ Admin panel UI/ 1/ HIGH/ 0
2/ User model/ 0/ MED/ 1
3/ Delete user route/ 2/ HIGH/ 1
5/ Progress bar UI/ 1/ MED/ 1
4/ Login page/ 0/ MED/ 2
7/ Email notifications/ 2/ LOW/ 2
8/ Email notifications/ 1/ MED/ 2
9/ Bug fixes/ 1/ MED/ 3
10/ Deploy on Heroku/ 2/ LOW/ 3
```

# Sample Input 4

```
3
5
17
0/ Create boilerplate/ 1/ MED
1/ Setup dev environment/ 1/ MED
2/ User model/ 2/ MED
3/ User model/ 1/ HIGH
4/ Search bar component/ 0/ MED
5/ Progress bar UI/ 0/ LOW
6/ Admin model/ 2/ HIGH
7/ Admin panel UI/ 1/ LOW
8/ More unit tests/ 2/ HIGH
9/ Form validation/ 0/ LOW
10/ E2E tests/ 2/ MED
11/ Track user metrics/ 0/ MED
12/ Email notifications/ 1/ MED
13/ Push notifications/ 2/ HIGH
14/ Bug fixes/ 0/ LOW
15/ Deploy on Heroku/ 2/ LOW
16/ Deploy on Heroku/ 0/ LOW
```

# Sample Output 4

```
3/ User model/ 1/ HIGH/ 0
4/ Search bar component/ 0/ MED/ 0
6/ Admin model/ 2/ HIGH/ 0
0/ Create boilerplate/ 1/ MED/ 1
8/ More unit tests/ 2/ HIGH/ 1
11/ Track user metrics/ 0/ MED/ 1
1/ Setup dev environment/ 1/ MED/ 2
5/ Progress bar UI/ 0/ LOW/ 2
13/ Push notifications/ 2/ HIGH/ 2
2/ User model/ 2/ MED/ 3
9/ Form validation/ 0/ LOW/ 3
12/ Email notifications/ 1/ MED/ 3
7/ Admin panel UI/ 1/ LOW/ 4
10/ E2E tests/ 2/ MED/ 4
14/ Bug fixes/ 0/ LOW/ 4
15/ Deploy on Heroku/ 2/ LOW
16/ Deploy on Heroku/ 0/ LOW
```

# Sample Input 5

```
1
3
5
0/ Setup CI/CD/ 0/ HIGH
1/ Full text search/ 0/ HIGH
2/ Admin model/ 0/ HIGH
3/ Email notifications/ 0/ MED
4/ Deploy on Heroku/ 0/ LOW
```

# Sample Output 5

```
0/ Setup CI/CD/ 0/ HIGH/ 0
1/ Full text search/ 0/ HIGH/ 1
2/ Admin model/ 0/ HIGH/ 2
3/ Email notifications/ 0/ MED
4/ Deploy on Heroku/ 0/ LOW
```

# Sample Input 6

```
10
10
109
0/ Create boilerplate/ 0/ LOW
1/ Create boilerplate/ 8/ HIGH
2/ Create boilerplate/ 1/ HIGH
3/ Create boilerplate/ 9/ HIGH
4/ Setup dev environment/ 5/ HIGH
5/ Setup dev environment/ 0/ HIGH
6/ Setup dev environment/ 7/ HIGH
7/ Setup dev environment/ 2/ MED
8/ Setup dev environment/ 1/ HIGH
9/ Setup CI/CD/ 0/ MED
10/ Setup CI/CD/ 1/ MED
11/ Setup CI/CD/ 4/ LOW
12/ Setup CI/CD/ 6/ MED
13/ Setup CI/CD/ 2/ HIGH
14/ Setup CI/CD/ 7/ HIGH
15/ Setup CI/CD/ 5/ MED
16/ User model/ 2/ MED
17/ User model/ 1/ MED
18/ User model/ 7/ HIGH
19/ User model/ 8/ LOW
20/ User authentication/ 0/ MED
21/ User authentication/ 2/ HIGH
22/ User authentication/ 1/ HIGH
23/ User authentication/ 8/ LOW
24/ User authentication/ 6/ LOW
25/ User authentication/ 4/ LOW
26/ Create user route/ 1/ HIGH
27/ Create user route/ 7/ LOW
28/ Create user route/ 2/ MED
29/ Create user route/ 8/ LOW
30/ Delete user route/ 8/ MED
31/ Delete user route/ 1/ LOW
32/ Delete user route/ 7/ MED
33/ Delete user route/ 6/ HIGH
34/ Delete user route/ 4/ HIGH
35/ Delete user route/ 0/ LOW
36/ Login page/ 1/ LOW
37/ Login page/ 0/ MED
38/ Full text search/ 1/ LOW
39/ Full text search/ 7/ HIGH
40/ Search bar component/ 1/ MED
41/ Search bar component/ 8/ MED
42/ Progress bar UI/ 0/ HIGH
43/ Progress bar UI/ 1/ HIGH
44/ Progress bar UI/ 4/ LOW
45/ Progress bar UI/ 2/ MED
46/ Admin model/ 2/ MED
47/ Admin model/ 0/ MED
48/ Admin model/ 7/ LOW
49/ Admin model/ 8/ MED
50/ Admin panel UI/ 2/ LOW
51/ Admin panel UI/ 6/ LOW
52/ More unit tests/ 3/ HIGH
53/ More unit tests/ 1/ LOW
54/ More unit tests/ 0/ LOW
55/ Form validation/ 4/ LOW
56/ Form validation/ 7/ LOW
57/ Form validation/ 8/ MED
58/ Form validation/ 3/ LOW
59/ Form validation/ 2/ MED
60/ Refactor backend/ 6/ LOW
61/ Refactor backend/ 2/ HIGH
62/ Refactor backend/ 1/ MED
63/ Refactor backend/ 0/ HIGH
64/ Refactor backend/ 9/ MED
65/ E2E tests/ 9/ MED
66/ E2E tests/ 0/ MED
67/ E2E tests/ 1/ HIGH
68/ E2E tests/ 2/ HIGH
69/ Standardize CSS styles/ 3/ LOW
70/ Standardize CSS styles/ 1/ HIGH
71/ Standardize CSS styles/ 6/ MED
72/ Standardize CSS styles/ 0/ LOW
73/ Standardize CSS styles/ 2/ LOW
74/ Standardize CSS styles/ 7/ LOW
75/ Track user metrics/ 2/ LOW
76/ Track user metrics/ 7/ LOW
77/ Track user metrics/ 1/ LOW
78/ Track user metrics/ 0/ HIGH
79/ Track user metrics/ 4/ LOW
80/ Data visualization/ 0/ HIGH
81/ Data visualization/ 4/ MED
82/ Data visualization/ 9/ MED
83/ Data visualization/ 6/ LOW
84/ Data visualization/ 2/ MED
85/ Data visualization/ 8/ LOW
86/ Data visualization/ 7/ MED
87/ Migrate from MongoDB to PostgreSQL/ 1/ LOW
88/ Migrate from MongoDB to PostgreSQL/ 0/ HIGH
89/ Migrate from MongoDB to PostgreSQL/ 7/ MED
90/ Migrate from MongoDB to PostgreSQL/ 8/ LOW
91/ Email notifications/ 6/ HIGH
92/ Email notifications/ 7/ MED
93/ Email notifications/ 0/ HIGH
94/ Push notifications/ 8/ MED
95/ Push notifications/ 2/ HIGH
96/ Push notifications/ 1/ LOW
97/ Push notifications/ 5/ LOW
98/ Push notifications/ 7/ MED
99/ Bug fixes/ 8/ LOW
100/ Bug fixes/ 0/ HIGH
101/ Bug fixes/ 6/ MED
102/ Bug fixes/ 4/ MED
103/ Bug fixes/ 2/ MED
104/ Bug fixes/ 7/ LOW
105/ Deploy on Heroku/ 2/ HIGH
106/ Deploy on Heroku/ 4/ HIGH
107/ Deploy on Heroku/ 7/ LOW
108/ Deploy on Heroku/ 0/ MED
```

# Sample Output 6

```
1/ Create boilerplate/ 8/ HIGH/ 0
2/ Create boilerplate/ 1/ HIGH/ 0
3/ Create boilerplate/ 9/ HIGH/ 0
4/ Setup dev environment/ 5/ HIGH/ 0
5/ Setup dev environment/ 0/ HIGH/ 0
6/ Setup dev environment/ 7/ HIGH/ 0
13/ Setup CI/CD/ 2/ HIGH/ 0
33/ Delete user route/ 6/ HIGH/ 0
34/ Delete user route/ 4/ HIGH/ 0
52/ More unit tests/ 3/ HIGH/ 0
8/ Setup dev environment/ 1/ HIGH/ 1
14/ Setup CI/CD/ 7/ HIGH/ 1
15/ Setup CI/CD/ 5/ MED/ 1
21/ User authentication/ 2/ HIGH/ 1
30/ Delete user route/ 8/ MED/ 1
42/ Progress bar UI/ 0/ HIGH/ 1
58/ Form validation/ 3/ LOW/ 1
64/ Refactor backend/ 9/ MED/ 1
91/ Email notifications/ 6/ HIGH/ 1
106/ Deploy on Heroku/ 4/ HIGH/ 1
12/ Setup CI/CD/ 6/ MED/ 2
18/ User model/ 7/ HIGH/ 2
22/ User authentication/ 1/ HIGH/ 2
41/ Search bar component/ 8/ MED/ 2
61/ Refactor backend/ 2/ HIGH/ 2
63/ Refactor backend/ 0/ HIGH/ 2
65/ E2E tests/ 9/ MED/ 2
69/ Standardize CSS styles/ 3/ LOW/ 2
81/ Data visualization/ 4/ MED/ 2
97/ Push notifications/ 5/ LOW/ 2
26/ Create user route/ 1/ HIGH/ 3
39/ Full text search/ 7/ HIGH/ 3
49/ Admin model/ 8/ MED/ 3
68/ E2E tests/ 2/ HIGH/ 3
71/ Standardize CSS styles/ 6/ MED/ 3
78/ Track user metrics/ 0/ HIGH/ 3
82/ Data visualization/ 9/ MED/ 3
102/ Bug fixes/ 4/ MED/ 3
11/ Setup CI/CD/ 4/ LOW/ 4
32/ Delete user route/ 7/ MED/ 4
43/ Progress bar UI/ 1/ HIGH/ 4
57/ Form validation/ 8/ MED/ 4
80/ Data visualization/ 0/ HIGH/ 4
95/ Push notifications/ 2/ HIGH/ 4
101/ Bug fixes/ 6/ MED/ 4
24/ User authentication/ 6/ LOW/ 5
25/ User authentication/ 4/ LOW/ 5
67/ E2E tests/ 1/ HIGH/ 5
86/ Data visualization/ 7/ MED/ 5
88/ Migrate from MongoDB to PostgreSQL/ 0/ HIGH/ 5
94/ Push notifications/ 8/ MED/ 5
105/ Deploy on Heroku/ 2/ HIGH/ 5
7/ Setup dev environment/ 2/ MED/ 6
19/ User model/ 8/ LOW/ 6
44/ Progress bar UI/ 4/ LOW/ 6
51/ Admin panel UI/ 6/ LOW/ 6
70/ Standardize CSS styles/ 1/ HIGH/ 6
89/ Migrate from MongoDB to PostgreSQL/ 7/ MED/ 6
93/ Email notifications/ 0/ HIGH/ 6
10/ Setup CI/CD/ 1/ MED/ 7
16/ User model/ 2/ MED/ 7
23/ User authentication/ 8/ LOW/ 7
55/ Form validation/ 4/ LOW/ 7
60/ Refactor backend/ 6/ LOW/ 7
92/ Email notifications/ 7/ MED/ 7
100/ Bug fixes/ 0/ HIGH/ 7
9/ Setup CI/CD/ 0/ MED/ 8
17/ User model/ 1/ MED/ 8
28/ Create user route/ 2/ MED/ 8
29/ Create user route/ 8/ LOW/ 8
79/ Track user metrics/ 4/ LOW/ 8
83/ Data visualization/ 6/ LOW/ 8
98/ Push notifications/ 7/ MED/ 8
20/ User authentication/ 0/ MED/ 9
27/ Create user route/ 7/ LOW/ 9
40/ Search bar component/ 1/ MED/ 9
45/ Progress bar UI/ 2/ MED/ 9
85/ Data visualization/ 8/ LOW/ 9
0/ Create boilerplate/ 0/ LOW
31/ Delete user route/ 1/ LOW
35/ Delete user route/ 0/ LOW
36/ Login page/ 1/ LOW
37/ Login page/ 0/ MED
38/ Full text search/ 1/ LOW
46/ Admin model/ 2/ MED
47/ Admin model/ 0/ MED
48/ Admin model/ 7/ LOW
50/ Admin panel UI/ 2/ LOW
53/ More unit tests/ 1/ LOW
54/ More unit tests/ 0/ LOW
56/ Form validation/ 7/ LOW
59/ Form validation/ 2/ MED
62/ Refactor backend/ 1/ MED
66/ E2E tests/ 0/ MED
72/ Standardize CSS styles/ 0/ LOW
73/ Standardize CSS styles/ 2/ LOW
74/ Standardize CSS styles/ 7/ LOW
75/ Track user metrics/ 2/ LOW
76/ Track user metrics/ 7/ LOW
77/ Track user metrics/ 1/ LOW
84/ Data visualization/ 2/ MED
87/ Migrate from MongoDB to PostgreSQL/ 1/ LOW
90/ Migrate from MongoDB to PostgreSQL/ 8/ LOW
96/ Push notifications/ 1/ LOW
99/ Bug fixes/ 8/ LOW
103/ Bug fixes/ 2/ MED
104/ Bug fixes/ 7/ LOW
107/ Deploy on Heroku/ 7/ LOW
108/ Deploy on Heroku/ 0/ MED
```
