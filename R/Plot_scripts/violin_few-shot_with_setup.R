#### DATA LOADING

## regular few shot

a <- read_csv("Data/Few_Shot/mixtral_fs.csv")
b <- read_csv("Data/Few_Shot/llama3_full_fs_normal.csv")
c <- read_csv("Data/Few_Shot/gpt3_full_fs.csv")
d <- read_csv("Data/Few_Shot/gpt4_full_fs.csv")

full_data <- do.call("rbind", list(a,b,c,d))


### perturbation

a <- read_csv("Data/Few_Shot/mixtral_fs_crit-noncrit.csv")
b <- read_csv("Data/Few_Shot/llama3_full_fs_crit_non-crit.csv")
c <- read_csv("Data/Few_Shot/gpt3_full_fs_crit_non-crit.csv")
d <- read_csv("Data/Few_Shot/gpt4_full_fs_crit_non-crit.csv")

full_data <- do.call("rbind", list(a,b,c,d))


for_plot  = filter(full_data, (setting == 1 | setting == 2 | setting ==3 | setting == 4) & (setup == "high"| setup == "low") )

for_plot$condition = 0
for_plot$world     = 0
for_plot$condition[for_plot$setting == 1 | for_plot$setting == 2] = "before"
for_plot$condition[for_plot$setting == 3 | for_plot$setting == 4] = "after"
for_plot$world[for_plot$setting == 1 | for_plot$setting == 3]     = "ordinary"
for_plot$world[for_plot$setting == 2 | for_plot$setting == 4]     = "wonky"

exc.habitual.data_plot = for_plot #filter(for_plot, prompt_method == "few_shot" & Q == 1)

exc.habitual.data_plot$world     = factor(exc.habitual.data_plot$world, 
                                          levels=c("wonky", "ordinary"))
exc.habitual.data_plot$condition = factor(exc.habitual.data_plot$condition,
                                          levels=c("after","before"))

exc.habitual.data_plot = exc.habitual.data_plot %>% dplyr::filter(world=="ordinary")

dodge = position_dodge(width = 0.85)

exc.habitual.summary = exc.habitual.data_plot %>% dplyr::group_by(world, condition, setup, model) %>% dplyr::summarise(val = mean(A_clean))

# define short names for LLMs according to the paper:
model.labs        = c("GPT-3.5-t", "GPT-4", "Llama 3", "Mixtral")
names(model.labs) = c("gpt-3.5-turbo", "gpt-4", "llama3_instruct", "mixtral")

p.ordinary.habit = ggplot(exc.habitual.data_plot, aes(x = world, y = A_clean, fill = condition)) + 
  geom_violin(position = dodge, scale="count") +
  ## outlier.size - to change the size of the outliers, 
  ## size         - to change how thick the borders of the boxplots are:
  geom_boxplot(outlier.size = 8, width=.175, aes(fill=NULL,group=interaction(world,condition)),
               fill="white", position = dodge, size = 1) +
  ## stroke - to make the white borders thicker, 
  ## size   - to increase the size of the mean point,
  ## color  - to make white borders of the mean point:
  geom_point(data = exc.habitual.summary, aes(y = val), position = dodge,
             shape=21, size = 12, colour = "white", stroke = 3) +
  ## add an arrow to mark a significant difference between the utterance conditions in gpt-4:
  geom_line(data = filter(exc.habitual.summary, world=="ordinary", model== "gpt-4"),
            aes(y = val, group = world),
            position = position_dodge(width = 1),
            arrow = arrow(angle = 25, ends = "first", type = "closed",
                          length = unit(1, "cm")))+
  ylab("Typicality ratings") +
  xlab("") +
  theme(legend.position="bottom") +
  scale_fill_grey(start = 0.2, end = 0.8, name="Utterance:", 
                  breaks=c("before","after"), 
                  labels=c("baseline (no utterance)","conv. habitual ('She ate there!')")) + 
  scale_y_continuous(breaks = c(0,25,50,75,100), 
                     labels = c("0","25","50","75","100"),limits = c(0,100)) + 
  scale_x_discrete(labels = c("","")) + 
  coord_flip()+
  facet_grid(setup~model, labeller=labeller(model = model.labs))+
  theme(panel.spacing.x = unit(10, "mm"))
p.ordinary.habit


png(paste("", "Setup_thesis_violin_fewshot.png", sep = ""), width = 2500, height = 1142)
p.ordinary.habit +
  theme(axis.text.x  = element_text(size = 40, colour = "black"),
        axis.text.y  = element_text(size = 60, colour = "black"),
        axis.title.y = element_text(size = 60),
        axis.title.x = element_text(size = 60),
        legend.text  = element_text(size = 45, face = "italic"),
        legend.title = element_text(size = 45),
        strip.text.x = element_text(size = 65),
        strip.text.y = element_text(size = 65), # size of the facet labels 
        plot.title   = element_blank()) # remove title
dev.off()


