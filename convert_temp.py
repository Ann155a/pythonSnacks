# convert_temp(temp, scale = "C") function, if the scale is c, the temp is in celsius, if scale equals F convert to celsius
def convert_temp(temp, scale = "C"):
  if scale.upper == "C":
    tempF = temp * (9/5) + 32
    return tempF
    
    else:
      tempC = (temp - 32) * (5/9)
      return tempC
