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

## Survey on reinforcement learning for language processing - 37 pages
https://arxiv.org/abs/2104.05565 (probably)

## Argument mining survey - 54 pages
https://direct.mit.edu/coli/article/45/4/765/93362/Argument-Mining-A-Survey

## thesis (Habana) - automatic ontology generation - 90 pages
https://github.com/jromero132/bachelor_thesis_paper/blob/master/thesis.pdf

automatic ontology creation from a a colleciton of doucmnets
eHealth KD challenge

# new papers

## Kunz Rittel 70

## class notes Talmage 46


# second wave of papers



