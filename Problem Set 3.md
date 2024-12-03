> # Problem Set 3

## A 
> Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it reliable enough; Or will it scale? If not, what are the problems with it? And, what else would you recommend to fix this problem at scale in production?



### Answer
I'll use Celery to schedule periodic tasks. 
 - I chose Celery because it is a powerful and flexible task scheduler that is well-suited for a variety of use cases. 
 - Celery is also highly scalable, so it can handle large workloads without any problems.

## B
> In what circumstances would you use Flask instead of Django and vice versa? 

When to Use Flask:
 - Small-scale projects
 - Quick development
 - Less API(API like call ML model or etc just for run some python script)

When to Use Django:
 - Large-scale projects
 - Enterprise-level applications
 - Rapid development
 - Built-in security features so for some high security project but we can also use flask if we want security manually