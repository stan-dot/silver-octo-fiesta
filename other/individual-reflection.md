

Indiivudal reflectiuon for the software hut module
Stanislaw Malinowski

# Introduction

I started this project as a third year CS and AI student after a year in industry.
I have had no prior experience with the Ruby on Rails framework but familiarity with negotiating and then working on a full stack project based on a specification. 
During my placement I closely collaborated on the developer - to - developer basis only with 1 other person. Communications with others were in terms of supervision meetings or asking for advice with a specific technical problem.
I expected the main challenges in this module to be - working in a coordinated team of 7, and learning the new technological stack (Ruby on Rails with Bootstrap CSS).

## Our project
The goal of the project was to provide a reviews system for the University School of Medicine. The system specifically concerns electives, which are non-mandatory short (6-12 weeks) internships that medicine students go to. These weigh on their future employability.
Arrangement of such an event is a complicated process much helped by domain-specific knowledge and social capital.
That creates an inequality for students from Widening Participation backgrounds.
The system proposed equalizes the playing field, providing a one stop solution for a student to learn about, organize their elective and then give feedback so that the cycle may continue.


# Examples for lessons
During the course of the project, we encountered numerous technical, teamwork, and project management lessons. 
Starting with how our meetings went - there were many iterations of the process of setting up meetings. We were using the when2meet application to take into account timetables of all team members.
That was quite successful in ensuring we have regular meetings and everyone is up to date.
I will continue using that software in the future.

This helped us keep team cohesion necessary to deal with challenges such as troubles with communication with the client. That was not perfect.

We also missed one of our team members who participated with us during the first 3-4 weeks but later we lost contact. We were still expecting some feedback, as before during the initial meetings we split responsibilities he picked keeping tabs on the communication with the client.
Even once we decided we needed to assume he is not rejoining us anytime soon, responses to our messages were not timely. 
There was a missing piece of data - the format of user input.
That forced us to operate in conditions of uncertainty and make decisions based on limited data.
We managed to extrapolate what was missing from the present data and our implementation was liked by the client. In retrospect we need not have waited for the format and could have presented the demo. As of writing this there's still no data format.

We also managed to coordinate and keep remote work discipline between ourselves. That proved relaxed over the Easter break. 

We did not succeed in updating the kanban board regularly. We did move items from the backlog to the 'develop' section at a steady pace, but then they stuck in the 'ready for testing'. 
The reasons for this are uncertain.
I was dissatisfied with the format of the board. The layout was quite elaborate, with 'ready to develop', 'develop', 'ready for test', 'test', and also 'QA' and ready for 'demo', 'pilot', 'live'. We did not manage to use these efficiently. The width of this table of columns is over two screen widths, not allowing for a bird-eye view of the progress. It is more complicated than it is needed. 
The lesson from this is that overly complex tools are discouraging in the same sense as elaborate passwords end up on a post-it note on the screen.

Finally I took on a leadership role on the team. Responsibilities included setting the agenda for each meeting, making sure all voices are heard and ideas are given floor, and opportunity to feedback and discuss. 
This also involved encouraging more reserved and distant team members to take voice their opinion in the meetings. That saw moderate success, but perhaps the commmand of spoken langauge was the issue here.
On the other hand, dividing floor time equally is not a practical goal. Perhaps structuring the meetings more and always having a round of questions for comments would be a good solution to this.
That also included giving positive feedback and keeping up the morale, both during in person meetings and online communications. 


# Professional issues - security, privacy and ethics

There are a number of issues regarding the potential security, privacy and ethics concerns in the project. They center around the power of the administrators over the reviews and displayed electives. It is them who decide how each review is judged, and which electives feature on the landing page first. That power is unchecked in the current solution. There is no consensus or feedback mechanism to hold administrators accountable. 


Decisions of administrators have a big weight. They need to ensure the data is GDPR compliant, with regards to students' description and also points of contact at the hospitals. To ensure that is compliant, the reviews submitted by the students have a declaration field that contacts consent to being contacted. 
Moreover the administrators should be able to moderate successfully content made by the students. Reviews submitted by students should be scanned for inappropriate language.
Regarding the ethics choices, when choosing which electives feature on the landing page the administrators make a choice that might be judged variously by the electives. If the criteria for judgment are unclear, a hospital could claim it's arbitrary and discriminate against their institution. There is a conflict of interests in that sense.

That all ties into security concerns in a hypothetical scenario of a database leak. That could be a result of a vulnerability in the code or in the hosting environment.
Then the negative consequences could be for all the persons whose data the system contains: students, administrators, contact points at hospitals.

# Conclusion
In conclusion, our Ruby on Rails project taught us many technical, teamwork, and project management lessons. I learned the importance of effective communication, regular meetings, and maintaining discipline when working remotely. I also recognized the value of using simple and streamlined tools and the risks associated with overly complex ones.
Finally, I learned to adapt and be persistent in dealing with challenges, even when dealing with limited data or missing information. These lessons will undoubtedly serve me well in future projects.



