A Simple, Basic Sessionizer for Web Usage Mining

Table of Contents

What is Web Usage Mining?  What is a Sessionizer?  Why should you care?

An example of what this sessionizer can do for you

How to scale this sessionizer for big data on multiple nodes

Web Usage Mining is all about improved user satisfaction.  It is the process of studying the browsing behavior of users at your Web site, so that you can better serve their needs.  It gives you valuable insight and empathy into what your users actually want (rather than what you may think they want) and you can use this insight to attract and retain users.

A sessionizer mines the Web server logs for user data, then organizes that data into "sessions."  An example of a session might display a single user’s behavior at a single website: her IP address (usually anonymized to protect privacy) the pages she visited, the items she ordered, the duration of her session, etc.  Organizing the Web log data into sessions helps you to discover patterns in your users’ behavior on your site, so you can tailor your site to better address your users’ needs in a timely and cost-effective manner.  

To put it in Design Thinking terms, a sessionizer allows you to listen to, and empathize with what your user actually wants.  It helps your website create a pipeline of data that you can store and analyze, using machine learning, to discover patterns of what your users actually want, so you can respond to their needs better, faster, and more cheaply.  Amazon.com is a great example of using sessionizers to help customers search effectively to find what they need and to suggest additional items customers may find helpful.  The Google search box is another good example.

An example of what this sessionizer can do for you

I built this sessionizer as part of my interview process with the Insight Fellows Program in data engineering.  Below is an example of what it can do, and I believe this software can benefit many websites, with a little modification to suit your needs:

Many investors, researchers, journalists and others use the Securities and Exchange Commission's Electronic Data Gathering, Analysis and Retrieval (EDGAR) system to retrieve financial documents, whether they are doing a deep dive into a particular company's financials or learning new information that a company has revealed through their filings.

The SEC maintains EDGAR weblogs.  This sessionizer takes the data and produces a dashboard that provides a real-time view into how users are accessing EDGAR, including how long they stay and the number of documents they access during the visit.  

To summarize, this sessionizer takes existing publicly available EDGAR weblogs and parses them into sessions, each of which contains one user, the duration of and number of documents requested during that visit, and then writes the output to a file.  This back-end program creates a data pipeline that organizes and hands off user information to the front-end developers, who could create a GUI (Graphic User Interface) that is user-friendly for your company’s leadership or for the public.

How to scale this sessionizer for big data on multiple nodes

This sessionizer is an algorithm that takes web log entries that have no updates for a determined duration (default is 2 seconds) and adds them to a table (array), then dumps them periodically to the output file, "Sessionization.txt."  It is designed for only one node, but can be scaled if you know how to “shard” into “buckets.” 

To build a scalable solution you need to get it working on 1 instance. An instance can only handle X events/sec. In order to handle, say, 5X events/sec, you will need to have 5 instances of your application. In such a scenario you need to distribute the events across 5 instances. The constraint is that an event with the same IP address should always land on the same instance as you are keeping all counters for that IP on that particular instance. The shard here is 5-way. 

Read the file and spray the row (one row per IP address) into this shard. You can take a hash of the IP address and then do a modification of the hash to figure out the shard. Note that you can store the IP address in clear text, as this software does.  However, a hash table (aka a "dictionary" in Python) will require you to hash this to find the value. The value will be a complex type which would serve as a bucket for various counters.

Getting Started

The following instructions will get you a copy of the project up and running on your local machine for development and testing purposes:

If you do not have a Linux laptop, then download and install a virtualizer (which emulates a Linux hardware environment onto which you can install the Ubuntu operating system) such as Oracle’s VMWare Virtual Box: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads) 

Then download and install the Ubuntu operating system: [https://www.ubuntu.com/download/desktop](https://www.ubuntu.com/download/desktop) 

Create a folder in your hard drive’s Documents folder and name it EDGAR.  Inside your EDGAR folder, create the following subfolders to emulate this screenshot below: [https://github.com/InsightDataScience/edgar-analytics/blob/master/README.md#repo-directory-structure](https://github.com/InsightDataScience/edgar-analytics/blob/master/README.md#repo-directory-structure) 

![image alt text](image_0.png)

Next, go to this link: [https://github.com/InsightDataScience/edgar-analytics](https://github.com/InsightDataScience/edgar-analytics) 

and download the above files (those with: .py, .txt, .csv, .sh) into their proper folders.  

If you haven’t used Ubuntu before, take heart!  Everyone feels overwhelmed at first with a new interface.  In the bottom LH corner of your Ubuntu desktop you’ll see 9 dots arranged like a Tic Tac Toe board.  That’s your applications launcher.  Open up the Text Editor app, and within it, open up your sessionization.py file (the one within your SRC folder).  This is where you see my code, and you can modify it here to suit your needs.

When you’re ready, open the Terminal app and run the "run.sh" file.  To do this, first you type this on the command line: cd ~ and press Enter.  

To make sure that your code has the correct directory structure and the format of the output files are correct, I have included a test script called run_tests.sh in the insight_testsuite folder.

The tests are stored simply as text files under the insight_testsuite/tests folder. Each test should have a separate folder with an input folder for inactivity_period.txt and log.csv and an output folder for sessionization.txt.

You can run the test with the following command in the Terminal:

insight_testsuite~$ ./run_tests.sh "

If your tests yield positive results, you are now ready to run your modified Sessionizer!

Type: cd ~ and press Enter to return to your home directory.  Then type:

./run_tests.sh and press Enter

Prerequisites

What things you need to install the software and how to install them

Give examples

Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

Give the example

And repeat

until finished

End with an example of getting some data out of the system or using it for a little demo

Running the tests

Explain how to run the automated tests for this system

Break down into end to end tests

Explain what these tests test and why

Give an example

And coding style tests

Explain what these tests test and why

Give an example

Deployment

Add additional notes about how to deploy this on a live system

Built With

Dropwizard - The web framework used

Maven - Dependency Management

ROME - Used to generate RSS Feeds

Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

Versioning

We use SemVer for versioning. For the versions available, see the tags on this repository.

Authors

Billie Thompson - Initial work - PurpleBooth

See also the list of contributors who participated in this project.

License

This project is licensed under the MIT License - see the LICENSE.md file for details

Acknowledgments

Hat tip to anyone who's code was used

Inspiration

etc

END: PLEASE IGNORE THE VARIOUS STUFF BELOW

sessionization, 

Web Usage Mining is the application of data mining techniques to discover interesting usage patterns from Web data in order to understand and better serve the needs of Web-based applications. Usage data captures the identity or origin of Web users along with their browsing behavior at a Web site.

Web mining is the application of data mining techniques to discover patterns from the World Wide Web. As the name proposes, this is information gathered by mining the web. It makes utilization of automated apparatuses to reveal and extricate data from servers and web2 reports, and it permits organizations to get to both organized and unstructured information from browser activities, server logs, website and link structure, page content and different sources.

[https://en.wikipedia.org/wiki/Web_mining](https://en.wikipedia.org/wiki/Web_mining) 

Web Usage Mining is the application of data mining techniques to discover interesting usage patterns from Web data in order to understand and better serve the needs of Web-based applications. Usage data captures the identity or origin of Web users along with their browsing behavior at a Web site.

Web usage mining itself can be classified further depending on the kind of usage data considered:

Web Server Data: The user logs are collected by the Web server. Typical data includes IP address, page reference and access time.

Pros

Web usage mining essentially has many advantages which makes this technology attractive to corporations including the government agencies. This technology has enabled e-commerce to do personalized marketing, which eventually results in higher trade volumes. Government agencies are using this technology to classify threats and fight against terrorism. The predicting capability of mining applications can benefit society by identifying criminal activities. Companies can establish better customer relationship by understanding the needs of the customer better and reacting to customer needs faster. Companies can find, attract and retain customers; they can save on production costs by utilizing the acquired insight of customer requirements. They can increase profitability by target pricing based on the profiles created. They can even find customers who might default to a competitor the company will try to retain the customer by providing promotional offers to the specific customer, thus reducing the risk of losing a customer or customers.

(same source as above link)

A book chapter on web usage mining: [https://pdfs.semanticscholar.org/553c/f6b89a7c73caa2d32e45719bf609a37423a4.pdf](https://pdfs.semanticscholar.org/553c/f6b89a7c73caa2d32e45719bf609a37423a4.pdf) 

An Overview on Web Usage Mining

Part of the Advances in Intelligent Systems and Computing book series (AISC, volume 338)

Abstract

The prolific growth of web-based applications and the enormous amount of data involved therein led to the development of techniques for identifying patterns in the web data. Web mining refers to the application of data mining techniques to the World Wide Web. Web usage mining is the process of extracting useful information from web server logs based on the browsing and access patterns of the users. The information is especially valuable for business sites in order to achieve improved customer satisfaction. Based on the user’s needs, Web Usage Mining discovers interesting usage patterns from web data in order to understand and better serve the needs of the web based application. Web Usage Mining is used to discover hidden patterns from weblogs. It consists of three phases like Preprocessing, pattern discovery and Pattern analysis. In this paper, we present each phase in detail, the process of extracting useful information from server log files and some of application areas of Web Usage Mining such as Education, Health, Human-computer interaction, and Social media.

[https://link.springer.com/chapter/10.1007/978-3-319-13731-5_70](https://link.springer.com/chapter/10.1007/978-3-319-13731-5_70) 

"The data commonly used for web usage mining are sessions. A session is the sequence of pages visited by a single user at a single web site for a specified length of time." [http://wic.uchile.cl/wp-content/uploads/2015/09/Identifying-User-Sessions-from-Web-Server-Logs-with-Integer-Programming.pdf](http://wic.uchile.cl/wp-content/uploads/2015/09/Identifying-User-Sessions-from-Web-Server-Logs-with-Integer-Programming.pdf) 

Abstract

A system groups the data into sessions to allow tracking and evaluation of individual user behavior. By grouping clicks of a user in a session, the pattern of clicks can be observed, such as which path or pattern of clicks leads to a purchase. In particular, the session data is organized by session, using session transformers or "sessionizers," before it is provided for database storage, enabling real-time session based analytics.

[https://patents.google.com/patent/US20080086558](https://patents.google.com/patent/US20080086558) 

