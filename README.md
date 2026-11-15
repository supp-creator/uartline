 # Real-Time Signal Processing Systems.
<br></br>
## Digital Communications Final Project Group 9

<br></br>
**DUE DATE: DECEMBER 12, 2026 @ 23:59**
<br></br>

### INTERNAL TASKS ASSIGNMENTS

| Member    |   Task    |
| ----------| :--------:|
| Joshua    |           |
| Brex      |           |
| Jacob     |           |
| Tyrone    |           |

<br></br>
### Generative LLM AI usage

I know someone's going to use it. I don't blame you.
Just put an in-line comment saying so.

That way I can check out if it would actually work, and make it look more human-made.

### To Do:

- [ ] main.py
- [ ] audio.py
- [ ] detector.py
- [ ] framing.py
- [ ] link.py
- [ ] metrics.py
- [ ] morse.py 
- [ ] pcm.py
<br></br>
- [ ] Actually write the paper.
- [ ] Rewrite the README.md. Can't talk shit about AI.
- [ ] Assemble actual circuit.
- [ ] *PRESENTATION*
<br></br>

### Baby's First Guide to Git

0. Download git?

**Mac:** `brew install git`

**Windows:** `winget install --id Git.Git -e --source winget` 

_Fuck is that, Microsoft?_

**Linux:** Lmao, sure. YOU use Linux.

**BSD:** Someone knows ball.


Verify by running: `git version`. Some output should print.

1. Initial Setup

```bash
git config --global user.name "Your name"
git config --global user.email "you@example.com"
```

2. Download the existing project repository.

```bash
git clone <repository-url>
```

I highly recommend setting up SSH or your GitHub account first.





3. Daily Workflow

    - **Check if there's any new changes.**

    `git status`

    - **If so, update your version.**

    `git pull`

    - **Staging files for new commit.**

    ```bash
    git add .           # Prepares all your new changes 
    git add <filename>  # Prepares only a specific file
    ```

    - **Commit prepared (a.k.a staged) changes.**

    ```bash
    git commit -m "Input description of what you did."
    ```

    By committing a change, you've essentially placed a checkpoint on it that you can go back to at any time.





4. Updating the rest of us on your work.

    - **Upload all your committed changes to the main repository.**

    ```bash
    git push
    ```






5. Correcting mistakes.

| Goal | Command |
|:-----| :-------|
| **Discard unstaged changes** | `git checkout -- <filename>` |
| **Unstage a file (keep changes)** | `git reset HEAD <filename>` |
| **Edit last commit message** | `git commit --amend -m "New Message` |
| **Undo a commit (creates a new commit)** | `git revert <commit-hash` |


Check out commit hashes using `git log`



That's all the git you need for this project, I think.
