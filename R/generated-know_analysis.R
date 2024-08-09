####### KNOW GENB ANALYSIS


a <- know_gen_mixtral
b <- gpt35_know_gen
c<- gpt4_know_gen
d <- llama_know_gen

data <- do.call("rbind", list(a,b,c,d))


overview <- data %>% 
  dplyr::group_by(model, setting) %>% tally()
overview


fs_means <- data %>%
  group_by(model, setting) %>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
fs_means


# HIGH -->*
all.sig <-filter(data, model == "mixtral" & (setting ==1 |setting ==3)) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig


# HIGH -->*
all.sig <-filter(data, model == "gpt-4" & (setting ==1 |setting ==5)) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig


write.csv(data, "full_know_gen_data.csv")
