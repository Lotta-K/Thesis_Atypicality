#############################
######## FEW SHOT ANALYSIS##########
##############################

#librarys from mastercript are required

# load files 
llama <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/llama3_full_fs_normal.csv")
gpt3<-read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt3_full_fs_march.csv")
gpt3<- filter(gpt3,  setup=="high" |setup == "low")
gpt4<-read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_full_fs_march.csv")
gpt4<- filter(gpt4,  setup=="high" |setup == "low")

full_fs <- rbind(llama, gpt3)
full_fs<-rbind(full_fs, gpt4)

write.csv(full_fs, "C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/full_fs_cmcl.csv")


full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt3_full_fs_march.csv")

full_working_fs <-read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt3_full_fs_march_alternate_behavior.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt3_full_fs_march_crit_nom-crit.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt3_full_fs_march_misleadng.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt3_full_fs_march_mislead_low_rate.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt3_full_fs_march_mislead_zero.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt3_full_fs_march_misleading100_strong_cert.csv")


full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_full_fs_march.csv")

full_working_fs <-read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_full_fs_march_alternate_behavior.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_full_fs_march_crit_non-crit.csv")
full_working_fs <-read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_full_fs_march_misleading.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_full_fs_march_mislead_low_rate.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_full_fs_march_mislead_zuero.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_full_fs_march_misleading100_strong_cert.csv")


full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_turbo_full_fs_march.csv")

full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_turbo_full_fs_march_alternate_behavior.csv")
full_working_fs_b <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_turbo_full_fs_march_accidental_alternate_behavior.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_turbo_full_fs_march_criz_non-crit.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_turbo_full_fs_march_mislead100.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_turbo_full_fs_march_mislead_0.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_turbo_full_fs_march_mislead_low.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/gpt4_turbo_full_fs_march_mislead100_strong_cert.csv")



full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/mixtral_fs_strong100.csv")



#full_working_fs <- rbind(full_working_fs, full_working_fs_b)

full_working_fs <- filter(full_working_fs, setup == "high" | setup == "low")



####Likert

full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/full_likert_fs_3turbo.csv")
full_working_fs <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/full_likert_fs_4.csv")
full_working_fs <- read.csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/likert_llama3_full_normal.csv")





####################################
#########General Check of data######

overview <- full_working_fs %>% 
  dplyr::group_by(setup, setting) %>% tally()
overview


full_working_fs <- filter(full_working_fs, !is.na(A_clean))




####### visualisation: means ####

fs_means <- full_working_fs %>%
  group_by(setup, setting) %>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
fs_means



fs_means <- full_working_fs %>%
  group_by(setting) %>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
fs_means



##### Summarize when there are multiple obsertvations


#full_working_fs <- summarySE(data = full_working_fs, measurevar = "A_clean", groupvars = c("setting","stimulus", "setup"))

full_working_fs <- summarySE(data = full_working_fs, measurevar = "A_clean", groupvars = c("setting","stimulus"))


################ ANOVA ###### --> ns

# only one obseravtion for each in each setting and data is complete so no summary magic is needed 

fs.anova<-oneway.test(A_clean ~ setup,
                      data = full_working_fs,
                      var.equal = TRUE # assuming unequal variances
)
fs.anova


###### Pairwise t-test #### 

fs.pw <- full_working_fs%>% pairwise_t_test(
  A_clean~setup, paired = TRUE, 
  p.adjust.method = "bonferroni")
fs.pw

all.sig <-filter(full_working_fs, setting !=5) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig

all.sig <-filter(full_working_fs, setting !=3) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig

all.sig <-filter(full_working_fs, setting !=5) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig

#### 1v3 significance ########

# HIGH -->*
high.sig <-filter(full_working_fs, setup =="high" & setting !=5) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
high.sig

# MIXED --> ns
mixed.sig <-filter(full_working_fs, setup =="mixed" & setting !=5) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
mixed.sig


# OPPOSITE MIXED --> ns
mixed.sig <-filter(full_working_fs, setup =="op_mixed" & setting !=5) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
mixed.sig


# LOW --> ns
low.sig <-filter(full_working_fs, setup =="low" & setting !=5) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
low.sig



#### 1v5 significance ########

# HIGH -->*
high.sig <-filter(full_working_fs, setup =="high" & setting !=3) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
high.sig

# MIXED --> ns
mixed.sig <-filter(full_working_fs, setup =="mixed" & setting !=3) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
mixed.sig

# OPPOSITE MIXED --> ns
mixed.sig <-filter(full_working_fs, setup =="op_mixed" & setting !=3) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
mixed.sig

# LOW --> **
low.sig <-filter(full_working_fs, setup =="low" & setting !=3) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
low.sig


#### 3v5 significance ########

# HIGH -->ns
high.sig <-filter(full_working_fs, setup =="high" & setting !=1) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
high.sig

# MIXED --> ns
mixed.sig <-filter(full_working_fs, setup =="mixed" & setting !=1) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
mixed.sig

# OPPOSITE MIXED --> ns
mixed.sig <-filter(full_working_fs, setup =="op_mixed" & setting !=1) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
mixed.sig

# LOW --> *
low.sig <-filter(full_working_fs, setup =="low" & setting !=1) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
low.sig



######## MIXED VS OPPOSITE MIXED #########

comp.mixed.test <-filter(full_working_fs, (setup == "mixed"| setup == "op_mixed")) %>% 
  t_test(A_clean~setup, detailed =TRUE, paired = TRUE) %>%
  add_significance()
comp.mixed.test

comp.mixed.test <-filter(full_working_fs, (setup == "mixed"| setup == "op_mixed") & setting ==3) %>% 
  t_test(A_clean~setup, detailed =TRUE, paired = TRUE) %>%
  add_significance()
comp.mixed.test


######## COMPARING NEW AGAINST OLD MIXED #######

data <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/full_clean_data.csv")
data$t <-1
# extract relevant old data
data_fs3 <- filter(data, model == "gpt-3.5-turbo" & prompt_method== "few_shot" & Q==1 & (setting ==1 | setting ==3 |setting == 5))

# averaging bc we have only one response to compare against

data_fs3_avg = summarySE(data = data_fs3, measurevar = "A_clean", groupvars = c("setting","stimulus"))
data_fs3_avg$ID <- "old"

# create full mixed and also "average just so the stupid dfs have the same format
full_mixed <- rbind(mixed, mixed_base)
full_mixed_avg = summarySE(data = full_mixed, measurevar = "A_clean", groupvars = c("setting","stimulus"))
full_mixed_avg$ID <-"new"
full_mixed_avg <- subset(full_mixed_avg, stimulus != 4)


comp.mixed_data <- rbind(full_mixed_avg, data_fs3_avg)

comp.mixed.test <-comp.mixed_data %>% 
  t_test(A_clean~ID, detailed =TRUE, paired = TRUE) %>%
  add_significance()
comp.mixed.test

# -> **

mean_mixed_data <- comp.mixed_data %>%
  group_by(setting, ID)%>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
mean_mixed_data



