import urllib                                                                   
  2                                                                                 
  3 def read_text():                                                                
  4     quotes = open("HD/Applications/TextEdit/movie_quotes")                      
  5     contents_of_file = quotes.read()                                            
  6     print (contents_of_file)                                                    
  7     quotes.close()                                                              
  8     check_profanity()                                                           
  9                                                                                 
 10 def check_profanity():                                                          
 11     connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
 12     output = connection.read()                                                  
 13     print(output)                                                               
 14     connection.close()                                                          
 15                                                                                 
 16 read_text()          
