Time = input("Input time (standard pm or am, eg, 11:45am: ")
location = Time.index(':')
mins_part = Time[location+1:location+3]
if 'AM' in Time:
    Time = Time.replace('AM','am')
if 'PM' in Time:
    Time = Time.replace('PM','pm')
if Time[-2:] == 'pm':
    cross_time = 'am'
if Time[-2:] == 'am':
    cross_time_a = 'pm'
if 'p' in Time and int(Time[:location]) != 12:
    Time_hours = int(Time[:location]) + 12
else:
    Time_hours = int(Time[:location])
starting_zone = input("Input your starting zone (Eastern, Central, Mountain or Pacific): ")
starting_zone = starting_zone.lower()
if starting_zone == 'eastern' or starting_zone == 'central' or starting_zone == 'mountain' or starting_zone == 'pacific':
    stored_start_zone = starting_zone
    ending_zone = input("Input your ending zone (Eastern, Central, Mountain or Pacific): ")
    ending_zone = ending_zone.lower()
    if ending_zone == 'eastern' or ending_zone == 'central' or ending_zone == 'mountain' or ending_zone == 'pacific':
        stored_end_zone = ending_zone
        if stored_end_zone == stored_start_zone:
            print(f"Your starting zone and ending zone are same, hence, the time is {Time}")
        else:
            #pm
            if Time[-2:] == 'pm':
                #1 Eastern to Pacific
                if stored_start_zone == 'eastern' and stored_end_zone == 'pacific':
                    Time_hours = Time_hours - 3
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #2 Pacific to Eastern
                elif stored_start_zone == 'pacific' and stored_end_zone == 'eastern':
                    Time_hours = Time_hours + 3
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #3 Eastern to Mountain
                elif stored_start_zone == 'eastern' and stored_end_zone == 'mountain':
                    Time_hours = Time_hours - 2
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #4 Mountain to Eastern
                elif stored_start_zone == 'mountain' and stored_end_zone == 'eastern':
                    Time_hours = Time_hours + 2
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #5 Eastern to Central
                elif stored_start_zone == 'eastern' and stored_end_zone == 'central':
                    Time_hours = Time_hours - 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #6 Central to Eastern
                elif stored_start_zone == 'central' and stored_end_zone == 'eastern':
                    Time_hours = Time_hours + 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #7 Central to Pacific
                elif stored_start_zone == 'central' and stored_end_zone == 'pacific':
                    Time_hours = Time_hours - 2
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #8 Pacific to Central
                elif stored_start_zone == 'pacific' and stored_end_zone == 'central':
                    Time_hours = Time_hours + 2
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #9 Central to Mountain
                elif stored_start_zone == 'central' and stored_end_zone == 'mountain':
                    Time_hours = Time_hours - 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #10 Mountain to Central
                elif stored_start_zone == 'mountain' and stored_end_zone == 'central':
                    Time_hours = Time_hours + 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #11 Mountain to Pacific
                elif stored_start_zone == 'mountain' and stored_end_zone == 'pacific':
                    Time_hours = Time_hours - 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #12 Pacific to Mountain
                elif stored_start_zone == 'pacific' and stored_end_zone == 'mountain':
                    Time_hours = Time_hours + 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
            #am
            elif Time[-2:] == 'am':
                #1 Eastern to Pacific
                if stored_start_zone == 'eastern' and stored_end_zone == 'pacific':
                    Time_hours = Time_hours - 3
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time_a 
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #2 Pacific to Eastern
                elif stored_start_zone == 'pacific' and stored_end_zone == 'eastern':
                    Time_hours = Time_hours + 3
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + cross_time_a
                        print(f"{final_time}, {ending_zone.title()} time")
                #3 Eastern to Mountain
                elif stored_start_zone == 'eastern' and stored_end_zone == 'mountain':
                    Time_hours = Time_hours - 2
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time_a
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #4 Mountain to Eastern
                elif stored_start_zone == 'mountain' and stored_end_zone == 'eastern':
                    Time_hours = Time_hours + 2
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + cross_time_a
                        print(f"{final_time}, {ending_zone.title()} time")
                #5 Eastern to Central
                elif stored_start_zone == 'eastern' and stored_end_zone == 'central':
                    Time_hours = Time_hours - 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time_a 
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:]) 
                        print(f"{final_time}, {ending_zone.title()} time")
                #6 Central to Eastern
                elif stored_start_zone == 'central' and stored_end_zone == 'eastern':
                    Time_hours = Time_hours + 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time_a
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #7 Central to Pacific
                elif stored_start_zone == 'central' and stored_end_zone == 'pacific':
                    Time_hours = Time_hours - 2
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time_a
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #8 Pacific to Central
                elif stored_start_zone == 'pacific' and stored_end_zone == 'central':
                    Time_hours = Time_hours + 2
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"a{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + cross_time_a
                        print(f"b{final_time}, {ending_zone.title()} time")
                #9 Central to Mountain
                elif stored_start_zone == 'central' and stored_end_zone == 'mountain':
                    Time_hours = Time_hours - 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time_a 
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #10 Mountain to Central
                elif stored_start_zone == 'mountain' and stored_end_zone == 'central':
                    Time_hours = Time_hours + 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + cross_time_a
                        print(f"{final_time}, {ending_zone.title()} time")
                #11 Mountain to Pacific
                elif stored_start_zone == 'mountain' and stored_end_zone == 'pacific':
                    Time_hours = Time_hours - 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + cross_time_a
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                #12 Pacific to Mountain
                elif stored_start_zone == 'pacific' and stored_end_zone == 'mountain':
                    Time_hours = Time_hours + 1
                    New_Time_hours = Time_hours%12
                    if New_Time_hours != 0 and Time_hours > 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    elif New_Time_hours != 0 and Time_hours < 12:
                        final_time = str(New_Time_hours) + ':' + str(mins_part) + (Time[-2:])
                        print(f"{final_time}, {ending_zone.title()} time")
                    else:
                        final_time = str(Time_hours) + ':' + str(mins_part) + cross_time_a
                        print(f"{final_time}, {ending_zone.title()} time")
                        
                
    else:
        print('incorrect, check the ending zone format inputted')
else:
    print('incorrect, check the starting zone format inputted')