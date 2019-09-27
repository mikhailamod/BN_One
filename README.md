# BN Assignment1

All the data fields:
- Genre (has 16 genres)
- Readability, discretized into:
  - x<3
  - 3<=x<5
  - 5<=x<7
  - x>=7
- Difficulty, discretized into:
  - x<4
  - 4<=x<5
  - 5<=x<7
  - x>=7
- Number of duplicates, discretized into:
  - x<20
  - 20<=x<30
  - 30<=x<50
  - x>=50
- Number of words in song, discretized into:
  - x<200
  - 200<=x<300
  - 300<=x<400
  - x>=400
- Sentiment, discretized into:
  - Negative: x<-0.05
  - Neutral: -0.05<=x<0.05
  - Positive: x>=0.05
- WonGrammy (boolean)

This also has a `split_data` function which takes 20 random songs from each year and produces a `testdata.json`, and puts the rest into `traindata.json`
