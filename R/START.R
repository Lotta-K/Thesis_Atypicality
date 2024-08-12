
###### START SCRIPT THESIS ATYPICALITY


#### PLEASE LOAD THE BELOW PACAKGES AND LIBRARIES


library(languageR)
library(ggplot2)
library(dplyr)
library("tidyverse")
library(rstatix)
library(Rmisc)
library("readxl")
library(tidystats)
library(rstudioapi)
library(tidyr)
library(tidyverse)
library(gtools)



##### DATA PROCESSING

### see the below script for an example of how output data 
### from the Python Code was processed
### all provided Data is already processed

Data_loading_example.R



##### Find below all scripts for replicating analysis in order 
##### of appearance in the thesis


##### Chapter 4: Zero Shot

### replicate presented analysis
zero-shot_analysis.R


### create the provided violin plot
Plot_script/violin_zero-shot.R


### replicate annotation distribution based on provided annotated data
annotation_analysis.R


### perform the analysis using results acquired with varying temperatures
analysis_temperature-test.R


### compare the results of AI vs pretend Human responses
zero-shot_human-vs-AI-responses.R



##### Chapter 5: Few Shot

### replicate presented analysis
few-shot_analysis.R


### create the provided violin plot
Plot_script/violin_few-shot.R


### replicate annotation distribution based on provided annotated data
annotation_analysis.R


### analysis differentiating between exemplars
few-shot_by_exemplar_seting.R


### violin differentiating between exemplars
Plot_script/violin_few-shot.R



##### CHAPTER 6: Analysis of reasoning steps

### replicate graph from step 1
Plot_script/plot_distrib_step1.R


### replicate graph from step 3
Plot_script/plot_distrib_step3.R


### replicate graph from step 4
Plot_script/plot_distrib_step4.R



##### Chapter 7: Generated Knowledge Prompting

### replicate presented analysis
generated-know_analysis.R


### create the provided violin plot
Plot_script/violin_generated_know.R


### replicate annotation distribution based on provided annotated data
annotation_analysis.R



##### Chapter 8: Multi-hop


### replicate presented analysis
multi-hop_analysis.R


### create the provided violin plot
Plot_script/violin_multi-hop.R


### replicate annotation distribution based on provided annotated data
annotation_analysis.R






##### Chapter 9: Robustness


### obtain analysis from likert promting
Likert_analysis.R



### obtain results for calibration analysis
calibration_analysis.R






