def main():
    #layer = input("choose one layer in earth´s atmosphere: ")
   # Exosphere = input("700 10,000 km.")
  #  Thermosphere = input("85–700 km")
   # Mesosphere = input("your altittude level will be between 50–85 km")
    ##roposphere = input("your altittude lvel will be between 0–12 km")
    #altittude = input("enter exact altittude: ")
    #print(layer)
    #print(f"Your altittude:"(Exosphere))
    #print(f"Your altittude:"(Thermosphere))
    #print(f"your altittude level will be between{Exosphere}.")
    #print(f"your altittude level will be between{Thermosphere}.")
    #print()
    #if Exosphere:
     #   print(Exosphere)
    #elif Thermosphere:
     #   print(Thermosphere)
     layer = input("Descent atmosphere layer: ").strip().lower()
     if layer == "exosphere":
          print("Altitude between 700 and 10,000 km.")
        elif layer == "thermosphere":
          print("Altitude between 85 and 700 km.")
        elif layer == "mesosphere":
          print("Altitude between 50 and 85 km.")
        elif layer == "stratosphere":
          print("Altitude between 12 and 50 km.")
        elif layer == "troposphere":
          print("Altitude between 0 and 12 km.")
        else:
          print("Inexistent layer.")


    altitude = float(input("Enter exact altitude: "))
    time = 0
    if altitude > 700:
        time += (altitude - 85) / 0.5
        altitude = 85

if __name__ == "__main__":
    main()
