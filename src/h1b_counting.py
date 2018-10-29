import re
from collections import Counter

def parse_and_analyze():
    """
    This function parse the input csv file and return the 
    certified applications with occupation and state columns
    """
    all_soc_state_data=[]
    
    with open('./input/h1b_input.csv', encoding='utf-8', mode='r') as h1b:
        # Retrieve header row as we need to find the soc name, state, 
        # as well as the case status column indexes
        header=next(h1b).split(';')
        # Use regex to find soc_name, state, and case status indexes  
        # since different files have slightly different column names
        status_index=[i for i, s in enumerate(header) if re.findall('.*STATUS.*', s, re.IGNORECASE)][0]
        soc_name_index=[i for i, s in enumerate(header) if re.findall('.*SOC.*NAME.*', s, re.IGNORECASE)][0]
        state_index=[i for i, s in enumerate(header) if re.findall('.*WORK.*STATE.*', s, re.IGNORECASE)][0]
        # Then loop through each row and just take the certified rows with soc name and state
        soc_and_state=[]
        for row in h1b:
            row_list=row.split(';')
            if row_list[status_index]=='CERTIFIED':
                soc_and_state.append((row_list[soc_name_index], row_list[state_index]))
    all_soc_state_data.append(soc_and_state)
    # Now return all the data
    return(all_soc_state_data)

def get_top_n_counts(all_data, n):
    """
    This function take a list and return top n with
    names, counts and percentages as a list of tuples
    """
    top10_counter=Counter(all_data).most_common(n)
    top10_names=[name for (name, count) in top10_counter]
    top10_count=[count for (name, count) in top10_counter]
    top10_perc=["{0:.1%}".format(count/len(all_data)) for count in top10_count]
    # zip them together into one list
    top_10_stats=list(zip(*[top10_names, top10_count, top10_perc]))
    return(top_10_stats)

def output_txt(all_soc_state_data):
    """
    This function will take a list with all the soc name and state
    data for certified applications and then output text files with
    the top10 of each
    """
    # Use Counter module to find top10 occupations and states
    # for each year's data
    for idx, soc_state_data in enumerate(all_soc_state_data):
        # Unpack the list of tuples into occupations and states
        occupations=[o for (o, s) in soc_state_data]
        states=[s for (o, s) in soc_state_data]
        # Use the Counter most common 10 to find top10 occupations and states
        occupation_top10_stats=get_top_n_counts(occupations, 10)
        state_top10_stats=get_top_n_counts(states, 10)
        # Now write to the text files
        with open(''.join(['./output/', 'top_10_occupations', '.txt']), 'w') as data_file:
        	# First write the headers
            data_file.write(';'.join(['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE'])+'\n')
            for name, count, perc in occupation_top10_stats:
                data_file.write(';'.join([name,str(count), str(perc)])+'\n')
        with open(''.join(['./output/', 'top_10_states', '.txt']), 'w') as data_file:
        	# First write the headers
            data_file.write(';'.join(['TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE'])+'\n')
            for name, count, perc in state_top10_stats:
                data_file.write(';'.join([name,str(count), str(perc)])+'\n')

if __name__=='__main__':
	all_soc_state_data=parse_and_analyze()
	output_txt(all_soc_state_data)
