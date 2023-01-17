while True :
    try :
        fname = input('Enter file name: ')
        
        if fname != 'done' :    
            
            if len(fname) < 1 :
                fname = 'mbox-short.txt'
            file = open(fname)
            dic = {}
            hour_list = []
        
            for line in file :
                if not line.startswith('From ') : continue
            
                else :
                    time = line.rstrip().split()[5]
                    time_split = time.split( ':' )
                    hour_list.append( time_split[0] )
                
            for hour in hour_list :
                dic[hour] = dic.get(hour,0) + 1

            file.close()
            dic_list = sorted( dic.items() )
            for k,v in dic_list :
                print(k,v)
                
        else :
            print('See ya!')
            break
            
    except :
        print('Invalid file name or error')