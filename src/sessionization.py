import sys # library to get command line arguments
#Below are the parameters I need to read.  They are indexed from 0-3
# sys.argv = ['./src/sessionization.py', './input/log.csv', './input/inactivity_period.txt', './output/sessionization.txt']
import datetime #library to help with the time math

#Get the inactivity period. Integer in seconds from 1 to 86400 (24hrs)
inactivity_file_name = sys.argv[2]
with open(inactivity_file_name) as inactivity_file:
	for line in inactivity_file:
		#print(line)
		inactivity = int(line)
#The "int" above turns the variable "line" into an integer, if it isn't already
#Now I create an array, "active_users" into which I write my 4 parameters for each active user
active_users = []
	#Each row will be a list:[IP, first datetime, last datetime, count] 
#We calculate duration by subtracting the first date time from the last date time, and adding 1 (because it's inclusive)
expired_users = [] 
	#Each row will be a list:[IP, first date & time, last date & time, duration, count]
output_file_name = sys.argv[3]
log_file_name = sys.argv[1]

def write_out():
	"""This function apppends each expired user to the output file as we get them"""
	global expired_users	
	with open(output_file_name, "a") as output_file:
		for user in expired_users:
			output_line=user[0]+","+user[1].strftime('%Y-%m-%d %H:%M:%S')+","+user[2].strftime('%Y-%m-%d %H:%M:%S')+","+str(user[3])+","+str(user[4])+"\n"
			output_file.write(output_line)
	expired_users=[]

def run_cleanup(current_time):
	"""Run cleanup on active_users"""
	global active_users
	#print("Active Users" + str(len(active_users)))
	to_be_deleted = [] #Allows us to remove expired users from the active user list without breaking the loop
	for i in range(len(active_users)):
		delta = current_time - active_users[i][2]
		#print(delta.total_seconds()>inactivity)
		if delta.total_seconds() > inactivity:
			session_duration = active_users[i][2] - active_users[i][1]
			expired_users.append([active_users[i][0],active_users[i][1],active_users[i][2],int(session_duration.total_seconds())+1,active_users[i][3]])
			to_be_deleted.insert(0,i) #I inserted this because at first, the deletion of expired users was breaking the loop. This line allowed me to delete them afterward, separately, without breaking the loop, and I chose to insert this instead of reversing the loop.  This would need to be tested when scaling up to larger sizes.
	for j in to_be_deleted:
		del active_users[j]
	#print("Expired Users AFter Cleanup" + str(len(expired_users)))
	write_out()

"""This function just checks to see if the request line is valid (a way of skipping the header line).  Currently I'm just checking to see if time zone can be cast as a float, but the function would have to be improved to test all of the items in the row for security purposes, if this program went into production."""
def IsValid(request_line):
	try:
		float(request_line[3])
		return True
	except ValueError:
		return False

#Let's start by clearing out "Sessionization.txt"
with open(output_file_name, "w") as output_file:
	print ("Erasing a new output file " + output_file_name) 
#This is main loop of the program, which produces a data stream that we parse
with open(log_file_name) as log_file:
	for line in log_file:
		request=line.split(',')
		#Validating line
		if not IsValid(request):
			#print("Skipping malformed line")
			continue
		#Check active users to see if we need to update one of them
		user_ip=request[0] #add together col 1 and col 2 of date data
		request_datetime = datetime.datetime.strptime(request[1]+" "+request[2], '%Y-%m-%d %H:%M:%S')
		
		run_cleanup(request_datetime)

		update=False #We are assuming, at the start of this loop, that this line of the file (request) will be a new user, unless the loop proves us wrong.
		for i in range(len(active_users)):
			if active_users[i][0] == user_ip:
				update=True
				break #This is for efficiency, since we found the active user and there is only ever one, so no need to continue.
		if update==True:
			#print("Update")
			active_users[i][2]=request_datetime
			active_users[i][3]+=1
		else:
			#print("add")
			active_users.append([user_ip,request_datetime,request_datetime,1])
			#each new user starts out with 1 request, hence the 1 above

	#Write anynew output
run_cleanup(datetime.datetime.now())
print ("Your new output file is at " + output_file_name)

