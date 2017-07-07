import webapp2
from mapreduce import base_handler
from mapreduce import mapreduce_pipeline

class StarterTaskPipeline(base_handler.PipelineBase):
    def run(self, *args, **kwargs):
        shard_count = 16 # Pick the custom number of shards

        mapper_params = {
            "entity_kind": "entity.DummyEntity.DummyEntity", # Set the path to the desired entity. In this example we will keep entities in entity/ folder.
        }

        output = yield mapreduce_pipeline.MapreducePipeline(
            "starter_task", # The name of mapreduce job.
            mapper_spec="tasks.starter_task.dummy_map_function", # Set the path to the map function. In this example our map function is in this same file, inside tasks/ folder.
            mapper_params = mapper_params, 
            reducer_spec="tasks.starter_task.dummy_reduce_function", # Set the path to the reduce function. Again, in this example, it's in the same file as map function.
            input_reader_spec="mapreduce.input_readers.DatastoreInputReader", # Setting the input reader. The available input readers are in the mapreduce/input_readers.py file.
            shards=shard_count
        )

def dummy_map_function(dummy_entity):
    # Implement the map function
    pass

def dummy_reduce_function(key, values):
    # Implement the reduce function
    # If the output reader is set, write the result through the output reader.
    # DatastoreOutputReader has been removed from the library, and in case that you want to output to datastore, you can do something like
    # yield entity.put()
    pass

class StarterTaskPipelineStartHandler(webapp2.RequestHandler):
    def get(self):
        starter_task_pipeline = StarterTaskPipeline()
        starter_task_pipeline.start()

app = webapp2.WSGIApplication([
    ('/starter_task', StarterTaskPipelineStartHandler) # Your url which will trigger the task to start
], debug=True)