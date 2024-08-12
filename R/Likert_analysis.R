###### ZERO SHOT Likert


## data Loading

full_working_fs <- read_csv("Data/Robustness/Likert/likert_zs_gpt3.csv")
full_working_fs <- read_csv("Data/Robustness/Likert/likert_zs_gpt4.csv")
full_working_fs <- read_csv("Data/Robustness/Likert/likert_zs_llama.csv")
full_working_fs <- read_csv("Data/Robustness/Likert/likert_zs_mixtral.csv")



### overview

full_working_fs <- filter(full_working_fs, !is.na(A_clean))


overview <- full_working_fs %>% 
  dplyr::group_by(Q, setting) %>% tally()
overview


overview <- full_working_fs %>% 
  dplyr::group_by(setup, setting) %>% tally()
overview


#### means

fs_means <- full_working_fs %>%
  group_by(Q,setting) %>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
fs_means



## paired t-test

#### insert q==1 or Q==2

# baseline v criticsl

all.sig <-filter(full_working_fs, Q==1& (setting ==1 |setting ==3)) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig


#baseline v control

all.sig <-filter(full_working_fs, Q==1& (setting ==1 |setting ==5)) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig


#critical v contrl


all.sig <-filter(full_working_fs, Q==1& (setting ==3 |setting ==5)) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig
