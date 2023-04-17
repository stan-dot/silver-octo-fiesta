Dissertation Project: Survey and Analysis Stage
Stanislaw Malinowski
COM3610 supervisor: Rob Gaizauskas
4th December 2022
This report is submitted in partial fulfillment of the requirement for the degree of Bachelor of Science by Stanislaw Malinowski

Declaration
All sentences or passages quoted in this report from other people's work have been specifically acknowledged by clear cross-referencing to author, work and page(s). Any illustrations that are not the work of the author of this report have been used with the explicit permission of the originator and are specifically acknowledged. I understand that failure to do this amounts to plagiarism and will be considered grounds for failure in this project and the degree examination as a whole

Abstract
To rely on long and expensive annotation or to run only partially supervised machine learning algorithms? That is the dilemma faced by the argument mining researchers worldwide. This project aims to bridge the gap by using gamified crowdsourcing to create labeled data. So far an overview of possible application platforms has been performed, and a demo solution on the web has been produced.

Abstract
## Chapter 1: Introduction
## Chapter 2: Literature Survey
Expert annotation
Annotation with crowdsourcing
Online current corpora
Mixed approaches
## Chapter 4: Similar software review
Business solutions
Personal knowledge management tools
Research-grade software
## Chapter 3: Requirements and analysis
Requirements
Design decisions to be taken
success criteria
## Chapter 4: Conclusions, progress to date and project plan
Achievements to date
Gantt chart for the project

## Chapter 1: Introduction
How to get beyond bag-of-words approaches for meaning and sentiment analysis? 
How to get to the structure of the argument, that may escape even the utterer?
These are questions that interested researchers in discourse analysis for many years.

Data science has been applied with incredible success in many NLP tasks, sentiment analysis market valued at $3.15 billion in 2021 (“Sentiment Analytics Market Size Global Report, 2022 - 2030”, n.d.) The results are limited. Opinions gathered in this way are devoid of reasoning structure. The problem in many studies of argumentation is the undersupply of data. Yet there is plenty of online discourse. Online platforms, such as reddit, quora, twitter are host to the most resounding debates, heard by hundreds of millions.  Discussion topics include current political controversies and religious questions. Realms of both life and fiction provide vast space for disagreements. These discussions form the core of the public discourse in modern society. 

The act of commenting online corresponds to 'claiming ownership for a new piece of knowledge’ (Teufel, Siddharthan, and Batchelor 2009). Expressing arguments for, negotiating compromises, pursuing social shifts, finding or failing-to-find common ground - are all different types of discourses. The usual output is a series of posts, comments or tweets, that are under structured. Previous studies included attempts to automatically derive representations of the discourse structure from unstructured text (Anand et al 2011). The main drawback is the annotation cost, using dozens of hours of expert work, and tens of pages of annotation manuals.

This project is focused on data gathering. The goal is to investigate the 'games with purpose' paradigm to make crowdsourcing viable in this area. This report will go over the relevant literature, including human annotation schemas, and semi-supervised learning approaches, then review similar software. Based on that an outline of requirements is given. 
That section will be the basis for development of a more technical design document on a later date. Report will end with a description of achievements to date and plans for the future.

## Chapter 2: Literature Survey
Argument structure analysis goes back to antiquity. I. Angelelli. The techniques of disputation in the history of logic, 1970. Analysis of argumentation has been an active topic in numerous research areas, such as philosophy (van Eemeren et al., 2014), communication studies (Mercier and Sperber, 2011), and informal logic (Blair, 2004), among others
This ## Chapter will cover the areas that this project touches. There are different ways to approach the topic, here there will be examined the annotation and semi-supervised approaches.

Expert annotation
There are different strategies for annotation. Much of the study of annotation has focused on citation function in scientific papers. Many annotation schemes for argument citation motivation have been created (Teufel, Siddharthan, and Batchelor 2009), (Mann and Thompson 1987) and had success in research. 

These studies work by outlining analytically from a sample of essays, articles or other texts, an exhaustive list of types of roles of statements. Then the researchers proceed to create long, multi-page annotation guidelines. Up to 111 sides of A4 in some cases! (Teufel, Siddhartha, and Batchelor 2009). As the next step, annotators are selected. Some studies choose discipline experts, some on purpose select persons not familiar with the discipline. That is done in order to increase domain-independence of the annotation schema. 

The next step is usually to collate the annotations created by the annotators. 

Study by Siddharthan and Tidhar from 2006 (Teufel, Siddharthan, and Tidhar, n.d.) 'automatic classification of citation function' describes use of Kappa coefficient for that purpose. The paper describes the use of Kappa coefficient thus: “coefficient κ (Fleiss, 1971; Siegel and Castellan, 1988), the agreement measure predominantly used in natural language processing research (Carletta, 1996). κ corrects raw agreement P(A) for agreement by chance P(E)”.

In summary, the pure annotation strategy is costly but its experiences are quite helpful. The basic information flow pipeline is shown in (Razuvayevskaya and Teufel 2017): “mining: argument extraction, segmentation, i.e. identification of minimal argumentative discourse units (ADUs), segment classification, i.e. labeling of ADUs based on their argumentative roles, identification of relations between these segments, and argument completion, i.e. automatic construction of statements from implicit propositions”. The latter part includes enthymeme detection, which is defined as: “enthymemes are standard-form syllogisms with one missing proposition”.  (ibid.) For the crowdsourced model the 5 steps can be performed as a set of microtasks.

Annotation with crowdsourcing
A number of researchers explored the crowdsourcing area of the potential solution space to the problem of argument structure extraction. Following (von Ahn and Dabbish 2008), we can distinguish between 3 types of approaches to crowdsourcing with respect to the type of incentive provided to the participants. There is the financial approach, the altruistic approach, and the gamification (enjoyment) approach. Papers reviewed did not feature the enjoyment approach.

Starting chronologically, the first paper is (Abott et al. 2011). One of the features of this paper to note is its use of Amazon's "Mechanical Turk" service for contributions. Paid experts did the annotations. Another one is the choice of possible labels. These are 'agree/disagree', 'fact/emotion/, 'attack/insult', 'sarcasm', 'nice/nasty'. 

Another example comes from (Wyner, Peters, and Price 2015). They describe the tool: “ArgumentWorkbench, which is an interactive, integrated, modular tool set to extract, reconstruct, and visualize arguments. [...] The Argument Workbench is a processing cascade, developed in collaboration with DebateGraph. [...] it is an open source desktop application written in Java that provides a user interface for professional linguists and text engineers to bring together a wide variety of natural language processing tools and apply them to a set of documents”.

It is worth noticing that they used a desktop application. The other option being mobile application, there are tradeoffs visible. Mobile applications don't have the 'screen real estate' for complex interfaces, yet a higher number of people use them. Over 50% more people use mobile (“Desktop vs Mobile vs Tablet Market Share Worldwide”, n.d.). For a low-entry-cost crowdsourcing approach that is essential.

Then the authors attach a diagram and describe the workflow: “We harvest and preprocess comments; highlight argument indicators, speech act and epistemic terminology; model topics; and identify domain terminology [...] we use the GATE framework (Cunningham et al.(2002)) for the production of semantic metadata in the form of annotations.
Online current corpora
There are some ready corpora for argument meaning. This section will focus on their formats, topics and limitations.

Many studies mention source data themselves. For instance, (Awadallah, Ramanath, and Weikum 2012) say the following: ” For matching names in text sources against canonical entities, we leverage existing knowledge bases like DBpedia, Freebase, or Yago.”

Moreover, Argument mining survey (Lawrence and Reed, n.d.) mentions many of them:
“Internet Argument Corpus (IAC) (Walker et al. 2012) is a corpus for research in political debate on Internet forums. It consists of approximately 11,000 discussions, 390,000 posts, and some 73,000,000 words” 
“ AIFdb17 (Lawrence et al. 2012), containing over 14,000 Argument Interchange Format (AIF) argument maps, with over 1.6m words and 160,000 claims in 14 different languages. These numbers are growing rapidly, thanks to both the increase in analysis tools interacting directly with AIFdb and the ability to import analyses produced with the Rationale and Carneades tools (Bex et al. 2012). 

Both corpora focus on manual labeling.
The Argument Interchange Format seems as a valid standard for any argument crowdsourcing project to follow. Uniform storage of large quantities of data is very useful, and AIFdb Web platform allows portability across formats. This standardized JSON graph format makes data transport and display easier. That is a great opportunity as their platform features a display tool.  The project can leverage this external tool and standard and focus on other features of the crowdsourcing process. (“AIFdb Website”, n.d.)


Another resource of arguments online is the `args.me` online resource. Its creation is described in (Wachsmuth et al. 2017)- building an argument search engine for the WEB. Args.me has an exposed search API and database schemas. The paper also emphasizes the ethical choice contained in the construction of personalized search. It also mentions the high cost of the long hours of expert time. Another resource is the Araucaria program, mentioned by several papers. Link provided seems to be broken, though. (“Araucaria website”, n.d.)

There are cons to the current corpora, though. Only few publicly available argumentation corpora exist, as annotations are costly, error-prone, and require skilled human annotators (Habernal et al. 2014) (Stab and Gurevych 2014). Although argumentation mining in user-generated Web discourse has a long way to go (our methods currently achieve only about 50% of human performance)(ibid.).

Mixed approaches
The above approaches were deemed to be limited. In fact, there seems to have been a shift in approaches around 2014. There has been an argument that automatic processing is preferred due to the cost, unreliability of annotations and scarcity of trained personnel (Stab and Gurevych, 2014a)( Habernal et al., 2014)
With that being the turning point, the efforts thereafter have focused on putting the main weight of the process on the automated process. 
That reflects the wider industry shift towards the use of Machine Learning over the past 10 years.

Researchers concluded that manual analysis is not feasible in some studies (Habernal and Gurevych 2015). They attempted to bypass that problem using semi-supervised learning with some success.

Another approach is a blending approach. That consists in adding a small amount of high quality and manually labeled data. That vein of thought is explored in (Shnarch et al. 2018). Existence of this approach fares well for the crowdsourcing approach. Primarily the data will be strongly labeled, but if it proves weak for training using ML techniques, supplementation with weakly labeled data will be saving the utility of crowdsourced data.

Another attempt was this paper (Al-Khatib et al. 2016). This study makes the strongest case for the exclusion of crowdsourcing as a means of data acquisition: “Studies reveal that annotators need multiple training sessions to identify and classify argumentative segments with moderate inter-annotator agreement, and crowdsourcing-based annotation does not help notably (Habernal et al., 2014)
Of note is also the source of the data. Authors say: “we acquire a large corpus with 28,689 argumentative text segments from the online debate portal idebate.org. The corpus covers 14 separate domains with strongly varying feature distributions.

This source is highly specific. That argumentative discourse is not a representative sample of human argument space. Verbal arguments can be expected to be different; moreover users of idebate.org are likely to be students, or non-experts.

These arguments are put into the search system using the PageRank algorithm (Brin and Page 1998). That gives grounds to considering that algorithm a good basis for a ranking of arguments in other circumstances.

Games with purpose to the rescue
How to apply the GWP approach?
A guiding paper to this area of literature review was “Designing games with a purpose” (von Ahn and Dabbish 2008). Main takeaways from this paper is what makes games successful.
These are three main factors: enjoyment, timed response, and the ELO system.

"Enjoyment" is not defined formally there, but simply a result of knowing the games by their fruits: “ The key property of games is that people want to play them. We therefore sidestep any philosophical discussions about “fun” and “enjoyable,” defining a game as “successful” if enough human-hours are spent playing it”

That *a posteriori* features can be predicted by keeping the right level of challenge in front of the player. (Locke and Latham 1990) Right level of challenge is measured through a 'timed response' mechanic built into the game. The player's skill is evaluated on the basis of duration of the task. Self awareness of the speed of execution and the increasingly narrowing bar representing time left provides live feedback. ELO system ensures that in player versus player games there is balance. Each player can't go against players very far from their own skill level.

Moreover, it exploits the competitive desire in humans. The social factor seems valued in games as competitive sports are a growing market, with nearly 2 million US dollars revenue predicted in 2025. (Gough 2022)
Social factors have not been observed to feature in the studies mentioned so far. There was no competitiveness, the workflow was each annotator working individually. There was no incentive for agreement between annotators. This is a limitation that could be overcome.

The other takeaway is a set of metrics. These are
 labels per human hour
Average Lifetime Play

While the first one is self-explanatory, the second might not be. Study describes the latter as: “ALP is the overall amount of time the game is played by each player averaged across all people who have played it. For instance, on average, each player of the ESP Game plays for a total of 91 minutes.” Average score of 91 minutes is a good benchmark to compare with.

The other game is ‘Phrase Detectives’. (Poesio et al. 2013). It is the leading example of the use of the 'game with purpose' paradigm in view to gather data for NLP research. ALP in only 30 minutes. It seems there is a headspace to improve on that. nothing indicates that this area has hit a ceiling. What they excel at is: 'task completion, scoring and storyline as a seamless experience'. These are qualities worth emulating. 
Task completion and scoring are the easiest to implement. In contrast, creating a coherent and engaging storyline would require a specific skill set that might not always be available. Possibly emphasizing social features could substitute this.

## Chapter 4: Similar software review
There is a plethora of similar software. There are commercial B2B SAAS solutions, aiming to help in meetings, by providing a way to write structured notes and diagrams. There are also hacker-ethics personal knowledge management tools. There is also a record of software developed specifically for research. 

That software often can’t be directly used for creation of new datasets. Issues include data format portability, proprietary software and user interface.
Business solutions
There are many companies offering business-to-business services in NLP. These range from meeting minutes or report summaries, live structured note taking, visualization software, or customer sentiment analysis. Business model is frequently 'freemium', where users can use the app for free, but some features are hidden behind a paywall. I will only give a brief summary of each:

Lexikat provides "no-code concept maps and text analysis models from any document." (“Lexikat Website”, n.d.)
Infranodus is a multi-purpose analytics tool, extracting arguments and enhancing it through various AI techniques.  It is unknown whether the analysis uses argument mining. (“Infranodus Website”, n.d.)
Lexisnexis provides analytic tools in the legal domain, also providing visualization (“LexisNexis homepage”, n.d.)
Summetix uses Argument Mining to provide summaries of trends in customer behavior.
Reasoning lab is the creator of the Rationale Online service described below (“Argument Mapping - Reasoninglab”, n.d.)
Rationale Online - a huge collection of public maps. Of limited use as a dataset for studies in English, as most of the data is not in English. (“Rationale - online argument mapping”, n.d.)
Mindup - a tool for creating 'mind maps'. (“Mindup website”, n.d.)
Crowdee is a service providing crowdsourced contributions to business customers, with the specific niche of creating ML training datasets. (“Crowdee website”, n.d.)
Amazon Mechanical Turk is a service acting as a middleman between businesses seeking temporary increase in workforce to solve a specific issue. The service accomplishes this through splitting the workload into 'microtasks' that are then handled by a distributed workforce. (“Amazon Mechanical Turk Website”, n.d.)
Personal knowledge management tools
Argunet (Voigt and Betz 2018) (started in 2006) and the successor project argdown is a tool for argument representation. What is exceptional about the Argdown (“Argdown website”, n.d.) is that it provides a textual standard to represent arguments of any complexity.

Planner is the pioneer in the field, even if not exactly with *personal* applications in mind.
It was created in 1969 for forward and backward chaining of statements to prove some goal from the database. (Hewitt, Fikes, and Coles, n.d.) Its function was thus *synthetic*, not analytic - so the reverse of argument mining. Nevertheless, it is an interesting reference point.

Research-grade software

Started in 2000 and with the latest release in 2020, Flora2 is a system for knowledge representation using XSB for inference As it is clear from the website look and feel, this software is not for mass adoption. With less than 600 downloads over the last year (“Flora2 source code”, n.d.) it does not seem to have taken off. (“Flora2 website”, n.d.)

Zooniverse is a thriving crowdsourcing platform. There are many projects in the categories such as medicine, nature, climate and history. Not many projects in the language processing domain have been found yet. One example is an Optical Character Recognition crowdsourcing dealing with 19th century newspapers. (“Living with Machines — Zooniverse”, n.d.)

Insofar as the argument mining relates to Knowledge Graphs and Ontology extraction, Kelpie is one of the frameworks for the former. Authors say Kelpie is a: “XAI framework for interpreting Link Predictions on Knowledge Graphs” (“AndRossi/Kelpie: XAI framework for interpreting Link Predictions on Knowledge Graphs”, n.d.) It is in active development and it might be useful for downstream processing of the data obtained through crowdsourcing.
## Chapter 3: Requirements and analysis
Requirements
To avoid the pitfalls of human annotation, a quantitative approach should be pursued. A diverse range of both source texts and human participants is needed. Through the 'games with purpose' paradigm, we can expect users/ players to contribute for their own enjoyment (von Ahn and Dabbish 2008) . Enjoyment maximization should result in a higher number of Average Lifetime Contribution(ibid.). A spotless user flow and an intuitive application are of the highest priority to achieve that.

A sample user flow can be imagined as the following:
Player finds the landing page
Browses the list of topics popular at the moment
clicks to read more, is redirected to the app page
Finds a tutorial on how to engage with the system: read, and contribute new nodes

Over the following week:
user completes a small number of interactions with the application
user integrates the app importing some content on their own, be it from Twitter or other dynamic corpora (for instance a blog article to annotate to understand it better)
user continues to grow their use of the app, perhaps using it as a note taking app

Design decisions to be taken
There is the option for a debate mode for the app. That would be a type of game, where addition of a node to the argument tree would constitute a move. That type of game was examined in Prakken 2005. There were distinguished different types of 'reply protocols' - unique vs multi-reply, immediate and non-immediate, unique, multi-move. The configuration space is non-trivial, and the choice which of these protocols would be implemented in the game needs to be pondered. (Prakken 2005)
Another distinction between game-states comes from (Rienks, Heylen, and van der Weijden 2005)- argument diagramming of meeting conversations. That is the observation that there are more types of issues than just 'yes/no' issues. They call them: A/B issues, yes-no issue, open issue. It is obvious that the yes-no issue might be the simplest to implement, yet it would be a lost opportunity to forsake the other modes. Some consideration should be given to incorporating them into the space of possible arguments on the app.

As mentioned above, AIFdb format may be used for data portability, and Argdown for markdown notation.

Success criteria
The final criteria is the volume of quality annotated corpus. It could be uploaded to AIFdb. This will be known after performing quality control on the main argument database created through the lifetime of the app. The other criterion is the number of downloads - if larger than 150 better than global average, if more than 1300, over global average. (Ceci 2021) These data will be obtained from app publisher analytics.
## Chapter 4: Conclusions, progress to date and project plan
Achievements to date
To date the main achievement is exploration of the possibilities of mobile app development. 
Expo library was chosen for the simplicity of deployment to host the app https://expo.dev/, while a Nextjs website will serve as a landing page. There was some work - a demo of a drag-and-drop implemented in Reactjs. The full interactive interface proved harder than expected, and in the light of further discoveries of extant work, has proven superfluous.
Therefore it was not finished. The OVA platform already performs graph visualization quite well. (“Ova website”, n.d.)

Gantt chart for the project
Weeks up to 12 inclusive are from semester 1. Later weeks are from semester 2. With a remarked break for 8 weeks of Christmas break and examination period, and later 3 weeks of Easter break.

PCT OF TASK COMPLETE
11
12
Break
1
2
3
4
5
6
7
8
Break
9
10
Simple connected setup

SEO optimized landing page

design document


app MVP

publishing the app


gathering data

adding new tasks

adding new resource datasets

analyzing data

References
Abott, Rob, Marilyn Walker, Pranav Anand, Jean E. Fox Tree, Robeson Bowmani, and Joseph King. 2011. “How can you say such things?!?: Recognizing disagreement in informal political argument.” Proceedings of the Workshop on Language in Social Media LSM 2011:2-11.
“AIFdb Website.” n.d. AIFdb Corpora. Accessed December 5, 2022. https://corpora.aifdb.org/.
Al-Khatib, Khalid, Henning Waschsmuth, Matthias Hagen, Jones Köhler, and Benno Stein. 2016. “Cross-Domain Mining of Argumentative Text through Distant Supervision.” ACL Anthology. https://aclanthology.org/N16-1165.pdf.
“Amazon Mechanical Turk Website.” n.d. Amazon Mechanical Turk. Accessed December 5, 2022. https://www.mturk.com/.
“AndRossi/Kelpie: XAI framework for interpreting Link Predictions on Knowledge Graphs.” n.d. GitHub. Accessed December 5, 2022. https://github.com/AndRossi/Kelpie.
“Araucaria website.” n.d. YouTube. Accessed December 5, 2022. http://araucaria.computing.dundee.ac.uk/.
“Argdown website.” n.d. Argdown. Accessed December 5, 2022. https://argdown.org/.
“Argument Mapping - Reasoninglab.” n.d. - Reasoninglab. Accessed December 5, 2022. https://www.reasoninglab.com/argument-mapping/.
Awadallah, Rawia, Maya Ramanath, and Gerhard Weikum. 2012. “Harmony and dissonance: organizing the people's voices on political controversies.” WSDM '12: Proceedings of the fifth ACM international conference on Web search and data mining, (February), 523-532. https://doi.org/10.1145/2124295.2124359.
Blair, J Anthony, and Ralph H. Johnson. 2000. “Informal Logic: An Overview.” Informal Logic 20 (2). 10.22329/il.v20i2.2262.
Brin, Sergey, and Lawrence Page. 1998. “The anatomy of a large-scale hypertextual Web search engine.” Computer Networks and ISDN Systems 30:107-117.
Ceci, L. 2021. “Average downloads of U.S. apps 2020.” Statista. https://www.statista.com/statistics/1119893/average-number-downloads-united-states-app-publishers/.
“Crowdee website.” n.d. Crowdee – Innovative Crowd Solutions. Accessed December 5, 2022. https://www.crowdee.com/.
“Desktop vs Mobile vs Tablet Market Share Worldwide.” n.d. Statcounter Global Stats. Accessed December 5, 2022. https://gs.statcounter.com/platform-market-share/desktop-mobile-tablet.
“Flora2 source code.” n.d. Sourcefoge website for flora2. Accessed December 5, 2022. https://sourceforge.net/projects/flora/files/stats/timeline?dates=2021-12-04%20to%202022-12-03&period=daily.
“Flora2 website.” n.d. Flora-2. Accessed December 5, 2022. https://flora.sourceforge.net/.
Gough, Christina. 2022. “Global eSports market revenue 2025.” Statista. https://www.statista.com/statistics/490522/global-esports-market-revenue/.
Habernal, Ivan, and Iryna Gurevych. 2015. “Exploiting Debate Portals for Semi-Supervised Argumentation Mining in User-Generated Web Discourse.” ACL Anthology. https://aclanthology.org/D15-1255.pdf.
Habernal, Ivan, Henning Waschsmuth, Iryna Gurevych, and Benno Stein. 2014. “The Argument Reasoning Comprehension Task: Identification and Reconstruction of Implicit Warrants - Ivan Habernal† Henning Wachsmuth‡ Iryna Gurevych† Benno Stein.” ACL Anthology. https://aclanthology.org/N18-1175.pdf.
Hewitt, Carl, Richard Fikes, and Steven Coles. n.d. “Planner (programming language).” Wikipedia. Accessed December 5, 2022. https://en.wikipedia.org/wiki/Planner_(programming_language).
“Infranodus Website.” n.d. InfraNodus: Visual Text Network Insight Platform. Accessed December 5, 2022. https://infranodus.com/.
Lawrence, John, and Chris Reed. n.d. “Argument Mining: A Survey.” Computational Linguistics 2019:765–818. https://doi.org/10.1162/coli_a_00364.
“Lexikat Website.” n.d. Lexikat Facebook Word Cloud Generator. Accessed December 5, 2022. https://lexikat.com/#/.
“LexisNexis homepage.” n.d. Welcome to LexisNexis Legal & Professional. Accessed December 5, 2022. https://www.lexisnexis.com/en-us/home.page.
“Living with Machines — Zooniverse.” n.d. Zooniverse. Accessed December 5, 2022. https://www.zooniverse.org/projects/bldigital/living-with-machines.
Locke, Edwin, and Gary Latham. 1990. “A Theory of Goal Setting & Task Performance.” he Academy of Management Review. 10.2307/258875.
Mann, William C., and Sandra A. Thompson. 1987. Antithesis: A Study in Clause Combining and Discourse Structure. N.p.: Corporate Author: UNIVERSITY OF SOUTHERN CALIFORNIA MARINA DEL REY INFORMATION SCIENCES INST. https://apps.dtic.mil/sti/citations/ADA181350.
Mercier, H., and D. Sperber. n.d. Why do humans reason? Arguments for an argumentative theory. Vol. 34(2). N.p.: Behavioral and Brain Sciences.
“Mindup website.” n.d. MindMup. Accessed December 5, 2022. https://www.mindmup.com/.
“Ova website.” n.d. Ova website with an example graph. Accessed December 5, 2022. http://ova.arg-tech.org/analyse.php?url=local&aifdb=1238&akey=dd8dd1dfd567f735f46df14ff08a0fc5.
Poesio, Massimo, Jon Chamberlain, Udo Kruschwitz, Livio Robaldo, and Luca Ducceschi. 2013. “Phrase Detectives: Utilizing Collective Intelligence for Internet-Scale Language Resource Creation.” ACM Trans. Interact. Intell. Syst. 3, no. 1 (April). https://doi.org/10.1145/2448116.2448119.
Prakken, Henry. 2005. “Coherence and Flexibility in Dialogue Games for Argumentation.” Journal of Logic and Computation, 15, no. 6 (December): 1009-1040. https://doi.org/10.1093/logcom/exi046.
“Rationale - online argument mapping.” n.d. Rationale - online argument mapping. Accessed December 5, 2022. https://www.rationaleonline.com/browse/all.
Razuvayevskaya, Olesya, and Simone Teufel. 2017. “Finding enthymemes in real-world texts: A feasibility study.” Argument & Computation 8:11-129. 10.3233/AAC-170020.
Rienks, Rutger, Dirk Heylen, and Erik van der Weijden. 2005. “Argument Diagramming of Meeting Conversations.” Research Information System (RIS) Pure | research.utwente.nl | University of Twente | Service Portal. https://ris.utwente.nl/ws/portalfiles/portal/246973183/Rienks2005argument.pdf.
“Sentiment Analytics Market Size Global Report, 2022 - 2030.” n.d. Polaris Market Research. Accessed December 4, 2022. https://www.polarismarketresearch.com/industry-analysis/sentiment-analytics-market.
Shnarch, Eyal, Carlos Alzate, Lena Dankin, Martin Gleize, Hou Yufang, Leshem Choshen, Ranit Aharonov, and Noam Slonim. 2018. “Will it Blend? Blending Weak and Strong Labeled Data in a Neural Network for Argumentation Mining.” ACL Anthology. http://aclweb.org/anthology/P18-2095.
Stab, Christian, and Iryna Gurevych. 2014. “Identifying Argumentative Discourse Structures in Persuasive Essays.” ACL Anthology. https://aclanthology.org/D14-1006.pdf.
“Summetix website.” n.d. summetix (formerly ArgumenText). Accessed December 5, 2022. https://www.summetix.com/.
Teufel, Simone, Advaith Siddharthan, and Colin Batchelor. 2009. “Towards domain-independent argumentative zoning: Evidence from chemistry and computational linguistics.” Proceedings of the 2009 conference on empirical methods in natural language processing,, 1493-1502. https://aclanthology.org/D09-1155.pdf.
Teufel, Simone, Advaith Siddharthan, and Dan Tidhar. n.d. “Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing.” ACL Anthology. Accessed December 5, 2022. https://aclanthology.org/W06-1613.pdf.
van Eemeren, Frans H., and Bart Garssen. 2014. “Argumentation by analogy in stereotypical argumentative patterns.” Systematic approaches to argument by analogy Springer, Cham.
Voigt, Christian, and Gregor Betz. 2018. “Argunet Website.” Argunet - Open-Source Argument Mapping. http://www.argunet.org/.
von Ahn, Luis, and Laura Dabbish. 2008. “Designing Games With a Purpose.” CMU School of Computer Science. https://www.cs.cmu.edu/~biglou/GWAP_CACM.pdf.
Wachsmuth, Henning, Martin Potthast, Khalid Al-Khatib, Yamen Ajjour, Jana Puschmann, Jiani Qu, Jonas Dorsch, Viorel Morari, Janek Bevendorff, and Benno Stein. 2017. “Building an Argument Search Engine for the Web.” ACL Anthology. https://aclanthology.org/W17-5106.pdf.
Wyner, Adam, Wim Peters, and David Price. 2015. “Argument Discovery and Extraction with the Argument Workbench.” https://aclanthology.org/W15-0510.pdf.
