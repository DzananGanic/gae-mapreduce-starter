# gae-mapreduce-starter
Starting helper for implementing [mapreduce library on Google App Engine](https://github.com/GoogleCloudPlatform/appengine-mapreduce).
In this repo, I have included all the files and libraries you need in order to start your first mapreduce job on Google App Engine.

## Why?
As you may have noticed, the official library documentation is pretty old and lots of things have changed since the last update. The library itself is pretty easy to setup, but the lack of support and outdated documentation can make it harder than it should be. That's why I decided to create this simple service to get you up and running as fast as possible, so you can start writing your own mapreduce jobs pretty quickly.

Thing to note:
[appengine-mapreduce]((https://github.com/GoogleCloudPlatform/appengine-mapreduce)) requires [graphy](https://github.com/artemyk/graphy) library in order to function properly. When heading to '/mapreduce' url, you can see the overview of the jobs as well as the graphs related to it.

## Steps to start out:

1. In 'app.yaml', set the 'service' to your own
2. Under 'handlers', define the handlers which will trigger specific tasks.
3. In tasks/ folder, create your own tasks based on 'starter_task.py'
4. In entity/ folder, you can have your ndb models. If you want to have it somewhere else, just change the 'entity_kind' path under mapper_spec in your tasks
5. Implement your own map and reduce functions, and you're done.

Other substeps should be easily understood from the commented code.
