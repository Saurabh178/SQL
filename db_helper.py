import mysql.connector

class DB:
    def __init__(self):
        #connect to database server
        try:
            self.conn=mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='178@SAurabh',
                database='Flights'
            )
            self.mycursor=self.conn.cursor()
            print('Connection established')
        except mysql.connector.Error as e:
            print('Connection error:', e)

    def  fetch_city_name(self):
        self.mycursor.execute("""
                                select distinct(source) from airport
                                union
                                select distinct(destination) from airport
                              """)
        
        data=self.mycursor.fetchall()
        city=[]

        for item in data:
            city.append(item[0])

        return city
    
    def fetch_all_flights(self, source, destination):
        self.mycursor.execute("""
                              select Airline, Route, Dep_Time, Duration, Total_Stops, Price 
                              from airport where Source='{}' and Destination='{}'
                              """.format(source, destination))
        
        data=self.mycursor.fetchall()
        return [len(data), data]
    
    def fetch_airline_freq(self):
        self.mycursor.execute("""
                              select Airline, count(*) from airport group by Airline
                              """)
        
        data=self.mycursor.fetchall()

        airline=[]
        freq=[]

        for item in data:
            airline.append(item[0])
            freq.append(item[1])

        return airline, freq
    
    def fetch_busy_airport(self):
        self.mycursor.execute("""
                              select t.source, count(*) as count_flights from (select source from airport union all 
                              select destination from airport) as t group by t.source 
                              order by count_flights desc
                              """)
        
        data=self.mycursor.fetchall()

        city=[]
        freq=[]

        for item in data:
            city.append(item[0])
            freq.append(item[1])

        return city, freq
    
    def fetch_daily_flight_freq(self):
        self.mycursor.execute("""
                              select Date_of_Journey, count(*) from airport group by Date_of_Journey
                              """)
        
        data=self.mycursor.fetchall()

        doj=[]
        freq=[]

        for item in data:
            doj.append(item[0])
            freq.append(item[1])

        return doj, freq
