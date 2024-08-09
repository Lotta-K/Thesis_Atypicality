####### KNOW GEN ANALYSIS


# load data
data <- read_csv("Data/Generated_Knowledge/full_know_gen_data.csv")


#overview

overview <- data %>% 
  dplyr::group_by(model, setting) %>% tally()
overview


#means

fs_means <- data %>%
  group_by(model, setting) %>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
fs_means


##### Paired T-TEST

#### insert correct model names (gpt-3.5-turbo, gpt-4, llama3_instruct, mixtral)

# baseline v critical significance

all.sig <-filter(data, model == "mixtral" & (setting ==1 |setting ==3)) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig



# baseline v control significance


all.sig <-filter(data, model == "gpt-4" & (setting ==1 |setting ==5)) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig


# critical v control significance

all.sig <-filter(data, model == "gpt-4" & (setting ==3 |setting ==5)) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig

