
# from final text

This project is focused on data gathering. The goal is to investigate the 'games with purpose' paradigm to make crowdsourcing viable in this area.
These are questions that interested researches in discourse analysis for many years.
How to get beyond bag-of-words approaches for meaning and sentiment analysis? How to get to the structure of the argument, that may escape even the utterer?

The App will be optimized for generation of Labeled Argument Data (LAD). 
Structure of incentives is the more non-standard part of the project, more novel than just construing the interactive website.

Argument mining is importnat,
% todo add reasons
add bottleneck is the data

% todo write this out, need to implement
There is the option for a debate mode for the app.  That would be a type of game, where addition of a node to the argument tree would constitute a move.

Study by Siddarthan and Tidhar from 2006 'automatic classification of citation function' describes use of Kappa coefficient for that purpose.
The paper describes the use of Kappa coefficient thus:
\begin{quote}
  coefficient κ (Fleiss, 1971; Siegel and Castellan, 1988), the agreement measure predominantly used in natural language processing research (Carletta, 1996). κ corrects raw agreement P(A) for agreement by chance P(E)
\end{quote}

### too specific for this
https://en.wikipedia.org/wiki/X.690#BER_encoding
https://en.wikipedia.org/wiki/Propositional_calculus


### side comments
from @brunowick
> Cf my threat encouraging using new made-up names for new concepts instead of trying to form nice sentences and intensive use of an alias in wikilinks. 
> Concepts are mental landmarks and need names as soon as possible.
https://twitter.com/brunowinck/status/1513789272708599809

### Overspecific visualization
http://www.visualcomplexity.com/vc/
http://www.visualcomplexity.com/vc/project_details.cfm?index=10&id=68&domain=Knowledge%20Networks

### dead projects
> ransparent, open, public, autopoietic information system. The main idea of TaOPis is to provide a platform for self-organizing communities. Such communities can be either organizations or projects for which TaOPis provides suitable tools like semantic wiki systems, forums, blogs, ranking mechanisms, content filtering, tagging etc.
https://archive.ph/20130108094001/http://autopoiesis.foi.hr/


### multi agents
agent speak for multiagent environments
https://en.wikipedia.org/wiki/AgentSpeak
this is too niche, even if the multi agent human network would do a similar thing
https://en.wikipedia.org/wiki/Distributed_multi-agent_reasoning_system

introspective mood - green or warm orange
battle mood - red
collaboration - blue
the admins control what schools are showing to whom every week

to create the structure and then use it as embedded model - another paper could be out of this

encoder + decoder CNNs, pushing this structure around in the argument-space

a 'shadow place' for possible additions to the graph 
- add a child somewhere, it's as large as the number of nodes

## architecture document
- inflows from different datasets
- gamification database
- temporary events - in partnership would be the best!
- make it work for more people
- actually train the ai
- against a standard set and live dataset

The app also includes an AI-powered feature that allows users to simulate different perspectives and explore the underlying values and assumptions of different ideologies. This feature is designed to help users develop more empathy and engage in more productive dialogue with those who hold different views.
The results of the proof of concept support the goals of the Lully project, demonstrating the potential of AI-based tools to facilitate ethical decision-making and critical thinking. The gamification approach and progress bars were found to be effective in encouraging user engagement and exploration of the different scenarios.
It is unknown whether the analysis uses argument mining.

Lexisnexis provides analytic tools in the legal domain, also providing visualization
https://www.lexisnexis.com/en-us/home.page

This should be two or three short paragraphs (100-150 words total), summarising the dissertation. It is important that this is not just a restatement of the original project outline. A suggested flow is background, project aims and main achievements. A bad abstract would have a final paragraph that just said "the achievements will be described" - this is useless, as it says nothing. From the abstract a reader should be able to ascertain if the project is of interest to them and presents results of which they would like to know more details.
Thanks to whoever may have helped you in any way - both serious and a bit of fun.
The title the dissertation ends up with need not be the one it started with in the project choice stage more than a year earlier but it should be meaningful.  "My Design Project" is not meaningful.
There is a scarcity of open datasets in many domains of data science. In NLP there is an abundance of linear textual archives, but adversarial, debate-like data is scarce.
The third factor is probably above {90\%}.

What is exceptional about the Argdown is that it provides a textual standard to represent arguments of any complexity.

Insofar as the argument mining relates to Knowledge Graphs and Ontology extraction, Kelpie is one of the frameworks for the former.

Authors say Kelpie is a:
> XAI framework for interpreting Link Predictions on Knowledge Graphs
https://github.com/AndRossi/Kelpie
It is in active development and it might be useful for downstream processing of the data obtained through crowdsourcing.

% todo describe these
semantic network, formal concept analysis and ontology languages
% todo stakeholder analysis
% use cases
% functional requirments - one opinion relating to a different one
% non-finctional requiremnts
% technology considerations - consider web app
% constraints and assumptions

\subsection{technique chosen from available }
select a subst of things from analysis and design (3), say about tradeoffs. 


% write about entities: statement, relation, all 3 of the games
% information archiecture, hierachy, search and filtering, design principles
% data model - relational databse
% technical architecture - supabase.js SDK
% external APIs integration
% error handling

Our goals of developing an ethical decision-making tool with an easy-to-use interface were achieved, as evidenced by the positive feedback from initial user tests.

The use of progress bars and games to incentivize user engagement was particularly impactful, leading to increased motivation and participation.
Specifically, the ethical decision-making framework successfully identified potential conflicts and provided solutions aligned with ethical principles.

- findings - productsgenerated
- goals achieved - how much do the findings support the objectives
- say that no exeprimental wide participation
-  over some of the cases

- user feedback
- list of changes
- unmet goals
- lessons learned

Throughout the implementation phase, we tested the application extensively to ensure that it met our goals and objectives. However, due to time and legal constraints, we were unable to conduct a large-scale experimental study with a wide range of users. Nevertheless, the feedback we received from early users was positive, and we used this feedback to refine the application and improve its user flow.

- development process, tools, challenges
  -  vscode with extensions for working with expo platform
  - testing metholodology, Testing
  - user testing - target audience
  - deployment - infrastructure, platform used
- illustrate code traps
design of the interface, screens in the application in a logical way. 
data transmission and validation cross-update of topics
- aspects of update algoritmhs for the data structure

- aspects of update algoritmhs for the gamification pit

- aifdb - data translation

- working with argdown - hard to work with library


I also learned valuable lessons about using Supabase and writing mobile apps, which will inform future development.
  \item altruism
  \item progression - new capabilities unlocked  

mining: argument extraction, segmentation, i.e. identification of minimal argumentative discourse units (ADUs), segment classification, i.e. labeling of ADUs based on their argumentative roles, identification of relations between these segments, and argument completion, i.e. automatic construction of statements from implicit propositions
Some consideration should be given to incorporating them into the space of possible arguments on the app.

As mentioned above, AIFdb format may be used for data portability, and Argdown for markdown notation.
[ add about future plans]
[add challenges and obstacles]