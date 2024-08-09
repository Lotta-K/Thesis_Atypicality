
full_working_fs <- all_thesis_hop_reasoning

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



# HIGH -->*
all.sig <-filter(full_working_fs, (setting ==1 |setting ==3) & conv == "l" & model == "mixtral") %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig
