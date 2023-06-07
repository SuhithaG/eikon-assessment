# eikon-assessment
Contains needed solution files for the initial tech assessment

<h2>Assumptions for the Deriverables</h2>
<h3>Feature Derivation </h3>
I have made few assumptions while doing the feature derivation and folowing are the features dervied and the assumptions made:
1. Total experiments a user ran -> computed the total number of experiments a user ran
2. Average experiments amount per user -> Computed the average run time of experiments per user
3. User's most commonly experimented compound -> Found the compound experimented maximum number of times per user, in case of multiple compound used maximum times, the compound with least compound id is returned.

<h3>Other Assumptions</h3>
In the users.csv, there is field "signup_date" and I have used this field to eliminate the users who are not signed up yet i.e., whose signup date greater than tody's date, which means these user's future experiments are not considered while computing the feature extraction.
