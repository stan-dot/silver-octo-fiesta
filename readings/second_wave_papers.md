

# myu topic
type ntpoation = my statement{srouce, year}


need to have a suggestion system - to empower the user to make better arguments


a shilling promotion page
o
need a handy place to build ontologies too
maybe then properties can be arguments?


# list

## Phetch
https://en.wikipedia.org/wiki/Phetch#:~:text=Phetch%20is%20played%20by%20three,find%20the%20image%20being%20described.
75% of images don't have ALT text labels
von Ahn made it
3-5 people
1 seeker, others are seekers
data = describer's description of the image
discontinued in 2008

## Mann and Thompson 1987

nucleus and satellite, one nucleau in every sentence, nucleus with vertical notation

- might to a game identifying evidence sentences in the text!
- 

effectively it's a platform for different word-games


elements
- nuclear unit
- solutionhood relation
- concession relation
- elaboration
  - set - member
  - abstraction - isntance
  - whole - part
  - process - step
  - object - attribute


antithesis relation - but author is not dead

## Brin and Page 1998

advantages of a centralized system
many papers had already been in the area, fast iteration
pagerank algorithm
26 million web pages computed in a few hours back then

high level architecture (page 5/11)
most written in C

Huffman coding

Python crawlers, each 300 connections
DNS cache

conclusions - quality first, optimizing on one specific bottleneck

were hoping this would be a step for many researchers - ended becoming that step


## Soricut and Marcu 2003 sentence level discourse parsing

discourse parsing model

Marus 1993 syntactic trees

each document paired with a dicourse structure manually built using Mann and Thompsoe 1988

training section is a set of triples

s, tree, discourse tree

83% accuracy on discourse segmentation not enough

## Prakken 2005 - coherence and flexibility in dialogue games for argumentation

> Systems for argumentation dialogues were studied in medieval times [3].
I. Angelelli. The techniques of disputation in the history of logic. The Journal ofPhilosophy, 67, 800–815, 1970.

[8] 8] G. Brewka. Dynamic argument systems: a formal model ofargumentation processes based on situation calculus. Journal ofLogic and Computation, 11, 257–282, 2001

different structural variants of game systems - unique vs multi-reply protocols

unique vs multi-move protocols

immediate vs non-immediate reply protocols
R.P. Loui. Process and policy: resource-bounded non-demonstrative reasoning. Computational Intelligence, 14, 1–38, 1998.

> A logic for defeasible argumentation L is a tuple (Lt,R, Args,→), where Lt (the topic language)is a logical language, R is a set of inference rules over Lt, Args (the arguments) is a set of AND-trees of which the nodes are in Lt and the AND-links are inferences instantiating rules in R, and → a binary relation of defeat defined on Args. For any argument A, prem(A) is the set of leaves of A (its premisses) and conc(A) is the root ofA (its conclusion)


> DEFINITION 2.5 (Moves and dialogues) • The set M ofmoves is defined as N ×{P,O}× Lp
c × N, where the four elements of a move m
are denoted by, respectively: – id(m), the identifier of the move, – pl(m), the player of the move, – s(m), the speech act performed in the move, – t(m), the target of the move.

for every unanswered challenge, claim can be defended or not

> Therefore, we are interested in proving that the initial move of a dialogue is in just in case the defended part of its dialectical graph contains a justified argument for the dialogue topic. In fact, as will be discussed below, such a result can only be proven for dialogues in which the players play logically ‘perfectly'

need to assume perfect play for the purely exact reasoning to be valid.


unique--reply protocols can be unfair

> The structure ofweakly relevant dialogues differs in two main respects from that ofstrongly relevant dialogues. First, a player has some freedom to make additional moves after he has made himself the current winner, possibly creating additional winning parts. Second, each player must counterattack all attacks of the other player in order to make himself the current winner.

maybe social voting on who's winning?


maybe only one type of element at a time?

only put one challenge


liberal vs strict protocols
> Thus four categories of dialogue rules can be distinguished. Basic protocol rules should be respected in all discussions. Context-dependent protocol rules hold whenever this is appropriate in a certain context of application. Conventions formulate behaviour that participants should ideally have to promote coherence of the dialogue, for example, ‘do not challenge too much or retract too rapidly’. Finally, player strategies and heuristics are meant to promote the player’s individual goal, i.e. to win the dialogue: for example, ‘no irrational surrenders’, that is, surrenders when one is not losing. The assertion and concession attitudes of [25] ( for example ‘concede a proposition only if you cannot construct a counterargument’) can also be regarded as player heuristics.

> Gordon’s work on the Pleadings Game [13] is seminal AI and Law work on the modelling of
legal procedures as dialogue games. The Game was intended as a normative model of civil pleading in Anglo-American legal systems, where the participants aim to identify the issues to be decided in court

### pleadings game - Gordon
Pleadings Game http://www.tud.ttu.ee/im/Ermo.Taks/IDK0310/Reading/p10-gordon.pdf
> The distinction between attacking and surrendering replies is implicit in Gordon’s distinction between three kinds of moves that have been made during a dialogue: the open moves, which have not yet been replied to, the conceded moves,

> At each turn a player must respond in some allowed way to every open move of the other player that is still ‘relevant’ (in a sense similar but not identical to that of Section 6), and may reply to any other open move

### end

> It may be that an approach with an explicit reply structure is more suitable for ‘verbal struggles’ but less suitable for dialogues where investigation and inquiry are more important than ‘winning'.

the need for investigative approach


## Rienks, Heylen and Weijden 2005 - argument diagramming of meeting conversations
> relations and the forthcoming structure between the arguments. In this paper we introduce the Twente Argument Schema, a diagramming model, developed in order to structure textual units by providing an annotation enabling people as well as automatic systems to find answers to questions related to the decision making process

> Argument diagrams provide a representation leading to quicker cognitive comprehension, deeper understanding and enhances detection of weaknesses [Schum and Martin, 1982, Kanselaar et al., 2003].
• Argument diagrams aid the decision making process, as an interface for communication to maintain focus, prevent redundant information and to save time. [Yoshimi, 2004, Veerman, 2000].
• Argument diagrams keep record and function as organizational memory.[Buckingham Shum, 1997, Pallotta et al., 2005]
• The development of argument diagrams may teach critical thinking.[Reed and Rowe, 2001, Van Gelder, 2003]

#### good for the promotion page

> Several diagramming techniques have been developed, all with their own goals in mind and their own ways of creation. We discuss three of them : Wigmore’s charting method, Toulmin’s model and the model developed for the EUCLID project.

[on EUCLID model]
> This model is rather simple as the resulting claims can only be related to each other by either ‘support’ or ‘refute’ links [Smolensky et al., 1988]

> These components can be used to model argument trees. In the resulting argument trees, a ‘child’ is always evidence for or against a parent. Similar trees can be constructed with software package such as Athena2 and Belvedere [Suthers et al., 1995].

> The Belvedere environment allows the nodes to be labelled with labels as Principle, Theory, Hypothesis, Claim, Data where as in Reasonable, the nodes can be only of type Claim.

> A somewhat different tool is Compendium [Selvin et al., 2001], which was designed as a tool to support the real time mapping of discussions in meetings, collaborative modelling, and the longer term management of this information as organizational memory.


> Another observation is that in all of the tools, except compendium, the main conclusion or thesis that was debated is represented as the uppermost node.

uppermost node - tthat's why this convention chosen

Boolean questions, Enum questions, open questions
open questions need to have hypotheses and questioning assumptions
> In our Schema we have defined three different labels for our nodes to represent the issues: The ‘Open issue’, the ‘A/B issue’ and the ‘Yes-No issue’. The open issue allows for any number of possible replies possibly revealing positions or options that were not considered beforehand. This in contrast with the A/B issue, that allows participants to take a position for a countable number of positions which should be known from the context (c.f. ‘Would you say ants, cats or cows?’). The yes-no issue, in line with the yes-no question directly requests whether the participants positions agree or disagree with the issue. The reader should note that we leave out the why question. This is done because a why question can be modelled as an open question with a clarification relation, explained in the next section


# 5 done
## Siddarthan and Tidhar 2006 - automatic classicification of citation function
> A plethora of manual annotation schemes for citation motivation have been invented over the years (Garfield, 1979; Hodges, 1972; Chubin and Moitra, 1975). Other schemes concentrate on citation function (Spiegel-R¨using, 1977; O’Connor, 1982; Weinstock, 1971; Swales, 1990; Small, 1982)

obviously, funcional> motivations

> (Moravcsik and Murugesan, 1975) divides citations in running text into four dimensions: conceptual or operational use (i.e., use of theory vs. use of technical method); evolutionary or juxtapositional (i.e., own work is based on the cited work vs. ownwork is an alternative to it); organic or perfunctory (i.e., work is crucially needed for understanding of citing article or just a general acknowledgement); and finally confirmative vs. negational (i.e., is the correctness of the findings disputed?).
4 types of recall

or Kulbach−Leibler (KL) distance, bet−
https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence


annotation schmee about citations - many types

> Guidelines (25 pages, ∼ 150 rules) describe the
categories with examples, provide a decision tree and give decision aids in systematically ambiguous cases

long guidelines- must mention - neither scalable nor efficient

> Another difficult distinction concerns the judgement of whether the authors continue somebody’s research (i.e., consider their research as intellectual ancestry, i.e. PBas), or whether they simply use the work (PUse).

feature space not clearly cut clean

On average, our papers contain 26.8 citation instances in running text3.

> We observe that more PMot categories appear towards the beginning of the paper, as do Weak citations, whereas comparative results (CoCoR0, CoCoR-) appear towards the end of articles. More fine-grained location features, such as the location within the paragraph and the section, have also been implemented.


## Cialdini 2001 - the science of persuasion
> Six basic tendencies of human behavior come into play in generating a positive response: reciprocation, consistency, social validation, liking, authority and scarcity.
>
>A 1998 study in the New England Journal of Medicine found that only 37 percent of researchers who published conclusions critical of the safety of calcium channel blockers had received prior drug company support. Among researchers whose conclusions supported the drugs’ safety, however, the number of those who had received free trips, research funding or employment skyrocketed—to 100 percent.

> “Will you please call if you have to change your plans?”
> An example is the understandable but potentially misguided tendency of health educators to call attention to a problem by depicting it as regrettably frequent

need to say people are doing the DESIRABLE thing

> a Tupperware party begins somewhere in the world every 2.7 seconds. In fact, 75 percent of all Tupperware parties today occur outside the individualistic U.S., in countries where group social bonding is even more important than it is here
> Physical attractiveness can be such a tool. In a 1993 study conducted by Peter H. Reingen of Arizona State University and Jerome B. Kernan of the University of Cincinnati, good-looking fund-raisers for the American Heart Association generated nearly twice as many donations (42 versus 23 percent) as did other requesters. In the 1970s researchers Michael G. Efran and E.W.J. Patterson of the University of Toronto found that voters in Canadian federal elections gave physically attractive candidates several times as many votes as unattractive ones. Yet such voters insisted that their choices would never be influenced by something as superficial as appearance.

> Research at the University of North Carolina at Chapel Hill found that compliments produced just as much liking for the flatterer when they were untrue as when they were genuine
> scarcity double whammy: not only was the beef scarce, but the information that the beef was scarce was itself scarce


about the author
> He attributes his long-standing interest in the intricacies of influence to the fact that he was raised in an entirely Italian family, in a predominantly Polish neighborhood, in a historically German city (Milwaukee), in an otherwise rural state


## Teufel, Siddharthan and Batchelor  2009 - towards discipline - independent argumentative zoning - evidence from chemistry and computationl linguistics

> knowledge claim (Myers, 1992; Luukkonen, 1992): the act of writing a paper corresponds to an attempt of claiming ownership for a new piece of knowledge, which is to be integrated into the repository of scientific knowledge in the authors’ field by the process of peer review and publication.
> Category AIM
Description Statement of research goal.
BACKGROUND Description of generally accepted background knowledge.
BASIS CONTRAST
OTHER OWN
TEXTUAL
Existing KC provides basis for new KC.
An existing KC is contrasted, compared, or presented as weak.
Description of existing KC.
Description of any other aspect of new KC.
Indication of paper’s textual structure.

> decidable, in principle, without specific domain knowledge about what is discussed in detail in the paper

> Our annotation guidelines are 111 sides ofA4 and contain a decision tree, detailed description of the semantics of the 15 categories, 75 rules for pairwise distinction of the categories and copious examples from both chemistry and computational linguistics.

#### lots of rules

> Category AIM remained the same. • Category BACKGROUND was renamed CO GRO, or common ground.
• Category OTHER was split into other people’s work (OTHR) and the authors’ own previous work (PREV OWN).
• Category BASIS was split into usage (USE) and support (SUPPORT).
• Category CONTRAST was split into neutral comparison (CODI), contradiction (ANTISUPP), and a category combining research gaps with criticism (GAP WEAK).
• Category OWN was split into description of method (OWN MTHD), results (OWN RES) and conclusions (OWN CONC), and a category which specifies recoverable errors made by the authors (OWN FAIL).

> AIM
NOV ADV CO GRO OTHR Description Category
Statement of specific research goal, or hypothesis of current paper
Novelty or advantage of own approach
No knowledge claim is raised (or knowledge claim not significant for the paper)
Knowledge claim (significant for paper) held by somebody else. Neutral description
PREV OWN Knowledge claim (significant) held by authors in a previous paper. Neutral description.
OWN MTHD New Knowledge claim, own work: methods
OWN FAIL A solution/method/experiment in the paper that did not work
OWN RES Measurable/objective outcome of own work

good for many-people collab

> Other AZ-like schemes for scientific discourse
created for the biomedical domain (Mizuta and Collier, 2004) and for computer science (Feltrim et al., 2005) also made the decision to subdivide OWN, in similar ways to how we propose here. The current work, however, is the first experimental proof that humans can make this distinction – and the others encoded in AZ-II – reliably, and in two quite distinct disciplines.

> The discipline-specific generics in chemistry
come in the form of a “chemistry primer”, a 10page collection of high-level scientific domain knowledge. It contains: a glossary ofwords a nonchemist would not have heard about or would not necessarily recognise as chemical terminology; a list of possible types of experiments performed in chemistry; a list of commonly used machinery; a list of non-obvious negative characterisations of experiments and compounds (“sluggish”, “inert”); and a list of possible types of knowledge claims.

very valuable list

> As agreement measure we choose the Kappa
coefficient κ (Fleiss, 1971; Siegel and Castellan, 1988), the agreement measure predominantly used in natural language processing research (Carletta, 1996). κ corrects raw agreement P(A) for agreement by chance P(E)

Kappa coefficient for agreement

> To solve this in a fundamentally sound way, there seems to be no other way than to annotate more texts, at the cost of more human effort.
> This might point to the fact that Annotators A and B might have used a certain amount of domain-knowledge which the chemistry primer in the guidelines does not yet, but should, cover
> There is also the faint possibility that discourse
annotation of chemistry is intrinsically easier than discourse annotation of CL, because it is a more established discipline and not despite of it. For instance, it is likely that the problem-solving categories OWN FAIL, OWN MTHD, OWN RES and OWN CONC are easier to describe in a discipline with an established methodology (such as chemistry), than they are in a younger, developing discipline such as computational linguistics


## Bechhofer 2009

https://www.w3.org/TR/skos-reference/

reading this should be secondary - thta's not the primary funcion of the system


## Anand et al 2011 How can you say such things?!?: Recognizing Disagreement in Informal Political Argument

> In this paper, we focus on an important initial task
for the recognition of argumentative structure: automatic identification of agreement and disagreement. We introduce the ARGUE corpus, an annotated collection of 109,553 forum posts (11,216 discussion threads) from the debate website 4forums.com. On 4forums, a person starts a discussion by posting a topic or a question in a particular category, such as society, politics, or religion

> This work has treated each post as a text to be classified in terms of stance, for a particular topic, and shown that discourse relations such as concessions and the identification of argumentation triggers improves performance .
> . It is a typical internet forum built on the vBulletin software. People initiate discussions (threads) and respond to
vbulletin

> Turkers to use their native intuitions about what it means for a post to be sarcastic, since previous work suggests that non-specialists tend to collapse all forms of verbal irony under the term sarcastic (Bryant and Fox Tree, 2002). We did not ask Turkers to distinguish between sarcasm and other forms of verbal irony such as hyperbole, understatement, rhetorical questions and jocularity (Gibbs, 2000).

https://en.wikipedia.org/wiki/VBulletin 

proprietary

> Agree/Disagree: Does the respondent agree or disagree with the prior post?
S 0.32 Fact/Emotion: Is the respondent attempting to make a fact based argument or appealing to feelings and emotions?
S 0.42
Attack/Insult: Is the respondent being supportive/respectful or are they attacking/insulting in their writing?
B 0.22 Sarcasm: Is the respondent using sarcasm? S 0.46
Nice/Nasty: Is the respondent attempting to be nice or is their attitude fairly nasty?

#### these as different dimensions

> Based on manual inspection of a subset of the corpus, we constructed a list of 20 discourse markers; 17 of these occurred at least 50 times in a quote response (upper bound of 700 samples): actually, and, because, but, I believe, I know, I see, I think, just, no, oh, really, so, well, yes, you know, you mean.

discourse markers

> For our experiments we used the Weka machine learning toolkit
> People on these forums get to know one another and often enjoy repeatedly arguing with the same person. In addition, we hypothesized that the “heat” of a particular conversation could be correlated with rapid-fire exchanges, as indicated by short time periods between posts.


# 10 done

## Awadallah, Ramanath, and Weikum 2012 Harmony and dissonance: organizing the people's voices on political controversies

> News, Al-Jazeera, BBC, CNN, New York Times, and Wikipedia, and extracts 4-tuples of the following form: hpersoni hsupport/opposei htopici{hcontexti}
where the triple: hpersoni hsupport/opposei htopici is extracted from the textual context.

> Finally, we show use-case scenarios for identifying flip-flop politicians who change their opinions on the same topic, and for discovering people with divergent opinions on otherwise highly correlated topics
> DEFINITION 2.1. A facet fi is denoted by a string str(fi). Examples of facets on the controversial topic “Iran’s Nuclear Program, 2010” include “military strikes on Iran” and “sanctions on Iran”. We use the term facet name to refer to str(fi).

facet system

> . Disambiguation: As many names are ambiguous, YAGO actually connects the surface names to all possible meanings. For example, for “Obama”it provides both Barack_Obama as well as Michelle_Obama as entity candidates. Fortunately, YAGO comes with a simple but powerful heuristics for the preferred meaning of a name: the entity which most frequently occurs in Wikipedia as a link target for an href anchor text with the given name

could use this automatic processing for input

> For matching names in text sources against canonical entities, we leverage existing knowledge bases like DBpedia, Freebase, or Yago. We specifically make use of the means relation that Yago [18]

other knowledge bases


## Walker, Anand et al 2012 - corpus for research on deliberation and debate

this one was kind of redundant

## Su et al 2012 online reward

not relevant, as for bots - and heavy in maths and ML

## Peldszus and Stede 2013a - from argument disgrams to argumentatio mninig in texts: a survey

> A very useful earlier overview of the use of argument diagramming techniques to represent the structure of arguments has been given by Reed et al. (2007). They review the theories and diagramming schemes in logic, law and artificial intelligence and cover many important aspects relevant to (automatic) evaluation of arguments. In contrast, our aim is of a rather descriptive nature and our second focus is on the linguistic realization of argumentation, especially on the representation of argumentative opposition

> Stephen E. Toulmin’s influential analysis of argument (Toulmin, 1958).
> Similarly, Klein (1980) argued for a recursively applicable argumentation scheme. Furthermore, he claimed that the distinction between Toulmin’s data and warrant cannot always be drawn precisely
> Wunderlich (1980) thus interpreted Klein’s support-tree as a ’decision’-tree, where the root node is the ’quaestio’, i.e. the question to be decided on. From there, not only arguments for and but also against the decision unfold recursively. Since there can be pro and contra for every node in the tree, the opponents role is integral to this representation.

> Recently, an updated but compatible version of the theory has been presented in (Freeman, 2011

> Freeman’s diagramming technique is not perfect, though, especially for certain complex combinations of features: For some reason, Freeman lists all rebuttals of one argument in a single rebuttal-box. In order to relate the counter-rebuttals to their target, co-indexation is introduced instead of representing the relation by links in the diagram
>
uselss structure

> While Freeman (1991, p. 173) argued that such counterconsiderations need not to be represented in argument structure, because they could be seen as rhetorical accessory, logically not effecting the case for the claim, they are now represented as a special ’even though’ rebuttal in (Freeman, 2011, p. 29). This extension
>
why disregard this???

basic argument (b) linked support, multiple support, serial support, example support

> Figure 4: Challenger’s attacks of the proponent’s argument
rebut a conclusion, rebut a premise, undercut an argument, support a rebutter

> However, the challenger is not allowed to assert a proposition in the basic dialectical situation. His role is defined very restrictively as that of a constructive partner testing the proponent’s argumentation by asking critical questions. His goal is to wrench the best possible argument for the main claim from the proponent
>
only defense mode

rebut a rebutter, rebut an undercuter, undercut a rebutter, undercut an undercutter

> last possibility to react to an attack is to leave it uncountered. At first glance this seems counterproductive to the author’s goal to convince the reader of his main claim. However, this appears frequently in commentary text

can leave an attack unreflected

> The first study that we consider here is that of Apoth´eloz et al. (1993),

objection strategies
> The theory is integrated as a diagramming technique in argument visualization tools such as Carneades (Gordon, 2010)

> The approach that obviously is a candidate for representing argument structure is Rhetorical Structure Theory (RST; Mann and Thompson (1988)), which has been conceived as an empirical tool for practical text analysis, and the developers originally justified their design decisions with the claim that a fairly large number of texts from different genres have been successfully analyzed.

> Finding arguments in text automatically is a relatively new research area. It is potentially relevant to any kind of text mining application that is directed at argumentative text; in particular, promising applications have been suggested for the following types:

> Political deliberation: An extension of product-oriented mining for reasons is to be found in discussions of political issues, to be found in letters to the editor, or, again, in social media. The problem is more difficult because the issues tend to be more complex – it does no longer to suffice to look for sentences including the target term and the evaluation (“I don’t like that new cheeseburger) and then for the reason in the immediate context (“...because it’s much too spicy.”). Instead, it can take several sentences to mention the target issue, or some aspect of it, and to formulate an attitude toward it

probvlems in argumentation mining
> Segmentation: Break the text down into minimal units of analysis, henceforth called ‘argumentative discourse units’ (ADUs)
1. segmentation
2. segment classificiation
3. relation identification
4. argument completion - postulation of cinlucit ADUs

> While there are no specific results for argumentative text, we can expect that the argumentative support (‘causal’) relations will often go unsignalled, whereas the rebuttal/counter-rebuttal configurations usually require a lexical signal so that the reader can identify the contrastive argumentative move
 
harder to see supportive arguments

This is the task we defined at the beginning of Subsection 4.1, which in its complete form would map a text (portion) to a graph representation such as the one we proposed in Section 2.2.

http://araucaria.computing.dundee.ac.uk/
broken link

> AML, the markup language used in Araucaria, and the argument interchange format AIF (Rahwan and Reed, 2009) provide a good basis for representing arguments but were not intended specifically for purposes of text annotation

AML language

> The difficulty of finding the thesis differs widely between genres, which is one reason for the goal of ensuring genre-diversity in the corpus

why only 1 thesis?!

## Green 2014 - towards creation fo a corpus for argumentation mining the biomedical genetics research literature

done, not much - give a quick browse
> : data, i.e., observations or conclusions of other arguments, and warrant, i.e., a fielddependent accepted principle (such as a legal rule or a “law” of science)
>
data vs warrant

> The Araucaria argumentation diagramming
tool was developed to aid human analysts and students to visualize and annotate naturally occurring arguments (Reed and Rowe, 2004).

> Mochales and Moens (2011) experimented
with the Araucaria corpus and a legal corpus. They developed a multi-stage approach to argumentation mining. The

> An extension of AZ (AZ-II) developed for application to chemistry articles, refined AZ‟s distinctions into fifteen categories (Teufel, 2010)

> The CoreSC (Core Scientific Concepts) annotation scheme was developed for automatic classification of sentences in terms of the components of a scientific investigation: Hypothesis, Motivation, Goal, Object, Background, Method, Experiment, Model, Observation, Result and Conclusion (Liakata et al., 2012a). An

# 15 done


## Ong, Litman, and Brusilovsky 2014 - ontyology based argument mining
> concretely visualize their argumentation structure. Our work is part of the ArgumentPeer project (Falakmassir et al., 2013), which combines computer-supported argument diagramming
>
what school is following

> Potentially, answering these questions in the affirmative would allow us to assist students with their writing by allowing computer tutors to label sentences with the ontology, determine which elements are missing, and suggest adding these missing elements to improve essay qualit

http://lasad.dfki.de

> Our rules were developed using our intuition and informal examination of 9 essays from the corpus of 52. The algorithm consists of the following ordered4 rules

> manual rules, might be informative

this tagging could be replicated in the app
using the 8 rules


## Stab and Gurevych 2014 - identifying argumentative discourse structures in persuasive essays
> Argumentation is a crucial aspect of writing skills acquisition. The ability of formulating persuasive arguments is not only the foundation for convincing an audience of novel ideas but also plays a major role in general decision making and analyzing different stances. However, current writing support is limited to feedback about spelling, grammar, or stylistic properties and there is currently no system that provides feedback about written argumentation. By integrating argumentation mining in writing environments, students will be able to inspect their texts for plausibility and to improve the quality of their argumentation.
> Grammarly for arguments

> that should not be accepted by the reader without additional support.1 The premise underpins the validity of the claim. It is a reason given by an author for persuading readers of the claim. Argumentative relations model the discourse structure of arguments

tutorial expressions
Penn Discourse Treebank (PDTB) (Prasad et al., 2008

> Previous research on argumentation mining spans several subtasks, including (1) the separation of argumentative from non-argumentative text units (Moens et al., 2007; Florou et al., 2013),

pre-processing step

> In our experiments, we use several classifiers (see section 4.2) from the Weka data mining software (Hall et al., 2009). For preprocessing the corpus, we use the Stanford POS-Tagger (Toutanova et al., 2003) and Parser (Klein and Manning, 2003) included in

> In addition, we adopt the first word features proposed by Pitler et al. (2009). We extract the first word either from the argument component or from non-annotated tokens preceding the argument component in the covering sentence if present. So, the first word of an argument component is either the first word of the sentence containing the argument component, the first word following a preceding argument component in the same sentence or the first word of the actual argument component if it commences the sentence or directly follows another argument component

> lexical features perform best.

> However, our experiments revealed that the current accuracy for identifying argument components is not sufficient for increasing the performance of argumentative

then accuracy not enough

## Boltuˇzi´c and ˇSnajder 2015 - identifying prominent arguments in online debates using sematic textual similarity

> also moved to mining from user-generated content, such as online debates (Cabrio and Villata, 2012)

> The above approaches are supervised and rely on
datasets manually annotated with arguments from a predefined set of arguments

supervised learning

> We conduct our study on the dataset of users’ posts compiled by Hasan and Ng (2014)

> a distributed representation based on the recently proposed neural network skip-gram model of Mikolov et al. (2013a)

neural network model

## Habernal and Gurevych 2015 - exploiting debate portals for semi-supervised

> We propose novel features that exploit clustering of unlabeled data from debate portals based on a word embeddings representation. Using these features, we significantly outperform several baselines in the cross-validation, cross-domain, and cross-register evaluation scenarios

> Current approaches to automatic analysis of argumentation usually follow the fully supervised machinelearning paradigm (Biran and Rambow, 2011; Stab and Gurevych, 2014b; Park and Cardie, 2014) and rely on manually annotated datasets. Only few publicly available argumentation corpora exist, as annotations are costly, error-prone, and require skilled human annotators (Stab and Gurevych, 2014a; Habernal et al., 2014).

problems with annotation

> Analysis of argumentation has been an active topic in numerous research areas, such as philosophy (van Eemeren et al., 2014), communication studies (Mercier and Sperber, 2011), and informal logic (Blair, 2004), among others
#### Blair, informal logic

> There are five different components in this model, namely, the claim (the statement about to be established in the argument which conveys author’s stance towards the topic), the premise(s) (propositions that are intended to give reasons of some kind for the claim), the backing (additional information used to back-up the argument), the rebuttal (attacks the claim), and the refutation (which attacks the rebuttal). Relations between the argument components are encoded implicitly in the function of the particular component type, for instance, premises are always attached to the claim.

limited nesting

> In only 1% of the sentences there are two or more argument components in it; we arbitrarily choose the largest one

> The data were then indexed using the Lucene framework and the top 100 debates for each of the 6 domains were retrieved which resulted into 5,759 posts (≈ 35k sentences) in the unlabeled data in total. Our approach is formalized in the following paragraph.

> Although argumentation mining in usergenerated Web discourse has a long way to go (our methods currently achieve only about 50% of human performance
only 50% !!!!

> This work has been supported by the Volkswagen Foundation


## Kirschner, Eckle-Kohler, and Gurevych - linking the thorughts - in scientifici publications

need to give annotation power to the masses!
> We developed an annotation tool that supports the annotation of such graphs

details relation, a different one from the support and attack ones

> For instance, Liakata et al. (2012) proposed CoreSC (“Core Scientific Concepts“), an annotation scheme consisting of 11 categories1. Mizuta and Collier (2004) provide a scheme consisting of 7 categories (plus 5 subcategories) for the biology domain. In addition Yepes et al. (2013) provide a scheme to categorize sentences in abstracts of articles from biomedicine with 5 categories.
> the studies, the annotators are at least semi-experts in the particular domain and get detailed annotation guidelines
> detailed guidelines, ngmi

> All in all, the annotation study extended over several months part time work. The annotation of one single document took about two hours
lots of time, like medieval monks

> There are four types of relations: the directed relations support, attack, detail, and the undirected sequence relation
4 types of relation

# 20 done

## Al-Khatib Kiesel et al 2015 - shared task on argumentation mining in newspaper editorials

> The automatic analysis of this discourse structure has several applications, such as supporting writing skills or assisting informationseeking users in constructing a solid personal standpoint on controversial topics.

> An (argumentative) relation in our model is a directed link from one base unit to the target unit it supports or attacks most directly
> Our proposed model for the shared task does not explicitly categorize argumentative units into premises and claims since such a distinction gets problematic when claims are premises for further claims

finally, no explicit difference from claims!
> Unlike Peldszus and Stede (2013), we do not directly distinguish between units from proponent or opponent views since this distinction is difficult for discussions evolving around several topics. In our model, such a distinction is present on a local level: when one unit attacks another.

also no division here

> https://www.odesk.com/

> We plan to use the same system as the CoNLL task, TIRA (Gollub et al., 2012),5


## Carstens and Toni 2015 - towards relation based Argumentation Mining
> We consider any sentence which supports or attacks another sentence to be argumentative

> including the automatic construction of Argument Frameworks (AFs) (Cabrio and Villata, 2012; Feng and Hirst, 2011)

> Park and Cardie, 2014) use multi-class Support Vector Machines (SVM) (Crammer and Singer, 2002) to identify different classes of argumentative propositions in online user comments. (Ghosh et al., 2014) use SVM to analyse multilogue, instead, classifying relations between user comments
>
> If this relation is classified as an attack or support relation we consider both sentences to be argumentative, irrespective of their individual quality

>2www.BBCNewsLabs.co.uk

## Wyner, Peters, and Price 2015 - arugment discovery and extraction with the Argument Workbench

> ArgumentWorkbench, which is a interactive, integrated, modular tool set to extract, reconstruct, and visualise arguments.
> The Argument Workbench is a processing cascade, developed in collaboration with DebateGraph.
> analysis, and then building an argument graph. We harvest and preprocess comments; highlight argument indicators, speech act and epistemic terminology; model topics; and identify domain terminology.
> we use the GATE framework (Cunningham et al.(2002)) for the production of semantic metadata in the form of annotations
> it is an open source desktop application written in Java that provides a user interface for professional linguists and text engineers to bring together a wide variety of natural language processing tools and apply them to a set of documents

#### copy the argument workbench workflow

> The ANNIC interface thus uses the annotations to reduce the search space for human engineers, and focuses their attention on passages that are relevant for sourcing arguments

## Al-Khatib et al 2016 - crossdomain mining fo arguemntatinve text through Distant Supervision
> We freely provide the underlying corpus for research
> text segments relevant to the topic. Among others, a classifier is needed for this task that can distinguish argumentative from non-argumentative segments. Since we cannot presuppose a specific domain or register within a general retrieval scenario, the classifier needs to robustly deal with documents from diverse domains and registers. In this regard the following two key issues arise
another input flow, also suggestion
> Second, all major existing approaches follow a supervised learning scheme based on manual annotation of argumentative text segments

> Studies reveal that annotators need multiple training sessions to identify and classify argumentative segments with moderate inter-annotator agreement, and crowdsourcing-based annotation does not help notably (Habernal et al., 2014)

very important about outsourcing
#### Habernal et al must do

> In addition, we observe that n-grams seem to be most do main-dependent, while syntax features turn out to be more robust.
> then this should be available out there!
http://www.uni-weimar.de/medien/webis/corpora
no, it's not available there
> Starting point is a complex and often expensive manual annotation of argumentative text segments in a collection of documents, including the segments’ roles (e.g., premise or conclusion) and their relations (e.g., support or attack).
this is trivial tbh

#### another architecture diagram
> The idea of relying on idebate.org for argument annotation acquisition is in line with related research of Cabrio and Villata (2012c) and Gottipati et al. (2013).
"in line with.....  research" - good phrase

> three tailored cleansing rules from them: (1) We remove all literature references from the argumentative instances. (2) We delete all special brackets and symbols from the argumentative instances. (3) We delete some keywords from the non-argumentative instances that are used by the community to organize a discussion (e.g., “this house” or “this debate”).
removals

> In this regard, we propose a “PageRank for arguments” based on the link network of support and attack relations between arguments.
PageRank for arguments - needs to be added fr fr
also here the API, right?

## Razuvayevskaya and Teufel 2017 - finding enthymemes in real-world text - a feasibility study
> According to the Aristotelian definition [6], enthymemes are standard-form syllogisms with one missing proposition. But in the modern usage of this term in argumentation theory, enthymemes are often defined as any
> ad task - enthymeme detection

> mining: argument extraction, segmentation, i.e. identification of minimal argumentative discourse units (ADUs), segment classification, i.e. labeling of ADUs based on their argumentative roles, identification ofrelations between these segments, and argument completion, i.e. automatic construction of statements from implicit propositions
all 5 steps
> The automatic reconstruction of enthymemes would be highly desirable for various applications, such as knowledge mining, i.e. the automated acquisition of common knowledge information that can potentially be stored in knowledge bases, argument validity verification, and automatic simplification of written texts for children or adult readers of lower reading age. It would also further our insights into the process of text understanding and argument interpretation, in particular into the question which inference steps are necessary when reading and understanding atext.

uses

> Agreement on whether the given argument is enthymematic, i.e., whether there exists a missing inference;
• Agreement on which subtype of inference is concerned; • Agreement on the missing premise explicitly stated in natural language

> It can be attacked by both the undercut, Penguins are also birds, but they do not fly, and the rebuttal, But tweety is too heavy to fly.
undercut vs rebuttal

> For instance, Campbell [4] argues that the majority of Darwin’s claims cannot be expressed through logical arguments

need to inspect this
.A. Campbell, Scientific discovery and rhetorical invention: The path to Darwin’s origin, The Rhetorical Turn: Invention and Persuasion in the Conduct ofInquiry (1990), 58–90.

> Implicit argumentative propositions are not always defeasible. Some of them represent universally true facts that are too trivial to be stated explicitly [18]. This observation is captured by Grice’s Maxim of Quantity – Do not make your contribution more informative than is required [16]. This pragmatic principle discourages a speaker from making explicit statement of facts that are widely accepted by the audience; in fact, the explicit statement of such facts would sound both trivial and also unnatural to a listener. This is another reason why enthymemes are so frequent in natural language discourses
worth mentioning

> We categorised the scaling relations based on a development corpus of about 250 cases of let alone sentences, resulting in the scheme in Table 1.

greater schemes

holonym vs meronym
> Independence implies that a pair of raters agree about as often as two people who effectively flip coins to make their ratings. Kappa’s possible values are constrained to the interval [−1; 1]. K< 0 means that the observed agreement is less than the one expected by chance, K = 0 means that agreement is not different from chance, and K = 1 means perfect agreement

Kappa for agreement for ENUM values

> While one of the annotators classified this relation as a strike is smaller than a revolution, the second participant preferred the easier than category (a strike is easier than a revolution).

could lower the number of these for the ENUM task
Part of Smaller than Precondition for
8 9
61
Other lexical entailment with 11 5
Earlier date
Additional constraint on Additional referent
Cumulative/independent Less likely than
More extreme case than Easier than

size of the enthymeme - should always be the smaller one - from that smaller also create the larger one, but 2 different truth-able statements

only 1 fallback category in the future

> We therefore intend to outsource the decision of whether two paraphrases are identical or near-identical to unrelated humans, e.g., on Mechanical Turk [26], thus eliminating any possible bias.

outsourcing, Mechanical Turk used once more

# 25 done

## Wachsmuth, Stein, and Ajjour 2017 - buildign an argument search engine for the WEB
> Based on the framework, we build a prototype search engine, called args, that relies on an initial, freely accessible index of nearly 300k arguments crawled from reliable web resources. The framework and the argument search
>
> Initially, we crawled and indexed a total of 291,440 arguments from five diverse online debate portals, exploiting the portals’ structure to avoid mining errors and manual annotation while unifying the arguments based on the model (Section 4).

> An argument search index. We provide an index of 291,440 arguments, to our knowledge the largest argument resource available so far
> Unlike IBM, we build an open research environment, not a commercial application
> Argumentation theory proposes a number of major models: Toulmin (1958) focuses on fine-grained roles of an argument’s units, Walton et al. (2008) capture the inference scheme that an argument uses, and Freeman (2011) investigates how units support or attack other units or arguments
>
#### different models, I pick Freeman 2011

> No approach, however, seems robust enough, yet, to obtain arguments reliably from the web. Therefore, we decided not to mine at all for our initial index. Instead, we follow the distant supervision idea to obtain arguments automatically

> but recent research hints at future extensions: In (Wachsmuth et al., 2017b), we adapt the PageRank method (Page et al., 1999) to derive an objective relevance score for arguments from their relations, ranking arguments on this basis

#### database schemas
> Concept Description
Argument ID
Unique argument ID.
Conclusion Text span defining the conclusion. Premises
k ≥ 0 text spans defining the premises. Stances k ≥ 0 labels, defining each premise’s stance.
Argument context Discussion Text of the web page the argument occurs in. URL
Source URL of the text.
C’Position Start + end index of the conclusion in the text. P’Positions k ≥ 0 start + end indices, once per premise. Previous ID ID of preceding argument in the text if any. Next ID ID of subsequent argument in the text if any.
Model extensions (exemplary) P’Roles
k ≥ 0 labels, defining each premise’s role.
Scheme Label defining the argument’s scheme. Scores
m ≥ 0 values from [0, 1], defining scores

> In particular, we crawled all debates found on
five of the largest portals: (1) idebate.org, (2) debatepedia.org, (3) debatewise.org, (4) debate.org, and (5) forandagainst.com. Except for the second, which was superseded by idebate.org some years ago, these portals have a living community

all of those should be living

> For instance, issues on debate.org are partly specified as claims (“Abortion should be legal”), partly as questions (“Should Socialism be preferred to Capitalism?”), and partly as controversial issues (“Womens’ rights”).
noisy nature - need specific statements, that's the clearest

> 8args is available at http://www.arguana.com/
args. Notice that the prototype is under ongoing development and periodically updated

> Issue list: https://en.wikipedia.org/wiki/Wikipedia:List_of_controversial_issues
> search result personalization — all problems with intricate ethical issues attached
personalization and user modeling ethical

> Training a one-fits-all ranking function on the argumentative portion of the web and on joint user behaviors will inevitably incorporate bias from both the web texts and the dominating user group, affecting the search results seen by the entire user base. On the other hand, tailoring results to individual users would induce a form of confirmation bias

tailoring is difficult

> In other words, should a search engine “argue” like the devil’s advocate or not? This decision is of utmost importance;
should be able to choose mode


## Rakshit et al 2017 - Debbie, the debate bot of the future
> Our initial prototype of Debbie works with three topics: death penalty, gun control, gay marriage
> Using agglomerative clustering from scikit-learn, we created 15 clusters.

that is a bad chatbot
> Given that our database only has high quality arguments, the appropriateness of Debbie’s responses are primarily dependent on the performance of the similarity algorithm
lol, not true

> Lukin et al.(2017) talk about the role of personality in persuasion
#### Lukin et al

## I. Mordatch and P. Abbeel 2018 - emergence of grounded compositional lanaguege in Multi-Agent populations
> We adopt a view of (Gauthier and Mordatch 2016) that an agent possesses an understanding of language when it can use language (along with other tools such as non-verbal communication or physical acts) to accomplish goals in its environment.
> definition

> There are no pre-designed meanings associated with the uttered symbols - the agents form concepts relevant to the task and environment and assign arbitrary symbols to communicate them

> It is important to us to build an environment with a diverse set of capabilities which language use develops alongside with.

important to poast

> This is consistent with analysis in evolutionary linguistics (Nowak, Plotkin, and Jansen 2000) that finds composition to emerge only when number of concepts to be expressed becomes greater than a factor of agent’s symbol vocabulary capacity.

> In addition to performing physical actions, agents utter verbal communication symbols c at every timestep. These utterances are discrete elements of an abstract symbol vocabulary C of size K. We do not assign any significance or meaning to these symbols. They are treated as abstract categorical variables that are emitted by each agent and observed by all other agents

> These models would require agents learning to perform visual processing and source separation, which are orthogonal to this work
> At the end of the episode, we add a reward for predicting other agent’s goals, which in turn encourages communication utterances that convey the agent’s goals clearly to other agents

> Alternatively, (Nowak, Plotkin, and Jansen 2000) observed that emergence of compositionality requires the number of concepts describable by a language to be above a factor of vocabulary size
need complex environment generation then

> Instead, we propose to use a large vocabulary size limit but use a soft penalty function to prevent the formation of unnecessarily large vocabularies.

> While there is recent work on interpreting continuous machine languages (Andreas, Dragan, and Klein 2017)

> In this set of experiments we enable agents to observe other agents’ position and gaze location, and in turn disable communication capability via symbol utterances


## Z. Shi et al 2018 - toward diverse text generation with Inverse Reingorcement Learning
> The second problem is the mode collapse. The adversarial model tends to learn limited patterns because of mode collapse. One kind of methods, such as TextGAN [Zhang et al., 2017], uses feature matching [Salimans et al., 2016; Metz et al., 2016] to alleviate this problem, it is still hard to train due to the intrinsic nature of GAN. Another kind of methods [Bayer and Osendorfer, 2014; Chung et al., 2015; Serban et al., 2017; Wang et al., 2017] introduces latent random variables to model the variability of the generated sequences

> Secondly, a generation policy is learned to maximize the expected total rewards. The reward function aims to increase the rewards of the real texts in training set and decrease the rewards of the generated texts

> going around the generation problem

> sentence will get 1 point when it is viewed as a real one, otherwise 0 point. We perform the test on frameworks of MLE, SeqGAN, LeakGAN and our method on COCO Image captions dataset and IMDB movie review dataset

imitation game mode

## Carlile Gurrapadi et al 2018 - give me more feedback: annotating argument persuasiveness and related attributes in Student Essays
> The corpus we chose to annotate is composed of 102 essays randomly chosen from the Argument Annotated Essays corpus (Stab and Gurevych, 2014a). This collection of essays was taken from essayforum3
> Following van Eemeren et al. (2014), we define an argument as consisting of a conclusion that may or may not be supported/attacked by a set of evidences
> Argument assertions (major claims and claims) need not be believable on their own since that is the job of the supporting evidence. The Evidence score describes how well the su

> A decent, fairly clear argument. It could persuade some readers, but contains errors that detract from its strength or understandability
persuasiveness is important

> The PremiseType is common knowledge, which is mediocre compared to statistics and real example
common knowledge bad?!

# 30 done

## Green 2018b - towards mining sceintific discourse using arugmentation shcemes
> Although human-level understanding of natural language text is currently beyond the state of the art, we propose a semantics-informed approach to extracting individual arguments from biomedical research articles on human genetic variants with adverse health effects

> We present seven argumentation schemes that we defined in Prolog after analyzing the arguments in the first eight paragraphs of a ten-paragraph “
oh no, prolog, cringe

> Lawrence and Reed [18] investigated the problem of recognizing the “proposition type” of argument components in the AIFdb corpus [17]. In this corpus, the premises of an argument are subclassified according to type, e.g., the two premises of Practical Reasoning are labeled as Goal or GoalPlan. Thus, the proposition type provides a limited amount of semantic information. Using the labeling of premise type, conclusion, and argument scheme of text in the corpus, Lawrence and Reed built classifiers to recognize individual premises and conclusions based upon text features. They then experimented with identifying instances of schemes in a corpus of arguments extracted from a 19th century philosophy text

## Al Khatib et al 2018 - argumentation synthesis following rhetorical strategies
> We argue that such a strategy means to select, arrange, and phrase a set of argumentative discourse units.
> We find that the experts agree in the selection significantly more when following the same strategy
> Without a rhetorical strategy, arguments will hardly ever unfold their persuasive effectiveness.
> logos (providing logically reasoned arguments), ethos (demonstrating good character and credibility), and pathos (evoking the right emotions). Listeners or readers then decode the encoding, forming their view of the author’s logos, ethos, and pathos
> As Aristotle, we target argumentation that aims for persuasion — as opposed to critical discussions where strategic maneuvering is needed to achieve reasonableness (van Eemeren et al., 2014). Joviˇci´c (2006) proposed a procedure to evaluate the effectiveness of persuasive argumentation, though not in a computational way
> Similarly, Wang et al. (2017) reveal the importance of selecting the right framing of a discussion topic for winning classical debates
> Studying persuasive blog posts, Anand et al. (2011) develop a scheme with 16 persuasion tactics of four types: those that postulate outcomes of an uptake, those that generalize in some way, those that appeal to external authorities, and those that rely on interpersonal factors
> For giving a persuasive speech, Aristotle (2007) postulates five consecutive canons ofrhetoric: (1) inventio, the selection of arguments, (2) dispositio, the arrangement of the arguments to achieve maximum impact, (3) elocutio, the phrasing of the arguments in a clear and appropriate style, (4) memoria, the memorization of the speech, and (5) actio, the delivery of the speech with gestures, prosody, and further means

5 elements
rhetorical strategies

> Pair-strategy combinations varied across participants, but were balanced in overall terms. For each pair, the participants first had to select one thesis unit, one con unit, and three pro units from our pool that they thought could best form a persuasive argument following the given strategy.6 Then, they had to arrange these five units in the most suitable way they saw. Finally, they should phrase a coherent text by adding discourse markers and connectives (example terms were given) as well as punctuation marks before and after each unit.

strategy for writing in general

> We provide it at http://arguana.com/data

## DART: a dataset of argumetns and their relations on Twitter
> In the reconciliation phase among the three students annotators to build the final dataset, we chose the label that was annotated by at least 2 annotators out of 3 (majority voting mechanism).

how generous of them

# 33 and done!

