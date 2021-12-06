import pandas as pd
import numpy as np 
from pprint import pprint


predictions =  pd.read_csv("Post-Study_Survey_Data.csv")
talk_value_percentage = pd.read_csv("ParticipantDeviation.csv")

# print(predictions)
# print(talk_value_percentage)



id_predictions = predictions[['Participant_ID_new', 'TalkTime_Prediction']]

id_talk_value = talk_value_percentage[['Participant_ID', 'Group_ID', 'Talk_value']]

# print(id_predictions)
# print(id_talk_value) 

group_id_total_values = talk_value_percentage.groupby('Group_ID')['Talk_value'].sum().to_frame().reset_index()
# print(group_id_total_values['Group_ID'])
# print(group_id_total_values)

total_talk_time_dictionary = dict(zip(group_id_total_values['Group_ID'], group_id_total_values['Talk_value']))
# print(total_talk_time_dictionary)

# print(total_talk_time_dictionary[10])

# talk_value_percentage.assign(key=talk_value_percentage['Group_ID'].map(total_talk_time_dictionary))
talk_value_percentage['Percentage'] = (talk_value_percentage['Talk_value'] / talk_value_percentage['Group_ID'].map(total_talk_time_dictionary) * 100).round(2)

print(talk_value_percentage)

print(id_predictions['Participant_ID_new'])
print(id_predictions['TalkTime_Prediction'])

# skip first 2 rows
talk_value_percentage = talk_value_percentage[2:]
id_predictions = id_predictions[2:]
id_predictions.fillna(0)
id_predictions['TalkTime_Prediction'] = id_predictions['TalkTime_Prediction'].fillna(0)


groupid_talk_percentage_dictionary = dict(zip(talk_value_percentage['Participant_ID'], talk_value_percentage['Percentage'])) 
print(groupid_talk_percentage_dictionary)


print(id_predictions)

# pd.set_option('display.max_rows', 100)
id_predictions['TalkTime_Prediction'] = id_predictions['TalkTime_Prediction'].fillna(0)
id_predictions['TalkTime_Prediction'] = id_predictions['TalkTime_Prediction'].astype(float)

print(id_predictions['TalkTime_Prediction'])

id_predictions['Actual_Talk_Value'] = id_predictions['Participant_ID_new'].map(groupid_talk_percentage_dictionary).fillna(0)
id_predictions['Absolute_Difference'] = abs(id_predictions['TalkTime_Prediction'] - id_predictions['Actual_Talk_Value']).round(2)


id_predictions['Conditions'] = predictions['Conditions'] 

pprint(id_predictions)

id_predictions.to_csv('Percentage_Comparison.csv')
