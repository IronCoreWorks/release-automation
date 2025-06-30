import github
import os

auth = github.Auth.Token(os.environ['GITHUB_TOKEN'])
gh_client = github.Github(auth=auth)

org = gh_client.get_organization('ironcoreworks')
repo = org.get_repo('release-automation')

# try:
#     release = repo.create_git_release(
#         tag='0.2.0',
#         name='0.2.0',
#         draft=True,
#         generate_release_notes=True,
#         target_commitish='main',
#     )
# except Exception as e:
#     print(f'Error creating release: {e}')



def get_draft_release(repo):
    releases = repo.get_releases()
    for release in releases:
        if release.draft:
            return release
    return None

release = get_draft_release(repo)
print(release.title)
print(release.body)
release.update_release(name=release.title, message=release.body, draft=False)
