from prefect import flow, serve
from prefect.deployments import DeploymentImage

@flow(log_prints=True)
def hello():
    print("Hello!")


if __name__ == "__main__":
    # ToDo - Add multiple packages separated by space
    hello.deploy(
        name="my-deployment1234", 
        work_pool_name="my-managed-pool", 
        image="prefecthq/prefect:2-python3.11",
        job_variables={"env": {"EXTRA_PIP_PACKAGES": "python-dotenv"} },
    )