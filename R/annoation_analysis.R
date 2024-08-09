annodata <- full_TBA_FINAL_finished

annodata <- subset(annodata, !is.na(anno_level1))

annodata <- subset(annodata, prompt_method == "few_shot")


overview <- annodata %>% 
  group_by(run_ID, anno_level1, anno_level2_1, anno_level2_2)%>% tally()


overview <- annodata %>% 
  group_by(model, prompt_method, extra, anno_level1, anno_level2_1, anno_level2_2)%>% tally()


write.csv2(overview, "C:/Users/charl/PycharmProjects/Thesis_GPT/Thesis_GPT_R/anno_distib_fs.csv")
