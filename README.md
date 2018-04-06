## Approach

I built this sessionizer as part of my interview process with the Insight Fellows Program in data engineering.  Below is an example of what it can do, and I believe this software can benefit many websites, with a little modification to suit your needs.

Many investors, researchers, journalists and others use the Securities and Exchange Commission's Electronic Data Gathering, Analysis and Retrieval (EDGAR) system to retrieve financial documents, whether they are doing a deep dive into a particular company's financials or learning new information that a company has revealed through their filings.

The SEC maintains EDGAR weblogs.  This sessionizer takes the data and produces a dashboard that provides a real-time view into how users are accessing EDGAR, including how long they stay and the number of documents they access during the visit.  

To summarize, this sessionizer takes existing publicly available EDGAR weblogs and parses them into sessions, each of which contains one user, the duration of and number of documents requested during that visit, and then writes the output to a file.  This back-end program creates a data pipeline that organizes and hands off user information to the front-end developers, who could create a GUI (Graphic User Interface) that is user-friendly for your company’s leadership or for the public.

### Testing

I tested manually throughout my development process, and used the provided test to check the data.

## How to scale this sessionizer for big data 

As I wrote the code, I processed the information and deleted it out of memory as soon as possible, so as not to create big, unwieldy database with superfluous information.  

One method of scaling would be to direct the data onto an instance of the program running on different servers, and make sure that each request from a single IP got sent to the same server.  To use a metaphor, imagine many shoppers in a supermarket.  If you check them all out at one cashier, you have a very long and inefficient line of impatient shoppers.  Instead, you open 5 cash registers and divide that long queue into 5 queues.  However, in this situation you have many “shoppers” who want to “check out” multiple times, so you have to make sure each shopper is always directed to the same cashier, to end up on the same “receipt.”

My current file technique could be problematic when scaled to multi-server implementations, so I would have to change my system to append each instance without having one of my “cashiers” clean out my output file before all of my “receipts” had been picked up by the store manager.

## Dependencies

You will need Python 3 (python3) in a Bash shell.

## Run Instructions

Next, go to this link: https://github.com/InsightDataScience/edgar-analytics 
and download the above files (those with: .py, .txt, .csv, .sh) into their proper folders.  
When you’re ready, open the Terminal app and run the “run.sh” file.  

Tests can be found in the insight_testsuites folder, and run ./run_tests.sh

## Author

David Code

## Acknowledgments

Special thanks to my mentor, Carson Elmore Jr.

Sharad Murthy also helped me to understand sharding and buckets

The good folks of Stack Overflow

