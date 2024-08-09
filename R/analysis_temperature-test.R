# new data loading

# read  in the new data with different temperatures
# t= 0
data1 <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Clean_Data_for_R_new/clean_2024-03-04_20-00_gpt-3.5-turbo_t-0_zero_shot_fr.csv")
data2 <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Clean_Data_for_R_new/clean_2024-03-05_18-43_gpt-3.5-turbo_t-0_zero_shot_fr.csv")
# t = 1.3
data3 <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Clean_Data_for_R_new/clean_2024-03-05_18-53_gpt-3.5-turbo_t-1.3_zero_shot_fr.csv")

#bind t = 0 data in one frame
data_t0 <- rbind(data1, data2)


######## GPT4 data

data4 <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Clean_Data_for_R_new/clean_2024-03-12_16-27_gpt-4_t-0_zero_shot_temp_test_setting1_3.csv")
#### -->> processing at the bottom

# read in full old data
data <- read_csv("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/full_clean_data_with_t.csv")
# extract relevant comparison data
data_old <- filter(data, model == "gpt-3.5-turbo" & prompt_method== "zero_shot")




# statistic significance of the runs with t=0 as previously identified

zero_3_t0<- filter(data_t0, prompt_method == "zero_shot" & model == "gpt-3.5-turbo" & Q == 1  &(setting == 1 | setting == 3))
zero_3_avg_t0 = summarySE(data = zero_3_t0, measurevar = "A_clean", groupvars = c("setting","stimulus"))


zero_3_t0_sig <-zero_3_avg_t0 %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
zero_3_t0_sig


# obtain the means and maybe visualize distribution

total_response_tally <-data_t0%>%
  group_by(setting, Q)%>% tally()

t0_mean<- data_t0%>%
  group_by(Q, setting)%>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
t0_mean

t0_mean_byX <- data_t0%>%
  group_by(Q, setting, X)%>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
t0_mean_byX


t0_means <- data_t0%>%
  group_by(Q, setting, stimulus)%>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
t0_means

t0_means_byX <- data_t0%>%
  group_by(Q, setting, simulus, X)%>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
t0_means_byX



# comp1: comparison run 1 with t=0 against run 2 with t=0 only setting 3 and Q1 --> nan bc to identical


data_comp1 <- filter(data_t0, Q==1 & setting==3)

comp1_tally <- data_comp1 %>%
  group_by(run_ID, stimulus)%>%tally()


data_comp1_avg = summarySE(data = data_comp1, measurevar = "A_clean", groupvars = c("run_ID","stimulus"))

comp1 <-data_comp1_avg %>% 
  t_test(A_clean~run_ID, detailed =TRUE, paired = TRUE) %>%
  add_significance()
comp1


#comp2: t-test full dataset --> *significantly different --> ONE WAY ANOVA ns
data_comp2_avg = summarySE(data = data_t0, measurevar = "A_clean", groupvars = c("run_ID", "stimulus", "setting", "Q"))

comp2 <-data_comp2_avg %>% 
  t_test(A_clean~run_ID, detailed =TRUE, paired = TRUE) %>%
  add_significance()
comp2

### full dataset, Q1 only --> ns but no longer identical

data_comp2b_avg = summarySE(data = filter(data_t0, Q==1), measurevar = "A_clean", groupvars = c("run_ID","stimulus", "setting", "Q"))

comp2b <-data_comp2b_avg %>% 
  t_test(A_clean~run_ID, detailed =TRUE, paired = TRUE) %>%
  add_significance()
comp2b

data_comp2c_avg = summarySE(data = filter(data_t0, Q==2), measurevar = "A_clean", groupvars = c("run_ID","stimulus", "setting", "Q"))

comp2c <-data_comp2c_avg %>% 
  t_test(A_clean~run_ID, detailed =TRUE, paired = TRUE) %>%
  add_significance()
comp2c



#comparison respondents within new data

#### briefly looked at it by inserting X in above code and this feels like a slippery slope to not continue on
#### basically it don't matter for Q1 and it's only lowkey a little signficant for Q2 but Q2 is generally all over the place



# comp3: comparison t=0 vs t = 1

# adding t as column for independent variable
data_old <- data_old$t = 1
data_t0<-data_t0$t = 0



data_comp3<- rbind(data_old, data_t0)


data_comp3_avg = summarySE(data = data_comp3, measurevar = "A_clean", groupvars = c("setting","stimulus", "t", "Q"))


comp3 <-data_comp3_avg %>% 
  t_test(A_clean~t, detailed =TRUE, paired = TRUE) %>%
  add_significance()
comp3


data

#####################
####################
# data3 1=1.3

data3_tally <- data3%>%
  group_by(setting, Q)%>% tally()

data3_sig<- filter(data3, Q == 1  &(setting == 1 | setting == 3))
data3_sig_avg = summarySE(data = data3_sig, measurevar = "A_clean", groupvars = c("setting","stimulus"))


data3.test <-data3_sig_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
data3.test

t1.3_mean<- data3%>%
  group_by(Q, setting)%>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
t1.3_mean




########################
########################
# data4, GPT4 t = 0

data4_tally <- data4%>%
  group_by(setting, Q)%>% tally()

data4_sig<- filter(data4, Q == 1  &(setting == 1 | setting == 3))
data4_sig_avg = summarySE(data = data3_sig, measurevar = "A_clean", groupvars = c("setting","stimulus"))


data4.test <-data4_sig_avg %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
data4.test

data4_mean<- subset(data4, !is.na(A_clean)) %>%
  group_by(Q, setting)%>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
data4_mean

### compare against other temp

data_old4 <- filter(data, model == "gpt-4" & prompt_method== "zero_shot" & (setting ==1 | setting==3))
data_old4 <- subset(data_old4, select = -c(...2))
comp5_data<- rbind(data4, data_old4)
comp5_data <- subset(comp5_data, Q ==1)

comp5_avg <- summarySE(data = comp5_data, measurevar = "A_clean", groupvars = c("setting", "stimulus","run_ID"))
comp5.test <-comp5_avg %>% 
  t_test(A_clean~run_ID, detailed =TRUE, paired = TRUE) %>%
  add_significance()
comp5.test

##### I ended up not even loading in temp = 1.3 bc it was incomplete again bc the charmap error is not resolved
##### and visual inspection shows it looks the same


##### check annotations script for temperature tests

anno1 <- read_excel("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/0307_gpt3_t0_zs_annotations.xlsx", sheet = 1)
anno2 <- read_excel("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/0307_gpt3_t0_zs_annotations.xlsx", sheet = 2)
anno3 <- read_excel("C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/0309_gpt3_t13_zs_annotations.xlsx", sheet = 1)

annodata <- rbind(anno1, anno2)
annodata <- rbind(annodata, anno3)

annodata <- full_TBA_FINAL_finished

annodata <- subset(annodata, !is.na(anno_level1))

annodata <- subset(annodata, prompt_method == "few_shot")


overview <- annodata %>% 
  group_by(run_ID, anno_level1, anno_level2_1, anno_level2_2)%>% tally()


overview <- annodata %>% 
  group_by(model, prompt_method, extra, anno_level1, anno_level2_1, anno_level2_2)%>% tally()


write.csv2(overview, "C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/anno_distib_fs.csv")
