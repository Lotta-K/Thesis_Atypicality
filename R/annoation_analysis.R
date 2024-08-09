###### Analyse the distribution of annotations


#load in data
annodata <- read_excel("Data/Annotated/annoatations_first_half.xlsx")
annodata <- read_excel("Data/Annotated/annotations_second_half.xlsx")
annodata <- read_excel("Data/Annotated/llama_annotations.xlsx")

# filter to only include annotated data
annodata <- subset(annodata, !is.na(anno_level1))



# further filters if needed 
annodata <- subset(annodata, prompt_method == "few_shot")


# tally annotations either by individual runs or by model and prompt method 

overview <- annodata %>% 
  group_by(run_ID, anno_level1, anno_level2_1, anno_level2_2)%>% tally()

overview <- annodata %>% 
  group_by(model, prompt_method, extra, anno_level1, anno_level2_1, anno_level2_2)%>% tally()



# save distribution
write.csv2(overview, "anno_distrib_fs.csv")
