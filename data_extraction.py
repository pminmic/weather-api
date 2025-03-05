from datetime import datetime

class Weather:
    def __init__(self, data):
        self.data = data

    # returns the date and hour of creation of the information in the API
    def get_creation_time(self):
        return self.data['elaborado']

    # returns the name of the town from where the data comes from
    def get_town(self):
        return self.data['municipio']['NOMBRE']

    # returns the name of the province of the town
    def get_province(self):
        return self.data['municipio']['NOMBRE_PROVINCIA']

    # returns the date of the prediction (format: YYYY-MM-DD)
    def get_today_date(self):
        return self.data['fecha']                        

    # returns the altitude of the town
    def get_altitude(self):
        return self.data['municipio']['ALTITUD']

    #returns a tuple of the corsd
    def get_coords(self):
        latitude = self.data['municipio']['LATITUD_ETRS89_REGCAN95']
        longitude = self.data['municipio']['LONGITUD_ETRS89_REGCAN95']
        return (latitude, longitude)
    
    # returns the actual state of the sky
    def get_state_sky(self):
        return self.data['stateSky']['description']
    
    # returns the actual temperature
    def get_actual_temp(self):
        return self.data['temperatura_actual']
    
    # returns the minimum temperature of today
    def get_today_min(self):
        return self.data['temperaturas']['min']
    
    # returns the maximum temperature of today
    def get_today_max(self):
        return self.data['temperaturas']['max']
    
    # returns the actual humidity of the ambience
    def get_actual_humidity(self):
        return self.data['humedad']
    
    # returns the actual speed of the wind
    def get_actual_wind_speed(self):
        return self.data['viento']

    # returns the actual probability of rain
    def get_actual_probability_rain(self):
        return self.data['lluvia']
    
    # returns the actual precipitation
    def get_actual_precipitation(self):
        return self.data['precipitacion']
    
    # returns the hour of today's sunrise
    def get_today_sunrise(self):
        return self.data['pronostico']['hoy']['@attributes']['orto']
    
    # returns the hour of today's sunset
    def get_today_sunset(self):
        return self.data['pronostico']['hoy']['@attributes']['ocaso']

    # returns a list with the stimated precipitation for each hour
    def get_today_precipitation(self):
        return self.data['pronostico']['hoy']['precipitacion']
    
    # returns a list with the probability of rain every 8 hours (3 values)
    def get_today_prob_rain(self):
        return self.data['pronostico']['hoy']['prob_precipitacion']
    
    # returns a list with the probability of storm every 8 hours
    def get_today_prob_storm(self):
        return self.data['pronostico']['hoy']['prob_tormenta']
    
    # returns a list with the amount of snow each hour
    def get_today_snow(self):
        return self.data['pronostico']['hoy']['nieve']
    
    # returns a list with the probability of snow every 8 hours
    def get_today_prob_snow(self):
        return self.data['pronostico']['hoy']['prob_nieve']
    
    # returns a list of all the values of todays temperature one each hour
    def get_today_temp(self):
        return self.data['pronostico']['hoy']['temperatura']
    
    # returns a list of all the values of todays thermal sensation, one each hour
    def get_today_thermal_sens(self):
        return self.data['pronostico']['hoy']['sens_termica']
    
    # returns a list of all the values of the relative humidity, one each hour
    def get_today_relative_hum(self):
        return self.data['pronostico']['hoy']['humedad_relativa']
    
    # returns a list of dicts with all the values of the wind (speed, and direction), one for each hour
    def get_today_wind(self):
        return self.data['pronostico']['hoy']['viento']
    
    # returns a list with the max speed of the wind, one each hour
    def get_today_max_wind(self):
        return self.data['pronostico']['hoy']['racha_max']
    
    # returns a list with the description of the sky, one for each hour
    def get_today_sky_description(self):
        return self.data['pronostico']['hoy']['estado_cielo_descripcion']
    
    # returns de date of tomorrow (format: YYYY-MM-DD)
    def get_tomorrow_date(self):
        return self.data['pronostico']['manana']['@attributes']['fecha']
    
    # returns the hour of tomorrow's sunrise
    def get_tomorrow_sunrise(self):
        return self.data['pronostico']['manana']['@attributes']['orto']
    
    # returns the hour of tomorrow's sunset
    def get_tomorrow_sunset(self):
        return self.data['pronostico']['manana']['@attributes']['ocaso']

    # returns a list with the stimated precipitation for each hour (tomorrow)
    def get_tomorrow_precipitation(self):
        return self.data['pronostico']['manana']['precipitacion']
    
    # returns a list with the probability of rain every 8 hours (3 values)
    def get_tomorrow_prob_rain(self):
        return self.data['pronostico']['manana']['prob_precipitacion']
    
    # returns a list with the probability of storm every 8 hours
    def get_tomorrow_prob_storm(self):
        return self.data['pronostico']['manana']['prob_tormenta']
    
    # returns a list with the amount of snow each hour
    def get_tomorrow_snow(self):
        return self.data['pronostico']['manana']['nieve']
    
    # returns a list with the probability of snow every 8 hours
    def get_tomorrow_prob_snow(self):
        return self.data['pronostico']['manana']['prob_nieve']
    
     # returns a list of all the values of todays temperature one each hour
    def get_tomorrow_temp(self):
        return self.data['pronostico']['manana']['temperatura']
    
    # returns a list of all the values of todays thermal sensation, one each hour
    def get_tomorrow_thermal_sens(self):
        return self.data['pronostico']['manana']['sens_termica']
    
    # returns a list of all the values of the relative humidity, one each hour
    def get_tomorrow_relative_hum(self):
        return self.data['pronostico']['manana']['humedad_relativa']
    
    # returns a list of dicts with all the values of the wind (speed, and direction), one for each hour
    def get_tomorrow_wind(self):
        return self.data['pronostico']['manana']['viento']
    
    # returns a list with the max speed of the wind, one each hour
    def get_tomorrow_max_wind(self):
        return self.data['pronostico']['manana']['racha_max']
    
    # returns a list with the description of the sky, one for each hour
    def get_tomorrow_sky_description(self):
        return self.data['pronostico']['manana']['estado_cielo_descripcion']
    
    def check_all_correct(self):
        actual_date = self.get_today_date()
        expected_date = datetime.now().strftime("%Y-%m-%d")

        if actual_date == expected_date:
            return True
        else:
            raise ValueError(
                f"Something is going wrong with the API, its not up to date (the date of the data is not from today)"
            )

