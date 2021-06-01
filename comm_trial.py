from Convert import hex2signed, signed2hex
from init_start import getaddress
from COMM import setvalue, getvalue


print(signed2hex("1000"))

#setvalue(getaddress("pzt0_d", "offset"), signed2hex("20"), "1", "1")
#print(getvalue(getaddress("pzt0_d", "offset"), "1", "1"))
#print(hex2signed("100000014"))