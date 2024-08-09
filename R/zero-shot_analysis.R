#### ZERO SHOT ANALYSIS

a <- read.csv("Data/Zero_Shot/all_gpts_zs.csv")
b <- read.csv("Data/Zero_Shot/llama3_full_zs.csv")
c <- read.csv("Data/Zero_Shot/mixtral_zs.csv")

data <- do.call("rbind", list(a,b,c))

data<- subset(data, !is.na(A_clean))


#### MEANS



means <- data %>%
  group_by(model, Q, setting) %>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
means


######Paired T-TESTS

# normal context

####  NB! insert Q==1 or Q == 2

# baseline v critical sign

#GPT 3.5 turbo


zero_3 <- filter(data, prompt_method == "zero_shot" & model == "gpt-3.5-turbo" & Q == 1  &(setting == 1 | setting == 3))
zero_3_avg = summarySE(data = zero_3, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_3_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test

# GPT 4

zero_4 <- filter(data, prompt_method == "zero_shot" & model == "gpt-4" & Q == 1  &(setting == 1 | setting == 3))
zero_4_avg = summarySE(data = zero_4, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_4_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test

##llama

zero_llama <- filter(data, prompt_method == "zero_shot" & model == "llama3_instruct" & Q == 1  &(setting == 1 | setting == 3))
zero_llama_avg = summarySE(data = zero_llama, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_llama_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test


#Mixtral

zero_mixtral <- filter(data, prompt_method == "zero_shot" & model == "mixtral" & Q == 1  &(setting == 1 | setting == 3))
zero_mixtral_avg = summarySE(data = zero_mixtral, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_mixtral_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test

### baseline v control


zero_3 <- filter(data, prompt_method == "zero_shot" & model == "gpt-3.5-turbo" & Q == 1  &(setting == 1 | setting == 5))
zero_3_avg = summarySE(data = zero_3, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_3_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test

# GPT 4

zero_4 <- filter(data, prompt_method == "zero_shot" & model == "gpt-4" & Q == 1  &(setting == 1 | setting == 5))
zero_4_avg = summarySE(data = zero_4, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_4_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test

##llama

zero_llama <- filter(data, prompt_method == "zero_shot" & model == "llama3_instruct" & Q == 1  &(setting == 1 | setting == 5))
zero_llama_avg = summarySE(data = zero_llama, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_llama_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test


#Mixtral

zero_mixtral <- filter(data, prompt_method == "zero_shot" & model == "mixtral" & Q == 1  &(setting == 1 | setting == 5))
zero_mixtral_avg = summarySE(data = zero_mixtral, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_mixtral_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test



#### wonky context

# baseline v critical sign

#### NB! insert Q==1 or Q == 2

#GPT 3.5 turbo


zero_3 <- filter(data, prompt_method == "zero_shot" & model == "gpt-3.5-turbo" & Q == 1  &(setting == 2 | setting == 4))
zero_3_avg = summarySE(data = zero_3, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_3_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test

# GPT 4

zero_4 <- filter(data, prompt_method == "zero_shot" & model == "gpt-4" & Q == 1  &(setting == 2 | setting == 4))
zero_4_avg = summarySE(data = zero_4, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_4_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test

##llama

zero_llama <- filter(data, prompt_method == "zero_shot" & model == "llama3_instruct" & Q == 1  &(setting == 2 | setting == 4))
zero_llama_avg = summarySE(data = zero_llama, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_llama_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test


#Mixtral

zero_mixtral <- filter(data, prompt_method == "zero_shot" & model == "mixtral" & Q == 1  &(setting == 2 | setting == 4))
zero_mixtral_avg = summarySE(data = zero_mixtral, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_mixtral_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test

### baseline v control


zero_3 <- filter(data, prompt_method == "zero_shot" & model == "gpt-3.5-turbo" & Q == 1  &(setting == 2 | setting == 6))
zero_3_avg = summarySE(data = zero_3, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_3_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test

# GPT 4

zero_4 <- filter(data, prompt_method == "zero_shot" & model == "gpt-4" & Q == 1  &(setting == 2 | setting == 6))
zero_4_avg = summarySE(data = zero_4, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_4_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test

##llama

zero_llama <- filter(data, prompt_method == "zero_shot" & model == "llama3_instruct" & Q == 1  &(setting == 2 | setting == 6))
zero_llama_avg = summarySE(data = zero_llama, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_llama_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test


#Mixtral

zero_mixtral <- filter(data, prompt_method == "zero_shot" & model == "mixtral" & Q == 1  &(setting == 2 | setting == 6))
zero_mixtral_avg = summarySE(data = zero_mixtral, measurevar = "A_clean", groupvars = c("setting","stimulus"))

stat.test <-zero_mixtral_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
stat.test



