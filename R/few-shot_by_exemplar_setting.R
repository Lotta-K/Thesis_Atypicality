#############################
######## FEW SHOT ANALYSIS##########
##############################

#librarys from mastercript are required


### GPT-3.5-turbo

full_working_fs <- read_csv("Data/Few_Shot/gpt3_full_fs.csv")


full_working_fs <- read_csv("Data/Few_Shot/gpt3_full_fs_crit_nom-crit.csv")
full_working_fs <- read_csv("Data/Few_Shot/gpt3_full_fs_misleadng.csv")
full_working_fs <- read_csv("Data/Few_Shot/gpt3_full_fs_mislead_low_rate.csv")
full_working_fs <- read_csv("Data/Few_Shot/gpt3_full_fs_mislead_zero.csv")
full_working_fs <- read_csv("Data/Few_Shot/gpt3_full_fs_misleading100_strong_cert.csv")

### GPT-4


full_working_fs <- read_csv("Data/Few_Shot/gpt4_full_fs.csv")

full_working_fs <- read_csv("Data/Few_Shot/gpt4_full_fs_crit_non-crit.csv")
full_working_fs <-read_csv("Data/Few_Shot/gpt4_full_fs_misleading.csv")
full_working_fs <- read_csv("Data/Few_Shot/gpt4_full_fs_mislead_low_rate.csv")
full_working_fs <- read_csv("Data/Few_Shot/gpt4_full_fs_mislead_zero.csv")
full_working_fs <- read_csv("Data/Few_Shot/gpt4_full_fs_misleading100_strong_cert.csv")


### LLama


full_working_fs <- read_csv("Data/Few_Shot/llama_full_fs.csv")

full_working_fs <- read_csv("Data/Few_Shot/llama_full_fs_crit_non-crit.csv")
full_working_fs <-read_csv("Data/Few_Shot/llama_full_fs_misleading.csv")
full_working_fs <- read_csv("Data/Few_Shot/llama_full_fs_mislead_low_rate.csv")
full_working_fs <- read_csv("Data/Few_Shot/llama_full_fs_mislead_zuero.csv")
full_working_fs <- read_csv("Data/Few_Shot/llama_full_fs_misleading100_strong_cert.csv")


### Mixtral


full_working_fs <- read_csv("Data/Few_Shot/mixtral_fs.csv")

full_working_fs <- read_csv("Data/Few_Shot/mixtral_fs_crit-noncrit.csv")
full_working_fs <-read_csv("Data/Few_Shot/mixtral_fs_100.csv")
full_working_fs <- read_csv("Data/Few_Shot/mixtral_fs_lowrate.csv")
full_working_fs <- read_csv("Data/Few_Shot/mixtral_fs_zero.csv")
full_working_fs <- read_csv("Data/Few_Shot/mixtral_strong100.csv")

# select both high and low exemplars


full_working_fs <- filter(full_working_fs, setup == "high" | setup == "low")


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





##### Summarize when there are multiple obsertvations


full_working_fs <- summarySE(data = full_working_fs, measurevar = "A_clean", groupvars = c("setting","stimulus", "setup"))

#### PAIRED T-TESTS

#### baseline v critical significance ########

# HIGH
high.sig <-filter(full_working_fs, setup =="high" & setting !=5) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
high.sig


# LOW 
low.sig <-filter(full_working_fs, setup =="low" & setting !=5) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
low.sig



#### baseline v control significance ########

# HIGH
high.sig <-filter(full_working_fs, setup =="high" & setting !=3) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
high.sig


# LOW
low.sig <-filter(full_working_fs, setup =="low" & setting !=3) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
low.sig


#### control v critical significance ########

# HIGH -->ns
high.sig <-filter(full_working_fs, setup =="high" & setting !=1) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
high.sig



# LOW --> *
low.sig <-filter(full_working_fs, setup =="low" & setting !=1) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
low.sig





