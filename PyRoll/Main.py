import os
import csv
import pandas as pd

voting_dict = {}
total_votes_cast = 0
election_data_file = os.path.join("Resources","election_data.csv")


with open(election_data_file,"r",encoding="utf8") as csvfile:
    election_data_reader = csv.reader(csvfile,delimiter=",")
    #skip the header
    next(election_data_reader,None)

    #Read the csv file into a dictionary name => Numbe Of votes
    #Key is the name of the candidate and the value is number of votes
    for election_data in election_data_reader:
        #keep track of the total votes
        total_votes_cast+=1
        #If name ex. Khan is already in the dictionaary add the vote
        if( election_data[2] in voting_dict):
            voting_dict[election_data[2]] = voting_dict[election_data[2]] + 1
        #If not add a new Key/Value Pair
        else:
            voting_dict[election_data[2]] = 1
    
    print('\nElection Results')
    print('-----------------------------')
    print(f'\nTotal Votes: {total_votes_cast}\n')
    print('-----------------------------\n')

    election_resilt_file = os.path.join("Analysis","election_result.txt")

    with open(election_resilt_file,"w") as txtfile:
        txtfile.write('\nElection Results\n')
        txtfile.write('-----------------------------\n')
        txtfile.write(f'Total Votes: {total_votes_cast}\n')
        txtfile.write('-----------------------------\n')

        #Find the % of votes granered by each candidate
        #winner of the election
        #write the final results to ttxt file
        number_of_votes = 0
        for key, value in voting_dict.items():
            if value > number_of_votes:
                winner = key
                number_of_votes = value

            perc_vote = round((value/total_votes_cast)*100,4)
            print(f'{key}:   {perc_vote}% ({value})\n')
            txtfile.write(f'{key}:   {perc_vote}% ({value})\n')

        print(f'Winner: {winner}\n')
        txtfile.write(f'Winner: {winner}\n')
    