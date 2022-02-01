from flask import request, Flask
import json
import docker
app1 = Flask(__name__)
@app1.route('/')
def checkDockerContainerStatus( container):
    client = docker.from_env()
    #cli = docker.APIClient()
    if client.containers.list(filters={'name': container}):
        response = client.containers.list(filters={'name': container})
        return str(response[0].id)[:12]
    else:
        return None
running_id = checkDockerContainerStatus('app-container')
if running_id is not None:
    print(f"Found! {running_id}")
else:
    print("Container app-container is not found")
if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')


