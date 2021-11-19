import pandas as pd

def main():
    # Read csv and store as dataframe
    df = pd.read_csv('ParticipantEachMean.csv')
    
    group_id_mean_values = df.groupby('Group_ID')['Talk_value'].mean().to_frame()
    mean_dict = group_id_mean_values.iloc[0:].set_index(df['Group_ID'].unique()).to_dict()
    mean_dict = mean_dict['Talk_value']

    # 7 -> 348.61333
    # print(mean_dict[7])

    differences = []
    group_mean = []
    for group_id, talk_value in zip(df['Group_ID'], df['Talk_value']):
        # print(f'group_id = {group_id}', end='\t')
        # print(f'talk_value = {talk_value}')
        mean_value = mean_dict[group_id]
        difference = abs(mean_value - talk_value)
        print(f'mean for this group_id = {mean_value}')
        # print(f'DIFFERENCE = {difference}')
        differences.append(difference)
        group_mean.append(mean_value)

    df['groupmean'] = group_mean
    df['differences'] = differences
    

    print(df)
    df.to_csv('out.csv')











if __name__ == '__main__':
    main()