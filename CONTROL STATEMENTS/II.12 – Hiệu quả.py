from datetime import datetime, timedelta

a0, b0, c0 = map(int, input().split())  
a1, b1, c1 = map(int, input().split())  

fmt = '%H:%M:%S'
start_time = datetime.strptime(f"{a0}:{b0}:{c0}", fmt)
end_time = datetime.strptime(f"{a1}:{b1}:{c1}", fmt)

if end_time < start_time:
    end_time += timedelta(days=1)

res = int((end_time - start_time).total_seconds())
print(res)