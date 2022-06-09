import gitlab
import settings
import typing

gl = gitlab.Gitlab(settings.GITLAB_API_ADDR, private_token=settings.GITLAB_TOKEN)


def get_last_merge_requests() -> None:
    """ Get last merg request """
    if settings.GITLAB_ROOT_GROUP == '':
        all_mr: typing.Any = gl.mergerequests.list(state="opened")
    else:
        all_mr: typing.Any = gl.groups.get(settings.GITLAB_ROOT_GROUP).mergerequests.list(state="opened")
    try:
        last_mr: gitlab.v4.objects.merge_requests.MergeRequest = all_mr[0]
    except IndexError:
        print("Merge requests - Not found")
        return
    _auto_add_responsible(last_mr)


def _auto_add_responsible(mr: gitlab.v4.objects.merge_requests.GroupMergeRequest) -> None:
    project: gitlab.v4.objects.projects.Project = gl.projects.get(
        mr.project_id, lazy=True
    )
    editable_mr: gitlab.v4.objects.merge_requests.ProjectMergeRequest = (
        project.mergerequests.get(mr.iid, lazy=True)
    )
    editable_mr.assignee_id = mr.author["id"]
    editable_mr.reviewer_ids = settings.GITLAB_REVIEWERS
    print(editable_mr)
    editable_mr.save()


if __name__ == "__main__":
    get_last_merge_requests()
