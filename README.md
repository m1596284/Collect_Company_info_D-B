# Collect_Company_info_D-B
Collect company information on D&amp;B (~150 millions data)


## User :
set up the priority table for categary then run the program.  
<img src="https://github.com/m1596284/Collect_Company_info_D-B/blob/master/Collect_Company_information.gif" width="647" height="426">

## Backstage : Python + Thread + Tor(IP switcher)
Thread: to run 1~100 crawler for speed up the collecting task, and also avoid the IP blocking from website.  
Tor: a free IP switcher which can use specific country IP for your brower but have a little bit delay. "controller.signal(Signal.NEWNYM)" to switch.   
