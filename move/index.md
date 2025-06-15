# Moving repositories from [`psb-david-petty`](https://github.com/psb-david-petty?tab=repositories&sort=name) to [`dcpetty`](https://github.com/dcpetty?tab=repositories&sort=name)

In order to move the repository `repo` from [`psb-david-petty`](https://github.com/github.com/psb-david-petty?tab=repositories&sort=name) to [`dcpetty`](https://github.com/github.com/dcpetty?tab=repositories&sort=name) &mdash; assuming there are `psb-david-petty` &amp; `dcpetty` directories containing their respective [Github](https://github.com/) repos:
 
1. Create [`https://github.com/dcpetty/repo`](https://github.com/dcpetty/repo) with `README.md` & [MIT License](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository). 
1. Enable [Github Pages](https://pages.github.com/). Settings &rarr; Pages &rarr; Deploy from a branch: `main` &rarr; Save.
1. Copy the `git clone` URI for SSH (`git@github.com:dcpetty/repo`).
1. `git clone git@github.com:dcpetty/repo` into the `dcpetty` directory.
1. Add the appropriate `[user]` information to `repo/.git/config`.
<pre>[user]
    name = dcpetty
    email = 1700736+dcpetty@users.noreply.github.com 
</pre>
1. Copy [`.gitignore`](https://raw.githubusercontent.com/dcpetty/first/refs/heads/main/.gitignore) from [`dcpetty.github.io`](https://github.com/dcpetty/dcpetty.github.io/tree/main) &mdash; which is the latest.
2. 

> **Note:** the appropriate `[user]` information in `repo/.git/config` for [`psb-david-petty`](https://github.com/psb-david-petty?tab=repositories&sort=name) repositories is:
<pre>[user]
    name = psb-david-petty
    email = 43327098+psb-david-petty@users.noreply.github.com</pre>

<hr>

[&#128279; permalink](https://dcpetty.github.io/first/subfolder/moving.html) and [&#128297; repository](https://github.com/dcpetty/first/tree/main/subfolder/moving.md) for this page.

