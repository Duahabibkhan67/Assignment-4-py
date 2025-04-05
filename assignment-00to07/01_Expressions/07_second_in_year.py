DAYS_IN_YEAR = 365
HOURS_IN_DAY =24
MIN_IN_HOUR = 60
SEC_IN_MIN = 60

def main():
   total_seconds = DAYS_IN_YEAR* HOURS_IN_DAY * MIN_IN_HOUR* SEC_IN_MIN

   print(f"Total seconds in a year: {total_seconds}") 

   if __name__ == "__main__":
      main()