from textblob import TextBlob

wiki = TextBlob("Jordan Bernt Peterson (born June 12, 1962) is a Canadian clinical psychologist and a professor of "
                "psychology at the University of Toronto. His main areas of study are in abnormal, social, "
                "and personality psychology,[1] with a particular interest in the psychology of religious and "
                "ideological belief[2] and the assessment and improvement of personality and performance.[3] "
                "Peterson has bachelors degrees in political science and psychology from the University of Alberta "
                "and a Ph.D. in clinical psychology from McGill University. He was a post-doctoral fellow at McGill "
                "from 1991 to 1993 before moving to Harvard University, where he was an assistant and then an "
                "associate professor in the psychology department.[4][5] In 1998, he moved back to Canada as a "
                "faculty member in the psychology department at the University of Toronto, where, as of 2019, "
                "he is a full professor. "
                "s first book, Maps of Meaning: The Architecture of Belief (1999), examined several academic fields "
                "to describe the structure of systems of beliefs and myths, their role in the regulation of emotion, "
                "creation of meaning, and several other topics such as motivation for genocide.[6][7][8] His second "
                "book, 12 Rules for Life: An Antidote to Chaos, was released in January 2018.[4][9][10] "
                "In 2016 Peterson released a series of YouTube videos criticizing political correctness and the "
                "Canadian government's Bill C-16, An Act to amend the Canadian Human Rights Act and the Criminal "
                "Code. The Act added gender identity and expression as a prohibited ground of discrimination,"
                "[a][11] which Peterson characterised as an introduction of compelled speech into law,[12][13][14] "
                "although legal experts have disagreed.[15] He subsequently received significant media coverage, "
                "attracting both support and criticism.[4][9][10] Peterson is associated with the "
                ".[16][17][18]")
print(wiki.sentiment.polarity)

# https://www.youtube.com/watch?v=o_OZdbCzHUA&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=2