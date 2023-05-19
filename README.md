# RL_tutorial
起こしたコンフリクトについて
1. conflictTest.txtをmainブランチに作成した
2. メンバー３人で、各々のローカルリポジトリで同時にconflictTest.txtを編集した
3. 1人がpushした後、残り２人がpushをした
4. コンフリクトが発生した。下記にエラーメッセージを示す
```
$ git push origin main
To https://github.com/Issa-N/RL_tutorial.git
 ! [rejected]       main -> main (non-fast-forward)
error: failed to push some refs to ‘https://github.com/Issa-N/RL_tutorial.git’
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: ‘git pull ...’) before pushing again.
hint: See the ‘Note about fast-forwards’ in ‘git push --help’ for details.
git pull origin main
git merge origin main
```
