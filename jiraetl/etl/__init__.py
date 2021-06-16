import json
from jiraetl.common.jiraconfig import Config
from jiraetl.etl.jiraextractor import make_jira_client, JiraDataSource


class JiraEtl:
    def __init__(self, source: JiraDataSource,
                 jira_query: str,
                 jira_query_limit: int,
                 json_filepath: str,
                 ):
        self.jira = source
        self.jira_query = jira_query
        self.jira_query_limit = jira_query_limit
        self.json_filepath = json_filepath

    def extract(self):
        with open(self.json_filepath, 'w') as f:
            jira_results = [i.raw for i in
                            self.jira.query(
                                jql=self.jira_query,
                                limit=self.jira_query_limit,
                            )]
            print(jira_results)
            json.dump(jira_results, f)
            print('Jiras extract completed')


def make_jira_etl(config: Config) -> JiraEtl:
    return JiraEtl(
        source=make_jira_client(config),
        jira_query=config.jira_query,
        jira_query_limit=int(config.jira_query_limit),
        json_filepath=config.json_filepath,
    )
