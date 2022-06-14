# Gitlab auto-assign reviewer assignee for merge request
#### The purpose of the script is to automatically select the responsible persons when creating a merge request
![Alt text](https://akmalov.com/wp-content/uploads/2022/06/merge.png "New merge request")



### Preparation
For execution, it is necessary to track events.
* Gitlab CI workflow event
* Schedules
* other events

I use gitlab workflow - **merge request event**
```yml
workflow:
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
```


#### There are two options >>

### Option 1 - Gitlab (pipline)
add API Token to Settings -> CI/CD -> Variables

script execution steps:
1. Get last merge request ID
2. Parse Author
3. Put Assigne = Author
4. Put Reviewers = Reviewers(list) variable



### Option 2 - Python (script)
Simple scripts usage python-gitlab project

Change your variables in Python/settings.py


####
[Ссылка на сайт]([http://example.com/](https://akmalov.com/blog/gitlab-auto-assign/)). 
