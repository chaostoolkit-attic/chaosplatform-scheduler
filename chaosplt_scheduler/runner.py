from chaoslib.experiment import run_experiment
from chaoslib.types import Journal
import requests
import simplejson as json


def run(schedule_id: str, user_id: str, org_id: str, workspace_id: str,
        experiment_id: str, token_id: str, token: str, experiment: str,
        platform_url: str, settings: str = None, configuration: str = None,
        secrets: str = None) -> Journal:
    """
    Execute an experiment and return its journal

    See also:
    https://docs.chaostoolkit.org/reference/api/journal/
    """
    settings = json.loads(settings) if settings else {}
    experiment = json.loads(experiment)

    if configuration:
        configuration = json.loads(configuration)
        experiment.setdefault("configuration", {})
        experiment["configuration"].update(configuration)

    if secrets:
        secrets = json.loads(secrets)
        experiment.setdefault("secrets", {})
        experiment["secrets"].update(secrets)

    journal = run_experiment(experiment)

    headers = {"Authorization": "Bearer {}".format(token)}
    requests.post(
        "{}/api/v1/executions".format(platform_url), json={
            "experiment_id": experiment_id,
            "journal": journal
        }, headers=headers)

    return journal
