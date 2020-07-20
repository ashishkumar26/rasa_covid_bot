## happy_path
* greet
  - utter_greet
* inform{"country":"india"}
  - action_covid
  - utter_ask_country
* thanks
  - utter_goodbye

## happy_path1
* greet
  - utter_greet
* inform{"country":"uk"}
  - action_covid
  - utter_ask_country
* thanks
  - utter_goodbye

## happy_path2
* greet
  - utter_greet
* covid_search{country:"usa"}
    - action_covid
    - utter_ask_country
* thanks
  - utter_goodbye

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
