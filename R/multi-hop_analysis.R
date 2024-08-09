### Multi Hop analysis


### load data

full_working_fs <- read_csv("Data/Multi_hop/all_thesis_hop_reasoning.csv")



###########overview 


overview <- full_working_fs %>% 
  dplyr::group_by(model, conv, setting) %>% tally()
overview



#################################################




####### visualisation: means ####





fs_means <- full_working_fs %>%
  group_by(model, conv, setting) %>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
fs_means

fs_means <- full_working_fs %>%
  group_by(conv, setting) %>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
fs_means


########## FS SUmmarization

full_working_fs <- summarySE(data = full_working_fs, measurevar = "A_clean", groupvars = c("model", "conv", "setting","stimulus"))



##### paired t-test

#### insert correct model names (gpt-3.5-turbo, gpt-4, llama3_instruct, mixtral)

#Multi-hop 1 


# baseline v critical
all.sig <-filter(full_working_fs, (setting ==1 |setting ==3) & conv == "c" & model == "mixtral") %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig

# baseline v control
all.sig <-filter(full_working_fs, (setting ==1 |setting ==5) & conv == "c" & model == "mixtral") %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig


# Multi Hop 2

# baseline v critical
all.sig <-filter(full_working_fs, (setting ==1 |setting ==3) & conv == "g" & model == "mixtral") %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig

# baseline v control
all.sig <-filter(full_working_fs, (setting ==1 |setting ==5) & conv == "g" & model == "mixtral") %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig


#Multi-hop 3

# baseline v critical
all.sig <-filter(full_working_fs, (setting ==1 |setting ==3) & conv == "l" & model == "mixtral") %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig

# baseline v control
all.sig <-filter(full_working_fs, (setting ==1 |setting ==5) & conv == "l" & model == "mixtral") %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig

