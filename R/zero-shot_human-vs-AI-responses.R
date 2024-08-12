# paired t-test: responses as AI vs responses as human


#load data

data <- read.csv("Data/Zero_Shot/all_gpts_zs.csv")

# summarize while keeping , i.e. responder distinction intact

data <- summarySE(data = data, measurevar = "A_clean", groupvars = c("model", "setting","stimulus", "X"))



#paired t-test

stat.test <-subset(data, model == "gpt-3.5-turbo") %>% 
  t_test(A_clean~X, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test


stat.test <-subset(data, model == "gpt-4") %>% 
  t_test(A_clean~X, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test
