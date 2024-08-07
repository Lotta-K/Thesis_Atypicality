###### DATA LOADINg EXAMPLE

### This script is exemplary for the code that was used to load a file that was created cleaned with the Generation Code provided,
### and then added dummy data points in case there were missing data points. Additionally, it shows how multiple dataset such as 
### the baseline and critical and control conditions of few-shot prompting were combined into one file



##### Example llama few shot perturbation 


high_base <- read_csv("Example_Data/clean_2024-05-01_20-40_llama3_instruct_t-0.6_base_few_shot_fr_base_high.csv")
high_base$setup <- "high"
high_base <- subset(high_base, stimulus !=1 & stimulus != 6)
high <- read_csv("Example_Data/clean_2024-05-13_13-49_llama3_instruct_t-0.6_few_shot_fr_mislead_zero_High.csv")
high$setup <- "high"
high <- subset(high, stimulus !=1 & stimulus != 6)


low_base <- read_csv("Example_Data/clean_2024-05-01_21-13_llama3_instruct_t-0.6_base_few_shot_fr_base_low.csv")
low_base$setup <- "low"
low_base <- subset(low_base, stimulus !=10 & stimulus != 3)
low <- read_csv("Example_Data/clean_2024-05-13_16-40_llama3_instruct_t-0.6_few_shot_fr_mislead_zero_Low.csv")
low$setup <- "low"
low <- subset(low, stimulus !=10 & stimulus != 3)

# combine into one

full_working_fs <- do.call("rbind", list(high, high_base, low, low_base))

#### creating entries that are missing entirely 
### (this step was not needed outside of zero-shot prompting but is included for completeness, 
### the commenetd out code was used if responses to both Q1 and Q2 were expected)

for(i in 1: 24) {
  thing <- which(full_working_fs$stimulus == i)
  temp_frame <- full_working_fs[thing[1]:thing[length(thing)],]
  #print(temp_frame)
  for (j in c(1,3,5)){
    that <- which(temp_frame$setting == j)
    if (length(that)>0){
      new_temp_frame <- temp_frame[that[1]:that[length(that)],]
      one <- subset(new_temp_frame, Q==1)
      #print(one)
      two <- subset(new_temp_frame,Q==2)
      #print(two)
      if (nrow(one) == 0){
        print("ONE ENTERED")
        new <- data.frame(...1 = 1 ,run_ID = full_working_fs$run_ID[10],model= full_working_fs$model[10],prompt_method=full_working_fs$prompt_method[10],t=full_working_fs$t[10],stimulus = i,setting = j ,X = NA, Q= 1,A= NA,A_clean=NA,R="generated",failsafe=NA)
        full_working_fs <- rbind(full_working_fs, new)
      }
    #   if (nrow(two) == 0){
    #     print("Two ENTERED")
    #     new <- data.frame(...1 = 1 ,run_ID = full_working_fs$run_ID[10],model= full_working_fs$model[10],prompt_method=full_working_fs$prompt_method[10],t=full_working_fs$t[10],stimulus = i,setting = j ,X = NA, Q= 2,A= NA,A_clean=NA,R="generated",failsafe=NA)
    #     full_working_fs <- rbind(full_working_fs, new)
    #   }
     }
    # else{
    #   print("CREATING BOTH")
    #   new1 <- data.frame(...1 = 1 ,run_ID = full_working_fs$run_ID[10],model= full_working_fs$model[10],prompt_method=full_working_fs$prompt_method[10],t=full_working_fs$t[10],stimulus = i,setting = j ,X = NA, Q= 1,A= NA,A_clean=NA,R="generated",failsafe=NA)
    #   new2 <- data.frame(...1 = 1 ,run_ID = full_working_fs$run_ID[10],model= full_working_fs$model[10],prompt_method=full_working_fs$prompt_method[10],t=full_working_fs$t[10],stimulus = i,setting = j ,X = NA, Q= 2,A= NA,A_clean=NA,R="generated",failsafe=NA)
    #   full_working_fs <- do.call("rbind", list(full_working_fs, new1, new2))
    #   
    #}

}}

## replace nas with average of all same setting observations as a dummy

nas <- which(is.na(full_working_fs$A_clean))
nas
for (x in nas){
  temp <- full_working_fs
  cur_setting <- temp$setting[[x]]
  #print(cur_setting)
  temp <- filter(full_working_fs, setting == cur_setting)
  #print(temp)
  full_working_fs$A_clean[is.na(full_working_fs$A_clean) & full_working_fs$setting == cur_setting] <- mean(temp$A_clean, na.rm = TRUE)
} 


write.csv(full_working_fs, "Example_Data/llama_full_fs_mislead_zero.csv")



