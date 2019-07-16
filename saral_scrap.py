import requests
import json

# url = requests.get("http://saral.navgurukul.org/api/courses")
# # print(url)														#write a data
# data = url.text
# with open("courses.json","w") as json_file:
# 	json_file.write(data)

def up():									#make function for calling 
	with open("courses.json","r")as json_file:  #read a file
		configration= json.load(json_file)      #data to convert into json format and store 
		# print (configration)
		all_courses=configration['availableCourses']
		# print(course)

		for course in range(len(all_courses)):	       			#use of dictionary  print all course
			print(course,all_courses[course]['name'])

		user=int(input("\nPlease choose the name of courses:"))  
		for course in range(len(all_courses)):					
			if user == course:						#select course
				print (all_courses[user]['id'], all_courses[user]['name'])
				print("")

				link = "http://saral.navgurukul.org/api/courses/"+str(all_courses[user]['id'])+"/exercises" # a link access by id from user
				data1 = requests.get(link)      # calling API access
				data2=data1.text
				inf=json.loads(data2)			# convert to json format use dictionary form
				# print(inf)
				all_data=inf['data']					# use of dictionary key value print
				# print(all_data)

				index=1
				for j in range(len(all_data)):			#use of dictionary  print all course
					print(j+1,all_data[j]["name"])
					for k in (all_data[j]['childExercises']):
						print('      ',index,k['name'])
						index+=1

				user2=int(input("\nPlease enter the name of Topic:"))   #select of topic content
				def navigation(user2):
					for exercise1 in range(len(all_data)+1):
						if user2 == exercise1:
							slug=(all_data[exercise1-1]["slug"])	# find the slug and print 
							print(slug)

							link2="http://saral.navgurukul.org/api/courses/"+str(all_courses[user]['id'])+"/exercise/getBySlug?slug="+slug
							content1=requests.get(link2)    # calling API access
							content2=content1.text
							print(content2)
							# print(all_data[exercise1-1]["slug"])
							break

					user3=str(input("Enter the input of navigation: "))     #use of navigation selection
					if user3=="up":		  
						up()			   #up navigation call
					elif user3=='p':	 
						user2=user2-1
						navigation(user2)  #previous navigation call
					elif user3=='n':	  
						user2=user2+1
						navigation(user2)  #next navigation call
					elif user3=='exit':
						print()
				navigation(user2)	#fucntion call
up()                        		#fucntion call