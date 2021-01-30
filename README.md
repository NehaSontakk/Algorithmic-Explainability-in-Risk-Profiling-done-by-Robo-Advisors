# Operationalizing explanations of the risk profiling algorithm used by robo financial advisory apps.
## Why?
<br>
There is a growing ubiquity regarding the decision-making algorithms that have started affecting people's lives. Our research is an attempt to operationalize the concept of explainability in automated tools used in fintech. We have selected the case of robo financial advisory apps which conduct a risk profiling of users based on a questionnaire and use it to give them investment advice. These algorithms are subjected to regulations in India and several other countries. However, regulators without the technical knowledge possess no means to understand the algorithms and test it themselves. Our research explores various explainability methods and implements it.
<br>
The detailed reasoning behind the methodology used is presented in our research paper, an excerpt displayed below.
<br>
<img src="Images/Paper1.png" width="600" height="650" align="middle"/>


## How?
<br>
Questions were gathered using many robo financial advisory app questionnaires. These questions and their respective answers were assigned scores according to the table given below. Four different equations were used to create different types of datasets, with different relationships. These datasets were then sampled (After chosing an appropriate size using the sampling analysis) to represent data given to a regulator. Reverse engineering the equations and explanations are found from these samples of data. The entire method as well as our thought process behind the study is explained further in the paper.
<br>
<img src="Images/Paper2.png" width="1001" height="520" align="middle"/>
<br>
<img src="Images/process.png" width="1001" height="520" align="middle"/>


## Contents of the Repository

1.  Generation of total data, initial analysis and sampling.
    1.  Polynomial Data 
    2.  Linear Data
    3.  Quadratic Data
    4.  Logarithmic Data
2.  __Operationalizing_Explanations.ipynb__ : Explanations of the data sample
    1.  Modelling the dataset
    2.  Global Explanations
        a.  Feature Importances
        b.  Feature Relations
    3.  Local Explanations
3.  __Risk_Data_Sampling.ipynb__ : Using the polynomial data with different sampling strategies
    1.  Random Sampling
    2.  Stratified Sampling
    3.  Categorical Random Sampling
4.  __Sample_Size_Analysis.ipynb__ : Analysing effect of different training sizes on best fit line accuracies.


#### Using this Repository

This repository is mainly used to display the analysis behind the paper. An automated tool to do the same is under construction. After downloading the repository unzip all the data files.


## Presented at the following conferences
[Changing Landscape of Securities (CLSM) Market by SEBI and NISM](https://www.nism.ac.in/SM2020/) <br>
[Data Governance Network](http://datagovernance.org/research?topic=&search=)
Mechanism Design For Social Good 2020

## Honours
Best Research Paper at CLSM (1st out of 56 shortlisted from 160+ submissions)

### Interesting Links
[Sebi bans investment advisors from providing free trials of services](https://www.livemint.com/market/stock-market-news/sebi-tightens-norms-for-investment-advisors-in-india-11577453148135.html)
