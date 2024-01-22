# Nesting
capitals={"France":"Paris",
          "Germany":"Berlin"}

print(capitals)

# Nesting a list in a dictionary

travel_log={"France":["Paris","Lille","Dijon"],
            "Germany":["Berlin","Hamburg","Stuttgart"]}
print(travel_log)

# Nesting a Dictionary in a dictionary
travel_log={"France":{"cities_visited":{"Paris":14,"Lille":3,"Dijon":2}},
            "Germany":{"cities_visitied":{"Berlin","Hamburg","Stuttgart"}}}
print(travel_log["France"]["cities_visited"]["Paris"])
