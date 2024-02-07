[q1]

~~~
Given an array of integers numbers, your task is to count all numbers that are not equal to numbers[0] or numbers[1], if they exist in the array.
Assume that array indices are 0-based.
Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(numbers.length2) will fit within the execution time limit.
Example
* For numbers = [4, 3, 2, 3, 2, 5, 4, 3], the output should be solution(numbers) = 3.Explanation:numbers[0] and numbers[1] are 4 and 3 respectively. There are three elements in numbers that are not equal to 4 or 3:
    * numbers[2] = 2
    * numbers[4] = 2
    * numbers[5] = 5So, the answer is 3.
* For numbers = [3, 3, 1, 1, 3], the output should be solution(numbers) = 2.Explanation:numbers[0] and numbers[1] are both 3. There are two elements in numbers that are not equal to 3:
    * numbers[2] = 1
    * numbers[3] = 1So, the answer is 2.
* For numbers = [-2], the output should be solution(numbers) = 0.Explanation:numbers[0] is -2, and numbers[1] does not exist, so the only requirement is to count numbers different from -2. There are no elements in numbers that are not equal to -2, so the answer is 0.
Input/Output
* [execution time limit] 4 seconds (js)
* [memory limit] 1 GB
* [input] array.integer numbersAn array of integers.Guaranteed constraints:0 ≤ numbers.length ≤ 1000,-109 ≤ numbers[i] ≤ 109.
* [output] integerThe number of elements in the array numbers that are not equal to numbers[0] or numbers[1].
[JavaScript] Syntax Tips
~~~
---
[q2]
~~~
In Unix, there are two common ways to execute a command:
* Entering its name, e.g. "cp" or "ls";
* Entering "!<index>". This notation is used to repeat the indexth (1-based) command since the start of the session. For example, suppose that the user has entered the following commands:
ls
cp
mv
mv
mv
!1
!3
!6
"!1" would trigger the execution of "ls", "!3" would repeat "mv", and "!6" would execute "!1" which in turn would trigger the execution of "ls".
You are given a sequence of commands commands that the user has entered in the terminal since the start of the session. Each command can be one of the following: "cp", "ls", "mv" or "!<index>". Calculate the number of times each of "cp", "ls" and "mv" commands was executed and return an array of three integers in the following form: [# of times for "cp", # of times for "ls", # of times for "mv"].
Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(commands.length3) will fit within the execution time limit.
Example
* For commands = ["ls", "cp", "mv", "mv", "mv", "!1", "!3", "!6"], the output should be solution(commands) = [1, 3, 4].
    * First, "ls" was executed once;
    * Then "cp" was executed once;
    * After that, "mv" was executed three times;
    * Then "!1" was executed, triggering the execution of commands[0] = "ls";
    * Then "!3" was executed, triggering commands[2] = "mv";
    * Finally, "!6" was executed, triggering commands[5] = "!1", which in turn triggered commands[0] = "ls".
* In total, "cp" was executed once, "ls" was executed three times, and "mv" was executed four times, so the final answer is [1, 3, 4].
* For commands = ["ls", "cp", "mv", "!3", "mv", "!1", "!6"] the output should be solution(commands) = [1, 3, 3].
    * First, each one of the three commands was executed once;
    * Then "!3" was executed, triggering commands[2] = "mv";
    * After that, "mv" was executed one more time;
    * Then "!1" was executed, triggering commands[0] = "ls";
    * Finally "!6" was executed, triggering commands[5] = "!1", which in turn triggered commands[0] = "ls".
* In total, "cp" was executed once, "ls" was executed three times, and "mv" was executed three times, so the final answer is [1, 3, 3].
Input/Output
* [execution time limit] 4 seconds (js)
* [memory limit] 1 GB
* [input] array.string commandsAn array of strings representing the sequence of commands entered in the terminal by the user. It is guaranteed that all commands follow the format described above.Guaranteed constraints:1 ≤ commands.length ≤ 500.
* [output] array.integerReturn an array of size 3, in which:
    * 0-th element corresponds to the number of times "cp" was executed
    * 1-st element corresponds to the number of times "ls" was executed
    * 2-nd element corresponds to the number of times "mv" was executed
[JavaScript] Syntax Tips
// Prints help message to the console
// Returns a string
function helloWorld(name) {
    console.log("This prints to the console when you Run Tests");
    return "Hello, " + name;
}


~~~
---
[q3]
~~~
Think about a team chat with numerous users writing messages in it. The chat supports two types of actions:
* "MESSAGE" – Messages a set of users. The format looks as follows: ["MESSAGE", "<timestamp>", "<mentions>"]. Mentions string can contain the following space-separated tokens:
    * id<number>, where <number> is an integer in range [1:999] - mentioning of individual users
    * ALL - mentioning all users
    * HERE - mentioning active users
* "OFFLINE" – Makes a user with a given id inactive for 60 time ticks – the user will be active again at time <timestamp> + 60. It is guaranteed that the user with given <id> will be active when this action is applied. The format looks as follows: ["OFFLINE", "<timestamp>", "<id>"], where id is a single individual mention.
Note: all the events are sorted by their timestamp.
Examples of events
* ["MESSAGE", "0", "id1"] – mentioning user with id id1
* ["MESSAGE", "9", "HERE id3"] – mentioning all the active users and user with id id3
* ["MESSAGE", "6", "ALL"] – mentioning all the users
* ["MESSAGE", "100", ""] – message, without mentioning any user
* ["OFFLINE", "200", "id3"] – making user with id id3 inactive
Please note, that mentions do not contain any other text, but only a list of ids or aliases separates by a space.
Your task is to calculate mention statistics. Given a list of users in the group chat and a list of chat events, count the number of message events that each user is mentioned in.
Return the results in an array of strings, with each string following this format: "[user id]=[mentions count]". The array should be sorted lexicographically by user id in ascending order.
Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(members.length * events.length) will fit within the execution time limit.
Example
For members = ["id42", "id158", "id23"] and
events = [
  ["MESSAGE", "0", "ALL id158 id42"],
  ["OFFLINE", "1", "id158"],
  ["MESSAGE", "2", "id158 id158"],
  ["OFFLINE", "3", "id23"],
  ["MESSAGE", "60", "HERE id158 id42 id23"],
  ["MESSAGE", "61", "HERE"]
]
the output should be solution(members, events) = ["id158=4", "id23=2", "id42=3"].
Explanation:
* In the first event at time 0, all users are mentioned with ALL alias. Note that id158 and id42 are mentioned twice – once by ALL alias and once by their ids, but they should be counted once.
* In the second event at time 1 the user id158 becomes inactive.
* In the third event at time 2 the user id158 is mentioned and they get notified even when inactive. Note that id158 is mentioned twice, but it should be counted once.
* In the fourth event at time 3 the user id23 becomes inactive.
* In the fifth event at time 60 all active users and id158, id42, and id23 are mentioned. Note that id158 and id23 are mentioned by their username, so they will be notified even when they are inactive, and id42 is mentioned twice – once by HERE alias and once by their id, but it should be counted once.
* In the last event at time 61 the user with id158 is back online again as they have been offline for 60 time ticks already. Here all the active users are mentioned – which are id42 and id158.
* So, the output should be ["id158=4", "id23=2", "id42=3"].
Input/Output
* [execution time limit] 4 seconds (js)
* [memory limit] 1 GB
* [input] array.string membersMember id list.Guaranteed constraints:2 ≤ members.length ≤ 50,3 ≤ members[i].length ≤ 5.
* [input] array.array.string eventsEvents occurred in chronological order. Note, that timestamps can be in range [0:200].Guaranteed constraints:1 ≤ events.length ≤ 100.
* [output] array.stringReturn an array of strings containing all user ids from members, with count of each user id mentions across events (described above) separated by = sign. This array should be sorted lexicographically by user id in ascending order.
* 

~~~

[q4]
~~~
Given an empty array that should contain integers numbers, your task is to process a list of queries on it. Specifically, there are two types of queries:
* "+x" - append x to numbers. numbers may contain multiple instances of the same integer.
* "-x" - remove all the instances of x from numbers.
After processing each query, count the number of triples (x, y, z) in numbers which meet this condition: both x - y and y - z are equal to a given diff. Note that elements in numbers can be rearranged to form triples to meet the condition. The final output should be an array of counts after each query in queries.
Notes:
* All integers in queries are guaranteed to be in the range of [-109, 109]. It is also guaranteed that for each "-x" query, the specified x exists in numbers.
* It is guaranteed that the answer for each query fits into a 32-bit integer type.
Example
For queries = ["+4", "+5", "+6", "+4", "+3", "-4"] and diff = 1, the output should be solution(queries, diff) = [0, 0, 1, 2, 4, 0].
* First, process queries[0] = "+4" and append 4 to numbers, resulting in numbers = [4]. There are no triples yet, so append 0 to the output.
* Next, process queries[1] = "+5" and append 5 to numbers, resulting in numbers = [4, 5]. There are no triples yet, so append 0 to the output.
* Process queries[2] = "+6" and append 6 to numbers, resulting in numbers = [4, 5, 6]. These can form the triple (6, 5, 4) which meets the condition (6 - 5 = 5 - 4 = 1 = diff), so append 1 to the output.
* Process queries[3] = "+4" and append 4 to numbers, resulting in numbers = [4, 5, 6, 4]. Now, there are two ways to form the triple (6, 5, 4) which meets the condition, so append 2 to the output.
* Process queries[4] = "+3" and add 3 to numbers, resulting in numbers = [4, 5, 6, 4, 3]. Now, there are two ways to form the triple (6, 5, 4) and two ways to form the triple (5, 4, 3) which meet the condition, so append 4 to the output.
* Process queries[5] = "-4" and remove all instances of 4 from numbers, resulting in numbers = [5, 6, 3]. There are no way to form triples which can meet the condition, so append 0 to the output.
Finally, the output is [0, 0, 1, 2, 4, 0].
Input/Output
* [execution time limit] 4 seconds (js)
* [memory limit] 1 GB
* [input] array.string queriesAn array of strings representing queries in the format described above. It is guaranteed that all numbers are integers between -109, 109. It is also guaranteed that for each removal query, the removed integer exists in the current numbers array.Guaranteed constraints:1 ≤ queries.length ≤ 105.
* [input] integer diffA positive integer value representing the expected difference in triples.Guaranteed constraints:1 ≤ diff ≤ 109.
* [output] array.integerAfter processing each query, count the number of triples (x, y, z) in numbers which meet this condition: x - y = y - z = diff. It is guaranteed that the count will always fit into a signed 32-bit integer type. Return an array of such values for all queries.
[JavaScript] Syntax Tips
// Prints help message to the console
// Returns a string
function helloWorld(name) {
    console.log("This prints to the console when you Run Tests");
    return "Hello, " + name;
}

~~~