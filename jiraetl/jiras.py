from jiraetl.common.jiraconfig import Config
from jiraetl import make_jira_etl


def main():
    config = Config()
    etl = make_jira_etl(config)
    etl.extract()


if __name__ == '__main__':
    main()
