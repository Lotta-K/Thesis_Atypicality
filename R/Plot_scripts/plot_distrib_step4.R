
df_long <- gather(STEP4_DISTRIB, key = "Model", value = "Value", -Q, -Category)

# Update category labels
#df_long$Category <- factor(df_long$Category, levels = c("correct", "reverse", "other"),
  #                         labels = c("Informational Redundancy", "Reverse Redundancy", "Other / None"))

# Update Q labels
#df_long$Q <- factor(df_long$Q, levels = c(1, 2), labels = c("Q1", "Q2"))

# Generate the bar plot with updated settings
step.4.distrib <- ggplot(df_long, aes(x = Category, y = Value)) +
  geom_bar(stat="identity", alpha=.6, width=.4, aes(fill=Category)) +
  #scale_fill_grey(start=0, end=0.8) +  # start and end define the range of grays
  #theme_bw() +
  theme(axis.text.x=element_blank(),
        axis.title.x=element_blank(),
        legend.position = "bottom")+
  facet_grid( ~ Model) +
  scale_y_continuous(breaks = seq(0, 24, by = 2)) +
  #scale_fill_brewer(palette = "Set1")+
  #scale_fill_manual(values = c("blue", "orange", "magenta"))+
  #scale_fill_viridis_d(direction = -1)+
  scale_fill_viridis_d(option = "turbo", direction = -1)+
  labs(y = "Number of occurrences",
       fill = "Accommodation")

step.4.distrib

png(paste("", "Step4_distrib.png", sep = ""), width = 4000, height = 2500)
step.4.distrib +
  theme(#axis.text.x  = element_text(size = 40, colour = "black"),
        axis.text.y  = element_text(size = 60, colour = "black"),
        axis.title.y = element_text(size = 60),
        #axis.title.x = element_text(size = 60),
        legend.text  = element_text(size = 60, face = "italic"),
        legend.title = element_text(size = 60),
        strip.text.x = element_text(size = 65),
        strip.text.y = element_text(size = 65), # size of the facet labels 
        plot.title   = element_blank()) # remove title
dev.off()


ggplot(df_long, aes(x = Category, y = Value)) +
  geom_bar(stat="identity", alpha=.6, width=.4, aes()) +
  #scale_fill_grey(start=0, end=0.8) +  # start and end define the range of grays
  #theme_bw() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))+
  facet_grid(Q ~ Model) +
  scale_y_continuous(breaks = seq(0, 24, by = 2)) +  # set y axis to show every second value from 0 to 24
  labs(title = "Bar Plot of Models by Q and Category",
       x = "Category",
       y = "Value")

