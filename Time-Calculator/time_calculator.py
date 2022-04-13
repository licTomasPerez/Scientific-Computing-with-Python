def add_time(start, duration, user_wday = "None"):

  ### Now, we are to process start, breaking it into its components by using rstrip and split.
	start_Time_hsmins, start_meridian = start.split() ## 1. We start by receiving something like 11:06 PM and we divide it into two subcomponents, a time list and the meridian list. We get <<['11:06', 'PM']>>.
	start_Time_hsmins_div = start_Time_hsmins.split(":") ## 2. We take the 'time' list, <<['11:06'], and we further divide into two sublist, one giving the hour and the other giving the minute. We do this by splitting the time list into two halves. 
	start_Time_hs = int(start_Time_hsmins_div[0]) ## 3. Hour list
	start_Time_mins = int(start_Time_hsmins_div[-1]) ## 4. Mins list

	### Same logic will be applied to duration
	duration_timespan_div = duration.split(":")
	duration_timespan_hs = int(duration_timespan_div[0])
	duration_timespan_mins = int(duration_timespan_div[-1])

	### Change PM to 12-24
	if start_meridian == "PM" :
		start_hs_24format = int(start_Time_hs + 12)
	elif start_meridian == 'AM':
		start_hs_24format = int(start_Time_hs)
  #else: 
  #  print('Error: time format has no meridian')
			
	### We add the hours and the minutes.
	resulting_summed_hs = start_hs_24format + duration_timespan_hs
	resulting_summed_mins = int(start_Time_mins + duration_timespan_mins)

  ### Now, if the sum of the minutes is greater or equal than 60, we need to reset it to minutes % 60 and add 1 hour. Should the resulting minute % 60 be strictly less than 10, for convenience's sake, we will write with a zero to the left.
	if resulting_summed_mins >= 60 :
		resulting_summed_hs += resulting_summed_mins // 60 ## For example, if 120 minutes have passed, we are to add two hours to the previously defined count. 
		summed_minutes_str = str(resulting_summed_mins % 60).rjust(2, "0") ## Here we reset the number of minutes, and according to the prescription, should the result be strictly less than 10, we will write with a zero to the left. 
	elif resulting_summed_mins < 60 : ## Should the number of minutes passed be less than 60, we are not to reset the numbers, only the printing format. 
		resulting_summed_hs = resulting_summed_hs
		summed_minutes_str= str(resulting_summed_mins).rjust(2, "0")
  #else:
  #  print('Math error due to unknown cause. Restart')

	### If more than 24 hours have passed, we are to add 1 day to the count. 
	if resulting_summed_hs >= 24 :
		days_passed = int(resulting_summed_hs // 24)
	else :
		days_passed = 0

	### Here we'll change the time-printing format, from 0:XX to 12:XX, without changing the minutes
	new_period = resulting_summed_hs - (days_passed * 24)

  ### With the next lines of codes we establish a biunovical isormorphism between the PM/AM-format to the
	new_time_hours_12 = None
	if resulting_summed_hs % 12 == 0 :
		new_time_hours_12 = 12
	else:
		new_time_hours_12 = resulting_summed_hs % 12
  
  ### Here we write the summed up times in the final printing notation of "hours:minutes PM/AM"
	if new_period >= 12 :
		resulting_Time = str(new_time_hours_12) + ":" + str(summed_minutes_str) + " PM"
	else :
		resulting_Time = str(new_time_hours_12) + ":" + str(summed_minutes_str) + " AM"

  ### The following lines of codes are to be executed if and only if the user gives us an additional input.
	if user_wday != "None":
		
    ### here we are to define a list and a dictionary with the days of the week. 
		days_list = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")    

		### In the next lines of code we're to calculate the index of the user-input weekday eg. should the user tell us 'friday', index must be <<4>>. Note that user might not write in capitals, so we should addres this by using .capitalize() function.
		new_weekday = days_list[(days_list.index(user_wday.lower()) + days_passed) % 7].capitalize()

		### We concatenate strings according to the exercise's guidelines. 
		if days_passed == 0 :
				resulting_Time += ", " + str(new_weekday)
		elif days_passed == 1 :
				resulting_Time += ", " + str(new_weekday) + " (next day)"
		else:
			resulting_Time += ", " + str(new_weekday) + " (" + str(days_passed) + " days later)"
	else: 
	### Should the user not give us additional information, we add this condition in order to be sure that we are printing this correctly. 
		if days_passed == 0 :
				resulting_Time += ""
		elif days_passed == 1 :
				resulting_Time += " (next day)"
		else:
			resulting_Time += " (" + str(days_passed) + " days later)"
  
	return resulting_Time