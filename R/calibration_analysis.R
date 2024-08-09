##############################
#### CALIBRATION#############
###########################

#### LOADING ####


calib <- read_csv("Data/Robustness/Calibration/clean_2024_05_27_14_32_llama3_instruct_t_0_6_calib_zero_shot_fr_calibration.csv")

calib <- read_csv("Data/Robustness/Calibration/clean_2024_06_06_17_29_gpt_4_t_1_calib_zero_shot_fr.csv")

calib <- read_csv("Data/Robustness/Calibration/clean_2024_06_07_15_03_gpt_3_5_turbo_t_1_calib_zero_shot_fr.csv")


calib <- read_csv("Data/Robustness/Calibration/clean_2024_07_01_21_06_mixtral_t_0_6_calib_zero_shot_fr.sv")



##### OVERVIEW ####



overview <- calib %>% 
  dplyr::group_by(stimulus,setting) %>% tally()
overview




#### Extract best guess #####

columns = c("...1","run_ID", "model", "prompt_method","t","stimulus", "setting", "X", "Q", "A", "A_clean", "R", "P")

new = data.frame(matrix(nrow = 0, ncol = length(columns))) 

# assign column names
colnames(new) = columns

for(i in 1: 24) {
  for(j in list(1,3,5)){
    final <- max(calib$P[calib$setting == j & calib$stimulus ==i])
    col <- filter(calib, setting == j & stimulus ==i & P == final)
    new <- rbind(new, col)
  }
}



##### crate na in place of faulty observations ###

new$A_clean[new$R == "<Reasoning>"] <- NA

new$Q <-1

overview <- new %>% 
  dplyr::group_by(setting, Q) %>% tally()
overview

calib <- new

####insert missing

for(i in 1: 24) {
  thing <- 
    ugh <- which(calib$stimulus == i)
  
  temp_frame <- calib[thing[1]:thing[length(thing)],]
  #print(temp_frame)
  for (j in c(1,3)){
    one <- subset(temp_frame, setting == j)
    if (nrow(one) == 0){
      print("ONE ENTERED")
      new <- data.frame(...1 = 1 ,run_ID = calib$run_ID[10],model= calib$model[10],prompt_method=calib$prompt_method[10],t=calib$t[10],stimulus = i,setting = j ,X = NA, Q= 1,A= NA,A_clean=NA,R="generated",P=0)
      calib <- rbind(calib, new)
    }
    if (nrow(one) == 2){
      print("eliminating")
      calib <- subset(calib, ...1 != one$...1[1] & ...1 != one$...1[2])
      mean <- mean(c(one$A_clean))
      new <-data.frame(...1 = 1 ,run_ID = calib$run_ID[10],model= calib$model[10],prompt_method=calib$prompt_method[10],t=calib$t[10],stimulus = i,setting = j ,X = NA, Q= 1,A= NA,A_clean=mean,R="summarized",P=0)
      calib <- rbind(calib, new)
      
    }
    
  }
  
}
new <- calib

####remove na
nas <- which(is.na(new$A_clean))
nas
for (x in nas){
  print(x)
  temp <- new
  cur_setting <- temp$setting[[x]]
  #print(cur_setting)
  temp <- filter(new, setting == cur_setting)
  #print(temp)
  print("XXXX")
  print(mean(temp$A_clean, na.rm = TRUE))
  new$A_clean[is.na(new$A_clean) & new$setting == cur_setting] <- mean(temp$A_clean, na.rm = TRUE)
}



overview <- new %>% 
  dplyr::group_by(setting) %>% tally()
overview


###### Analysis #####


##MEANS


means <- new %>%
  group_by(setting) %>%
  dplyr::summarize(mean_A = mean(A_clean), sd_A = sd(A_clean))
means





### PAIRED T_TEST

## Change out settings == , and Q== for other tests)


all.sig <-filter(new, Q == 1 & (setting ==1 |setting ==3)) %>% 
  t_test(A_clean~setting, detailed =TRUE, paired = TRUE) %>%
  add_significance()
all.sig

