# for later

## Stanford textbook
https://web.stanford.edu/~jurafsky/slp3/

## ibm debater
### what is it
https://research.ibm.com/interactive/project-debater/about/
> How does the Debater system know if a claim is for or against the topic it's given?
> This is one of the many aspects that make Project Debater unique. It has been taught to understand the nuances of language and decide the stance of an argument given the topic. Imagine debating the pros and cons of the use of traffic enforcement cameras. When given the claim 'the photo radar program fails to provide any clear safety benefit,' a human debater instinctively understands it contests the use of traffic cameras. But this type of understanding is very hard for AI. The Debater system approaches this by breaking it down into smaller tasks. The system understands that 'the photo radar program' is associated with 'traffic enforcement cameras' and further understands that the rest of the sentence—even though it includes positive words like 'safety' and 'benefit'—is, in fact, contesting the use of traffic enforcement cameras



### how does it work
https://research.ibm.com/interactive/project-debater/how-it-works/
> The third is the system’s ability to model human dilemmas and form principled arguments made by humans in different debates based on a unique knowledge graph.

step 1 undertstanding the topic
10 billion sentences, newspapers, journals


step 2 argument construction
into few hundred relevant arguments


step 3 content organization
deleting weak and repetitive arguments

arrangement by theme
// is the theme some emotion?
knowledge graph to support general human dilemmas


step 4 constructing an argument and rebuttal
rebutal the hardest part
- anticipate and identigy
- respond

#### argument mining
- relevant documents
Context Dependent Claim Detection
Ran Levy et al.

COLING, 2014
http://www.aclweb.org/anthology/C/C14/C14-1141.pdf 


- detecting evidence inside documents
http://aclweb.org/anthology/D15-1050
Show Me Your Evidence - An Automatic Method for Context Dependent Evidence Detection
Ruty Rinott et al.
EMNLP, 2015

study, expert and anecdotal evidence types

- negating claims
first rule-based see what is a good negation
second statiscially see when can be used

http://www.aclweb.org/anthology/W15-05#page=96
Automatic Claim Negation∶ Why, How and When
Yonatan Bilu et al.

2nd Argument Mining Workshop, NAACL, 2015


- novel claims - through recycling - text extraction
- Claim Synthesis via Predicate Recycling
Yonatan Bilu and Noam Slonim

ACL, 2016
http://www.aclweb.org/anthology/P/P16/P16-2.pdf#page=559

- detecting claims - for unsupervised - no human annotation
- Unsupervised Corpus-Wide Claim Detection Recycling
Ran Levy, Shai Gretz, Benjamin Sznajder, Shay Hummel, Ranit Aharonov, and Noam Slonim

Argument Mining, 2017
http://www.aclweb.org/anthology/W17-5110


- improving the detecxtion
- argumentative content search engine - DNNs with weak supervision, automatic labeling
Towards an Argumentative Content Search Engine Using Weak Supervision Detection
Ran Levy et al.

COLING, 2018
http://aclweb.org/anthology/C18-1176

- argumentation quality
- systenatic typology
Computational Argumentation Quality Assessment in Natural Language
Henning Wachsmuth et al.
https://www.uni-weimar.de/medien/webis/publications/papers/stein_2017c.pdf
EACL, 2017

Argumentation Quality Assessment∶ Theory vs. Practice
Henning Wachsmuth et al.
https://www.uni-weimar.de/medien/webis/publications/papers/stein_2017g.pdf
ACL, 2017

- across texts
- Argument Relation Classification Using a Joint Inference Model
Yufang Hou and Charles Jochim

4th Argument Mining Workshop, EMNLP, 2017
http://aclweb.org/anthology/W17-5107




#### stance classification and sentiment analysis
- determining exprert stance
- - Wikipedia, 100'000 experts, 100 topics
Expert Stance Graphs for Computational Argumentation
Orith Toledo-Ronen et al.
http://aclweb.org/anthology/W/W16/W16-2814.pdf

ArgMining @ ACL, 2016

- whether each claim supports some topic
- sub-tasks and AI solutions
- Stance Classification of Context-Dependent Claims
Roy Bar-Haim et al.

EACL, 2017
http://www.aclweb.org/anthology/E/E17/E17-1024.pdf

- improving that classification
- sentiment prediction based on context
Improving Claim Stance Classification with Lexical Knowledge Expansion and Context Utilization
Roy Bar-Haim et al.

4th Argument Mining Workshop, EMNLP, 2017

https://argmining2017.files.wordpress.com/2017/08/argmining2017-04.pdf

- sentiment phrase classification 
- Learning Sentiment Composition from Sentiment Lexicons
Orith Toledo-Ronen et al.

COLING, 2018
http://www.aclweb.org/anthology/C18-1189

- classifiying idioms - 5000 common ones
- SLIDE - A Sentiment Lexicon of Common Idioms
Charles Jochim et al.

LREC, 2018
http://www.lrec-conf.org/proceedings/lrec2018/pdf/602.pdf


#### DNNs and weak supervision
weak supervision, also for speaking and listening
- scoring arguments - 19 DNN based methods
An Empirical Evaluation of Various Deep Learning Architectures for Bi-Sequence Classification Tasks
Anirban Laha and Vikas Raykar

COLING, 2016
http://www.aclweb.org/anthology/C16-1260

- speech recognition - adding punctuation
- Joint Learning of Correlated Sequence Labelling Tasks Using Bidirectional Recurrent Neural Networks
Vardaan Pahuja et al.

Interspeech, 2017
https://arxiv.org/pdf/1703.04650.pdf

- phrase breaks prediction to have intelligibile, natural expressive speech
- Weakly-Supervised Phrase Assignment from Text in a Speech-Synthesis System Using Noisy Labels
Asaf Rendel et al.

Interspeech, 2017
https://www.researchgate.net/publication/319184974_Weakly-Supervised_Phrase_Assignment_from_Text_in_a_Speech-Synthesis_System_Using_Noisy_Labels

- emhasis on word na dsentence level
- Emphatic Speech Prosody Prediction with Deep LSTM Networks Slava Shechtman and Moran Mordechay
ICASSP, 2018
https://www.semanticscholar.org/paper/Emphatic-Speech-Prosody-Prediction-with-Deep-Lstm-Shechtman-Mordechay/8bfa38df475029dd09a25651d0dfdd5538963898

- improving speech 
- Emphatic Speech Prosody Prediction with Deep LSTM Networks Yosi Mass et al.
Interspeech, 2018
https://www.isca-speech.org/archive/Interspeech_2018/pdfs/1159.pdf

- finding similarities between sentences
Learning Thematic Similarity Metric from Article Sections Using Triplet Networks
Liat Ein-Dor et al.

ACL, 2018
https://aclanthology.org/P18-2009/


# important
- adding small amont of high quality and manually labeled data
Will it Blend? Blending Weak and Strong Labeled Data in a Neural Network for Argumentation Mining
Eyal Shnarch et al.

ACL, 2018
http://aclweb.org/anthology/P18-2095


- whole corpus search
- waek supervision - not human intervention

Towards an Argumentative Content Search Engine Using Weak Supervision 
Ran Levy et al.
COLING, 2018
http://aclweb.org/anthology/C18-1176


- seeing if abstract or concrete
- Learning Concept Abstractness Using Weak Supervision 
Rabinovich et al.

EMNLP, 2018
https://arxiv.org/abs/1809.01285



#### TTS systems
- predicting phrase breaks
DNN for pause

Weakly-Supervised Phrase Assignment from Text in a Speech-Synthesis System Using Noisy Labels
Asaf Rendel et al.

Interspeech, 2017

- emphasis - world and sentence level
Emphatic Speech Prosody Prediction with Deep LSTM Networks Slava Shechtman and Moran Mordechay
ICASSP, 2018
https://www.semanticscholar.org/paper/Emphatic-Speech-Prosody-Prediction-with-Deep-Lstm-Shechtman-Mordechay/8bfa38df475029dd09a25651d0dfdd5538963898


- improvbing speech patterns
- prediction with DNN, 1 module for emphasis, another for speech patterns

Emphatic Speech Prosody Prediction with Deep LSTM Networks Yosi Mass et al.
Interspeech, 2018
https://www.isca-speech.org/archive/Interspeech_2018/pdfs/1159.pdf


### importantcce
https://research.ibm.com/interactive/project-debater/importance/
> The rise of one-sided and doctored narratives is challenging society and our platforms. Too often, we talk past one another. We need a smarter way. New developments in language and reasoning in AI can help shine a light in the darkness of distorted facts to provide diverse, well-informed viewpoints—both the pro and the con.

> The world is awash with information, misinformation, and superficial thinking. Project Debater pushes the frontiers of AI to facilitate intelligent debate so we can build well-informed arguments and make better decisions.

Text Categorization: Email spam filters
AI can categorize text based on its content.

Basic Q&A: Virtual assistants
AI can support short, command-based interactions using templated responses.

Open Questions: Watson on Jeopardy!
AI can respond to open-ended questions.

Free-Form Debate: Project Debater
AI can meaningfully engage in full debates on complex topics.

### research
https://research.ibm.com/interactive/project-debater/research/
3 latest (2021) papers, all seem similar

### Nature paper - done


### datasets - needs investigating
https://research.ibm.com/haifa/dept/vst/debating_data.shtml


## games with purpose - 10 pages
Designing games with a purpose
https://dl.acm.org/doi/10.1145/1378704.1378719

list of issues and problems from the wikipedia page for Google Image Labeler

https://en.wikipedia.org/wiki/Google_Image_Labeler#Issues_and_problems 

> paradigm we describe here does not rely on altruism or financial incentives to entice people to perform certain actions; rather, they rely on the human desire to be entertained

output-agrement games
inversion problem games - one side describes, the other guesses input
- a level of transparency after the results
- alternation


display time remaining

> We know from the literature on motivation in psychology and organizational behavior that goals that are both well-specified and challenging lead to higher levels of effort and task performance than goals that are too easy or vague.


player ranks and points 
high score list

randomness
#### output accuracy
- random matching to prevent pre-match agreement
- player testing - with known outputs - 50% of the tasks can be tests
- repetition - not 1 player input to decide something valid


diff than 2 players
- pairing with pre-recorded responses
- more than 2 - first 2 to agree win the round


#### metrics for evaluation
- algorithm - liuke efficincy
ESP game - 233 labels per human hour

> Our approach to quantifying this elusive measure is to calculate and use as a proxy the “average lifetime play” (ALP) for a game. ALP is the overall amount of time the game is played by each player averaged across all people who have played it. For instance, on average, each player of the ESP Game plays for a total of 91 minutes.

getting the expected contribution
contagion not factored in in this model

- bite sized
> The “bite-size” nature of these games adds to their popularity and appeal to casual gamers in particular, since such players typically go for games they can play “just one more time” without having to make too much of a time commitment


## rl for nlp - 53 slides
-  https://en.wikipedia.org/wiki/ROUGE_(metric)
-  the standard approach
https://en.wikipedia.org/wiki/Seq2seq


# additional GWAP papers
> M-GWAP: An Online and Multimodal Game With A
Purpose in WordPress for Mental States Annotation
https://arxiv.org/ftp/arxiv/papers/1905/1905.12884.pdf

> How to Design a Game With a Purpose
https://shivamrana.me/2020/02/gwap-2/


Peekabum
https://www.cs.cmu.edu/~biglou/Peekaboom.pdf

ESP game
https://en.wikipedia.org/wiki/ESP_game


Amazon Mechanical Turk
https://www.mturk.com/


openminds
https://openminds.harrys.com/

psdoom
https://psdoom.sourceforge.net/


verbosity
https://www.cs.cmu.edu/~biglou/Verbosity.pdf 

phetch
https://en.wikipedia.org/wiki/Phetch#:~:text=Phetch%20is%20played%20by%20three,find%20the%20image%20being%20described.


# long reads
## phrase detectives - 44 pages
Phrase detectives: Utilizing collective intelligence for internet-scale language resource creation
https://dl.acm.org/doi/10.1145/2448116.2448119
phrase detectives is a game
collective interlligence, Wikipedia

crowdflower, mechanical turk
von Ahn and collegues mentioned
1http://www.mturk.com. 2http://crowdflower.com. 3http://www.phrasedetectives.org.

Wikipedia-style “citizen science,” crowdsourcing, and games-with-a-purpose

there was a remark on adult themes

need definitely 'Argument detectives' mode
### papers mentioned
SALSA [Burchadt et al 2009]
ONTONOTES [Hovy et al 2009, Pradhan et al 2007]

open mind common sense - Singh 2002 - 14,5k volunteers

LEARNER [Chklovski and GIl 2005]

concept netmedia mit edu
freebase.com
trueknowledge

data for multimedia tagging
FoldIt important
onto tube, tag a tune - gwap com
verbosity, ontogame, categorilla, free association - get all links

15http://en.wikipedia.org/wiki/Google Image Labeler. 16http://ontogame.sti2.at/games. 17http://www.gwap.com/gwap/gamesPreview/tagatune. 18http://www.gwap.com/gwap/gamesPreview/verbosity. 19http://ontogame.sti2.at/games. 20http://www.doloreslabs.com/stanfordwordgame/categorilla.html. 21http://www.doloreslabs.com/stanfordwordgame/freeAssociation.html. 22The current GWAP from von Ahn’s lab are playable from http://www.gwap.com. 23http://fold.it/portal.

Phylo, EteRNA


underlie social incentive
consistent metaphor
ancientlives.org - university of Oxford



ESP game - advertised in press and tv
retainment - volunteer attrition - Lieberman and Teeters 2007]

3.4 summary of von Ahn's theory - enjoymnet - timed response, scores, ELO system

geoguesser?

discourse model [Kamp and Reyle 1993]

choice of algorithm aiming at maximum variety

need to be able to commment about markables


validating annotations fater than creating - [Chklovski and GIl 2005], bu not quite - almost twice as much time


task completion, scoring and storyline as a seamless experience
smalll prize campaign, monthly prizes
any sumbission can do, so don't need to do a lot of them
7http://www.modul.ac.at/nmt/sentiment-quiz. 38http://languagelog.ldc.upenn.edu/nll. 39http://lingpipe-blog.com.

only 4$ indicate topic preference

only 1 player generated content on their own

game tips at random in waiting screen

annotation + agreement - disagreemtn

using social network to fitler out rogue players

not much movement through Facebook advert

on ARRAU corpus [Poesia and Artstein 2008]

university of Bielefeld's Seregenti system [ Poesia et al. 2011a]

preprocessing pipeline - Berkeley parser [Petrov et a 2006], openNLP toolkit
http://incubator.apache.org/opennlp. 46http://saxon.sourceforge.net.

51http://www.gutenberg.org. 52http://www.textfiles.com.

average lifetime play 35 mins

if truly entertaining no other incentives - need personal, social as well

56http://galoap.codeplex.com.

## Survey on reinforcement learning for language processing - 37 pages
https://arxiv.org/abs/2104.05565 
Russel and Norvig - natural langue as probability distributions over sentnces, not definitive sets
need to deal with ambiguity


reinvorfement learning multi-agent system
I. Mordatch and P. Abbeel. Emergence of Grounded Compositional Language in Multi-Agent Populations. Proceedings of the AAAI Conference on Artificial Intelligence, 32(1), Apr. 2018.

this work --> problems of reward sparsity and mode collapse
Z. Shi, X. Chen, X. Qiu, and X. Huang. Toward Diverse Text Generation with Inverse Reinforcement Learning. In International Joint Conference on Artificial Intelligence (IJCAI), volume 27th, pages 4361–4367, Stockholm, Sweden, July 2018

Li et al. [74] simulated a dialogues between two virtual agents, and sequences that display three useful conversational properties are rewarded. These properties are: informativity, coherence, and ease of answering. This RL model uses policy gradient methods.

Thus, we argue that a future research direction would be to develop a reinforcement learning approach for generating internal semantic representations of the user’s message from which other fields within and beyond natural language processing could benefit.

Sentence generation is also difficult for supervised sentence embeddings such as InferSent [21] or Google’s Universal Sentence Encoder [12].

For example, it could be desired to maximize the positive sentiment of an upcoming utterance which can be estimated by a differentiable neural network [6].


## Argument mining survey - 54 pages
https://direct.mit.edu/coli/article/45/4/765/93362/Argument-Mining-A-Survey

For example, Robert Horn, talking about the argument maps he produced on the debate as to whether computers can think, quotes a student as saying “These maps would have saved me 500 hours of time my first year in graduate school”; 1 however, Metzinger (1999) notes that over 7,000 hours of work was required in order for Horn and his team to create these maps.

(with ACL workshops on the topic being held annually, from the first in 2014,3 up to the most recent in 2019,4 which received a record number of 41 submissions. These have been complemented by further workshops organized in Warsaw,5 Dundee,6 Dagstuhl,7 and tutorials at IJCAI,8 ACL 2016,9 ACL 2019,10 and ESSLLI.11) This increasing activity makes a comprehensive review of both timely and practical value.

1 http://www.stanford.edu/~rhorn/a/topic/phil/artclTchngPhilosphy.html. 2 Sometimes also referred to as argumentation mining. 3 http://www.uncg.edu/cmp/ArgMining2014/. 4 https://argmining19.webis.de/. 5 http://argdiap.pl/argdiap2014. 6 http://www.arg-tech.org/swam2014/. 7 https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=16161. 8 http://www.i3s.unice.fr/~villata/tutorialIJCAI2016.html. 9 http://acl2016tutorial.arg.tech/.
10 http://arg.tech/~chris/acl2019tut/index.html. 11 https://www.irit.fr/esslli2017/courses/20.

Finally, in Section 2.4, we look at argumentative zoning, where scientific papers are annotated at the sentence level with labels that indicate the rhetorical role of the sentence (criticism or support for previous work, comparison of methods, results or goals, etc.).

Negation tagging is also performed using a technique from Das and Chen (2001) whereby the tag NOT_ is prepended to each of the words between a negation word (“not,” “isn’t,” “didn’t,” etc.) and the first punctuation mark occurring after the negation word. In terms of relative performance, the support vector machines (SVMs) achieved the best results, with average 3-fold cross-validation accuracies over 0.82 using the presence of unigrams and bigrams as features.


Conflicting elements in an opinion tree are then used to generate a “conflict tree,” similar to the dialectical trees (Prakken 2005) used traditionally in defeasible argumentation (Pollock 1987)

Using reviews from epinions.com, which allows a user to give their review as well as specific positive and negative points, these specific positive and negative phrases were first collected and then the main review searched for sentences that covered most of the words in the phrase

Boltuˇzi´c and ˇSnajder (2015), where argumentative statements are clustered based on their textual similarity, in order to identify prominent arguments in online debates

The results for subtopic identification are poor, with an F-score of 0.50; however, identifying controversial issues is considerably more successful, with a precision of 0.83.14

Awadallah, Ramanath, and Weikum (2012) present the OpinioNetIt system, which
aims to automatically derive a map of the opinions-people network from news and other Web documents. The network is constructed in four stages.

Siddharthan, and Tidhar (2006) look at how this classification can be automated. A classification scheme is first developed using guidelines for twelve different categories (explicit statement of weakness, four types of contrast/comparison, six types of agreement/ usage, and neutral

In Teufel, Siddharthan, and Batchelor (2009), an annotation scheme covering 14
possible roles is used to classify sentences into mutually exclusive categories

In this section we look at the task of manual argument analysis, considering the steps involved and tools available, as well as the limitations of manually analyzing large volumes of text. Understanding manual analysis can offer unique insight into how this task can be automated and provides a valuable insight into how an analyst unpicks the complex argumentative relationships represented in natural language texts

a wide range of specific argument diagramming tools (Scheuer et al. 2010) has been developed to allow an analyst to identify the argumentative sections of the text and diagram the structure that they represent (Kirschner, Buckingham-Shum, and Carr 2003; Okada, Shum, and Sherborne 2008). The

all agree that EDUs are non-overlapping spans of text corresponding to the atomic units of discourse. Peldszus and Stede (2013a) refer to these argument segments as “argumentative discourse units” (ADUs

The Argument from Expert Opinion scheme (Walton 1996) is commonly used to
illustrate the concept:
Major Premise: Source E is an expert in subject domain S containing proposition A. Minor Premise: E asserts that proposition A is true (false). Conclusion: A is true (false).
with the associated critical questions:
1. 2. 3.
Expertise Question: How credible is E as an expert source? Field Question: Is E an expert in the field F that A is in? Opinion Question: What did E assert that implies A?
4. Trustworthiness Question: Is E personally reliable as a source? 5.
Consistency Question: Is A consistent with what other experts assert? 6. Backup Evidence Question: Is E’s assertion based on evidence?


Recent study has resulted in the identification and analysis of the most important
and commonly used schematic structures (Hastings 1963; Perelman and OlbrechtsTyteca 1969; Kienpointer 1992; Pollock 1995; Walton 1996; Grennan 1997; Katzav and Reed 2004; Walton, Reed, and Macagno 2008)
Araucaria, for example, supports theWalton, Grennan, Perelman and Olbrechts-Tyteca, Katzav and Reed, and Pollock scheme sets.


One of the challenges faced by current approaches to argument mining is the lack of large quantities of appropriately annotated arguments to serve as training and test data. Several recent efforts have been made to improve this situation by the creation of corpora across a range of different domains.

Green (2014) aims to create a freely available corpus of open-access,
full-text scientific articles from the biomedical genetics research literature, annotated to support argument mining research.

Similarly, Habernal and Gurevych (2015) use large volumes of unlabeled data from
online debate portals. By identifying clusters of both sentences and posts from these debate portals that contain similar phrases, and then finding the centroids of these clusters, “prototypical arguments” are identified. Al-Khatib et al. (2016) likewise leverage online debate portals, generating annotations by automatically mapping source data, in this case the labeled text components from the idebate.org (e.g., “Introduction,” “point,” “counterpoint”), to a set of predefined class labels to create a large corpus with argumentative and non-argumentative text segments from several domains

Drawn from 402 English language essays, the final corpus contains 751 major claims, 1,506 claims, and 3,832 premises, connected by 3,613 support and 219 attack relations. A random sample of 102 essays taken from the AAEC have been further annotated, as described in Carlile et al. (2018), to also

Kirschner, Eckle-Kohler, and Gurevych (2015) present a corpus of 24 German language articles, which were selected from the education research domain, and annotated using a custom designed tool (DiGAT). The annotation scheme used identifies binary relations between argument components, which in this work correspond to sentences from the original texts. Four types of relation are identified: support, attack, detail, and sequence. The first two of these relations are argumentative, whereas the latter two are discourse relations similar to the sequence and background relations of Rhetorical Structure Theory (Mann and Thompson 1987).
Four types of relation are identified: support, attack, detail, and sequence. The first two of these relations are argumentative, whereas the latter two are discourse relations similar to the sequence and background relations of Rhetorical Structure Theory (Mann and Thompson 1987

A different domain is considered in Kiesel et al. (2015), who present a corpus of
200 newspaper editorials annotated for their argumentative structure. The annotation is based on a model consisting of explicit argumentative units, and the implicit argumentative relations (i.e., support or attack) between them. In this case, an argumentative unit is understood to be a segment of the original text containing at least one proposition. Argumentative relations are considered as the links from one unit to the unit that it most directly supports or attacks

Internet Argument Corpus (IAC) (Walker et al. 2012) is a corpus for research
in political debate on Internet forums. It consists of approximately 11,000 discussions, 390,000 posts, and some 73,000,000 words

AIFdb17 (Lawrence et al. 2012), containing over 14,000 Argument Interchange Format (AIF) argument maps, with over 1.6m words and 160,000 claims in 14 different languages.18 These numbers are growing rapidly, thanks to both the increase in analysis tools interacting directly with AIFdb and the ability to import analyses produced with the Rationale and Carneades tools (Bex et al. 2012). Indeed, AIFdb aims to provide researchers with a facility to store large quantities of argument data in a uniform way. AIFdb Web services allow data to be imported and exported in a range of formats to encourage re-use and collaboration between researchers independent of the specific tools and data format that they require.

as DebateGraph,19 TruthMapping,20 Debatepedia,21 Agora,22 Argunet23 and Rationale Online24

At the moment, some research projects continue to introduce ad hoc, idiosyncratic data representation languages for argumentation and debate, which can limit reusability, integration, and longevity of the data sets.


The most striking example of such are recent data sets gathered from the ChangeMyView (CMV) Reddit subcommunity25 (Tan et al. 2016; Hidey and McKeown 2018; Musi, Ghosh, and Muresan 2018

17 http://www.aifdb.org. 18 Chinese, Dutch, English, French, German, Hindi, Italian, Japanese, Korean, Polish, Portuguese, Russian, Spanish, and Ukrainian.
19 http://debategraph.org 20 https://www.truthmapping.com 21 http://www.debatepedia.org 22 http://agora.gatech.edu/ 23 http://www.argunet.org/ 24 https://www.rationaleonline.com/ 25 https://www.reddit.com/r/changemyview/

meeting data from the AMIDA Meeting Corpus26 annotated using the Twente Argumentation Scheme (Rienks, Heylen, and Weijden 2005), and product reviews fromWeb sites such as Amazon and epinions.com.

https://www.kurzweilai.net/introducing-a-new-feature-of-ibms-watson-the-debater

then combined with a smaller quantity of high quality, manually labeled data (strong labeled data). Using the combined strong and weak data set resulted in improved performance for topicdependent evidence detection, suggesting that this kind of data gathering can be a valuable asset, particularly in data-hungry neural network systems. The annotated data sets used in this and other Project Debater work are all available online.30

DART (Data set of Arguments and their Relations on Twitter) data set containing 4,000 tweets annotated as argument/not-argument with 446 support and 122 attack relations.


if the goal is to reconstruct enthymemes (Razuvayevskaya and Teufel 2017) (see also the discussion of Feng and Hirst [2011] in Section 8.2) or ask critical questions about support relations, we also need to extract the nature of the argumentation schemes being used.

Rumshisky et al. (2017) look at the dynamics of social or political conflict as it develops over time, automatically identifying controversial issues where such conflict is occurring

Similarly, Goudas et al. (2014) look at extracting arguments from social media,
proposing a two-step approach for argument extraction similar to that used by Moens et al., first using a statistical approach through the use of machine learning and, more specifically, the logistic regression classifier to classify sentences as being part of the argument being made or not.

Carstens and Toni (2015), who instead advocate classifying pairs of sentences according to their argumentative relation and, if the relation is classified as support or attack, considering both sentences to be argumentative.

Similarly, Wachsmuth, Stein, and Ajjour (2017) propose a model for determining
the relevance of arguments using PageRank (Brin and Page 1998). In this approach, the relevance of an argument’s conclusion is decided by what other arguments reuse it as a premise. These

Soricut and Marcu (2003) as part of the SPADE system, which also operates on lexicalized syntactic trees

Anand et al. (2011) consider a different level of intrinsic clausal properties than
those discussed so far, looking not at the structural nature of propositions, but at their function

Persuasion involves the change in mental state of the other party classed as either Belief Revision, Attitude Change, or Compliance Gaining

12 strategy types for securing behavioral compliance. A further six nonlogical “principles of influence” are covered in Cialdini (2001). By combining these with argumentative patterns inspired by Walton, Reed, and Macagno (2008), and removing overlapping tactics, Anand et al. produce a list of 16 types of rhetorical tactic for persuasive acts


The Automatic Argumentative Analysis (A3) algorithm described in Pallotta and
Delmonte (2011) provides an alternative approach to classifying statements according to rhetorical roles. A3 is a module developed based on the GETARUNS system (Delmonte 2007) for interaction mining (the discovery and extraction of insightful information from digital conversations, namely, those human–human information exchanges mediated by digital network technology).

The benefits of using even a simple linguistic analysis to study the argumentative
structure of a document are illustrated in Ong, Litman, and Brusilovsky (2014), where a series of simple rules are used to tag sentences with their role (either Current Study, Hypothesis, Claim, or Citation), for example, if the sentence contains a four-digit number, then it is tagged as Citation, if the sentence contains string prefixes from {suggest, evidence, shows, essentially, indicate}, then it is tagged as Claim. This approach again highlights the similarities between AZ (Section 2.4) and the determination of argumentative role. The ability to determine these roles offers the opportunity to link related elements, for example, a Claim may be backed by a nearby Citation

Wyner further develops the concept of using argument mining as a way to assist
manual analysis in Wyner, Peters, and Price (2015), which describes the development of Argument Workbench, a tool designed to help the analyst reconstruct arguments from textual sources by highlighting a range of discourse indicators, topics used in the text, domain terminology, and speech act terminology. The tool integrates with the DebateGraph software,33 to allow the user to produce detailed argument graphs

A
...explicitly attacks the argument a
N s
S
...vaguely/implicitly attacks the argument ...makes no use of the argument
...vaguely/implicitly supports the argument ...explicitly supports the argument
semantic textual similarity features with the best models outperforming the baselines and giving a 0.71 to 0.82 micro-averaged F-score. Although these results give a promising indication of the ability to determine how a comment relates to the argument being made, the topics studied are limited and the training data taken from procon.org and idebate.org would not extend to general topics.


Topic: There She Is, Miss America
Additional info: In 1968, feminists gathered in Atlantic City to protest the Miss America pageant, calling it racist and sexist. Is this beauty contest bad for women?)
Argument: Miss America gives honors and education scholarships. And since . . . , Miss America is good for women.
a) scholarships would give women a chance to study b) scholarships would take women from the home

, with Token Edit Distance performing significantly less well (accuracy= 0.53), suggesting that semantic similarity plays a more important role than syntactic similarity (a result backed up by the comparative analysis of Aker et al. [2017], who also found syntactic features to be the least informative in all of the experimental settings considered

Although the assumption of a tree structure does not hold for all arguments, it is the case for around 95% of the argument

36 http://www.debatepedia.org.


The ability to successfully extract premises and conclusions is built upon in Feng and Hirst (2011), which presents the first step in the long-term goal of a method to reconstruct enthymemes, by first, classifying to an argumentation scheme (Walton, Reed, and Macagno 2008)

Green (2018b) then explores how argumentation schemes in this domain can be implemented as logic programs in Prolog and used to extract individual arguments. In this case, the schemes are formulated in terms of semantic predicates obtained from a text by use of BioNLP (biomedical/biological natural language processing) tools.

automated analysis. To pick an example from a substantially different theoretical approach, Musi, Ghosh, and Muresan (2016) present a novel set of guidelines for the annotation of argument schemes based on the Argumentum Model of Topics (Rigotti and Morasso 2010)


FIPA Agent Coordination Language (McBurney and Parsons 2009), the Dialogue Game Description Language (Bex, Lawrence, and Reed 2014), or the Lightweight Coordination Calculus (Robertson 2004)

In these cases, software such as Arvina (Lawrence, Bex, and Reed 2012) or D-BAS (Krauthoff et al. 2018)

Al Khatib et al. (2018) identify six distinct “discourse acts” (Socializing, Providing
evidence, Enhancing the understanding, Recommending an act, Asking a question, and Finalizing the discussion) in

Harris et al. (2018) argue for the importance of rhetorical figures for argument
mining in particular, and present an annotation scheme to make figure detection more tractable for computational approaches. It is claimed in this work that many figures are formal patterns that algorithms can detect through surface analysis, illustrating this with an example from John F. Kennedy’s 1961 United States presidential inaugural address: “Ask not what your country can do for you. Ask what you can do for your country.” This constitutes an instance of the figure antimetabole, the repetition of words in reverse order, and is relatively easy to identify with a straightforward lexical or rulebased approach

For example, a figure like polyptoton (repetition of stems with different affixes: “hate the sin but not the sinner”) is easier to algorithmically detect than a trope like metaphor (a cross-domain mapping: “Juliet is the sun”).

epizeuxis (the repetition of a word or small group of words, with no other words in between, such as “very, very” or “many, many”) are

eutrepismus (the numbering and ordering of parts under consideration)

SEMEVAL 2020 focusing on the detection of “propaganda techniques” in news articles.

Attempts are being made to overcome this lack of data, including the use of crowdsourced annotation (Ghosh et al. 2014; Skeppstedt, Peldszus, and Stede 2018) and automatic methods to extend the data currently annotated (Bilu, Hershcovich, and Slonim 2015).



### thesis (Habana) - automatic ontology generation - 90 pages
https://github.com/jromero132/bachelor_thesis_paper/blob/master/thesis.pdf

automatic ontology creation from a a colleciton of doucmnets
eHealth KD challenge

this would be for the data processing bit - the output pipeline, not the input pipeline

https://pypi.org/project/es-core-news-sm/


I can definitely build on this. there could be a separate game where annontaions (whether a word or pharse is an entity, concept, action, etc) are done - then on the bassis of these annotations
the ontology is created
need to make it into some microservice, or just a package tbh fr fr

microservice input - a chunk of documents
output - ontology JSON and SVG



## Kunz Rittel 70

Elements of the system are topics, issues, questions of fact, positions, arguments, and model problems.

It is not possible to separate “understanding the problem” as a phase from “information” or “solution” since every formulation of the problem is also a statement about a potential solution.


Issues have the form of questions. • The origins of issues are controversial statements. • Issues are specific to particular situations; positions are developed by utilizing particular information from the problem environment and from other cases claimed to be similar.
• Issues are raised, argued, settled, “dodged,” or substituted.

With regard to content, the following types of issues can be
distinguished: • factual issues: “Is X the case?” • deontic issues: “Shall X become the case?” • explanatory issues: “Is X the reason for Y?” • instrumental issues: “Is X the appropriate means to accomplish Y in this situation?”

The most astonishing result is the eager acceptance by the users, although the implementation induced major changes in organization and working style




## class notes Talmage 46
pint 1.2 - goal was to determine author's position
1.3 ii separating out argument from non-argument


1.4 types of non-arguments

1.7 no urles for correct
but repeated affirmation, in different words is frequent

1.12 rectification of names 

2 analyzing advocative discourse
2.1 
v inherent plausiblity

3 chapter 3 - apacy - features impeding rational judgement

3.10 - monic / hekistic - at least or exactly

3.12 type / token amiguity - the cat has whiskers
3.18 vector of 2 theses - up thesis
premiss

4 elaboration
4.4
a development and other types


5 counters and countering
but numbers 6
6.2 classification of counters

6.6 illustration of convetions


appendix - A fuirther notes of analyzing advocative discourse:
Principle of Charity -
// each argument is invaluable


B some further types of ambiguity 
add to that

## spoken dialogue system for argument exploration 
Arguing chatbots such as Debbie, which used a similarity algorithm to retrieve counterarguments (Rakshit et al., 2017)

persuasive essays by Stab and Gurevych (2014). They structure arguments in three components: major claim, claim and premise.

stance
stance overall level up
exit
whypro whycon
Stance on current argument Stance on overall topic
Switches to parent argument Terminates conversation
Information-seeking for a pro argument Information-seeking for a con argument
jump to argument Switches to referred argument prefer
Preference of presented argument; update weights
prefer old/ new/equally
indifferent reject number visited
Compare preference between current and former argument(s); update weights
Indifference towards presented argument; update weights
Current argument and children are abandoned; weights updated
Shows stats on number of seen and unseen arguments
available moves Shows all available moves
Determiners Always
Always
Always (except for root) Always
If supporting child node exists If attacking child node exists
If argument is skipped without preference Always (except for root)
If sibling(s) are preferred Always (except for root) Always (except for root) Always Only in speech-based system Table 1: Explanation for the available moves the user can choose from in each turn of the interaction.

The nodes are updated recursively until the root node is reached. The difference between the sum of the strengths of the supporting children and the sum of the strengths of the attacking children of the root node displays the final “stance” of the user (Aicher et al., 2021). If it is greater than 0, the user supports the major claim, if it is smaller than 0, the user rejects it, and if it equals 0, the user is indifferent.


It serves as knowledge base for the arguments and is taken from the Debatabase of the idebate.org2 website

Material reproduced from www.iedebate.org with
the permission of the International Debating Education Association. Copyright © 2005 International Debate Education Association. All Rights Reserved

“The system should suggest new arguments, it would be more diversified.”) was stressed much more in the speech system. This might explained by the more natural appearance of the speech system which rose higher expectations with regard to its flexibility in contrast to the quite static appearance of the menu system.






## user interest modeling in argumenttaive dialogue systems
First, collaborative filters (Pavlov and Pennock, 2002; Chien and George, 1999; Gazdar and Hidri, 2020) which use the useruser similarity principle stating that if a user highly rated an item, similar users would probably highly rate that item. Second, content-based filters (Pazzani and Billsus, 2007; Son and Kim, 2017) which recommend items based on the item-item similarity principle stating that if users highly rated an item, they would highly rate similar items.

However, explicit user feedback (Su et al., 2012) requires user responses that are not content-related and disturb the dialogue flow. Due to the described drawbacks of explicit methods and to achieve our aim of a natural interaction we chose to assess user interest implicitly

To the best of our knowledge, existing literature lacks any reference to interest modelling in (argumentative) dialogue systems

and their corresponding relations and encoded in an OWL ontology (Bechhofer, 2009) for further use.

Figure 2 left to the dialogue history, the current root of the argument branch, the argument branch itself and the user’s current position (green bordered node) are displayed. Already visited nodes are shown in green and unknown ones in blue

If the user has visited |Bic,v| of these descendants, the 4Where i denoted a unique identifier.

The study was conducted online via the crowdsourcing platform “Crowdee” (https:// www.crowdee.com/, 12-29th November 2021) with participants from the UK, US and Australia

Even though we are able to detect a slight tendency with an accuracy of 62,9% (see Table 2) for both modalities, the prediction is not significantly better than a random guess. This might again be due to the fact, that the users were not asked to state which polarity they would choose next


# more resources

## benchmarks
http://debategraph.org		
http://www.mturk.com		
https://fold.it/		
https://psdoom.sourceforge.net/		
https://www.crowdee.com		

## other resources
a ready model for lemmatization
https://spacy.io/models/en#en_core_web_md		
library
https://opennlp.apache.org/

resource
https://www.gutenberg.org/help/mirroring.html		

