# indexing demo
topic = "Python"
print(topic[0])
print(topic[1])
print(topic[2])
print(topic[3])
print(topic[4])
print(topic[5])
print(topic[-1])
print(topic[-2])
print(topic[-3])
print(topic[-4])
print(topic[-5])
print(topic[-6])
# print(topic[7]) ---> IndexError

# slicing demo

city = "nashik"
partialCityData = city[3:6]
print(partialCityData)

message = "welcome to python session"
subMessage = message[4:20:2]
print(subMessage)

message1 = "hello all, welcome"
subMessage = message1[:10:]
print(subMessage)

message2 = "hi this is kalyani"
subMessage = message2[::]
print(subMessage)