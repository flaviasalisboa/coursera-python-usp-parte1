segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias= total_segs // 86400
segs_restantes_dias = total_segs % 86400

horas = segs_restantes_dias // 3600
segs_restantes_horas = segs_restantes_dias % 3600

minutos = segs_restantes_horas // 60
segs_final = segs_restantes_horas % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_final, "segundos.")