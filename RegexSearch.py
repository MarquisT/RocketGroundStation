import re

string = "[8]    [RX_RSSI:-72]Data:[ET=957286,T=3000,A=9022,P=100246] - ACK sent"

#found = re.search('[RX_RSSI:-{/d{1,2}]', string)
#print(found)

#match = re.search('(\d+)', string)
#if match:
array = re.findall(r':(-[0-9]+)', string) # Grabs the -71
data_array= re.findall(r'\[.*?\]', string)[2] # Grabs the -71

print(data_array)
print("Signal strength is {}".format(re.findall(r':(-[0-9]+)', string)[0]))

print(re.findall('ET=(\d+)', data_array)[0])
print("ET is {}".format(re.findall('ET=(\d+)', data_array)[0]))
print("T is {:.2f}".format(float(re.findall(',T=(\d+)', data_array)[0])/100))
#print(float(re.findall(',T=(\d+)', data_array)[0])/100)

print("P is {:.2f}".format(float(re.findall(',P=(\d+)', data_array)[0])/100))
print("A is {}".format(re.findall(',A=(\d+)', data_array)[0]))




#print(match.group(1))