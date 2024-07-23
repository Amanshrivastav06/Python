a={"key":"value",
   "Aman":"100",
   "list":[2,4,65,7,8]
}

#1 a.items():Returns a list of (key, value)tuples.
print(a.items())

#2 a.keys():Returns a list containing dictionary's keys.
print(a.keys())

#3 a.upadate({"friends":}):Updates the dictionary with supplied keys value pairs.
a.update({"Aman":101})
print(a)

#4 a.get("name"): Returns the value of the specified keys (and value is returned eg."harry")   docs.python.org
print(a.get("name")) # a.get - ye none return karega agr key nhi hoga to.
print(a["name"]) # ye error return karega.
