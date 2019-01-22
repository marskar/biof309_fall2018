import git
repo = git.Repo()

repo.index.add(repo.untracked_files)
repo.index.commit('add push.py')
repo.remotes.origin.push()

