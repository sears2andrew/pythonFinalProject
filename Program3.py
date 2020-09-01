'''
program 3 version 2 soccer stats
this program uses goal data read in from a file to determine
the total score of a set of soccer teams based on there wins, losses, and ties
then puts the output data into a table in another file
this program was written by andrew sears
'''
import sys, os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	
def sortData(allTeams): 
	
	numElts = len(allTeams)
	
	for val in range(0, numElts-1):
		for compare in range(val+1, numElts):
		
		# sort the data
			if (allTeams[compare][4] > allTeams[val][4]) or (allTeams[compare][4] == allTeams[val][4] and allTeams[compare][5] > allTeams[val][5]):
				temp = allTeams[val]   
				allTeams[val] = allTeams[compare]
				allTeams[compare] = temp
				
	return allTeams

	
	
def	displayRpt(sortedDataList, outputFile):
	outputFile.write('                  soccer results\n                                   Total   Goal\n')
	outputFile.write('team          wins   loses  ties   Score   Dif \n' + '=' * 50 + '\n')
	
	#write to file with formated information
	for val in sortedDataList:
	
		for now in range(6):
			outputFile.write(str(val[now]) + '      ')	
			
		outputFile.write('\n\n')
		
	
	
	

def main(__location__):
	#open files the get and write data
	outputFile = open(os.path.join(__location__,'soccerReport.txt'), 'w')
	inputFile = open(os.path.join(__location__, 'newsoccer.dat'), 'r')
	
	goalDif = wins = ties = loses = 0
	allTeams = [0, 0, 0, 0]
	
	for team in range(4):
		teamName = inputFile.readline()
		teamName = teamName.strip('\n')
		
		for scorePair in range(6):
			goals = inputFile.readline()
			goalsUs = int(goals[0])
			goalsthem = int(goals[2])
		
			#generate data points to sort and use	
			if goalsUs > goalsthem:
				wins = wins + 1
			elif goalsUs < goalsthem:
				loses = loses + 1
			else:
				ties = ties + 1
			
			
			totalScore = (wins * 3) + ties
			goalDif = goalDif + goalsUs - goalsthem
			
		teamName = [teamName, wins, loses, ties, totalScore, goalDif]		
		allTeams[team] = teamName		
		goalDif = wins = ties = loses = 0
		
	displayRpt(sortData(allTeams), outputFile)
	
	#close all files that are open
	inputFile.close()
	outputFile.close()
	
main(__location__)